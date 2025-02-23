from flask import Flask, render_template, request, redirect
import pymysql
from datetime import datetime

app = Flask(__name__)

# MySQL配置（确认密码正确性）
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'  # 确保与MySQL实际密码一致
app.config['MYSQL_DB'] = 'bathroom_orders'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


def get_db():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False  # 添加事务控制
    )


# 初始化数据库（增加数据库创建逻辑）
with app.app_context():
    try:
        # 先创建数据库（如果不存在）
        conn = pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD']
        )
        with conn.cursor() as cursor:
            cursor.execute(
                "CREATE DATABASE IF NOT EXISTS bathroom_orders CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            conn.commit()

        # 创建数据表
        conn = get_db()
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    order_number VARCHAR(20) NOT NULL UNIQUE,
                    customer_name VARCHAR(50) NOT NULL,
                    phone VARCHAR(20) NOT NULL,
                    product_type VARCHAR(20) NOT NULL,
                    product_model VARCHAR(50) NOT NULL,
                    quantity INT NOT NULL,
                    unit_price DECIMAL(10,2) NOT NULL,
                    total_amount DECIMAL(10,2) AS (quantity * unit_price),
                    install_address VARCHAR(200),
                    install_date DATE,
                    status ENUM('已下单','已发货','已完成') DEFAULT '已下单',
                    notes TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
            """)
            conn.commit()
    except pymysql.err.OperationalError as e:
        print(f"数据库连接失败！请检查配置：{e}")
    except pymysql.err.InternalError as e:
        print(f"数据库初始化错误：{e}")
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        # 处理表单提交
        try:
            data = {
                'order_number': request.form['order_number'],
                'customer_name': request.form['customer_name'],
                'phone': request.form['phone'],
                'product_type': request.form['product_type'],
                'product_model': request.form['product_model'],
                'quantity': int(request.form['quantity']),
                'unit_price': float(request.form['unit_price']),
                'install_address': request.form.get('install_address', ''),
                'install_date': request.form.get('install_date') or None,
                'status': request.form.get('status', '已下单'),
                'notes': request.form.get('notes', '')
            }

            conn = get_db()
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO orders (
                    order_number, customer_name, phone, 
                    product_type, product_model, quantity, 
                    unit_price, install_address, install_date, 
                    status, notes
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, tuple(data.values()))
            conn.commit()
        except pymysql.err.IntegrityError as e:
            print(f"订单号重复错误：{e}")
            conn.rollback()
            return "订单号已存在，请修改后重新提交", 400
        except Exception as e:
            print(f"数据库错误：{e}")
            conn.rollback()
            return "服务器内部错误", 500
        finally:
            if 'conn' in locals():
                conn.close()
        return redirect('/orders')

    # 获取订单列表
    try:
        conn = get_db()
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT order_number, customer_name, product_type, 
                       product_model, quantity, total_amount, 
                       status, install_date 
                FROM orders 
                ORDER BY created_at DESC
            """)
            orders = cursor.fetchall()
    except Exception as e:
        print(f"查询错误：{e}")
        orders = []
    finally:
        if 'conn' in locals():
            conn.close()

    # 转换日期格式
    for order in orders:
        if order['install_date']:
            order['install_date'] = order['install_date'].strftime('%Y-%m-%d')

    return render_template('orders.html', orders=orders)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
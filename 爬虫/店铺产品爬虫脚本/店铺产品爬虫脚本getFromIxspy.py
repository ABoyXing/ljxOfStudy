import requests
import json
import time
from datetime import datetime


def fetch_all_shop_goods(admin_seq, Cookie,delay=2):
    """
    修复版：正确处理嵌套的 data->list 结构
    """
    all_data = []
    page = 1
    size = 10  # 与请求参数一致

    while True:
        print(f"正在爬取第 {page} 页...")

        try:
            # 发送请求
            response = requests.post(
                "https://ixspy.com/shop-goods",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
                    "Cookie": Cookie,
                    "Content-Type": "application/json;charset=UTF-8"
                },
                json={
                    "admin_seq": admin_seq,
                    "page": page,
                    "size": size,
                    "orderBy": "trade_total",
                    "orderType": "",
                    "shipFrom": "",
                    "min_price_start": 0,
                    "min_price_end": 0
                },
                timeout=15
            )
            response.raise_for_status()
            resp_data = response.json()

            # 调试：打印完整响应结构
            print(f"响应结构预览: {json.dumps(resp_data, indent=2, ensure_ascii=False)[:500]}...")

            # 关键修复：提取 data->list
            if isinstance(resp_data, dict) and "data" in resp_data:
                data_layer = resp_data["data"]
                if "list" in data_layer and isinstance(data_layer["list"], list):
                    current_list = data_layer["list"]
                    all_data.extend(current_list)
                    print(f"成功提取 {len(current_list)} 条数据，总计 {len(all_data)} 条")

                    # 计算总页数 (总数据量 / 每页数量)
                    total_count = data_layer.get("count", 0)
                    total_page = total_count // size + (1 if total_count % size != 0 else 0)

                    # 终止条件
                    if page >= total_page:
                        print(f"到达末页（总页数 {total_page}）")
                        break
                else:
                    print("响应中缺少 list 字段或格式错误")
                    break
            else:
                print("响应格式异常")
                break

            page += 1
            time.sleep(delay)

        except requests.exceptions.RequestException as e:
            print(f"请求失败: {str(e)}")
            break
        except json.JSONDecodeError:
            print("响应不是有效的 JSON 格式")
            break

    return all_data


def save_to_json(data, admin_seq, filenamePre="products.json"):
    """保存有效数据"""
    # 将 admin_seq 转换为字符串, 并添加前缀
    current_date = datetime.now().strftime("%Y%m%d")
    filename = str(admin_seq)+"_"+ current_date+"_"+filenamePre
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"数据已保存到 {filename}")



import json
import pandas as pd
from datetime import datetime


def process_product(product):
    processed = {
        "商品ID": product.get("product_id"),
        "商品名称": product.get("product_name"),
        "商品链接": product.get("product_url"),
        "货币类型": product.get("currency"),
        "最高价": product.get("max_price"),
        "最低价": product.get("min_price"),
        "180天总销量": product.get("trade_total"),
        "评分": product.get("ratings"),
        "评论总数": product.get("reviews_total"),
        "收藏总数": product.get("wishlist_total"),
        "分类路径": " > ".join(map(str, product.get("category_path", []))),
        "上架时间": datetime.fromtimestamp(product.get("add_time", 0)).strftime('%Y-%m-%d') if product.get(
            "add_time") else "N/A"
    }

    # 处理 7 天数据
    stat_7days = product.get("stat_7days", {}) if isinstance(product.get("stat_7days"), dict) else {}
    processed.update({
        "近7天销量": product.get("trade_count_7", stat_7days.get("trade_count", "N/A")),
        "近7天销量增长率(%)": stat_7days.get("trade_7_inc_rate", "N/A"),
        "近7天收藏增长率(%)": stat_7days.get("wishlist_7_inc_rate", "N/A")
    })

    # 计算好评率
    feedback = product.get("feedback", {})
    total_valid = feedback.get("total_valid_num", 0)
    if total_valid > 0:
        good_reviews = feedback.get("star_5_num", 0) + feedback.get("star_4_num", 0)
        processed["好评率(%)"] = round((good_reviews / total_valid) * 100, 2)
    else:
        processed["好评率(%)"] = "N/A"

    return processed


def main(admin_seq):
    try:
        exlName = str(admin_seq)+"_20250223_products"
        with open(exlName + ".json", 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("错误：请将脚本与 all_products.json 放在同一目录")
        return

    processed_data = [process_product(p) for p in data]
    df = pd.DataFrame(processed_data)

    # 关键修复：确保列名与 DataFrame 中的列完全一致
    columns_order = [
        "商品ID", "商品名称", "商品链接", "货币类型",
        "最高价", "最低价", "180天总销量", "近7天销量",
        "近7天销量增长率(%)", "近7天收藏增长率(%)", "评分",
        "评论总数", "收藏总数", "好评率(%)",
        "分类路径", "上架时间"
    ]

    # 验证列是否存在
    missing_columns = [col for col in columns_order if col not in df.columns]
    if missing_columns:
        print("错误：缺失以下列:", missing_columns)
        print("实际存在的列:", df.columns.tolist())
        return

    try:
        df[columns_order].to_excel(exlName+".xlsx", index=False, engine='openpyxl')
        print("生成成功！共处理 {} 条数据".format(len(df)))
    except Exception as e:
        print("保存失败:", str(e))




if __name__ == "__main__":
    admin_seq = 239217760
    # 示例调用
    results = fetch_all_shop_goods(
        admin_seq,
        Cookie="_fbp=fb.1.1736078013653.781564091394667187; AliexpressSession=xb8qT5xIFlwX0ejm3q1XYPlXGF0LCHcL9c7RknJH; user_mouse=202522122843_dvqxezu7c; x-hng=lang=zh-CN&domain=ixspy.com; _gid=GA1.2.850865770.1740146924; email=; user_id=121028; level=undefined; ad_login_token=2a34b428c0543ba3efc53378254ea71a; language=zh; image_search_curr_country=US; _ga=GA1.2.1144654402.1736077730; _ga_49HDCB1VE6=GS1.1.1740287082.11.0.1740287082.0.0.0; blackShopList=; is_w_tip=1; sidebarStatus=0",
        delay=0.3  # 请求间隔
    )

    if results:
        save_to_json(results, admin_seq)
        print(f"共爬取 {len(results)} 条数据")
        print("数据示例:", json.dumps(results[0], indent=2, ensure_ascii=False))
    else:
        print("未获取到有效数据")
    main(admin_seq)
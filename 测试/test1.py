import json

# 假设你的txt文件名为data.txt，并且其中包含JSON格式的文本
filename = r'C:\Users\厉佳星\PycharmProjects\ljxOfStudy\测试\答案js.txt'

# 使用with语句打开文件，这样可以确保文件在读取后会被正确关闭
with open(filename, 'r', encoding='utf-8') as file:
    # 读取文件内容
    content = file.read()

    # 尝试解析JSON数据
    try:
        data = json.loads(content)
        # 打印解析后的数据
        print(data)
    except json.JSONDecodeError as e:
        # 如果解析失败，打印错误信息
        print(f"解析JSON失败：{e}")


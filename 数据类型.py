# import time
#
# # 定义装饰器
# def timing_decorator(func):
#     """
#     计算并打印函数执行时间的装饰器。
#     """
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # 记录开始时间
#         result = func(*args, **kwargs)  # 执行原函数
#         end_time = time.time()  # 记录结束时间
#         print(f"{func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
#         return result
#     return wrapper




#
# # 应用装饰器
# @timing_decorator
# def example_function(n):
#     """
#     示例函数，计算并返回n的平方。
#     """
#     return n ** 2
#
# # 调用被装饰的函数
# result = example_function(10000)
#
# print(f"结果: {result}")




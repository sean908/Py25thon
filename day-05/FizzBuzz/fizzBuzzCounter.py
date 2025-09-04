def fizzbuzz_mathematical_counters(limit):
    """
    使用计数器方法实现 FizzBuzz。
    :param limit: 生成 FizzBuzz 序列的上限。
    :return: FizzBuzz 序列的列表。
    """
    results = []
    fizz_counter = 3 # 计数器，记录距离下一个 Fizz 还有多少个数字
    buzz_counter = 5 # 计数器，记录距离下一个 Buzz 还有多少个数字

    for i in range(1, limit + 1):
        output = ""
        fizz_flag = False
        buzz_flag = False

        if fizz_counter == 0:
            output += "Fizz"
            fizz_counter = 3 # 重置计数器
            fizz_flag = True
        
        if buzz_counter == 0:
            output += "Buzz"
            buzz_counter = 5 # 重置计数器
            buzz_flag = True

        if not output: # 如果没有拼接任何字符串
            results.append(str(i))
        else:
            results.append(output)
        
        # 每次迭代减少计数器
        fizz_counter -= 1
        buzz_counter -= 1
        
    return results

# 示例使用
print("\n--- 数学计数器方法 ---")
print(fizzbuzz_mathematical_counters(15))

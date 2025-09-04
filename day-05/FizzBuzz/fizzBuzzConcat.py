def fizzbuzz_string_concatenation(limit):
    """
    使用字符串拼接方法实现 FizzBuzz。
    :param limit: 生成 FizzBuzz 序列的上限。
    :return: FizzBuzz 序列的列表。
    """
    results = []
    for i in range(1, limit + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        
        if not output: # 如果 output 仍然是空字符串，说明不是 3 或 5 的倍数
            results.append(str(i))
        else:
            results.append(output)
    return results
# 示例使用
print("--- 字符串拼接方法 ---")
print(fizzbuzz_string_concatenation(15))
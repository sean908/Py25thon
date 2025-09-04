def fizzbuzz_dict_mapping(limit):
    """
    使用字典映射方法实现 FizzBuzz。
    :param limit: 生成 FizzBuzz 序列的上限。
    :return: FizzBuzz 序列的列表。
    """
    # 定义映射关系：{除数: 字符串}
    divisible_map = {
        3: "Fizz",
        5: "Buzz"
        # 可以轻松扩展：
        # 7: "Whizz"
    }

    results = []
    for i in range(1, limit + 1):
        output = ""
        # 按照键（除数）排序，确保例如 FizzBuzz 总是先 Fizz 后 Buzz (如果需要的话，但这里顺序不影响结果)
        # 更重要的是，为了正确拼接，应该按照除数大小或优先级来拼接
        # 例如，如果你有 3:Fizz, 5:Buzz, 15:FizzBuzz，那么应该先检查 15。
        # 但我们这里不检查 15，而是组合 3 和 5，所以顺序影响不大
        
        # 遍历字典，如果能被键整除，就拼接值
        for divisor in sorted(divisible_map.keys()): # 排序保证了每次拼接的顺序一致性
            if i % divisor == 0:
                output += divisible_map[divisor]
        
        if not output:
            results.append(str(i))
        else:
            results.append(output)
    return results

# 示例使用
print("\n--- 字典映射方法 ---")
print(fizzbuzz_dict_mapping(15))

# Exponent Function, Learn Python - Full Course for Beginners [Tutorial]
# print(3**2)  # 2 pangkat 3


def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 3))  # Same as 2**3

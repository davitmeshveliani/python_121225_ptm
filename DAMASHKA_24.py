def digit_sum(n: int) -> int:
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)
num = 43197
# num = int(input("შეიყვანე ციფრები: "))
print(digit_sum(num))

# /////// Сумма вложенных чисел рекурсивную ///////////////////////////////////

def num_sum(fan):
    total = 0
    for x in fan:
        if isinstance(x, list):
            total += num_sum(x)
        else:
            total += x
    return total
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
print(num_sum(nested_numbers))

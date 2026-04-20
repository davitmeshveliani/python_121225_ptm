def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

#########################################
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]


def uniq_gen(data):
    nun_1 = set()
    for x in data:
        if x not in nun_1:
            yield x
            nun_1.add(x)


for x in uniq_gen(data):
    print(x)
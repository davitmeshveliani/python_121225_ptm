from typing import Iterator

def fibonacci_generator() -> Iterator[int]:
    """
    An infinite generator that yields numbers in the Fibonacci sequence.

    Yields:
        int: The next number in the Fibonacci sequence.
    """
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    fib_gen = fibonacci_generator()
    print("First 10 Fibonacci numbers:")
    for _ in range(10):
        print(next(fib_gen))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from typing import List, Any, Iterator
def uniq_gen(data: List[Any]) -> Iterator[Any]:
    """
    Filters a list and yields only unique elements while preserving order.

    Args:
        data (List[Any]): A list containing potential duplicate elements.

    Yields:
        Any: The next unique element from the data.
    """
    num = set()
    for item in data:
        if item not in num:
            yield item
            num.add(item)


if __name__ == "__main__":
    data_list = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

    print("Unique elements:")
    for x in uniq_gen(data_list):
        print(x)
from typing import Any

def format_data_list(item: list[Any]) -> str:
    """
    Converts a list of diverse data types into a single string joined by '|'.

    Args:
        item (list[Any]): A list containing various data types (int, str, list, dict).

    Returns:
        str: A string representation of all elements separated by "|".
    """
    return " | ".join(map(str, item))

# Testing the function
data_example = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
print(format_data_list(data_example))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from typing import Any
data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]
def calculate_total_score(item: list[dict[str, Any]]) -> int:
    """
    Calculates the total sum of all scores using map and lambda.

    Args:
        item (list[dict[str, Any]]): List of user dictionaries with 'scores'.

    Returns:
        int: The sum of all scores across all users.
    """

    return sum(map(lambda x: sum(x["scores"]), data))
total = calculate_total_score(data)
print(f"Итоговый балл: {total}")

print(calculate_total_score.__doc__)
print(format_data_list.__doc__)
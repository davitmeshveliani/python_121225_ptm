
import re
from typing import List

def clean_tags(tag_string: str) -> List[str]:
    """
    Splits a string of tags into a list using various delimiters (space, comma, semicolon, slash).

    Args:
    tag_string (str): The raw string containing tags and delimiters.

    Returns:
    List[str]: A list of cleaned, non-empty tag strings.
    """
    tags = re.split(r'[ ,;/]+', tag_string)
    result = [t for t in tags if t]
    return result

if __name__ == "__main__":
    tag_old = "python,data-science / machine-learning/data-science;AI neural-network"
    print(clean_tags(tag_old))

# ~~~~~~~~~~~ 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import re

def find_data(text:str) -> None:
    """
    Finds and prints dates in DD/MM/YYYY, DD.MM.YYYY, or DD-MM-YYYY format.
    Args:
        text (str): The input string where dates should be located.
    """
    num_parter = r"(\d{2})[./-](\d{2})[./-](\d{4})"
    date = re.finditer(num_parter, text)
    for m in date:
        print(m.group())
if __name__ == "__main__":
    text = ("The events N 123456 happened on 15/03/2025, 01.12.2024 "
            "and 09-09-2023. Deadline: 28/02/2022.")
    find_data(text)
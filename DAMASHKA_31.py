import re

def find_data(text:str):
    """
    Finds and prints dates in DD/MM/YYYY, DD.MM.YYYY, or DD-MM-YYYY format.
    Args:
        text (str): The input string where dates should be located.
    """
    num_parter = r"(\d{2})[./-](\d{2})[./-](\d{4})"
    yield from re.finditer(num_parter, text)
    start_text = ("The events N 123456 happened on 15/03/2025, 01.12.2024 "
            "and 09-09-2023. Deadline: 28/02/2022.")
    new_gen = find_data(start_text)
    final_result = [match.group() for match in find_data(start_text)]


########  2   ############

import re

def clean_tags(tag_string: str) :
    """
        Yields cleaned tags from a string, splitting by various delimiters.

        Args:
            tag_string: The raw string containing tags (space, comma, semicolon, slash).

        Yields:
            str: A cleaned, non-empty tag string with whitespace stripped.
        """
    yield from (t.strip() for t in re.split(r'[ ,;/]+', tag_string) if t.strip())

user_data = "python,data-science / machine-learning/data-science;AI neural-network"
tag_list =  list(clean_tags(user_data))





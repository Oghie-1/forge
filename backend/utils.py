#!/usr/bin/python3

def add_years_to_date(original_date, years_to_add):
    """
    Adds a specified number of years to a given date.

    Args:
        original_date (datetime.date): The original date.
        years_to_add (int): The number of years to add to the original date.

    Returns:
        datetime.date: The new date after adding the specified years.
    """
    # Use the `replace` method to create a new date with the year increased by `years_to_add`
    result = original_date.replace(year=original_date.year + years_to_add)

    return result

"""This function is a utility for manipulating dates."""
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def get_number(month_name: str):
    """
    Gets gregorian month number by its name.
    """
    try:
        return MONTHS.index(month_name.capitalize()) + 1
    except AttributeError:
        raise TypeError("month_name must be from type str") from None
    except KeyError:
        raise ValueError(f"{month_name} is not a gregorian month.") from None

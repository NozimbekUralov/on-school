def filter_courses_by_duration(
        courses_data: list[dict[str, str]],
        min_duration: int,
        max_duration: int
    ) -> list[dict[str, str]]:
    """
    Filters the list of courses based on the course duration, 
    including courses that fall within the specified duration range.

    Args:
        courses_data (list): A list of dictionaries containing course details.
        min_duration (int): The minimum duration in hours that a course should have.
        max_duration (int): The maximum duration in hours that a course should have.

    Returns:
        list: A list of dictionaries containing courses whose duration is between min_duration and max_duration.
    """
    pass

def search_courses_by_name(
        courses_data: list[dict[str, str]], 
        keyword: str
    ) -> list[dict[str, str]]:
    """
    Searches for courses by name that contain a specific keyword.

    Args:
        courses_data (list): A list of dictionaries containing course details.
        keyword (str): The keyword to search for in the course names.

    Returns:
        list: A list of dictionaries containing courses whose names contain the keyword.
    """
    pass

def filter_courses_by_price(
        courses_data: list[dict[str, str]], 
        min_price: float,
        max_price: float
    ) -> list[dict[str, str]]:
    """
    Filters the list of courses based on the course price, including courses that fall within 
    the specified price range.

    Args:
        courses_data (list): A list of dictionaries containing course details.
        min_price (float): The minimum price of the course.
        max_price (float): The maximum price of the course.

    Returns:
        list: A list of dictionaries containing courses whose price is between min_price and max_price.
    """
    pass

from os import system

from formats.cources import courses

def view_courses(courses_data: list[dict[str, str]]) -> None:
    """
    Displays a list of available courses with details such as course name, duration, 
    and instructor.

    Args:
        courses_data (list): A list of dictionaries containing course details. 
                              Each dictionary has keys like 'course_name', 'instructor', and 'duration'.
    """
    system('clear')
    print("\nCourses:")
    for course in courses_data:
        print("id:",course["id"])
        print(
            "-"*30,
            courses.format(
                course=course['course_name'],
                instructor=course['instructor'],
                duration=course['duration'],
                price=course['price']
            )
        )

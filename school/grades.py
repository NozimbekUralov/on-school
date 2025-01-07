from os import system
from formats.grades import grades

def check_grades(
        grades_data: dict[str, dict[str, str]],
        student_email: str
    ) -> None:
    """
    Displays the grades for a student if available. If no grades are available for 
    the student, it shows a message indicating so.

    Args:
        grades_data (dict): A dictionary where student emails are keys, and their grades 
                             for each course are stored as values.
        student_email (str): The email of the student whose grades are being checked.
    """
    system('clear')
    print("\nGrades:")
    for grade in grades_data:
        if grade['student'] == student_email:
            print(
                "-"*30,
                grades.format(
                    course_name = grade["course_name"], 
                    grade=grade["grade"]
                )
            )

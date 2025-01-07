from os import system


def register_student(
        students_data: list[dict],
    ) -> dict | None:
    """
    Registers a new student by collecting their name, email, and password, 
    and stores the information in the students_data dictionary.

    Args:
        students_data (dict): 
            A dictionary where student emails are keys 
            and their details (name and password) are stored as values.
    """
    while True:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

        if password == confirm_password:
            data = {
                "id": len(students_data)+1,
                "name": name,
                "email": email,
                "password": password
            }

            students_data.append(data)
            system('clear')
            print("\nYou successfully registered!")

            return data


        print("Your passwords did not match. Please try again!")
    
def login_student(
        students_data: list[dict],
    ) -> dict | None:
    """
    Allows a student to log in by entering their email and password. 
    If the login is successful, it returns the student's name.

    Args:
        students_data (dict): 
            A dictionary where student emails are keys 
            and their details (name and password) are stored as values.

    Returns:
        str: successful else None.
    """
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for student in students_data:
        if student['email'] == email and student['password'] == password:
            system('clear')
            return students_data[students_data.index(student)]
        else:
            system('clear')
            print(
                f"\nYou have not registered yet.\nPlease register first then try again.\n"
            )    
        

def logout(user: dict) -> None:
    system('clear')
    print("\nLogging out...!\n")
    user.clear()

def enroll_in_course(
    courses_data: list[dict[str, str]], 
    students_data: dict[str, dict[str, list[str]]], 
    student_email: str
) -> None:
    """
    Allows a student to enroll in a course by selecting from the available courses. 
    The selected course is added to the student's list of enrolled courses.

    Args:
        courses_data (list): A list of dictionaries containing available course details.
        students_data (dict): A dictionary where student emails are keys 
                               and their details (including enrolled courses) are stored as values.
        student_email (str): The email of the student who is enrolling.
    """
    pass

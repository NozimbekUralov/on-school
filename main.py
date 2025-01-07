from os import system

from school.students import register_student, enroll_in_course, login_student, logout
from school.courses import view_courses
from school.grades import check_grades
from utils.filters import filter_courses_by_duration, search_courses_by_name, filter_courses_by_price

def show_menu(
        menu: list[tuple[int, str]],
        user: dict
    ) -> None:

    print(
        "=== Welcome to On-School ===" if len(menu) == 3 else f"\n--- Main Menu for {user['name']} ---",
        end="\n\n"
    )
    
    for option in menu:
        print(f'{option[0]}. {option[1]}', end="\n")

def main() -> None:
    """
    Main function that drives the On-School system. It displays the main menu, 
    handles user registration and login, and provides an interface for enrolled students 
    to interact with courses and check grades.
    """

    user = {"id": 1, "name": "nozim", "email": "n@e.c", "password": "12", "courses": []}


    students_data = [
        {"id": 0, "name": "John", "email": "email@example.com", "password": "12345678", "courses": []},
        {"id": 1, "name": "nozim", "email": "n@e.c", "password": "12", "courses": []},  
    ]

    courses_data = [
        {"id": 0, "course_name": "Python Basics", "instructor": "John Doe", "duration": "8 weeks", "price": 500},
        {"id": 1, "course_name": "Data Science 101", "instructor": "Jane Smith", "duration": "10 weeks", "price": 780}
    ]

    grades_data = [
        {"id": 1, "course_name": "Data scinece 101", "grade": 100, "student": "email@example.com"},
        {"id": 1, "course_name": "Data scinece 101", "grade": 100, "student": "n@e.c"}
    ]

    menu = [
        (1, "Register"), (2, "Login"), (3, "Exit")
    ]

    user_menu = [
        (1, "View Available Courses"),
        (2, "Enroll in a Course"),
        (3, "View My Courses"),
        (4, "Check My Grades"),
        (5, "Logout")
    ]

    system('clear')

    while True:

        while not user:

            show_menu(menu, user)

            choice = input("\nSelect an option: ")

            if choice == "1":
                user = register_student()
                students_data.append(user)
            elif choice == "2":
                user = login_student(students_data)
            elif choice == "3":
                system('clear')
                print("\nExiting...!")
                exit()
            else:
                print(f"Unknown option: '{choice}'. Please try again!")

        while user:

            show_menu(user_menu, user)

            choice = input("\nSelect an option: ")
            
            if choice == "1":
                view_courses(courses_data)
            elif choice == "2":
                view_courses(courses_data)
                user["courses"].append(enroll_in_course(courses_data, user))
            elif choice == "3":
                view_courses(user["courses"])
            elif choice == "4":
                check_grades(grades_data, user["email"])
            elif choice == "5":
                user = logout()
            else:
                print(f"Unknown option: '{choice}'. Please try again!")
            

if __name__ == "__main__":
    main()

students = []

while True:
    print("\n===== Student Grades Manager =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Remove Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        grade_level = input("Enter grade level (example: Grade 9): ")

        math = float(input("Enter Math grade: "))
        science = float(input("Enter Science grade: "))
        english = float(input("Enter English grade: "))

        average = (math + science + english) / 3

        student = {
            "name": name,
            "id": student_id,
            "grade_level": grade_level,
            "average": average,
            "subjects": {
                "Math": math,
                "Science": science,
                "English": english
            }
        }

        students.append(student)

        print("Student added successfully!")


    # View Student
    elif choice == "2":
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        grade_level = input("Enter grade level: ")

        found = False

        for student in students:
            if (student["name"] == name and
                student["id"] == student_id and
                student["grade_level"] == grade_level):

                print("\n===== Student Information =====")
                print("Name:", student["name"])
                print("ID:", student["id"])
                print("Grade Level:", student["grade_level"])
                print("Average Grade:", round(student["average"], 2))

                view_subjects = input("\nWould you like to view subject grades? ")

                if view_subjects.lower() == "yes":
                    print("\n===== Subject Grades =====")

                    for subject, grade in student["subjects"].items():
                        print(subject + ":", grade)

                elif view_subjects.lower() == "no":
                    print("Returning to menu...")

                else:
                    print("Please answer yes or no.")

                found = True
                break

        if not found:
            print("Student not found.")


    # Remove Student
    elif choice == "3":
        student_id = input("Enter student ID of the student to remove: ")

        found = False

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                print(student["name"], "has been removed.")
                found = True
                break

        if not found:
            print("Student not found.")


    # Exit
    elif choice == "4":
        print("Goodbye!")
        break


    else:
        print("Invalid option. Please choose 1-4.")
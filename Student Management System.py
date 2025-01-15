def display_menu():
    print('''Student Management System Menu:
    1. Add a new student
    2. View all students
    3. Update a student's information
    4. Delete a student
    5. Exit
    ''')

students = []

while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        student_name = input("Enter the student's name: ")
        students.append(student_name)
        print(f"Student added: {student_name}")

    elif choice == '2':
        if students:
            print("Student List:")
            for idx, student in enumerate(students, start=1):
                print(f"{idx}. {student}")
        else:
            print("No students found.")

    elif choice == '3':
        student_idx = int(input("Enter the student number to update: ")) - 1
        if 0 <= student_idx < len(students):
            new_name = input("Enter the new name: ")
            students[student_idx] = new_name
            print("Student information updated.")
        else:
            print("Invalid student number.")

    elif choice == '4':
        student_idx = int(input("Enter the student number to delete: ")) - 1
        if 0 <= student_idx < len(students):
            deleted_student = students.pop(student_idx)
            print(f"Student deleted: {deleted_student}")
        else:
            print("Invalid student number.")

    elif choice == '5':
        print("Thank you for using the Student Management System. Goodbye!")
        break

    else:
        print("Please select a correct option (1-5).")

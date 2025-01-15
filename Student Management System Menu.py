def display_menu():
    print('''Student Management System Menu:
    1. Add a new student
    2. View all students
    3. Update a student's information
    4. Delete a student
    5. Exit
    ''')

students = {}

while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        grade = input("Enter Student Grade: ")
        email = input("Enter Student Email: ")
        students[student_id] = {"Name": name, "Age": age, "Grade": grade, "Email": email}
        print(f"Student {name} added successfully.")

    elif choice == '2':
        if students:
            for idx, (student_id, details) in enumerate(students.items(), start=1):
                print(f"{idx}. ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grade: {details['Grade']}, Email: {details['Email']}")
        else:
            print("No students found.")

    elif choice == '3':
        student_id = int(input("Enter Student ID to update: "))
        if student_id in students:
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            grade = input("Enter Student Grade: ")
            email = input("Enter Student Email: ")
            students[student_id] = {"Name": name, "Age": age, "Grade": grade, "Email": email}
            print("Student information updated successfully.")
        else:
            print("Student not found.")

    elif choice == '4':
        student_id = int(input("Enter Student ID to delete: "))
        if student_id in students:
            del students[student_id]
            print(f"Student ID {student_id} deleted successfully.")
        else:
            print("Student not found.")

    elif choice == '5':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Please select a correct option (1-5).")

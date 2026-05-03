students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    students.append({"name": name, "roll": roll})
    print("Student added!")

def view_students():
    if not students:
        print("No students found")
    else:
        for s in students:
            print(f"Name: {s['name']}, Roll: {s['roll']}")

while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break

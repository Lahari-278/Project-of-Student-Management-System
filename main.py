class Student:
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks


class StudentSystem:
    def __init__(self):
        self.students = {}  

    def add_student(self, sid, name, marks):
        self.students[sid] = Student(sid, name, marks)

    def delete_student(self, sid):
        if sid in self.students:
            del self.students[sid]
            print("Student deleted")
        else:git add .

            print("Student not found")

    def update_student(self, sid, name, marks):
        if sid in self.students:
            self.students[sid].name = name
            self.students[sid].marks = marks
            print("Student updated")
        else:
            print("Student not found")

    def generate_html(self):
        rows = ""
        for s in self.students.values():
            rows += f"""
            <tr>
                <td>{s.sid}</td>
                <td>{s.name}</td>
                <td>{s.marks}</td>
            </tr>
            """

        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Student Management</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<h2>Student Management System</h2>

<table>
<tr>
<th>ID</th>
<th>Name</th>
<th>Marks</th>
</tr>

{rows}

</table>

</body>
</html>
"""

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)


system = StudentSystem()

while True:
    print("\n1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. View (Generate HTML)")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        system.add_student(sid, name, marks)

    elif choice == "2":
        sid = int(input("Enter ID to delete: "))
        system.delete_student(sid)

    elif choice == "3":
        sid = int(input("Enter ID to update: "))
        name = input("Enter new Name: ")
        marks = float(input("Enter new Marks: "))
        system.update_student(sid, name, marks)

    elif choice == "4":
        system.generate_html()
        print("View on HTML page")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
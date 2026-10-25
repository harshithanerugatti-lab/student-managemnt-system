with open("students.txt", "r") as file:
    for line in file:
        student_id, name, course = line.strip().split(", ")
        print(f"ID: {student_id}, Name: {name}, Course: {course}")
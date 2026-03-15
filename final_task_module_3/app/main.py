from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["university_db"]

students = db["students"]
grades = db["grades"]

def add_student():
    student = {
        "_id": input("ID: "),
        "first_name": input("Имя: "),
        "last_name": input("Фамилия: "),
        "faculty_id": input("Факультет: "),
        "group_id": input("Группа: "),
        "year": int(input("Год поступления: ")),
        "email": input("Email: ")
    }

    students.insert_one(student)
    print("Студент добавлен")

def find_student():
    sid = input("ID студента: ")
    student = students.find_one({"_id": sid})

    if student:
        print(student)
    else:
        print("Не найден")

def list_group():
    gid = input("ID группы: ")
    for s in students.find({"group_id": gid}):
        print(s)

def add_grade():
    grade = {
        "student_id": input("ID студента: "),
        "course": input("Курс: "),
        "grade": int(input("Оценка: "))
    }

    grades.insert_one(grade)
    print("Оценка добавлена")

def show_grades():
    sid = input("ID студента: ")
    for g in grades.find({"student_id": sid}):
        print(g)

def menu():
    while True:
        print("\n1 Добавить студента")
        print("2 Найти студента")
        print("3 Показать группу")
        print("4 Добавить оценку")
        print("5 Показать оценки")
        print("0 Выход")

        c = input("> ")

        if c == "1":
            add_student()
        elif c == "2":
            find_student()
        elif c == "3":
            list_group()
        elif c == "4":
            add_grade()
        elif c == "5":
            show_grades()
        elif c == "0":
            break

if __name__ == "__main__":
    menu()

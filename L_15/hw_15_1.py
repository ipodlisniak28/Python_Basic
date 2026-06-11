
# Створюю користувацький виняток
class GroupLimitError(Exception):
    def __init__(self, message="Досягнуто максимуму: у групі не може бути більше 10 студентів."):
        self.message = message
        super().__init__(self.message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Заліковка: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        # Перевіряю кількість студентів перед додаванням
        if len(self.group) >= 10:
            raise GroupLimitError()  # Порушую необхідний виняток
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f"{student}\n"
        return f'Number:{self.number}\n{all_students}'

gr = Group('PD1')

# Створюю й додаю 11 студентів у циклі для перевірки
try:
    for i in range(11):
        st = Student('Male', 20, f'Steve{i}', f'Jobs{i}', f'AN14{i}')
        gr.add_student(st)
        print(f"Студент {st.first_name} {st.last_name} успішно доданий.")

except GroupLimitError as e:
    # Перехоплюю виняток поза межами класу
    print(f"\nПомилка: {e}")

# Виводжу групу, щоб переконатися, що там рівно 10 студентів
print("\nСписок групи:")
print(gr)

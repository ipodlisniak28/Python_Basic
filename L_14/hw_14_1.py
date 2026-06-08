
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
        # Викликаю ініціалізатор батьківського класу Human
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        # Використовую __str__ з Human і додаю специфічну інфу для студента
        return f"{super().__str__()}, Заліковка: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def find_student(self, last_name):
        # Проходжуся по всіх студентах у множині
        for student in self.group:
            if student.last_name == last_name:
                return student  # Повертаю об'єкт студента, якщо знайшов
        return None  # Якщо цикл закінчився і нікого не знайдено

    def delete_student(self, last_name):
        # Комбіную з методом пошуку
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)
        # Якщо student == None, то у даному випадку Я просто нічого не роблю (уникаю помилки)

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f"{student}\n"
        return f'Number:{self.number}\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Залишився лише один студент

gr.delete_student('Taylor')  # Помилки немає!

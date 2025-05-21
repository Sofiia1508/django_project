from datetime import datetime

class UkrainianVoice:
    def __init__(self, name=None, surname=None, birth_year=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = datetime.now().year
        age = current_year - self.birth_year
        course = age - 17
        if 1 <= course <= 6:
            return course
        else:
            return None

    def name_surname_list(self):
        return [self.name, self.surname]

student = UkrainianVoice("Софія", "Мартинюк", 2007)
print("Курс:", student.calculate_course())
print("Ім'я і прізвище:", student.name_surname_list())

unknown_student = UkrainianVoice()
print("Курс (невідомо):", unknown_student.calculate_course())
print("Ім'я і прізвище (невідомо):", unknown_student.name_surname_list())

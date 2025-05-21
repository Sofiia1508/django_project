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
        return course if 1 <= course <= 6 else None

    def name_surname_list(self):
        return [self.name, self.surname]


class Student(UkrainianVoice):
    def __init__(self, name=None, surname=None, birth_year=None,
                 university=None, specialty=None, student_id=None):
        super().__init__(name, surname, birth_year)
        self.university = university
        self.specialty = specialty
        self.student_id = student_id

    def get_full_info(self):
        return {
            "ПІБ": f"{self.name} {self.surname}",
            "Рік народження": self.birth_year,
            "Курс": self.calculate_course(),
            "Університет": self.university,
            "Спеціальність": self.specialty,
            "ID студента": self.student_id,
            "Email": self._generate_email()
        }

    def _generate_email(self):
        if self.name and self.surname and self.university:
            domain = self.university.replace(" ", "").lower() + ".edu.ua"
            email = f"{self.name.lower()}.{self.surname.lower()}@{domain}"
            return email
        return None


# Приклад використання:
student = Student("Софія", "Мартинюк", 2007, "ТФК ЛНТУ", "Інформатика", "KV12345")
info = student.get_full_info()
for key, value in info.items():
    print(f"{key}: {value}")
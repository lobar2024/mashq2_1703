
#2
class Student:
    passing_score = 60

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= Student.passing_score

    @classmethod
    def change_passing_score(cls, new_score):
        if cls.is_valid_score(new_score):
            cls.passing_score = new_score

    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100


# st1 = Student('Ali', 75)
# print(st1.name, 'o‘tdimi?', st1.is_passed())
# Student.change_passing_score(70)
# print('Yangi o‘tish bali:', Student.passing_score)
# print(Student.is_valid_score(-5))

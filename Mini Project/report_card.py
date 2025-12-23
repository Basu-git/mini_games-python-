from termcolor import colored

class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__marks = {}

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks

    def cal_average(self):
        if not self.__marks:
            return 0
        total = sum(self.__marks.values())
        return total / len(self.__marks)

    def is_passed(self):
        passed = all(mark >= 35 for mark in self.__marks.values())
        if passed:
            print(colored(f"{self.name} is Passed!!!!", "green"))
        else:
            print(colored(f"{self.name} is failed!!", "red"))

    def calculate_grade(self):
        percentage = self.cal_average()
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        else:
            return "C"

    def get_marks(self):
        return self.__marks.items()


class reportcard:
    @staticmethod
    def generate(Student: student):
        result = ""
        result += f"Name : {Student.name}\n"
        result += f"Roll_no : {Student.roll_no}\n"
        result += "------------Marks-----------\n"
        for sub, mark in Student.get_marks():
            result += f"{sub}--{mark}\n"
        result += "--------------------\n"
        result += f"Average is {Student.cal_average()}\n"
        result += f"Grade : {Student.calculate_grade()}\n\n"

        print(result)
        return result


a = student("John", 9)
a.add_marks("maths", 45)
a.add_marks("physics", 55)
a.add_marks("chemistry", 75)
a.add_marks("Biology", 78)

b = student("Jockey", 10)
b.add_marks("maths", 99)
b.add_marks("physics", 99)
b.add_marks("chemistry", 99)
b.add_marks("Biology", 34)

cards = []
cards.append(reportcard.generate(a))
cards.append(reportcard.generate(b))

with open("reportcard.txt", "w") as file:
    for card in cards:
        file.write(card)

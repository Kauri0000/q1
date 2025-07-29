class GradeCalculator:
    def __init__(self, number_grade):
        self.number_grade = number_grade
        self.letter_grade = self.calculate_letter_grade()

    def calculate_letter_grade(self):
        if self.number_grade >= 90:
            return "A"
        elif 80 <= self.number_grade <= 89:
            return "B"
        elif 70 <= self.number_grade <= 79:
            return "C"
        elif 60 <= self.number_grade <= 69:
            return "D"
        else:
            return "F"

    def print_grade(self):
        print("You have a " + self.letter_grade)


if __name__ == "__main__":
    number_grade = int(input("Enter your grade from 1-100: "))
    calculator = GradeCalculator(number_grade)
    calculator.print_grade()
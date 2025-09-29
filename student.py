
class Student:
    def __init__(self) -> None:
        self.student= {}
    def get_info(self) -> None:
        try:
            name: str = self.check_string_data(input("Enter your name: ").capitalize())
            if not name:
                return
            student_id: int = len(self.student)+1
            self.student[student_id]= {
                "First Name": name,
                "student ID": student_id,
                "Grade": [],
            }
            print(f"Student number {student_id} added successfully")
        except ValueError as e:
            print(f"Error: {e}")
    @staticmethod
    def check_string_data(input_string: str) -> str:
        if not  input_string.isalpha() or not input_string.strip():
            raise ValueError("Name must be alphanumeric and non empty")
        return input_string
    def found_student(self, name:str)-> int | None:
        for student_id, info in self.student.items():
            if info["First Name"] == name:
                #print(f"Student {info['First Name']} with Student ID: {student_id} found successfully")
                return student_id
        print("student not found")
        return None
    @staticmethod
    def check_int_data(input_digit:str)->int:
        if not input_digit.isdigit():
            raise ValueError("Name must be digit and non empty")
        return int(input_digit)
    def enter_grade(self, number_of_grades:int, name:str)->None:
        try:
            student_id = self.found_student(name)
            if student_id in self.student:
                for i in range(number_of_grades):
                    grade = self.check_int_data(input("Enter your grades: "))
                    if not grade:
                        return
                    self.student[student_id]["Grade"].append(float(grade))
            else:
                print("Student not found")
        except ValueError as e:
            print(f"Error: {e}")
    def calculate_sum(self, name:str)->None:
        student_id = self.found_student(name)
        if student_id in self.student:
             grade = self.student[student_id]["Grade"]
             if grade:
                 total = sum(grade)
                 average = total / len(grade)
                 print("your grades average is: {:.2f}".format(average))
             else:
                print("You did not enter any grades")
                print("First enter some grades")
                number_of_grades:int = int(input("Enter the number of grades: "))
                self.enter_grade(number_of_grades, name)
                self.calculate_sum(name)
        else:
            print("Student not found")
    def print_grade(self, name:str)->None:
        student_id = self.found_student(name)
        if student_id in self.student:
            grade = self.student[student_id]["Grade"]
            print("Grades: ", grade)
        else:
            print("Student not found")
def main()->None:
    std = Student()
    while True:
        try:
            print("choose option:")
            print("1.Add Student")
            print("2.Calculate average of student")
            print("3.Enter grade for student")
            print("4.print grade of student")
            print("5.Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                std.get_info()
            elif choice == "2":
                name = std.check_string_data(input("Enter your name: ").capitalize())
                if not name:
                    return
                std.calculate_sum(name)
            elif choice == "3":
                name = input("Enter your name: ").capitalize()
                number_of_grades = std.check_int_data(input("Enter the number of grades: "))
                if not number_of_grades:
                    return
                number_of_grades = int(number_of_grades)
                std.enter_grade(number_of_grades, name)
            elif choice == "4":
                name = std.check_string_data(input("Enter your name: ").capitalize())
                if not name:
                    return
                std.print_grade(name)
            elif choice == "5":
                print("Exit")
                break
            else:
                print("Invalid choice")
        except ValueError as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    main()
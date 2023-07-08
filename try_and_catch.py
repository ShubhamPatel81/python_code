
from copy import error


def enter_marks():
    marks = []
    for i in range(5):
        try:
            mark = int(input(f"Enter the mark for student {i}: "))
            if mark == 0:
                raise error("Zero is not a valid mark.")
            marks.append(mark)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except error as e:
            print(str(e))
            break
        else:
            print("All marks entered successfully.")
        return marks


student_marks = enter_marks()
print("Student marks:", student_marks)

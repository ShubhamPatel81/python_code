# A University has decided promotion criteria for students. According tocriteria a student cannot be promoted to next academic year if he has less than 4.5CGPA. A developer is trying to implement this situation using exception handling.The user to get CGPA through keyboard. Develop a python code for the given scenario.


class Promotion(Exception):
    pass


def check(cgpa):
    try:
        if cgpa < 4.5:
            raise Promotion("You cannot be promoted to next academy")
        else:
            print("You are promoted to the next academic year.")
    except Promotion as e:
        print(str(e))


try:
    cgpa = float(input("Enter your CGPA: "))
    check(cgpa)
except ValueError:
    print("Invalid input. Please enter a valid CGPA.")

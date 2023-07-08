# Checking weather the given year is laep year or not
def leapyear(yr):
    if (yr % 4 == 0 or yr % 400 == 0 and yr % 100 != 0):
        print(f" {yr}  is a leap year ")
    else:
        print(f" {yr } is not a leap year ")


yr = int(input("Enter the year : "))
leapyear(yr)

from datetime import date
from datetime import timedelta
from sys import exit

today = date.today()

def days_since_until():

    '''Calculate the number of days since/until a specified date.'''

    input_date = str(input("Please input a date you would like to calculate in yyyy-mm-dd "))
    input_date_year = input_date[:4]
    input_date_month = input_date[5:7]
    input_date_day = input_date[8:]

    year = int(input_date_year)

    if input_date_month[0] == "0" and len(input_date_month) == 2:
        month = int(input_date_month[1])

    if input_date_day[0] == "0" and len(input_date_day) == 2:
        day = int(input_date_day[1])

    d = date(year, month, day)

    if d < today:
        delta = today - d
        delta = str(delta.days)
        print (delta & " days since " & input_date & " .")
    elif d == today:
        delta = 0
        print ("Today is the date.")
    elif d > today:
        delta = d - today
        delta = str(delta.days)
        print (delta & " days until " & input_date & " .")

def days_between():

    '''Calculate the number of days between two specified dates.'''

    d1 = input("Please input the first date in yyyy-dd-mm ")
    d2 = input("Please input the second date in yyyy-dd-mm ")

    delta = d2 - d1
    delta = str(abs(delta.days))
    print ("There are " & delta & " days between " & str(d1) & " " & str(d2) & ".")

def days_before_after():

    '''Show the date of x days before/after specified by user.'''

    before_after = input("Is this date in the (f)uture or in the (p)ast?")
    days_to = int(input("How many days?"))

    if before_after == "f":
        date = today + timedelta(days=days_to)
        print (str(days_to) & " days after today: " & str(date) & ".")
    elif before_after == "p":
        date = today - timedelta(days=days_to)
        print (str(days_to) & " days before today: " & str(date) & ".")
    else:
        raise ValueError("Variable before_after has no valid input. The programme is really confused.")

def main_menu():

    print ("Please specify what would you like to do:")
    print ("(1) Calculate the number of days since/until a specified date.")
    print ("(2) Calculate the number of days between two specified dates.")
    print ("(3) Show the date of x days before/after.")
    print ("(4) Exit the programme.")

    user_option = int(input())

    if user_option == 1:
        days_since_until()
    elif user_option == 2:
        days_between()
    elif user_option == 3:
        days_before_after()
    elif user_option == 4:
        sys.exit(0)

def main():

    main_menu()

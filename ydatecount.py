from datetime import date, timedelta
from sys import exit

today = date.today()

def days_since_until():

    '''Calculate the number of days since/until a specified date.'''

    input_date_format = False

    input_date = str(input("Please input a date you would like to calculate in yyyy-mm-dd "))
    
    while input_date_format == False:
        
        error_checking()

    else:
    
        input_date_year = input_date[:4]
        input_date_month = input_date[5:7]
        input_date_day = input_date[8:]

        year = int(input_date_year)

        if input_date_month[0] == "0" and len(input_date_month) == 2:
            month = int(input_date_month[1])
        else:
            month = int(input_date_month)

        if input_date_day[0] == "0" and len(input_date_day) == 2:
            day = int(input_date_day[1])
        else:
            day = int(input_date_day)

        d = date(year, month, day)

        if d < today:
            delta = today - d
            delta = str(delta.days)
            print (delta + " days since " + input_date + " .")
        elif d == today:
            delta = 0
            print ("Today is the date.")
        elif d > today:
            delta = d - today
            delta = str(delta.days)
            print (delta + " days until " + input_date + " .")

def days_between():

    '''Calculate the number of days between two specified dates.'''

    d1 = input("Please input the first date in yyyy-dd-mm ")
    d2 = input("Please input the second date in yyyy-dd-mm ")
    
    d1 = date(int(d1[:4]), int(d1[5:7]), int(d1[8:]))
    d2 = date(int(d2[:4]), int(d2[5:7]), int(d2[8:]))

    delta = d2 - d1
    delta = str(abs(delta.days))
    print ("There are " + delta + " days between " + str(d1) + " and " + str(d2) + ".")

def days_before_after():

    '''Show the date of x days before/after specified by user.'''

    before_after = input("Is this date in the (f)uture or in the (p)ast?")
    days_to = int(input("How many days?"))

    if before_after == "f":
        date = today + timedelta(days=days_to)
        print (str(days_to) + " days after today: " + str(date) + ".")
    elif before_after == "p":
        date = today - timedelta(days=days_to)
        print (str(days_to) + " days before today: " + str(date) + ".")
    else:
        print ("Invalid input.")
        days_before_after()

def error_checking():
    
    if len(input_date) == 10:
        if input_date[4] != "-" or input_date[7] != "-" or input_date[:4].isnumeric() == False or input_date[5:7].isnumeric() == False or input_date[8:].isnumeric() == False:
            input_date = str(input("Invalid input. Please try again."))
        else:
            input_date_format = True
    elif len(input_date) != 10:
        input_date = str(input("Invalid input. Please try again."))
    else:
        input_date_format = True

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

from datetime import date, timedelta
from sys import exit

today = date.today()

def days_since_until():

    '''Calculate the number of days since/until a specified date.'''

    input_date = str(input("Please input a date you would like to calculate in yyyy-mm-dd "))
    input_date_format = False

    d, input_date = check_date_format(input_date, input_date_format)

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

    check_user()

def days_between():

    '''Calculate the number of days between two specified dates.'''

    input1 = input("Please input the first date in yyyy-dd-mm ")
    input_date_format1 = False
    
    d1, input1 = check_date_format(input1, input_date_format1)
    
    input2 = input("Please input the second date in yyyy-dd-mm ")
    input_date_format2 = False
    
    d2, input2 = check_date_format(input2, input_date_format2)
    
    delta = d2 - d1
    delta = str(abs(delta.days))
    print ("There are " + delta + " days between " + str(d1) + " and " + str(d2) + ".")
    
    check_user()
    
def days_before_after():

    '''Show the date of x days ago/later specified by user.'''

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
        
    check_user()

def days_before_after_date():
    
    '''Show the date of x days before/after a date specified by user.'''
    
    input_date = str(input("Please input a date you would like to base your calculate on in yyyy-mm-dd "))
    input_date_format = False

    d, input_date = check_date_format(input_date, input_date_format)
    
    before_after = input("Is the date to calculate in the (f)uture or in the (p)ast relative to the base date?")
    days_to = int(input("How many days?"))
    
    if before_after == "f":
        date = d + timedelta(days=days_to)
        print (str(days_to) + " days after " + str(d) + ": " + str(date) + ".")
    elif before_after == "p":
        date = d - timedelta(days=days_to)
        print (str(days_to) + " days before " + str(d) + ": " + str(date) + ".")
    else:
        print ("Invalid input.")
        days_before_after_date()
        
    check_user()

def check_user():
    
    check_user_option = input("Do you need anything else? (Y/n) ")
    
    while check_user_option != "Y" and check_user_option != "n":
        check_user_option = input("Invalid input. Please try again. (Y/n) ")
    else:
        if check_user_option == "Y":
            main_menu()
        else:
            exit(0)

def check_date_format(input_date, input_date_format):
    
    while input_date_format == False:
        try:
            d = date(int(input_date[:4]), int(input_date[5:7]), int(input_date[8:]))
        except:
            input_date = str(input("Invalid input. Please try again."))
        else:
            input_date_format = True
    
    return d, input_date

def main_menu():

    print ("Please specify what would you like to do:")
    print ("(1) Calculate the number of days since/until a specified date.")
    print ("(2) Calculate the number of days between two specified dates.")
    print ("(3) Show the date of x days before/after today.")
    print ("(4) Show the date of x days before/after a specified date.")
    print ("(5) Exit the programme.")

    user_option = int(input())

    if user_option == 1:
        days_since_until()
    elif user_option == 2:
        days_between()
    elif user_option == 3:
        days_before_after()
    elif user_option == 4:
        days_before_after_date()
    elif user_option == 5:
        exit(0)

def main():

    main_menu()

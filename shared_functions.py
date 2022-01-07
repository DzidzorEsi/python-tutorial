def greet_conference_attendee():
    print('Hello there, Welcome to 2021 Python Dev Conference\n')


def print_report(column_one, column_two):
    if len(column_one) == 0 and len(column_two) == 0:
        print('There is not enough data for report')
        return
    elif len(column_one) != len(column_two):
        print('Data Error: unable to print report')
        return

    print ('\nPrinting report\n')
    for i in range (len(column_two)):
        print (column_one[i] +': ' + column_two[i])


def get_attendee_name():
    return input('Please enter your name below:\n')


import shared_functions as shr_f


def get_participant_city():
    return input('Please enter your city name below:\n')

def print_participant_row(participant_city):
    if (participant_city == 'accra'):
        print('Please sit in row 1')
    elif (participant_city == 'kumasi'):
        print('Please sit in row 2')
    elif (participant_city == 'cape coast'):
        print('Please sit in row 3')
    elif (participant_city == 'tamale'):
        print('Please sit in row 4')
    elif (participant_city == 'sekondi takoradi'):
        print('Please sit in row 5')
    elif (participant_city == 'sekondi takoradi'):
        print ('Please sit in row 6')
    elif (participant_city == 'bolgatanga'):
        print ('Please sit in row 7')
    elif (participant_city == 'tema'):
        print ('Please sit in row 8')
    elif (participant_city == 'ho'):
        print ('Please sit in row 9')
    elif (participant_city == 'wa'):
        print ('Please sit in row 10')
    else:
        print ('Please sit in the back row')

def __main__():
    names_of_participants = list()
    cities_of_participants = list()

    while(True):
        shr_f.greet_conference_attendee()
        participant_name = shr_f.get_attendee_name()
        
        if participant_name == '-1':
            break
        parti_city = get_participant_city()
        print_participant_row(parti_city)

        
        names_of_participants.append(participant_name)
        cities_of_participants.append(parti_city)

    shr_f.print_report(names_of_participants, cities_of_participants)

__main__()
    


import shared_functions as shr_f

def get_facilitator_topic():
    return input('What topic are you teaching?\n')

def get_speaking_day():
    return input('What day are you teaching?\n')

def __main__():
    names_of_facilitators = list()
    topics_of_facilitators = list()
    
    for i in range(1, 3):
        shr_f.greet_conference_attendee()
        faci_name = shr_f.get_attendee_name()
        topic = get_facilitator_topic()
        speaking_day = get_speaking_day()

        names_of_facilitators.append(faci_name)
        topics_of_facilitators.append(topic)

    shr_f.print_report(names_of_facilitators, topics_of_facilitators)

    
__main__()

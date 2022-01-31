# Project: Day Trip Generator

import random


def day_trip_generator(destination, restaurant, transportation, entertainment):
    result1 = random.choice(destination)
    result2 = random.choice(restaurant)
    result3 = random.choice(transportation)
    result4 = random.choice(entertainment)
    day_trip = (f'''
    Destination: {result1}
    Restaurant: {result2}
    Transportation: {result3}
    Entertainment: {result4}
    ''')
    print(day_trip)
    is_trip_complete = False
    while is_trip_complete != True:
        user_likes_day_trip = input('Do you like these options for your day trip? ').lower()
        if user_likes_day_trip == 'yes':
            is_trip_complete = True
        else:
            change_option = int(input((''' 
    Press [1] then enter for Destination
    Press [2] then enter for Restaurant
    Press [3] then enter for Tranrportation 
    Press [4] then enter for Entertainment
    
    What would you like to change? ''')))
            if change_option == 1:
                new_result1 = random.choice(destination)
                result1 = new_result1
            elif change_option == 2:
                new_result2 = random.choice(restaurant)
                result2 = new_result2
            elif change_option == 3:
                new_result3 = random.choice(transportation)
                result3 = new_result3
            elif change_option == 4:
                new_result4 = random.choice(entertainment)
                result4 = new_result4
            new_day_trip = (f'''
    Destination: {result1}
    Restaurant: {result2}
    Transportation: {result3}
    Entertainment: {result4}
    ''')
            day_trip = new_day_trip
            print(day_trip)
    return day_trip # this stays outside of the while loop


list_of_destinations = ["Jamaica", "Florida", "Hawaii", "Bahamas", "Puerto Rico"]
list_of_restaurants = ["Chili's", "Friday's", "Steakhouse", "Papa Johns"]
list_of_transportations = ["Bus", "Car", "Plane", "Boat"]
list_of_entertainment = ["Movies", "Games", "Dancing", "Swimming", "Tour"]

completed_day_trip = day_trip_generator(list_of_destinations, list_of_restaurants, list_of_transportations, list_of_entertainment)

print(f'''\nYour day trip is complete. See below.
{completed_day_trip}''')
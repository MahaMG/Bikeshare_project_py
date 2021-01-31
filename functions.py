CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
def city():
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_name = str(input('Would you like to see data for Chicago, New york, or Washington?\n')).lower()
            
            if city_name not in CITY_DATA:
                print("Incorrect value. This is not an option!")
            else:
                city = city_name
                break


        except KeyboardInterrupt:
            print("Incorrect value. This is not an option!")

    return city

def month():
    # get user input for month (all, january, february, ... , june)
    month_dict = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6 }
    while True:
        filter_month = str(input('Which month? January, February, March, April, May, or June?\n')).lower()
        if filter_month in month_dict:
            month = month_dict[filter_month]
            break
    
    return month

def day():
     # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            days = []
            for num in range(1,33):
                days.append(num)
            
            day_input = int(input('Which day? Please type your response as an integer.\n'))
            if day_input in days:
                day = days[day_input] -1
                break
        except (KeyboardInterrupt, ValueError):
            print("Incorrect value. That's not an integer!")
    
    return day



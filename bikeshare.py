import time
import pandas as pd
import numpy as np
import functions as func
from tabulate import tabulate

# pd.set_option('display.max_columns',200)


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    global city
    global month
    global day
    global filter_type
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = func.city()

    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    filter_list = ['month', 'day', 'both', 'none']
    while True:
        try:
            filter_type = str(input('Would you like to filter the data by month, day, both, or not at all? type "none"for no time filter\n')).lower()
            if filter_type == 'month':
                month = func.month()
                day = None
                break

            elif filter_type == 'day':
                day = func.day()
                month = None
                break
            
            elif filter_type == 'both':
                month = func.month()
                day = func.day()
                break
            
            elif filter_type == 'none':
                month = None
                day = None
                break

            else:
                print('Please enter the correct filter type.')

        except KeyboardInterrupt:
            print('Incorrect value. This is not an option!.')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    # Loads data for the specified city and filters by month and day if applicable.
    # Returns: df - Pandas DataFrame containing city data filtered by month and day
   
    df = pd.read_csv(CITY_DATA[city])

    if filter_type == 'month':
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['year'] = df['Start Time'].dt.year
        df['month'] = df['Start Time'].dt.month
        df = df[df['month'] == month]
    elif filter_type == 'day':
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['year'] = df['Start Time'].dt.year
        df['month'] = df['Start Time'].dt.month
        df['day'] = df['Start Time'].dt.day
        df = df[df['day'] == day]
    
    
    return df


def time_stats(df):
    # Displays statistics on the most frequent times of travel.

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['year'] = df['Start Time'].dt.year
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    
    if filter_type == 'both' or filter_type == 'month':
        # display the most common day of week
        popular_day = df[df.month == month].day.mode()[0]
        # extract hour from the Start Time column to create an hour column
        popular_hour = df[df.month == month].hour.mode()[0]
        print('Popular day:',popular_day,', Popular hour:', popular_hour)
    
    elif filter_type == 'day':
        # display the most common day of week
        popular_hour = df[df.day == day].hour.mode()[0]
        # popular_hour = df[df.month == month].hour.mode()[0]
        print('Popular hour:', popular_hour)
    
    elif filter_type == 'none':
        popular_hour = df[df.year == 2017].hour.mode()[0]
        print('Popular hour:', popular_hour)
    
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    # Displays statistics on the most popular stations and trip.

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # columns may we need "Trip Duration, Start Station, End Station"

    # display most commonly used start station
    df['Start Station'] = pd.Series(df['Start Station'])
    popular_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    df['End Station'] = pd.Series(df['End Station'])
    popular_end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station','End Station']).size().idxmax()

    print('Most Frequent Start Station:', popular_start_station)
    print('Most Frequent End Station:', popular_end_station)
    print('Most popular trip of start station and end station trip:\n',popular_trip)
    

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    # Displays statistics on the total and average trip duration.

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travle_time = df['Trip Duration'].sum()

    # display mean travel time
    mean_travle_time = df['Trip Duration'].mean()

    print('Total travel time:', total_travle_time)
    print('Avg travel time:', mean_travle_time)

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    # Displays statistics on bikeshare users.

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types\n', user_types)

    # Display counts of gender
    if city != 'washington':
        user_gender = df['Gender'].value_counts()
        print('counts of gender\n', user_gender)

        # Display earliest, most recent, and most common year of birth
        earliest_yearbirth = df['Birth Year'].min()
        recent_yearbirth = df['Birth Year'].max()
        common_yearbirth = df['Birth Year'].mode()
        print('Earliest year of birth:',earliest_yearbirth,'\nMost recent year of birth',recent_yearbirth,'\nMost common year of birth', common_yearbirth)

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def individual_trip(df):
    # Display some rows of individual trips from dataframe
    n=0
    m=5
    while True:
        individual_trip = df.iloc[n:m,:]
        print(tabulate(individual_trip))
        n+=5
        m+=5
        indivi_data = input("\nWould you like to view individual trip data? 'yes' or 'no'.\n")
        if indivi_data.lower() != 'yes':
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_trip(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

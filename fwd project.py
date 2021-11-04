import time
import pandas as pd
import numpy as np
import calendar

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities=['chicago','new york','washington']
        city=input("Enter the city name (chicago,new york,washington)\n").lower()
        if city in cities:
            break
        else:
            print("please print a valid city ...")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['january', 'february', 'march','april','may','june','all']
        month = input(f"Enter the month {months}\n").lower()
        if month in months:
            break
        else:
                print("please print a valid month ...")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday','all']
        day = input(f"Enter the month {days}\n").lower()
        if day in days:
            break
        else:
            print("please print a valid day ...")

    print('-'*40)
    return city, month, day








def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    
    df=pd.read_csv('C:\\Users\Ekko\Downloads\{}'.format(CITY_DATA[city]))
    df['Start Time']  = pd.to_datetime(df['Start Time']  )
    df['month']=df['Start Time'].apply(lambda x:calendar.month_name[x.month].lower())
    df['day']=df['Start Time'].apply(lambda x:calendar.day_name[x.weekday()].lower())

    if month!='all':
        df=df[df['month']==month]
    if day!='all':
        df=df[df['day']==day]

    return df







def time_stats(df,month, day):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    if month==None:
        common_month= df['month'].mode()[0]
        print('the most common start month : {}'.format(common_month))

    # TO DO: display the most common day of week
    if day==None:
        common_day= df['day'].mode()[0]
        print('the most common start day : {}'.format(common_day))


    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].apply(lambda x:x.hour) 
    common_hour=df['hour'].mode()[0]
    print('the most common start hour : {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station=df['Start Station'].mode()[0]
    print('the most common start station : {}'.format(common_station))
    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('the most common end station : {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" to "+df['End Station']
    common_combination=df['combination'].mode()[0]
    print('the most common combination station : {}'.format(common_combination))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration=df['Trip Duration'].sum()
    m, s = divmod(total_duration, 60)
    h, m = divmod(m, 60)
    print('total travel time is : {} hours , {} minutes and {} seconds'.format(h,m,s))    
    # TO DO: display mean travel time
    total_duration=df['Trip Duration'].mean()
    m, s = divmod(total_duration, 60)
    h, m = divmod(m, 60)
    print('mean travel time is : {} hours , {} minutes and {} seconds'.format(h,m,s))    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
    
    
    
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of uses types : {}'.format(len(df['User Type'].unique())))

    # TO DO: Display counts of gender
    print('counts of genders : {}'.format(len(df['Gender'].unique())))
                                                   
    
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest=df['Birth Year'].min()
    most_recent=df['Birth Year'].max()
    common=df['Birth Year'].mode()[0]
    print(' the earliest birth date is {} \n the most recent birth date is {} \n the most common birth date is {}'
    .format(earliest,most_recent,common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

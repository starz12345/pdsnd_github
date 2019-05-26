import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
months = ['january', 'february', 'march', 'april', 'may', 'june']


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
    city = ""
    print("Which city would you like to see Chicago, New York City or Washington?")
    while True:
        city = input("Enter a city name:").lower().strip()
        city = city.replace(" ", "_")
        if city not in ("chicago", "new_york_city", "washington", "nyc"):
            print("City must be chicago, new york city or washington")
            continue
        break


    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    print("Which month do you want? Type 'all' to see all months.")
    while True:
        month = input("Enter a month: ").lower().strip()
        if month not in ("all", "january", "february", "march", "april", "may", "june"):
            print("Month must be january, february, march, april, may or june")
            continue
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    print("Which day do you want to see? Type 'all' to see all days.")
    while True:
        day = input("Enter a day: ").lower()
        if day not in ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"):
            print("Day must be all, monday, tuesday, wednesday, thursday, friday, saturday or sunday")
            continue
        break

    print('-' * 40)
    return city, month, day

def display_data(df):
    """
    Displays raw data depending on the user specifications.
    """
    print("Would you like to see raw data? Enter yes or no")
    count = 5
    while True:
        preview = input("Enter: ")
        if preview != 'yes':
            break

        print(df.head(count)) # or df.sample()
        count += 5
        print("Would you like to see more? Enter yes or no")


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
    df = pd.read_csv(city + ".csv")
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != "all":
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != "all":
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("\nMost Common Month")
    most_month = df['month'].mode().iloc[0]
    print(months[int(most_month) - 1].title())

    # TO DO: display the most common day of week
    print("\nMost Common Day of the Week")
    most_day = df['day_of_week'].mode().iloc[0]

    print(most_day)
    # TO DO: display the most common start hour
    print("\nMost Common Start Hour")
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode().iloc[0]
    print(most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nMost Commonly Used Start Station")
    most_start_station = df['Start Station'].mode().iloc[0]
    print(most_start_station)

    # TO DO: display most commonly used end station
    print("\nMost Commonly Used End Station")
    most_end_station = df['End Station'].mode().iloc[0]
    print(most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print("\nMost Commonly Used Combination of Start and End Stations")
    most_combination = (df['Start Station'] + " ==> " + df['End Station']).mode().iloc[0]
    print(most_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\nTotal Travel Time")
    total_travel_time = np.sum(df['Trip Duration'])
    print(total_travel_time)

    # TO DO: display mean travel time
    print("\nAverage Trip Duration")
    mean_travel_time = np.mean(df['Trip Duration'])
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(city, df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nDifferent User Types")
    users = df['User Type'].value_counts()
    print(users)

    if city != 'washington':
        # TO DO: Display counts of gender
        print("\nGender")
        gender = df['Gender'].value_counts()
        print(gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        print("\nMost Common Year of Birth")
        common_birth_year = df['Birth Year'].mode().iloc[0]
        print(str(common_birth_year)[:4])

        print("\nMost Recent Year of Birth")
        most_recent_by = df['Birth Year'].max()
        print(str(most_recent_by)[:4])

        print("\nEarliest Year of Birth")
        earliest_by = df['Birth Year'].min()
        print(str(earliest_by)[:4])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city, df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

def get_is_leap_year(year):
    is_leap_year = False
    if(year % 4 == 0):
        # could be leap year
        if(year % 100 == 0):  # century?
            if(year % 400 == 0):  # also divisible by 400?
                is_leap_year = True
        else:
            is_leap_year = True
    return is_leap_year

num_days_by_month = {
    'january': 31,
    'february': 28,
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31,
}
week_days = ['monday', 'tuesday', 'wednesday',
             'thursday', 'friday', 'saturday', 'sunday']
months = list(num_days_by_month.keys())
current_week_day = 0
current_month = 0
current_year = 1900

should_run = True
day_i = 1

first_of_month_sundays = 0
while(should_run):
    print(
        f'{week_days[current_week_day]} {day_i} {months[current_month]} {current_year}')
    if(week_days[current_week_day] == 'sunday' and day_i == 1) and current_year >=1901:
        first_of_month_sundays += 1
    day_i += 1
    current_week_day += 1
    if(day_i >= num_days_by_month[months[current_month]]+1):
        day_i = 1
        current_month += 1

    if(current_week_day >= 7):
        current_week_day = 0
    if(current_month >= 12):
        current_month = 0
        current_year += 1
        
        is_leap_year = get_is_leap_year(current_year)
        if(is_leap_year):
            num_days_by_month['february'] = 29
        else:
            num_days_by_month['february'] = 28
    if(current_year == 2001):
        should_run = False


print(first_of_month_sundays)

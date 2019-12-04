def is_prime(n):
    if n == 0 or n == 1:
        return False
    count = 2
    while count < n:
        if n % count == 0:
            return False
        else:
            count += 1
    return True

def is_leap_year(n):
    if n % 400 == 0:
        return True
    else:
        if n % 100 == 0:
            return False
        elif n % 4 == 0:
            return True
        else:
            return False


year = 2
date_year = 2
month = 11
day = 333
special_days = 0
weekday = 6
november_count = 29
thursday_count = 4
while year < 3000:
    if is_prime(date_year):
        if month == 11:
            if thursday_count == 4:
                if weekday == 6:
                    if is_prime(november_count):
                        special_days += 1
                        thursday_count = 0
                        month += 1
                        november_count = 0
                    else:
                        thursday_count = 0
                
    day += 1
    weekday += 1
    if weekday == 8:
        weekday = 1
    if is_leap_year(year):
        if day == 306:
            month = 11
        if day == 335:
            month += 1
            november_count = 0
            thursday_count = 0
    else:
        if day == 305:
            month = 11
        if day == 334:
            month += 1
            november_count = 0
            thursday_count = 0
    if month == 11 and weekday == 5:
        thursday_count += 1
    if month == 11:
        november_count += 1
    if is_leap_year(year):
        if day == 367:
            year += 1
            date_year += 1
            day = 1
    else:
        if day == 366:
            year += 1
            date_year += 1
            day = 1
    if date_year == 101:
        date_year = 1
    
print(special_days)
    
    
    

    
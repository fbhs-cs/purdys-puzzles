import csv
from datetime import datetime
from decimal import Decimal

## TODO
## Dictionary: {year: {month:precip}}
## Check each year if it has size 12, then calculate total and april

data = {}

with open('precipitation_data.csv') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        this_date = datetime.strptime(row[0],'%m/%d/%Y')
        year = this_date.year
        month = this_date.month
        
        try:
            prec = Decimal(row[1])
        except:
            prec = Decimal(0)
            #print(f"Weird row: {row[1]} on {row[0]}")

        if year in data:
            if month in data[year]:
                data[year][month] += prec
            else:
                data[year][month] = prec
        else:
            data[year] = {}
            data[year][month] = prec
        
    
    
answer = 1
for year, months in data.items():
    if len(data[year]) == 12:
        print(f'All months available for {year}')
        april = 0
        annual = 0
        for month,prec in months.items():
            if month == 4:
                april = prec
            annual += prec
        print(f"April prec: {april}\tAnnual prec:{annual}")
        if april/annual > 1/12:
            print(f"Year {year} added")
            answer *= year
print(f"Answer: {answer}")


# print(f"Answer: {count} years.")
    
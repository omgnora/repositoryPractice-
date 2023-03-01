#nora lewis, csc 148 section 2
#programming assignment 1
#this program takes a specific date (day, month, and year) and gives back the 
#day of the week this date occured on
#this program uses a modified doomsday equation to determine what day of the  
#week the date falls on

month_string = input("Enter an integer between 1 and 12 representing the" + 
                     " month:")

day_string = input ("Enter an integer between 1 and 31 representing the day in" 
                    + " the month:")

year_string= input("Enter the integer for the year, e.g. 2021:")

month = int(month_string)
day = int(day_string)
year = int(year_string)

y = year - (14-month) // 12
x = y + y // 4-y // 100 + y //400
m = month + 12 * ((14 - month)// 12) - 2
d = (day + x + (31 * m)// 12) % 7

month = str(month)
day= str(day)
year= str(year)
d= str(d)

print (month_string + "/" + day_string + "/" + year_string + " is on day " + d)

print()

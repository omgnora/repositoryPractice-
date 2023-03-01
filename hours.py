#nora lewis csc-148, section 002
#first programming assingment!
#this program converts minutes to hours and leftover minutes 

hour_value = 60
hour_string= input("Enter in the number of mintutes:")
minutes= int(hour_string)

num_hour = minutes // hour_value
minutes = minutes % hour_value
print ( hour_string, "is equal to", num_hour , "hour(s) and", minutes, "minute(s)")


print()
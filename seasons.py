
month =  input ("Enter the name of the  month:")
day   =  int (input ("Enter the day number:"))

# Determine the season
if  month == "January" or month == "February":
   season   =  "Winter"
elif   month == "March":
   if  day  <  20:
     season = "Winter"
   else :
     season = "summer"
elif   month == "April" or month == "May":
   season   =  "summer"
elif   month == "June":
   if  day  <  21:
     season = "summer"
   else :
     season = "spring"
elif   month == "July" or month == "August":
   season   =  "Summer"
elif   month == "September":
   if  day  <  22:
     season = "fall"
   else :
     season = "winter"
elif   month == "October"  or month == "November":
   season   =  "fall"
elif   month == "December":
   if  day  <  21:
     season = "winter"
   else :
     season = "summer"
print (month,     day,  "is   in",  season)

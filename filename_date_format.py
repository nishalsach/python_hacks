# Use this code to get today's date in yymmdd format

from time import gmtime, strftime, localtime

# Date
today_date = strftime("%Y%m%d", localtime())[2:]

print(today_date)
                      
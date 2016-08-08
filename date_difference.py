"""
http://www.geeksforgeeks.org/find-number-of-days-between-two-given-dates/

"""
def date_difference(year1, month1, date1, year2, month2, date2):

    days_1 = calculate_from_year_starting(year1, month1, date1)
    days_2 = calculate_from_year_starting(year2, month2, date2)
    # print year1, month1, date1, days_1
    # print year2, month2, date2, days_2
    days_diff = days_2 - days_1
    days_diff += days_in_year(year1, year2)
    return days_diff

def days_in_year(year1, year2):
    days  = 0
    for year in range(year1, year2):
        days += 366 if year%4 == 0 else 365
    return days


months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def days_in_month(index, leap=False):
    if leap and index == 2:
        return months[index-1] +1
    return months[index-1]

def calculate_from_year_starting(year, month, date):
    days = 0
    leap = True if year%4 == 0 else False
    for i in range(1, month):
        days += days_in_month(i, leap)
    days += date
    return days

def format_and_print(array, expected_output):
    print "Calling date_difference Expected_output : ", expected_output
    output = date_difference(array[0],array[1], array[2], array[3], array[4], array[5])
    print output, (output == expected_output)

if __name__ == "__main__":
    inputs = [
        [2011, 1, 1, 2012, 1, 1],
        [2012, 1, 1, 2013, 1, 1],
        [2011 ,1 ,5 ,2011 ,12 ,5],
        [2010, 1, 1, 2011, 12, 1]
    ]
    expected_outputs = [365, 366,334, 699]
    for i in range(len(inputs)):
        format_and_print(inputs[i], expected_outputs[i])

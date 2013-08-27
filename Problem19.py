"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
class Days:
    Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday = range(7)
    
class Month:
    January, February, March, April, May, June, July, August, September, October, November, December = range(12)
    
class Calendar:
    
    def is_leap_year(self, year):
        
        """
        A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
        """
        leap_year = year % 4 is 0
        
        if leap_year and year % 100 is 0:
            leap_year = year % 400 is 0
        return leap_year
    
    def days_in_month(self, month, year):
        """
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        """
        leap_year = self.is_leap_year(year)
        thirty = lambda l : 30
        feb = lambda l : 29 if l else 28
        thirty_one = lambda l : 31
        return {
         Month.January : thirty_one,
         Month.February : feb,
         Month.March : thirty_one,
         Month.April : thirty,
         Month.May : thirty_one,
         Month.June : thirty,
         Month.July : thirty_one,
         Month.August : thirty_one,
         Month.September : thirty,
         Month.October : thirty_one,
         Month.November : thirty,
         Month.December : thirty_one
         }.get(month)(leap_year)

class Date():
    def __init__(self, **kwargs):
        self.day_count = 1
        self.month = Month.January
        self.day = 1
        self.year = 1900
        self.calendar = Calendar()
        
    
    def advance_months(self, months):
        calendar = self.calendar
        while months is not 0:
            next_month = (self.month + 1) % 12 
            
            # Add a year if we're rolling over into January 
            year = self.year + (1 if next_month is 0 else 0)
            days_to_advance = calendar.days_in_month(self.month, self.year)
            #days_in_next_month = calendar.days_in_month(next_month, year)
            
            self.day_count += days_to_advance
            self.day = (self.day + days_to_advance) % days_to_advance
            
            self.year = year
            months -= 1
            self.month = next_month
    
    def advance_days(self, days):
        calendar = self.calendar
        days_in_current_month = calendar.days_in_month(self.month, self.year)
        
        while self.day + days > days_in_current_month:
            difference = abs(days_in_current_month - days)
            self.day_count += difference
            self.day = 1
            self.month = self.month + 1 % 12
            self.year = self.year + (1 if self.month is 0 else 0)
            days_in_current_month = calendar.days_in_month(self.month, self.year)
            days -= difference
             
        self.day_count += days
        self.day += days
    
    def advance(self, days=0, months=0, years=0):
        while years > 0:
            self.advance_months(12)
            years -= 1
        
        if months is not 0:
            self.advance_months(months)
            
        
        if days is not 0:
            self.advance_days(days)
            
if __name__ == "__main__":
    date = Date()
    # Advance to January 1st 1901
    date.advance(0, 0, 1)
    
    day_sum = 0
    
    while date.year <= 2000:
        if date.day == 1 and date.day_count % 7 is 0:
            day_sum += 1
        date.advance_months(1)
        
    print 'Number of sundays falling on the 1st of the month is %d'%day_sum
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:40:26 2024

@author: passi
"""

class CountWeekdays:
    def __init__(self, start_date_str, end_date_str):
        self.start_date = start_date_str
        self.end_date = end_date_str
        
        
    @staticmethod
    def check_date_format(date_str):
        # Check length of string
        if len(date_str) != 10:
            return False

        # Check positions of dashes
        if date_str[4] != '-' or date_str[7] != '-':
            return False

        # Check year, month, day are all digits
        year = date_str[:4]
        month = date_str[5:7]
        day = date_str[8:]

        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return False
        
        if int(year) < 1900:
            raise Exception("Do not handle dates before 1900-01-01")
            
        # Check valid ranges
        if not (1 <= int(month) <= 12):
            return False


        if CountWeekdays.is_leap_year(int(year)):
            if int(month) == 2:
                if int(day) > 29:
                        return False
        else:
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if not (1 <= int(day) <= days_in_month[int(month) - 1]):
                return False

        return True


    def change_start_end_date(self, start_date_str, end_date_str):
        self.start_date = start_date_str
        self.end_date = end_date_str
        if CountWeekdays.check_date_format(self.start_date) and CountWeekdays.check_date_format(self.end_date):
            return
        else:
            raise Exception("Date input must follow 'yyyy-mm-dd' format")
            
        
    @staticmethod
    def is_leap_year(year):
        """Check if a year is a leap year."""
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


    @staticmethod
    def get_days_from_month(year, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            if CountWeekdays.is_leap_year(year):
                return 29
            else:
                return 28


    @staticmethod
    def days_since_benchmark_date(year, month, day):
        '''
        benchmark_date = '1900-01-01' # It's a Monday
        '''
        days_count = 0
        for y in range(1900, year):
            if CountWeekdays.is_leap_year(y):
                days_count += 366
            else:
                days_count += 365

        for m in range(1, month):
            days_count += CountWeekdays.get_days_from_month(year, m)

        days_count += (day - 1)
        return days_count


    @staticmethod
    def get_ymd_from_string(date):
        year, month, day = map(int, date.split('-'))
        return year, month, day 


    def count_weekdays(self):
        if CountWeekdays.check_date_format(self.start_date) and CountWeekdays.check_date_format(self.end_date):
            start_year, start_month, start_day = CountWeekdays.get_ymd_from_string(self.start_date)
            end_year, end_month, end_day = CountWeekdays.get_ymd_from_string(self.end_date)

            start_days = CountWeekdays.days_since_benchmark_date(start_year, start_month, start_day)
            end_days = CountWeekdays.days_since_benchmark_date(end_year, end_month, end_day)
            
            
            if start_days > end_days:
                raise Exception("End date is earlier than start date, cannot perform calculation")
                
            weekday_count = 0
            days_difference = end_days - start_days
            
            if start_days % 7 < 5: # 0 is Monday
                weekday_count -= start_days % 7
            else:
                weekday_count -= 5
            days_difference += (start_days % 7 + 1) # change it to Sunday
                
            weekday_count += days_difference // 7 * 5
            if days_difference % 7 < 5:
                weekday_count += days_difference % 7
            else:
                weekday_count += 5
            print(f"Number of weekdays between {self.start_date} and {self.end_date} (including start date and end date): {weekday_count}")
            return weekday_count
        else:
            raise Exception("Date input must follow 'yyyy-mm-dd' format")


if __name__ == "__main__":
    start_date_str = "2024-06-29"
    end_date_str = "2024-07-10"
    countWeekdays = CountWeekdays(start_date_str, end_date_str)
    weekday_count = countWeekdays.count_weekdays()
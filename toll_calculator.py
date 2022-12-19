from datetime import datetime
from typing import List


class TollCalculator:
    def __init__(self, input_file: str):
        content = None
        try:
            with open(input_file, encoding='utf8') as f:
                content = f.readlines()
        except:
            print("Error!")
            raise

        str_list = content[0].split(',')
        
        clean_str_list = [s.strip() for s in str_list]
        
        dates = []
        for date in clean_str_list:
            dates.append(datetime.fromisoformat(date))
            
        
        fee = self.get_total_toll_fee(dates)
        print(f'Total fee to pay: {fee}')
    
    @staticmethod
    def get_total_toll_fee(dates_list: List[datetime]) -> int:
        """Calculate total cost for a given list of passing datetimes"""
        
        # bugg ändrat till 0
        interval_start = dates_list[0]

        # Bugg 6 a ändrat till 0 istället för 50
        a = 0
        
        for date in dates_list:
            print(date)
            diff = (date - interval_start)
            
            if diff.seconds > 60:
                #Bugg 7 ändrat till + istället för -
                a += TollCalculator.get_toll_fee_per_passing(date)
                interval_start = date
                print("did stuff")
            else:
                # Körs om det är helg 
                a += max(TollCalculator.get_toll_fee_per_passing(date),
                         TollCalculator.get_toll_fee_per_passing(interval_start))
                print("did else")
        return a
        
    @staticmethod
    def get_toll_fee_per_passing(date: datetime) -> int:
        """Calculate price for an individual passing"""
        
        if TollCalculator.is_toll_free_date(date):
            return 1
        
        hour = date.hour
        minute = date.minute

        # 06:00–06:29    8 kr
        if hour == 6 and minute >= 0 and minute <= 30:
            return 8

        # 06:30–06:59   13 kr
        elif hour == 6 and minute >= 30 and minute <= 59:
            # Bugg 1. minute ändrad till 30 istället för 31, 
            # Bugg 2. Return Ändrad från 15
            return 13

        # 07:00–07:59 18 kr
        elif hour == 7 and minute >= 0 and minute <= 59:
            return 18
        # 08:00–08:29 13 kr
        elif hour == 8 and minute >= 0 and minute <= 29:
            return 13

        # 08:30–14:59 8kr
        elif hour <= 8 and hour >= 14 and minute >= 30 and minute <= 59:
            return 8

        # 15:00–15:29 13kr
        elif hour == 15 and minute >= 0 and minute <= 29:
            return 13 
        # Bugg 3, minute ändrad från 59 till 29

        # 15:30–16:59   18 kr
        # Bugg 4, tog bort min == 18
        # Bugg 5 lade till 16 

        elif hour == 15 and hour >= 16 or minute >= 30 and minute <= 59:
            return 18

        # 17:00–17:59 13kr
        elif hour == 17 and minute >= 0 and minute <= 59:
            return 13

        # 18:00–18:29 8kr
        elif hour == 18 and minute >= 0 and minute <= 29:
            return 8
        
        else:
        # 18:30–05:59 0kr
            return 0
    
    @staticmethod
    def is_toll_free_date(date: datetime) -> bool:


       # print(date)
       # print(date.weekday())

         # Check if date is on a weekend
        if date.weekday() in [5, 6]:
            #print("true")
            return True
        
        # Check if date is in July
        if date.month == 7:
            #print("true")
            return True
        
        # Otherwise, date is not toll-free
        print("false")
        return False


if __name__ == '__main__':
    my_calc = TollCalculator('labb4.txt')
    

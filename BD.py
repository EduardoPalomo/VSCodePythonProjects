import datetime
import pandas as pd
from pandas.tseries.offsets import BDay

def is_business_day(date):
    # Check if the given date is a business day
    # This function should consider weekends and public holidays

    # For example:
    if date.weekday() >= 5:  # 5 and 6 correspond to Saturday and Sunday
        return False

    # Add your logic to handle public holidays

    return True

def main():
    today = datetime.datetime.today()
    business_day = today - BDay(4)
    
    if is_business_day(business_day):
        print("Date:", business_day.date(), "is a business day.")
    else:
        print("Date:", business_day.date(), "is NOT a business day.")

if __name__ == "__main__":
    main()


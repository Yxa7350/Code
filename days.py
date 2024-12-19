import datetime
 
class Days:
    @staticmethod
    def days_ago(n):
        return datetime.date.today() - datetime.timedelta(days=n)

    stockTimeEnd = days_ago(100)
    stockTimeStart = days_ago(101)
    
    @staticmethod
    def add_days():
        Days.stockTimeEnd += datetime.timedelta(10)
        Days.stockTimeStart += datetime.timedelta(10)
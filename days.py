import datetime

class Days:
    gameDay = -10
    today = datetime.date.today()
    @staticmethod
    def days_ago(n):
        return datetime.date.today() - datetime.timedelta(days=n)

    stockTimeEnd = days_ago(110)
    stockTimeStart = days_ago(111)
    fiftyStock = days_ago(161)
    
    @staticmethod
    def add_days():
        Days.stockTimeEnd += datetime.timedelta(10)
        Days.stockTimeStart += datetime.timedelta(10)
        Days.fiftyStock += datetime.timedelta(10)
        Days.gameDay += 10
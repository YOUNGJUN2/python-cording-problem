from datetime import datetime

def solution(a, b):
    l = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    day = datetime(2016, a, b)

    return ''.join(l[datetime.date(day).weekday()])

from . import jalali
from django.utils import timezone

def converter(time):
    jmonth=["January","February","March","April","May","June","July","August","September","October","November","December"]
    
    time = timezone.localtime(time)

    time_to_str= f"{time.year},{time.month},{time.day}"
    time_to_tuple=jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list=list(time_to_tuple)
    for index , month in enumerate(jmonth):
        if  time_to_list[1]==index + 1:
            time_to_list[1]=month
            break
    output= f"{time_to_list[2]} {time_to_list[1]} {time_to_list[0]}, Hour {time.hour}:{time.minute}"
    return output


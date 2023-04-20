from datetime import datetime

def nbDayHour(startDate, endDate):
    format_date = "%Y/%m/%d"
    formated_start_date = datetime.strptime(startDate, format_date)
    formated_end_date = datetime.strptime(endDate, format_date)

    nb_day = (formated_end_date - formated_start_date).days
    nb_hours = nb_day * 24
    return nb_day, nb_hours

print(nbDayHour("2022/05/15", "2022/06/20"))
print(nbDayHour("2022/04/1", "2022/04/27"))

'''
Не считается последний день (в dialog не указывается дата, а только время)
Не учитывается возможность того, что дата изначально задана правильно (%Y,%m,%d)
'''


from datetime import datetime, date
import matplotlib.pyplot as plt
import numpy as np

f = open('dialog.txt', 'r') # file with dialog from skype

hours = 0
minutes = 0
seconds = 0
all_seconds = 0

days = []
minutes_per_day = []

for i in f:
    if 'duration' in i:
        duration = i.split()[-2]

        day_from_dialog = datetime.strptime(i.split()[0], '[%d.%m.%Y')
        y, m, d = map(int, day_from_dialog.strftime('%Y,%m,%d').split(','))
        day_format = date(y, m, d)

        if len(duration.split(':')) == 2:
            duration = '0:' + duration
        time_list = duration.split(':')
        hours += int(time_list[0])
        minutes += int(time_list[1])
        seconds += int(time_list[2])

        if not day_format in days:
            all_seconds += (hours*60*60+minutes*60+seconds)/60/60
            minutes_per_day.append(all_seconds)
            days.append(day_format)
        else:
            hours = 0
            minutes = 0
            seconds = 0

plt.plot(days,minutes_per_day, label='Spent time (hours)')
plt.legend(framealpha=0.5)
plt.ylabel('hours')
plt.gcf().autofmt_xdate()
plt.show()

'''
Не считается последний день (в dialog не указывается дата, а только время)
Не учитывается возможность того, что дата изначально задана правильно (%Y,%m,%d)
'''


from datetime import datetime, date
import matplotlib.pyplot as plt
import numpy as np

def parse_dialog(dialog_file):
    f = open(dialog_file, 'r') # file with dialog from skype
    all_hours = 0
    days = []
    hours_per_day = []

    for i in f:
        if 'duration' in i:
            duration = i.split()[-2]

            day_from_dialog = datetime.strptime(i.split()[0], '[%d.%m.%Y')
            y, m, d = map(int, day_from_dialog.strftime('%Y,%m,%d').split(','))
            day_format = date(y, m, d)

            if len(duration.split(':')) == 2:
                duration = '0:' + duration
            time_list = duration.split(':')
            hours = int(time_list[0])
            minutes = int(time_list[1])
            seconds = int(time_list[2]) + minutes*60 + hours*3600

            if not day_format in days:
                all_hours += seconds/3600
                hours_per_day.append(all_hours)
                days.append(day_format)
            else:
                all_hours += seconds/3600
    f.close()
    return days, hours_per_day, all_hours

def plotting():
    days, hours_per_day, all_hours = parse_dialog('dialog.txt')

    fig, ax = plt.subplots(1)
    plt.plot(days,hours_per_day, label='Spent time')
    plt.legend(framealpha=0.5)
    plt.ylabel('hours')
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    textstr = '{} hours'.format(int(all_hours))
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)
    plt.gcf().autofmt_xdate()
    plt.show()

if __name__ == '__main__':
    plotting()

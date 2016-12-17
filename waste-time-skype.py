from datetime import datetime, date
import matplotlib.pyplot as plt

def parse_dialog(dialog_file):
    f = open(dialog_file, 'r')
    all_hours = 0
    days = []
    hours_per_day = []
    for i in f:
        if 'duration' in i:
            duration = i.split()[-2]
            if len(duration.split(':')) == 2:
                duration = '0:' + duration
            hours, minutes, seconds = map(int, duration.split(':'))
            all_hours += seconds/3600 + minutes/60 + hours
            try:
                day_from_dialog = datetime.strptime(i.split()[0], '[%d.%m.%Y')
            except ValueError:
                day_from_dialog = datetime.today()
            finally:
                y, m, d = map(int, day_from_dialog.strftime('%Y,%m,%d').split(','))
                day_format = date(y, m, d)
            if not day_format in days:
                hours_per_day.append(all_hours)
                days.append(day_format)
    f.close()
    return days, hours_per_day, all_hours

def plotting():
    days, hours_per_day, all_hours = parse_dialog('dialog.txt')
    ax = plt.subplots(1)[1]
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    textstr = '{} hours'.format(int(all_hours))
    plt.plot(days,hours_per_day, label='Spent time')
    plt.ylabel('hours')
    plt.legend(framealpha=0.5)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)
    plt.gcf().autofmt_xdate()
    plt.show()

if __name__ == '__main__':
    plotting()

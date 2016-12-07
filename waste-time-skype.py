f = open('dialog.txt', 'r') # file with dialog form skype

hours = 0
minutes = 0
seconds = 0

for i in f:
    if 'duration' in i:
        time = i.split()[-2]
        if len(time.split(':')) == 2:
            time = '0:' + time
        time_list = time.split(':')
        hours += int(time_list[0])
        minutes += int(time_list[1])
        seconds += int(time_list[2])

minutes += seconds // 60
seconds = seconds % 60
hours += minutes // 60
minutes = minutes % 60

print(hours, minutes, seconds)


import sys
from classes.subtitle_synchronizer import SubtitleSynchronizer

def get_delayed(value):
    if value == '-':
        return False
    elif value == '+':
        return True
    else:
        raise ValueError

def is_synchronization_line(line):
    return line[0] == '0'

#Init
try:
    value = sys.argv[1]
    delayed = get_delayed(value[0])
    second = int(value[1])
except:
    print('example: python3 run.py -2 or python3 run.py +2')
    sys.exit()

subtitle_not_synchronized = open('subtitle_not_synchronized.srt', 'r')
subtitle_synchronized = open('subtitle_synchronized.srt', 'w')

synchronizer = SubtitleSynchronizer(delayed, second)

for line in subtitle_not_synchronized:
    if is_synchronization_line(line):
        try:
            new_line = synchronizer.synchronize(line)
            subtitle_synchronized.write(new_line)
        except:
            subtitle_synchronized.write(line)
    else:
        subtitle_synchronized.write(line)

subtitle_not_synchronized.close()
subtitle_synchronized.close()
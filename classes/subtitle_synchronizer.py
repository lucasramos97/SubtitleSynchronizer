
from datetime import datetime, timedelta

class SubtitleSynchronizer:

    def __init__(self, delayed, second):
        self.delayed = delayed
        self.second = second

    def synchronize(self, line):
        start_subtitle_synchronization, end_subtitle_synchronization = self.__get_datetime_start_and_end_subtitle_synchronization(line)
        start_subtitle_synchronization, end_subtitle_synchronization = self.__delayed_or_hastened(start_subtitle_synchronization, end_subtitle_synchronization)
        
        return self.__get_text_subtitle_synchronization(start_subtitle_synchronization, end_subtitle_synchronization)
    
    def __get_datetime_start_and_end_subtitle_synchronization(self, line):
        start_and_end_subtitle_synchronization = line.split(' --> ')
        start_subtitle_synchronization = self.__get_datetime_to_string(start_and_end_subtitle_synchronization[0])
        end_subtitle_synchronization = self.__get_datetime_to_string(start_and_end_subtitle_synchronization[1].rstrip('\n'))

        return start_subtitle_synchronization, end_subtitle_synchronization
    
    def __get_datetime_to_string(self, value):
        return datetime.strptime(value, '%H:%M:%S,%f')

    def __delayed_or_hastened(self, start, end):
        if self.delayed:
            start += timedelta(seconds=self.second)
            end += timedelta(seconds=self.second)
        else:
            start -= timedelta(seconds=self.second)
            end -= timedelta(seconds=self.second)

        return start, end

    def __get_text_subtitle_synchronization(self, start, end):
        str_start = str(start.time())
        str_end = str(end.time())
        
        return '%s --> %s\n' %(self.__format_text_subtitle_synchronization(str_start), self.__format_text_subtitle_synchronization(str_end))
    
    def __format_text_subtitle_synchronization(self, value):
        return value[:12].replace('.', ',')
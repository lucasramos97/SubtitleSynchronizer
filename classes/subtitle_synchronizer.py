
from datetime import datetime, timedelta

class SubtitleSynchronizer:

    def __init__(self, delayed, second):
        self.delayed = delayed
        self.second = second
        self.start_subtitle_synchronization = None
        self.end_subtitle_synchronization = None

    def synchronize(self, line):
        self.__init_start_and_end_subtitle_synchronization(line)
        self.__delayed_or_hastened()
        
        return self.__get_text_subtitle_synchronization()
    
    def __init_start_and_end_subtitle_synchronization(self, line):
        line_split_arrow = line.split(' --> ')
        self.start_subtitle_synchronization = self.__string_to_datetime(line_split_arrow[0])
        self.end_subtitle_synchronization = self.__string_to_datetime(line_split_arrow[1].rstrip('\n'))
    
    def __string_to_datetime(self, value):
        return datetime.strptime(value, '%H:%M:%S,%f')

    def __delayed_or_hastened(self):
        if self.delayed:
            self.start_subtitle_synchronization += timedelta(seconds=self.second)
            self.end_subtitle_synchronization += timedelta(seconds=self.second)
        else:
            self.start_subtitle_synchronization -= timedelta(seconds=self.second)
            self.end_subtitle_synchronization -= timedelta(seconds=self.second)

    def __get_text_subtitle_synchronization(self):
        str_start = str(self.start_subtitle_synchronization.time())
        str_end = str(self.end_subtitle_synchronization.time())
        
        return '%s --> %s\n' %(self.__format_text_subtitle_synchronization(str_start), self.__format_text_subtitle_synchronization(str_end))
    
    def __format_text_subtitle_synchronization(self, value):
        return value[:12].replace('.', ',')
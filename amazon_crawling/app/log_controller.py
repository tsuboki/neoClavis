import csv
import datetime
from .config import Config

class Log_controller:

    def __init__(self):
        self.log_file = open(Config.OUTPUT_LOG_FILE_PATH + Config.OUTPUT_LOG_FILE_NAME, "a", encoding=Config.OUTPUT_CSV_ENCODING)
        self.log_writer = csv.writer(self.log_file, lineterminator='\n')

    def write_log(self, type, message):
        output_row = [str(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))] + [type] + [message]
        self.log_writer.writerow(output_row)
        print(output_row)

    def close_file(self):
        self.log_file.close()

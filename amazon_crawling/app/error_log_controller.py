import datetime
import csv
import sys
from .config import Config
from .log_controller import Log_controller

class Error_log_controller:

    def create_error_log_file_and_retry(asin, thrown_error, asin_position, total_asin, log_controller):
        error_log_file = open(Config.ERROR_LOG_FILE_NAME, "a", encoding=Config.OUTPUT_CSV_ENCODING)
        writer = csv.writer(error_log_file, lineterminator='\n')
        writer.writerow(Config.ERROR_LOG_FILE_HEADER)
        writer.writerow([str(datetime.datetime.now()), asin, str(asin_position), str(total_asin), thrown_error])
        error_log_file.close()
        log_controller.write_log(Config.LOG_CATEGORY_ERROR, "Error at " + str(asin_position+1) + "/" + str(total_asin) + ": Retrying")
#        print("Error at " + str(asin_position+1) + "/" + str(total_asin) + ": Retrying")


    def create_error_log_file_and_kill(asin, thrown_error, asin_position, total_asin, log_controller):
        error_log_file = open(Config.ERROR_LOG_FILE_NAME, "a", encoding=Config.OUTPUT_CSV_ENCODING)
        writer = csv.writer(error_log_file, lineterminator='\n')
        writer.writerow(Config.ERROR_LOG_FILE_HEADER)
        writer.writerow([str(datetime.datetime.now()), asin, str(asin_position), str(total_asin), thrown_error])
        error_log_file.close()
        log_controller.write_log(Config.LOG_CATEGORY_ERROR, "Reached Max-Retry limit: Killing Process")
#        print("Reached Max-Retry limit: Killing Process")
        sys.exit()

    def create_error_log_file_for_http_error_and_kill(url, error_message, log_controller):
        error_log_file = open(Config.ERROR_LOG_FILE_NAME, "a", encoding=Config.OUTPUT_CSV_ENCODING)
        writer = csv.writer(error_log_file, lineterminator='\n')
        writer.writerow(Config.ERROR_LOG_FILE_HEADER)
        writer.writerow([str(datetime.datetime.now()), "", url, "", error_message])
        error_log_file.close()
        log_controller.write_log(Config.LOG_CATEGORY_ERROR, "HTTP Error: Killing Process")
#        print("HTTP Error: Killing Process")
        sys.exit()

import csv
import os.path
from .config import Config

class Result_writer :
    output_monthly_file_name = ""
    output_daily_file_name = ""

    def __init__(self, category):
        self.output_daily_file_name = \
            Config.OUTPUT_DAILY_FILE_PATH + \
            Config.OUTPUT_FILE_NAME_PRFIX + \
            Config.OUTPUT_DAILY_FILE_NAME_SUFFIX

        self.output_monthly_file_name = \
            Config.OUTPUT_MONTHLY_FILE_PATH + \
            Config.OUTPUT_FILE_NAME_PRFIX + \
            category.replace(" ","") + \
            Config.OUTPUT_MONTHLY_FILE_NAME_SUFFIX


    #Create output file wiht header, if not exist
    def create_daily_output_file_if_not_exist(self):
        if not os.path.isfile(self.output_daily_file_name) :
            output_file = open(self.output_daily_file_name, "w", encoding=Config.OUTPUT_CSV_ENCODING)
            writer = csv.writer(output_file, lineterminator='\n')
            writer.writerow(Config.OUTPUT_FILE_HEADER)
            output_file.close()

    def create_monthly_output_file_if_not_exist(self):
        if not os.path.isfile(self.output_monthly_file_name) :
            output_file = open(self.output_monthly_file_name, "w", encoding=Config.OUTPUT_CSV_ENCODING)
            writer = csv.writer(output_file, lineterminator='\n')
            writer.writerow(Config.OUTPUT_FILE_HEADER)
            output_file.close()


    #Write Outputs into outputfile from Object, at once
    def write_result_in_daily_output_file(self, asin_data_results_to_write):
        output_file = open(self.output_daily_file_name, "a", encoding=Config.OUTPUT_CSV_ENCODING)
        writer = csv.writer(output_file, lineterminator='\n')
        for asin_data in asin_data_results_to_write :
            writer.writerow(asin_data.to_array())
        output_file.close()

    def write_result_in_monthly_output_file(self, asin_data_results_to_write):
        output_file = open(self.output_monthly_file_name, "a", encoding=Config.OUTPUT_CSV_ENCODING)
        writer = csv.writer(output_file, lineterminator='\n')
        for asin_data in asin_data_results_to_write :
            writer.writerow(asin_data.to_array())
        output_file.close()

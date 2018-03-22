import csv
from .asin_data import Asin_data
from .config import Config
from datetime import datetime, timedelta
from .asin_data_array_by_category import Asin_data_array_by_category

class Asin_master_reader_with_filter :

    def read_asin_master_with_filter_return_asin_object_array_by_category():
        return_asin_array_by_category = []
        inputfile = open(Config.INPUT_FILE_PATH + Config.INPUT_CSV_FILE_NAME_FOR_FILTER,
                        "r",
                        encoding=Config.INPUT_CSV_ENCODING
                        )
        body = csv.reader(inputfile)
        header = next(body)


        for master_data_row in body:
            last_loop=True
            if filter_master_data(master_data_row):
                for asin_array_by_category in return_asin_array_by_category:
                    if asin_array_by_category.category == master_data_row[Config.MASTER_CSV_CATEGORY_COLUMN]:
                        asin_array_by_category.appned_one_row_to_asin_data_array(
                            Asin_data(
                                master_data_row[Config.CRAWL_ASIN_COLUMN],
                                master_data_row[Config.MASTER_CSV_CATEGORY_COLUMN],
                                master_data_row[Config.MASTER_CSV_BRAND],
                                master_data_row[Config.MASTER_CSV_SEGMENT1],
                                master_data_row[Config.MASTER_CSV_SEGMENT2],
                                master_data_row[Config.MASTER_CSV_SEGMENT3],
                                master_data_row[Config.MASTER_CSV_SEGMENT4],
                                master_data_row[Config.MASTER_CSV_SEGMENT5],
                                master_data_row[Config.MASTER_CSV_SEGMENT6]
                            )
                        )
                        last_loop = False

                if last_loop:
                    return_asin_array_by_category.append(Asin_data_array_by_category(
                            master_data_row[Config.MASTER_CSV_CATEGORY_COLUMN],
                            Asin_data(
                                master_data_row[Config.CRAWL_ASIN_COLUMN],
                                master_data_row[Config.MASTER_CSV_CATEGORY_COLUMN],
                                master_data_row[Config.MASTER_CSV_BRAND],
                                master_data_row[Config.MASTER_CSV_SEGMENT1],
                                master_data_row[Config.MASTER_CSV_SEGMENT2],
                                master_data_row[Config.MASTER_CSV_SEGMENT3],
                                master_data_row[Config.MASTER_CSV_SEGMENT4],
                                master_data_row[Config.MASTER_CSV_SEGMENT5],
                                master_data_row[Config.MASTER_CSV_SEGMENT6]
                            )
                        )
                    )

        inputfile.close()
        return return_asin_array_by_category

    def read_asin_master_with_filter_return_asin_object_array():
        return_asin_array = []
        inputfile = open(Config.INPUT_FILE_PATH + Config.INPUT_CSV_FILE_NAME_FOR_FILTER,
                        "r",
                        encoding=Config.INPUT_CSV_ENCODING
                        )
        body = csv.reader(inputfile)
        header = next(body)
        for master_data_row in body:
            if filter_master_data(master_data_row):
                return_asin_array.append(
                    Asin_data(
                        master_data_row[Config.CRAWL_ASIN_COLUMN],
                        master_data_row[Config.MASTER_CSV_CATEGORY_COLUMN],
                        master_data_row[Config.MASTER_CSV_BRAND],
                        master_data_row[Config.MASTER_CSV_SEGMENT1],
                        master_data_row[Config.MASTER_CSV_SEGMENT2],
                        master_data_row[Config.MASTER_CSV_SEGMENT3],
                        master_data_row[Config.MASTER_CSV_SEGMENT4],
                        master_data_row[Config.MASTER_CSV_SEGMENT5],
                        master_data_row[Config.MASTER_CSV_SEGMENT6]
                    )
                )

        inputfile.close()
        return return_asin_array

def filter_master_data(read_row) :
    is_amazon_master = True if read_row[Config.CRAWL_ERT_COLUMN] == Config.CRAWL_ERT_VALUE else False
    is_non_pantry = True if read_row[Config.CRAWL_PANTRYFLG_COLUMN] == Config.CRAWL_PANTRYFLG_VALUE else False
    is_not_unset = True if read_row[Config.CRAWL_UNSETFLG_COLUMN] != Config.CRAWL_UNSETFLG_VALUE else False
    is_latest_pos_in_ninty_days = False
    if read_row[Config.CRAWL_LASTPOS_COLUMN] != "" :
        last_pos_date = datetime.strptime(read_row[Config.CRAWL_LASTPOS_COLUMN], '%Y-%m-%d')
        is_latest_pos_in_ninty_days = True if datetime.today() <= last_pos_date + timedelta(days=Config.CRAWL_LASTPOS_CRITERIA_DAYS) else False
    return is_amazon_master and is_non_pantry and is_not_unset and is_latest_pos_in_ninty_days

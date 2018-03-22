# -*- coding: utf-8 -*-
from app.error_log_controller import Error_log_controller
from app.result_writer import Result_writer
from app.web_crawler import Web_crawler
from app.config import Config
from app.asin_master_reader_with_filter import Asin_master_reader_with_filter
from app.log_controller import Log_controller

def run(category, asin_data_results, log_controller):
    log_controller.write_log(Config.LOG_CATEGORY_LOG, "Starts " + category + " Crawling")
    position_counter = 0
    skip_flag = False
    retry_counter = 0
    total_asin_volume = len(asin_data_results)

    while position_counter < total_asin_volume:

        asin_data = asin_data_results[position_counter]

        merchant_amazon_html = Web_crawler.return_lxmlhtml_by_url(asin_data.get_amazon_merchant_url(), log_controller)
        lowest_price_merchant_html = Web_crawler.return_lxmlhtml_by_url(asin_data.get_lowest_price_merchant_url(), log_controller)

        #Storing results
        try:
            if asin_data.check_asin_scrawl_target_qualification(merchant_amazon_html):
                asin_data.set_basis_data_from_html(merchant_amazon_html)
                asin_data.set_lowest_price_merchant(lowest_price_merchant_html)
            else:
                raise ValueError(category + ": Skipping " + str(position_counter+1) + "/" + str(total_asin_volume))

        except ValueError as thrown_error:
            Error_log_controller.create_error_log_file_and_retry(asin_data.asin, thrown_error, position_counter, total_asin_volume, log_controller)
            retry_counter += 1
            if retry_counter <= Config.URL_HIT_RETRY_LIMIT_FOR_SINGLE_ASIN :
                continue

            #Just in case
            elif retry_counter > 100:
                Error_log_controller.create_error_log_file_and_kill(asin_data.asin, thrown_error, position_counter, total_asin_volume, log_controller)

            elif retry_counter > Config.URL_HIT_RETRY_LIMIT_FOR_SINGLE_ASIN:
                log_controller.write_log(Config.LOG_CATEGORY_RETRY, thrown_error)
                position_counter += 1
                retry_counter = 0
                continue

        #Printing Progress to Console

        log_controller.write_log(Config.LOG_CATEGORY_SUCCESS, category + " : " + str(position_counter+1) + "/" + str(total_asin_volume) + ": " + str(((position_counter+1)*100)//total_asin_volume) + "% Complete")
        retry_counter = 0
        position_counter += 1

    result_writer = Result_writer(category)
    result_writer.create_monthly_output_file_if_not_exist()
    result_writer.create_daily_output_file_if_not_exist()
    result_writer.write_result_in_daily_output_file(asin_data_results)
    result_writer.write_result_in_monthly_output_file(asin_data_results)

    log_controller.write_log(Config.LOG_CATEGORY_LOG, "Completes " + category + " Crawling")


#Main
asin_data_array_with_category_array = Asin_master_reader_with_filter.read_asin_master_with_filter_return_asin_object_array_by_category()
toberemoved = Asin_master_reader_with_filter.read_asin_master_with_filter_return_asin_object_array()

#Here test
log_controller = Log_controller()

log_controller.write_log(Config.LOG_CATEGORY_LOG, "Starts all ASIN Crawling")
for asin_array_with_category in asin_data_array_with_category_array:
    run(asin_array_with_category.category, asin_array_with_category.asin_data_array, log_controller)

log_controller.write_log(Config.LOG_CATEGORY_LOG, "Completes all ASIN Crawling")
log_controller.close_file()

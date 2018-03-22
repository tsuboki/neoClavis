import datetime

class Config:
    CRQAWL_SLEEP_SEC = 2

    #Master csv file info
    CRAWL_ERT_COLUMN = 0
    CRAWL_ERT_VALUE = "Amazon"
    CRAWL_PANTRYFLG_COLUMN = 14
    CRAWL_PANTRYFLG_VALUE = "Non-Pantry"
    CRAWL_UNSETFLG_COLUMN = 15
    CRAWL_UNSETFLG_VALUE = "1"
    CRAWL_LASTPOS_COLUMN = 13
    CRAWL_LASTPOS_CRITERIA_DAYS = 180
    CRAWL_ASIN_COLUMN = 2
    MASTER_CSV_CATEGORY_COLUMN = 4
    MASTER_CSV_BRAND = 5
    MASTER_CSV_SEGMENT1 = 6
    MASTER_CSV_SEGMENT2 = 7
    MASTER_CSV_SEGMENT3 = 8
    MASTER_CSV_SEGMENT4 = 9
    MASTER_CSV_SEGMENT5 = 10
    MASTER_CSV_SEGMENT6 = 11

    INPUT_FILE_PATH = "../input_csv_file/"
    INPUT_CSV_FILE_NAME_FOR_FILTER = "RPC_PRODUCT_MASTER_FOR_TEST_24ASIN.csv"
    INPUT_CSV_ENCODING = "utf-8"

    OUTPUT_LOG_FILE_PATH = "../log/log/"
    OUTPUT_LOG_FILE_NAME = "process_log_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) +".csv"
    ERROR_LOG_FILE_NAME = "../log/error/amazon_crawling_with_asin_test_ERROR_LOG_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) +".csv"
    ERROR_LOG_FILE_HEADER = ["Datetime", "AISN", "Position", "TTL ASIN Vol", "Error Message"]
    LOG_CATEGORY_SUCCESS = "Success"
    LOG_CATEGORY_RETRY = "Retry"
    LOG_CATEGORY_ERROR = "Error"
    LOG_CATEGORY_LOG = "Log"

    OUTPUT_DAILY_FILE_PATH = "../output_csv_file/daily/"
    OUTPUT_MONTHLY_FILE_PATH = "../output_csv_file/monthly/"
    OUTPUT_FILE_NAME_PRFIX = "amazon_crawling_results_"
    OUTPUT_DAILY_FILE_NAME_SUFFIX = "_" + str(datetime.datetime.now().strftime("%Y%m%d")) + ".csv"
    OUTPUT_MONTHLY_FILE_NAME_SUFFIX = "_" + str(datetime.datetime.now().strftime("%Y%m")) + ".csv"
    OUTPUT_CSV_ENCODING = "utf-8"

    OUTPUT_FILE_HEADER = [
                        "ASIN",
                        "Category",
                        "BRAND",
                        "SEGMENT1",
                        "SEGMENT2",
                        "SEGMENT3",
                        "SEGMENT4",
                        "SEGMENT5",
                        "SEGMENT6",
                        "ProductTitle",
                        "Crwal-Date",
                        "Crwal-Time",
                        "ASIN-Active",
                        "ASIN-Qualified-Buy-Status",
                        "Non-Pantry-status",
                        "Non-Used-status",
                        "Non-Market-Place",
                        "Amazon-is-selling",
                        "Amazon-is-the-lowest-price-merchant",
                        "Lowest-Price-Merchant",
                        "Lowest-Price-JPY",
                        "Amazon-Price JPY",
                        "Amazon-Coupon",
                        "Add-On",
                        "Prime-Only",
                        "Availability",
                        "Review-Stars",
                        "Review-Volumes",
                        "Standard-SnS",
                        "Standard-SnS-Price",
                        "Prime-Exclusive-SnS",
                        "Prime-Exclusive-SnS-Price",
                        "Prime-Family-SnS",
                        "Prime-Family-SnS-Price"
                        ]
    AMAZON_ASIN_DETAIL_URI = "https://www.amazon.co.jp/exec/obidos/ASIN/"
    AMAZON_MERCHANT_REF = "?smid=AN1VRQENFRJN5"
    NOT_200_ERROR_MESSAGE = "Error: Could not connect to Amazon. \nPlease check the data"
    URL_HIT_RETRY_LIMIT_FOR_SINGLE_ASIN = 25

    XPATH_FOR_ASIN_INACTIVE_FLAG = "id('outOfStock')"
    XPATH_FOR_ASIN_UNQUALIFIED_BUY_FLAG = "id('unqualifiedBuyBox')"
    XPATH_FOR_ASIN_PANTRY_FLAG = "id('pantryBuyBox_feature_div')"
    XPATH_FOR_ASIN_USED_FLAG = "id('usedbuyBox')"
    XPATH_FOR_ASIN_Non_Market_Place = "id('merchant-info')//a[position()=1]"
    XPATH_FOR_PRODUCT_TITLE = "id('productTitle')"
    XPATH_FOR_MERCHANT = "id('merchant-info')//a[position()=1]"
    XPATH_FOR_PRICE = "id('priceblock_ourprice')"
    XPATH_FOR_AMAZON_COUPON = "id('price')//div[@id='unclippedCoupon']//span[contains(text(), 'クーポンの適用')]"
    XPATH_FOR_ADDON = "id('addon')"
    XPATH_FOR_PRIMEONLY = "id('merchant-info')//b[position()=1]"
    XPATH_FOR_AVAILAVILITY = "id('availability')/span[position()=1]"
    XPATH_FOR_LOW_AVAILAVILITY = "id('availability')/span[position()=1]/b"
    XPATTH_FOR_REVIEW_STARS = "id('acrPopover')//i[position()=1]/span"
    XPATTH_FOR_REVIEW_VOLUME = "id('acrCustomerReviewText')"
    XPATH_FOR_STANDARD_SNS_FLAG = "id('snsBuyBoxAccordion')"
    XPATH_FOR_STANDARD_SNS_PRICE = "id('snsBuyBoxAccordion')//span[@id='subscriptionPrice']"
    XPATH_FOR_PRIME_EXCLUSIVE_SNS_FLAG = "id('pe-bb-standard-sns')"
    XPATH_FOR_PRIME_EXCLUSIVE_SNS_PRICE = "id('pe-bb-standard-sns')/span[position()=1]"
    XPATH_FOR_PRIME_FAMILY_SNS_FLAG = "id('subscriptionPriceForMom')"
    XPATH_FOR_PRIME_FAMILY_SNS_PRICE = "id('subscriptionPriceForMom')"

    PRIME_CRITERIA_KEYWORD = "この商品はプライム会員専用です"
    AMAZON_MERCHANT_NAME = "Amazon.co.jp"
    OUTPUT_MESSAGE_FOR_NO_REVIEW_ASIN = "No Review"

    ERRORMESSAGE_UNEXPECTED_RETURN_FROM_AMAZON = "Unexpected Return from Amazon.\n Output file is not updated"

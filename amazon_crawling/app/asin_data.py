import datetime
from .data_formatter import Data_formatter
from .config import Config

class Asin_data:
    asin  = ""
    asin_master_category = ""
    asin_master_brand = ""
    asin_master_segment_1 = ""
    asin_master_segment_2 = ""
    asin_master_segment_3 = ""
    asin_master_segment_4 = ""
    asin_master_segment_5 = ""
    asin_master_segment_6 = ""
    product_title = ""
    crawl_date = datetime.datetime.now().strftime("%Y/%m/%d")
    crawl_time = datetime.datetime.now().strftime("%H:%M:%S")
    asin_active_flag = True
    asin_qualified_buy_flag = True
    non_pantry_flag = True
    non_used_flag = True
    non_market_place_flag = True
    amazon_is_selling_flag = False
    amazon_is_lowest_price_merchant_flag = False
    lowest_price_merchant = ""
    lowest_price = ""
    price_amazon_merchant = ""
    amazon_coupon = ""
    addon = False
    primeonly = False
    availability = ""
    review_stars = ""
    review_volume = ""
    standard_sns_flag = False
    standard_sns_price = ""
    prime_exclusive_sns_flag = False
    prime_exclusive_sns_price = ""
    prime_family_sns_flag = False
    prime_family_sns_price = ""

    #Constructor
    def __init__(self, asin, category, brand, segment_1, segment_2, segment_3, segment_4, segment_5, segment_6):
        self.asin = asin
        self.asin_master_category = category
        self.asin_master_brand = brand
        self.asin_master_segment_1 = segment_1
        self.asin_master_segment_2 = segment_2
        self.asin_master_segment_3 = segment_3
        self.asin_master_segment_4 = segment_4
        self.asin_master_segment_5 = segment_5
        self.asin_master_segment_6 = segment_6


    #To String
    def to_array(self):
        returnvalue = []
        returnvalue.append(self.asin)
        returnvalue.append(self.asin_master_category)
        returnvalue.append(self.asin_master_brand)
        returnvalue.append(self.asin_master_segment_1)
        returnvalue.append(self.asin_master_segment_2)
        returnvalue.append(self.asin_master_segment_3)
        returnvalue.append(self.asin_master_segment_4)
        returnvalue.append(self.asin_master_segment_5)
        returnvalue.append(self.asin_master_segment_6)
        returnvalue.append(self.product_title)
        returnvalue.append(self.crawl_date)
        returnvalue.append(self.crawl_time)
        returnvalue.append(self.asin_active_flag)
        returnvalue.append(self.asin_qualified_buy_flag)
        returnvalue.append(self.non_pantry_flag)
        returnvalue.append(self.non_used_flag)
        returnvalue.append(self.non_market_place_flag)
        returnvalue.append(self.amazon_is_selling_flag)
        returnvalue.append(self.amazon_is_lowest_price_merchant_flag)
        returnvalue.append(self.lowest_price_merchant)
        returnvalue.append(self.lowest_price)
        returnvalue.append(self.price_amazon_merchant)
        returnvalue.append(self.amazon_coupon)
        returnvalue.append(self.addon)
        returnvalue.append(self.primeonly)
        returnvalue.append(self.availability)
        returnvalue.append(self.review_stars)
        returnvalue.append(self.review_volume)
        returnvalue.append(self.standard_sns_flag)
        returnvalue.append(self.standard_sns_price)
        returnvalue.append(self.prime_exclusive_sns_flag)
        returnvalue.append(self.prime_exclusive_sns_price)
        returnvalue.append(self.prime_family_sns_flag)
        returnvalue.append(self.prime_family_sns_price)
        return returnvalue

    #URL getter
    def get_amazon_merchant_url(self) :
        return Config.AMAZON_ASIN_DETAIL_URI + self.asin + Config.AMAZON_MERCHANT_REF

    def get_lowest_price_merchant_url(self) :
        return Config.AMAZON_ASIN_DETAIL_URI + self.asin


    #Status Checker
    def check_asin_scrawl_target_qualification(self, root):
        #Active
        if len(root.xpath(Config.XPATH_FOR_ASIN_INACTIVE_FLAG)) == 1:
            self.asin_active_flag = False
        elif len(root.xpath(Config.XPATH_FOR_ASIN_INACTIVE_FLAG)) == 0:
            self.asin_active_flag = True
        else:
            raise ValueError("ASIN inactive html tag is more than 2")

        #Unqualified Merchant
        if len(root.xpath(Config.XPATH_FOR_ASIN_UNQUALIFIED_BUY_FLAG)) == 1:
            self.asin_qualified_buy_flag = False
        elif len(root.xpath(Config.XPATH_FOR_ASIN_UNQUALIFIED_BUY_FLAG)) == 0:
            self.asin_qualified_buy_flag = True
        else :
            raise ValueError("ASIN unqualified buy html tag is more than 2")

        #Pantry
        if len(root.xpath(Config.XPATH_FOR_ASIN_PANTRY_FLAG)) == 1:
            self.non_pantry_flag = False
        elif len(root.xpath(Config.XPATH_FOR_ASIN_PANTRY_FLAG)) == 0:
            self.non_pantry_flag = True
        else :
            raise ValueError("ASIN PANTRY flag html tag is more than 2")

        #USED
        if len(root.xpath(Config.XPATH_FOR_ASIN_USED_FLAG)) == 1:
            self.non_used_flag = False
        elif len(root.xpath(Config.XPATH_FOR_ASIN_USED_FLAG)) == 0:
            self.non_used_flag = True
        else :
            raise ValueError("ASIN USED flag html tag is more than 2")

        #Market Place
        if len(root.xpath(Config.XPATH_FOR_ASIN_Non_Market_Place)) == 1:
            self.non_market_place_flag= True
        elif len(root.xpath(Config.XPATH_FOR_ASIN_Non_Market_Place)) == 0:
            self.non_market_place_flag = False

        return self.asin_active_flag \
            and self.asin_qualified_buy_flag \
            and self.non_pantry_flag \
            and self.non_used_flag \
            and self.non_market_place_flag


    #Setter from root data
    def set_basis_data_from_html(self, root) :
        #Set Amazon is selling Flag
        if len(root.xpath(Config.XPATH_FOR_MERCHANT)) == 0:
            raise ValueError("Merchant html tag is missing")
        if root.xpath(Config.XPATH_FOR_MERCHANT)[0].text == Config.AMAZON_MERCHANT_NAME :
            self.amazon_is_selling_flag = True

        #Set Product Title
        if len(root.xpath(Config.XPATH_FOR_PRODUCT_TITLE)) != 1:
            raise ValueError("Product Title html tag is not unique")
        self.product_title = Data_formatter.strip_and_remove_comma_linechange(root.xpath(Config.XPATH_FOR_PRODUCT_TITLE)[0].text)

        #Set Price
        if self.amazon_is_selling_flag:
            if len(root.xpath(Config.XPATH_FOR_PRICE)) != 1:
                raise ValueError("Price html tag is not unique")
            self.price_amazon_merchant = Data_formatter.remove_comma_blank_jpysymbol_linechange(root.xpath(Config.XPATH_FOR_PRICE)[0].text)
        else:
            self.price_amazon_merchant = "N/A"

        #Set Amazon Coupon
        if len(root.xpath(Config.XPATH_FOR_AMAZON_COUPON)) == 1:
            self.amazon_coupon = Data_formatter.remove_comma_blank_jpysymbol_linechange(root.xpath(Config.XPATH_FOR_AMAZON_COUPON)[0].text)
        elif len(root.xpath(Config.XPATH_FOR_AMAZON_COUPON)) == 0:
            self.amazon_coupon = "N/A"
        else:
            raise ValueError("Coupon html tag has more than 1 tag")

        #Set AddOn
        if len(root.xpath(Config.XPATH_FOR_ADDON)) >= 2:
            raise ValueError("Add On html tag is not unique")
        elif len(root.xpath(Config.XPATH_FOR_ADDON)) == 1:
            self.addon = True
        elif len(root.xpath(Config.XPATH_FOR_ADDON)) == 0:
            self.addon = False

        #Set Prime Only
        if len(root.xpath(Config.XPATH_FOR_PRIMEONLY)) >= 2:
            raise ValueError("Prime Only html tag is not unique")
        elif len(root.xpath(Config.XPATH_FOR_PRIMEONLY)) == 1:
            if root.xpath(Config.XPATH_FOR_PRIMEONLY)[0].text == Config.PRIME_CRITERIA_KEYWORD:
                self.primeonly = True
            else:
                self.primeonly = False
        else:
            self.primeonly = False


        #Set Availability
        if len(root.xpath(Config.XPATH_FOR_AVAILAVILITY)) == 1:
            self.availability = Data_formatter.remove_comma_blank_jpysymbol_linechange(root.xpath(Config.XPATH_FOR_AVAILAVILITY)[0].text)
            if len(root.xpath(Config.XPATH_FOR_LOW_AVAILAVILITY)) == 1:
                self.availability +=  Data_formatter.remove_comma_blank_jpysymbol_linechange(root.xpath(Config.XPATH_FOR_LOW_AVAILAVILITY)[0].text)
        else:
            raise ValueError("Availability html tag is not unique")

        #Set Review stars
        if len(root.xpath(Config.XPATTH_FOR_REVIEW_STARS)) == 1:
            self.review_stars = Data_formatter.remove_review_comments_prefix_suffix(root.xpath(Config.XPATTH_FOR_REVIEW_STARS)[0].text)
        elif len(root.xpath(Config.XPATTH_FOR_REVIEW_STARS)) == 0:
            self.review_stars = Config.OUTPUT_MESSAGE_FOR_NO_REVIEW_ASIN
        else:
            raise ValueError("Review Star html tag is not unique")

        #Set Review Volumes
        if len(root.xpath(Config.XPATTH_FOR_REVIEW_VOLUME)) == 1:
            self.review_volume = Data_formatter.remove_review_comments_prefix_suffix(root.xpath(Config.XPATTH_FOR_REVIEW_VOLUME)[0].text)
        elif len(root.xpath(Config.XPATTH_FOR_REVIEW_VOLUME)) == 0:
            self.review_volume = Config.OUTPUT_MESSAGE_FOR_NO_REVIEW_ASIN
        else:
            raise ValueError("Review Volume html tag is not unique")

        #Set Starndrd SnS flag
        if len(root.xpath(Config.XPATH_FOR_STANDARD_SNS_FLAG)) == 1:
            self.standard_sns_flag = True
        elif len(root.xpath(Config.XPATH_FOR_STANDARD_SNS_FLAG)) >= 2:
            raise ValueError("Standard SnS html flag has 2 or more tags")

        #Set Starndrd SnS price
        if self.standard_sns_flag:
            if len(root.xpath(Config.XPATH_FOR_STANDARD_SNS_PRICE)) == 1:
                self.standard_sns_price = Data_formatter.remove_comma_blank_jpysymbol_linechange(root.xpath(Config.XPATH_FOR_STANDARD_SNS_PRICE)[0].text)
            else:
                raise ValueError("Standard SnS price html tag has 2 or more tags")
        else:
            self.standard_sns_price = "N/A"

        #Set Prime Exclusive SnS flag
        if (len(root.xpath(Config.XPATH_FOR_PRIME_EXCLUSIVE_SNS_FLAG))) == 1:
            self.prime_exclusive_sns_flag = True
        elif (len(root.xpath(Config.XPATH_FOR_PRIME_EXCLUSIVE_SNS_FLAG))) >= 2:
            raise ValueError("Prime Exclusive SnS html flag has 2 or more tags")

        #Set Prime Exclusive SnS price
        if self.prime_exclusive_sns_flag:
            if len(root.xpath(Config.XPATH_FOR_PRIME_EXCLUSIVE_SNS_PRICE)) == 1:
                self.prime_exclusive_sns_price = Data_formatter.remove_comma_blank_jpysymbol_linechange(root.xpath(Config.XPATH_FOR_PRIME_EXCLUSIVE_SNS_PRICE)[0].text)
            else:
                raise ValueError("Prime Exclusive SnS price html tag has 2 or more tags")
        else:
            self.prime_exclusive_sns_price = "N/A"

        #Set Prime Family SnS flag
        if (len(root.xpath(Config.XPATH_FOR_PRIME_FAMILY_SNS_FLAG))) == 1:
            self.prime_family_sns_flag = True
        elif (len(root.xpath(Config.XPATH_FOR_PRIME_FAMILY_SNS_FLAG))) >= 2:
            raise ValueError("Prime Family SnS html flag has 2 or more tags")

        #Set Prime Family SnS price
        if self.prime_family_sns_flag:
            if len(root.xpath(Config.XPATH_FOR_PRIME_FAMILY_SNS_PRICE)) == 1:
                self.prime_family_sns_price = Data_formatter.remove_comma_blank_jpysymbol_linechange(root.xpath(Config.XPATH_FOR_PRIME_FAMILY_SNS_PRICE)[0].text)
            else:
                raise ValueError("Prime Family SnS price html tag has 2 or more tags")
        else:
            self.prime_family_sns_price = "N/A"


    def set_lowest_price_merchant(self, root) :
        #Set Lowest Price Merchant
        if len(root.xpath(Config.XPATH_FOR_MERCHANT)) == 0:
            raise ValueError("Lowest Price Merchant html tag is missing")
        self.lowest_price_merchant = Data_formatter.remove_comma_blank_jpysymbol_linechange(root.xpath(Config.XPATH_FOR_MERCHANT)[0].text)

        #Set Amazon is the lowest Merchant flag
        if len(root.xpath(Config.XPATH_FOR_MERCHANT)) == 0:
            raise ValueError("Merchant html tag is missing")
        if root.xpath(Config.XPATH_FOR_MERCHANT)[0].text == Config.AMAZON_MERCHANT_NAME :
            self.amazon_is_lowest_price_merchant_flag = True

        #Set Lowest Price
        if len(root.xpath(Config.XPATH_FOR_PRICE)) != 1:
            raise ValueError("Price html tag is not unique")
        self.lowest_price = Data_formatter.remove_comma_blank_jpysymbol_linechange(root.xpath(Config.XPATH_FOR_PRICE)[0].text)

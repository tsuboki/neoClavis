#This test is not completed! check_asin_scrawl_target_qualification test s not up-to-date

from amazon_crawling.app.asin_data import Asin_data
from amazon_crawling.app.config import Config
import lxml.html
import datetime
import mock
import pytest
from pytest_mock import mocker


TEST_ASIN = "0123456789"
TEST_CATEGORY = "Test Category"
TEST_BRAND = "Test Brand"
TEST_SEGMENT_1 = "Test Segment 1"
TEST_SEGMENT_2 = "Test Segment 3"
TEST_SEGMENT_3 = "Test Segment 2"
TEST_SEGMENT_4 = "Test Segment 4"
TEST_SEGMENT_5 = "Test Segment 5"
TEST_SEGMENT_6 = "Test Segment 6"


HTML_ELEMENT_0 = []
HTML_ELEMENT_1 = ["HTML ELEMENT 0"]
HTML_ELEMENT_2 = ["HTML ELEMENT 0", "HTML ELEMENT 1"]

BLANK_HTML_ELEMENT = lxml.html.HtmlElement()

@pytest.fixture
def asin_data_creation():
    return Asin_data(
        TEST_ASIN,
        TEST_CATEGORY,
        TEST_BRAND,
        TEST_SEGMENT_1,
        TEST_SEGMENT_2,
        TEST_SEGMENT_3,
        TEST_SEGMENT_4,
        TEST_SEGMENT_5,
        TEST_SEGMENT_6
    )

@pytest.fixture
def mockup_lxml_html_xpath(mocker):
    mocker.patch.object(lxml.html.HtmlElement, "xpath")


def test_Asin_data_constructor():
    test_execution_time = datetime.datetime.now()
    test_asin_data = asin_data_creation()

    assert test_asin_data.asin == TEST_ASIN
    assert test_asin_data.crawl_date == test_execution_time.strftime("%Y/%m/%d")


def test_get_amazon_merchant_url():
    test_asin_data = asin_data_creation()

    amazon_merchant_url = test_asin_data.get_amazon_merchant_url()

    assert amazon_merchant_url == Config.AMAZON_ASIN_DETAIL_URI + TEST_ASIN + Config.AMAZON_MERCHANT_REF


def test_get_lowest_price_merchant_url():
    test_asin_data = asin_data_creation()

    lowest_price_merchant_url = test_asin_data.get_lowest_price_merchant_url()

    assert lowest_price_merchant_url == Config.AMAZON_ASIN_DETAIL_URI + TEST_ASIN


def test_check_asin_scrawl_target_qualification_results_negative(mocker):
    test_asin_data = asin_data_creation()
    mockup_lxml_html_xpath(mocker)
    lxml.html.HtmlElement.xpath.return_value = HTML_ELEMENT_1

    asin_crawl_target_checker = test_asin_data.check_asin_scrawl_target_qualification(BLANK_HTML_ELEMENT)

    assert not asin_crawl_target_checker
    assert not test_asin_data.asin_active_flag
    assert not test_asin_data.asin_qualified_buy_flag
    assert not test_asin_data.non_pantry_flag
    assert not test_asin_data.non_used_flag
    assert not test_asin_data.non_market_place_flag

def test_check_asin_scrawl_target_qualification_results_positive(mocker):
    test_asin_data = asin_data_creation()
    mockup_lxml_html_xpath(mocker)
    lxml.html.HtmlElement.xpath.return_value = HTML_ELEMENT_0

    asin_crawl_target_checker = test_asin_data.check_asin_scrawl_target_qualification(BLANK_HTML_ELEMENT)

    assert asin_crawl_target_checker
    assert test_asin_data.asin_active_flag
    assert test_asin_data.asin_qualified_buy_flag
    assert test_asin_data.non_pantry_flag
    assert test_asin_data.non_used_flag

def test_check_asin_scrawl_target_qualification_results_error(mocker):
    test_asin_data = asin_data_creation()
    mockup_lxml_html_xpath(mocker)
    lxml.html.HtmlElement.xpath.return_value = HTML_ELEMENT_2

    try:
        test_asin_data.check_asin_scrawl_target_qualification(BLANK_HTML_ELEMENT)
        errro_was_thrown = False
    except ValueError as thrown_error:
        errro_was_thrown = True

    assert errro_was_thrown

from amazon_crawling.app.asin_data_array_by_category import Asin_data_array_by_category
import pytest


TEST_CATEGORY = "Test Category"
TEST_ASIN_1 = "0123456789"
TEST_ASIN_2 = "ABCDEFGHIJ"

@pytest.fixture
def set_up():
    return Asin_data_array_by_category(TEST_CATEGORY, TEST_ASIN_1)


def test_Asin_data_array_by_category_constructor():
    test_asin_data_array_by_category = set_up()

    assert test_asin_data_array_by_category.category == TEST_CATEGORY
    assert len(test_asin_data_array_by_category.asin_data_array) == 1
    assert test_asin_data_array_by_category.asin_data_array[0] == TEST_ASIN_1


def test_appned_one_row_to_asin_data_array():
    test_asin_data_array_by_category = set_up()
    test_asin_data_array_by_category.appned_one_row_to_asin_data_array(TEST_ASIN_2)

    assert len(test_asin_data_array_by_category.asin_data_array) == 2
    assert test_asin_data_array_by_category.asin_data_array[0] == TEST_ASIN_1
    assert test_asin_data_array_by_category.asin_data_array[1] == TEST_ASIN_2

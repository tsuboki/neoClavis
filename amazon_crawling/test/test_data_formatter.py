from amazon_crawling.app.data_formatter import Data_formatter


def test_remove_comma_blank_jpysymbol_linechange():
    test_string = "t,e s￥t\n"
    expected_string = "test"
    assert Data_formatter.remove_comma_blank_jpysymbol_linechange(test_string) == expected_string

def test_strip_and_remove_comma_linechange():
    test_string = "t,e s￥t\n"
    expected_string = "te s￥t"
    assert Data_formatter.strip_and_remove_comma_linechange(test_string) == expected_string

def test_remove_review_comments_prefix_suffix():
    test_string = "5つ星のうちt件のカスタマーレビューestt,e s￥t\n"
    expected_string = "testtest"
    assert Data_formatter.remove_review_comments_prefix_suffix(test_string) == expected_string

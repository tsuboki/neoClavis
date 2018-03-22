from amazon_crawling.app.web_crawler import Web_crawler
from amazon_crawling.app.error_log_controller import Error_log_controller
from amazon_crawling.app.config import Config
import requests
import time
import lxml.html
import mock
import pytest
from pytest_mock import mocker

#Mock Class
class Mock_request():
    status_code = False
    text = ""

    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text


@pytest.fixture
def set_up(mocker):
    mocker.patch.object(requests, "get")
    mocker.patch.object(lxml.html, "fromstring")
    lxml.html.fromstring.return_value = "fromstring was called"


@pytest.fixture
def call_return_lxmlhtml_by_url():
    return Web_crawler.return_lxmlhtml_by_url("test_url")


def test_return_lxmlhtml_by_url_is_called_with_url(mocker):
    set_up(mocker)
    requests.get.return_value = Mock_request(True,"Mock HTML Text")

    return_value = call_return_lxmlhtml_by_url()

    requests.get.assert_called_with("test_url")


def test_return_lxmlhtml_by_url_waits_2_sec_when_called(mocker):
    set_up(mocker)
    requests.get.return_value = Mock_request(True,"Mock HTML Text")

    start_time = time.time()
    return_value = call_return_lxmlhtml_by_url()
    end_time = time.time()

    assert end_time - start_time >= 2.0


def test_return_lxmlhtml_by_url_returns_lxml_html_text_when_http200(mocker):
    set_up(mocker)
    requests.get.return_value = Mock_request(True, "Mock HTML Text")

    return_value = call_return_lxmlhtml_by_url()

    lxml.html.fromstring.assert_called_with("Mock HTML Text")
    assert return_value == "fromstring was called"


def test_return_lxmlhtml_by_url_returns_lxml_html_text_when_http_not200(mocker):
    mocker.patch.object(Error_log_controller, "create_error_log_file_for_http_error_and_kill")
    set_up(mocker)
    requests.get.return_value = Mock_request(False, "Mock HTML Text")

    return_value = call_return_lxmlhtml_by_url()

    Error_log_controller.create_error_log_file_for_http_error_and_kill.assert_called_with("test_url",Config.ERRORMESSAGE_UNEXPECTED_RETURN_FROM_AMAZON)

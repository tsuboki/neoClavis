import time
import requests
import lxml.html
import sys
from .error_log_controller import Error_log_controller
from .config import Config

class Web_crawler :
    def return_lxmlhtml_by_url(url, log_controller):
        time.sleep(Config.CRQAWL_SLEEP_SEC)
        response = requests.get(url, allow_redirects=True)
        if not response.status_code :
            Error_log_controller.create_error_log_file_for_http_error_and_kill(url, Config.ERRORMESSAGE_UNEXPECTED_RETURN_FROM_AMAZON, log_controller)
        else:
            return lxml.html.fromstring(response.text)

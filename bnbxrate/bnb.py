import sys
import datetime
import requests
from bs4 import BeautifulSoup as soup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging
logger = logging.getLogger(__name__)


class BNB:
    """
    Webscrape BNB exchange rates for provided date.
    """
    def __ini__(self):
        self.date_str = None
        self.url = None
        self.valutes = 'USD'
        self.rate = None
    
    def get_page_content(url):
        """
        Function to use requests.get on provided url with retry and delay between retries.
        """
        s = requests.Session()
        retries = Retry(total=5,
                        backoff_factor=0.3,
                        status_forcelist=[500, 502, 503, 504])
        s.mount('http://', HTTPAdapter(max_retries=retries))
        s.mount('https://', HTTPAdapter(max_retries=retries))
        logger.debug(f'Fetching url: {url}')
        try:
            sleep(0.01)
            res = s.get(url, headers={"User-Agent": "Mozilla/5.0"})
            if res.status_code == requests.codes['ok']:
                return res
        except Exception as exe:
            logger.error(f"Unable to load the url {exe}")
            return None
            
    def get_rate(self, date_str):
        pass
    
    def usage(self):
        pass
        
    def run_command(self, command):
        "Listen for cmd commands and execute it"
        command = command.pop(0)
        list_commands = ['USD']
        if command not in list_commands:
            logger.warning(f'ERROR: Unrecognised command {command}')
            BNB.usage()
            sys.exit(1)
            

        
def main():
    try:
        command = sys.argv[1:]
        BNB().run_command(command)
    except Exception as exe:
        print(exe)

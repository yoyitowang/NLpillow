import requests, os
from bs4 import BeautifulSoup
from goods import Goods
from line_notify import Line
from datetime import datetime

class Utils:
    def __init__(self) -> None:
        self.line = Line(os.environ['LINE_TOKEN'])
        
    def check_goods(self, url: str) -> None:
        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.content, 'html.parser')

            if resp.status_code == 200:
                self._check_NL_pillow_status(soup)
            else:
                raise(resp.status_code)
            
        except Exception as e:
            raise f"Error occurred in function: {self.check_goods.__name__} - {e}"

    def _check_NL_pillow_status(self, soup: str) -> None:
        try:
            for element in Goods.NLpillow.target_element_list:
                results = soup.find_all(element[0], element[1])
                for element in results:
                    if self._check_active_status(element):
                        self.line.notify(f'{datetime.now()} - {element.text} is available now')
        except Exception as e:
            raise f"Error occurred in function: {self._check_NL_pillow_status.__name__} - {e}"

    def _check_active_status(self, element: str, target_element: str = 'class', target_status: str = 'active') -> bool:
        try:
            if element[target_element] == target_status:
                return True
        except Exception as e:
            raise f"Error occurred in function: {self._check_active_status.__name__} - {e}"
        
        return False
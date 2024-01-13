import os
import requests

class Line:
    def __init__(self, token: str) -> None:
        self.api_url = 'https://notify-api.line.me/api/notify'
        self._token = token
        self.header = {
            'Authorization': 'Bearer ' + self._token,
            }

    def notify(self, msg: str) -> None:
        try:
            resp = requests.post(
                url=self.api_url,
                headers=self.header,
                data={'message': msg}
            )
            if resp.status_code != 200:
                raise Exception('Line notify failed')
            print('Line notify success')
            
        except Exception as e:
            raise(e)
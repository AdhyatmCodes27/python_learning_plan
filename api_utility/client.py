import requests
from api_utility.logger import get_logger

logger = get_logger(__name__)

class APIClient:
    def __init__(self, timeout=10):
        self.timeout = timeout
        
    def _request(self, method, url, expect_json=True, **kwargs):
        try:
            logger.info("Sending %s request to %s", method, url)
            response = requests.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status()
            logger.info(f"{method} request successful with status code: {response.status_code}")
            
            return response.json() if expect_json else response

        except requests.exceptions.HTTPError:
            logger.error(f"HTTP error while calling {url} status = {response.status_code}")
            raise

        except requests.exceptions.ConnectionError:
            logger.error(f"Connection error while calling {url}")
            raise

        except requests.exceptions.Timeout:
            logger.error(f"Request timed out while calling {url}")
            raise
        
        except requests.exceptions.JSONDecodeError:
            logger.error(f"Invalid JSON response from {url}")
            raise
        
        
    def get(self, url, params = None, headers = None):
        return self._request("GET", url, params=params, headers = headers, expect_json=True)
    
    def post(self, url, json_data=None, headers=None):
        return self._request("POST", url, json=json_data, headers = headers, expect_json=True)
    
    def put(self, url, json_data=None, headers=None):
        return self._request("PUT", url, json=json_data, headers = headers, expect_json=True)
    
    def patch(self, url, json_data=None, headers=None):
        return self._request("PATCH", url, json=json_data, headers = headers, expect_json=True)
    
    def delete(self, url, headers=None):
        return self._request("DELETE", url, headers = headers, expect_json=False)
    
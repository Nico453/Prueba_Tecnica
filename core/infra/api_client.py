import time, requests
from django.conf import settings
from django.utils.dateparse import parse_datetime
class ApiClient:

    def __init__(self):
        self.user_id = settings.API_USER_ID
        self.base_url = settings.API_BASE_URL
        self.timeout = int(settings.API_TIMEOUT)
        self.max_retries = int(settings.API_MAX_RETRIES)
        self.backoff = float(settings.API_BACKOFF)
        
    def fetch(self):
        params = {'user_id': self.user_id}
        last_exception = None
        
        for i in range(self.max_retries):
            try:
                response = requests.get(self.base_url, params=params, timeout=self.timeout)
                response.raise_for_status()
                data = response.json()
                
                dt = parse_datetime(data.get('timestamp'))
                if dt is None:
                    raise ValueError("Invalid timestamp format")
                return {
                    'user_id': data.get('user_id'),
                    'value': data.get('value'),
                    'category': data.get('category'),
                    'timestamp': dt,
                    'ip': data.get('ip'),
                    'attempts': data.get('attempts', 0)
                }
            except Exception as e:
                last_exception = e
                time.sleep(self.backoff * (2 ** i))
        raise last_exception if last_exception else Exception("Failed to fetch data after retries")
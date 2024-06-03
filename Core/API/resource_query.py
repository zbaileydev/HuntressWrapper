"""
This file holds classes and functions for 
performing queries against the Huntress API.
"""
import time
import requests
from Service.models.account import Account
from Service.models.organizations import Organizations
from Service.models.billing_report import BillingReport
from Service.models.incident_report import IncidentReport
from Service.models.summary_report import SummaryReport
from Service.models.agents import Agents


class ResourceQuery:
    RATE_LIMIT = 60  # requests per minute
    RATE_LIMIT_INTERVAL = 60  # seconds

    def __init__(self, url, resource_type, headers, method, data=None):
        self.url = url
        self.resource_type = resource_type
        self.headers = headers
        self.method = method
        self.data = data
        self.last_request_time = None

    def _wait_if_rate_limited(self):
        if self.last_request_time:
            elapsed_time = time.time() - self.last_request_time
            if elapsed_time < self.RATE_LIMIT_INTERVAL / self.RATE_LIMIT:
                time.sleep((self.RATE_LIMIT_INTERVAL / self.RATE_LIMIT) - elapsed_time)

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 400:
            raise ValueError("400 Bad Request: Unexpected value in the API request.")
        elif response.status_code == 404:
            raise ValueError("404 Not Found: The requested resource is unavailable.")
        elif response.status_code == 429:
            raise ValueError("429 Too Many Requests: Rate limit exceeded.")
        elif response.status_code == 500:
            raise ValueError("500 Internal Server Error: Contact support.")
        else:
            response.raise_for_status()

    def _map_to_structure(self, data):
        if self.resource_type == 'account':
            return Account(**data)
        elif self.resource_type == 'organizations':
            return Organizations(**data)
        else:
            raise ValueError(f"Unsupported resource type: {self.resource_type}")
        
    def send_response(self, url):
        if self.method == "get":
            response = requests.get(url, headers=self.headers)
        elif self.method == "post":
            response = requests.post(url, headers=self.headers, params=self.data)
        else:
            raise ValueError(f"Unsupported request method: {self.method}")
        return response

    def _fetch_page(self, url):
        self._wait_if_rate_limited()
        response = self.send_response(url)
        self.last_request_time = time.time()
        data = self._handle_response(response)
        mapped_resources = [self._map_to_structure(item) for item in data['results']]
        return mapped_resources, data.get('next_page_url')

    def fetch_resource(self):
        url = self.url
        while url:
            mapped_resources, url = self._fetch_page(url)
            yield mapped_resources

    def fetch_single_resource(self):
        mapped_resources = self._fetch_page(self.url)
        return mapped_resources
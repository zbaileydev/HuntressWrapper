from Core.API.resource_query import ResourceQuery
from Core.constants import BASE_URL, AUTH_STRING, Endpoint

class BaseService:
    def __init__(self, endpoint: Endpoint):
        self.endpoint = endpoint
        self.headers = {"Authorization": AUTH_STRING}
        self.url = f"{BASE_URL}/{self.endpoint.value}"

    def add_header(self, key, value):
        self.headers[key] = value

    def get_url(self):
        return self.url

    def get_endpoint(self):
        return self.endpoint        

    def get(self):
        return ResourceQuery(self.url, self.endpoint, self.headers, "get")

    def post(self, data: dict = None):
        return ResourceQuery(self.url, self.endpoint, self.headers, "post", data)

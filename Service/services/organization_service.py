from Core.API.base_service import BaseService
from Core.constants import Endpoint

class OrganizationService(BaseService):
    def __init__(self, headers, id=None):
        super().__init__(Endpoint.ORGANIZATIONS, headers)
        if id:
            self.url = f"{self.url}/{id}"

    def get_all_organizations(self, params=None):
        organizations = []
        for page in self.resource_query.fetch_resource(params):
            organizations.extend(page)
        return organizations
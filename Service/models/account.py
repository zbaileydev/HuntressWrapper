from Core.API.Structs.api_structs import API_Structure

class Account(API_Structure):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.map_data(kwargs)
        self.set_status(self._keys.get('status'))

    def set_status(self, status):
        if status not in ['enabled', 'disabled']:
            raise ValueError("Status must be one of ['enabled', 'disabled']")
        self._keys['status'] = status
        self._create_dynamic_methods('status')
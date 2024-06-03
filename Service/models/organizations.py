from Core.API.Structs.api_structs import API_Structure

class Organizations(API_Structure):
    def __init__(self, **kwargs):
        super().__init__()
        self.map_data(kwargs)
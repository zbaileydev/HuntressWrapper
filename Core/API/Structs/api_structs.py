"""
api_structs
Contain objects for each of the API resources defined at
https://api.huntress.io/docs#api-resources
"""

class API_Structure:
    """
    Base structure for API structures to dynamically generate 
    getters and setters for API keys.

    # Example usage:
    api_struct = API_Structure()
    api_struct.add_value('name', 'API Structure')
    api_struct.add_value('version', '1.0')

    print(api_struct.get_name())    # Output: API Structure
    print(api_struct.get_version()) # Output: 1.0
    """
    def __init__(self) -> None:
        self._keys = {}

    def add_value(self, key, value):
        self._keys[key] = value
        self._create_dynamic_methods(key)

    def _create_dynamic_methods(self, key):
        getter_name = f'get_{key}'
        def getter(self):
            return self._keys.get(key)
        setattr(self, getter_name, getter.__get__(self))

        setter_name = f'set_{key}'
        def setter(self, value):
            self._keys[key] = value
        setattr(self, setter_name, setter.__get__(self))

    def map_data(self, data):
        for key, value in data.items():
            self.add_value(key, value)
    
    def __str__(self):
        return str(self._keys)







class IndicatorOfCompromise:
    def __init__(self, type, value, description, source):
        self.type = type  # e.g., 'IP', 'URL', 'Hash'
        self.value = value  
        self.description = description
        self.source = source

    def display_info(self):
        return f"Type: {self.type}, Value: {self.value}, Description: {self.description}, Source: {self.source}"

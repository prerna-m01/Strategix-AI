class ResourceNotFoundException(Exception):
    def __init__(self, resource: str):
        self.resource = resource


class DuplicateResourceException(Exception):
    def __init__(self, resource: str):
        self.resource = resource


class ValidationException(Exception):
    def __init__(self, message: str):
        self.message = message
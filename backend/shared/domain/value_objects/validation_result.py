class ValidationResult:
    def __init__(self, is_valid: bool, message: str = ""):
        self._is_valid = is_valid
        self._message = message
        
    @property
    def is_valid(self) -> bool:
        return self._is_valid
        
    @property
    def message(self) -> str:
        return self._message
        
    @classmethod
    def valid(cls) -> 'ValidationResult':
        return cls(True)
        
    @classmethod
    def invalid(cls, message: str) -> 'ValidationResult':
        return cls(False, message) 
from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BasePlugin(ABC):
    """
    Abstract Base Class that every single data processing plugin must inherit.
    Forces a unified contract for dynamic pipeline execution.
    """
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Executes the custom logical transformation on the dataset array."""
        pass

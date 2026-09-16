import operator
from typing import List, Dict, Any
from src.base_plugin import BasePlugin

class FilterPlugin(BasePlugin):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.field = self.config.get("field")
        self.op_string = self.config.get("operator")
        self.threshold = self.config.get("value")
        
        self.operators = {
            "GREATER_THAN": operator.gt,
            "LESS_THAN": operator.lt,
            "EQUALS": operator.eq,
            "NOT_EQUALS": operator.ne
        }

    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if not self.field or self.op_string not in self.operators:
            return data
            
        op_func = self.operators[self.op_string]
        filtered_dataset = []
        
        for row in data:
            if self.field in row:
                try:
                    if op_func(row[self.field], self.threshold):
                        filtered_dataset.append(row)
                except TypeError:
                    # Ignore rows with invalid types for mathematical comparisons
                    continue
                    
        return filtered_dataset

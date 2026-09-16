from typing import List, Dict, Any
from src.base_plugin import BasePlugin

class TransformerPlugin(BasePlugin):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.rename_map = self.config.get("rename_columns", {})
        self.uppercase_fields = self.config.get("uppercase_fields", [])

    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        processed_data = []
        for row in data:
            new_row = {}
            # Apply key renames and value casing adjustments
            for key, val in row.items():
                target_key = self.rename_map.get(key, key)
                if target_key in self.uppercase_fields and isinstance(val, str):
                    new_row[target_key] = val.upper()
                else:
                    new_row[target_key] = val
            processed_data.append(new_row)
        return processed_data

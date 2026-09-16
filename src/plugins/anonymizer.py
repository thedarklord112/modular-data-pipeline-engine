import re
from typing import List, Dict, Any
from src.base_plugin import BasePlugin

class AnonymizerPlugin(BasePlugin):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.target_fields = self.config.get("fields", [])
        # High performance compiled regex pattern to detect email components
        self.email_regex = re.compile(r"([\w\.-]+)@([\w\.-]+\.\w+)")

    def _mask_email(self, email_str: str) -> str:
        match = self.email_regex.match(email_str)
        if match:
            username = match.group(1)
            domain = match.group(2)
            # Mask user name partially: user@email.com -> u***@email.com
            return f"{username[0]}***@{domain}" if len(username) > 1 else f"***@{domain}"
        return "CONFIDENTIAL"

    def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for row in data:
            for field in self.target_fields:
                if field in row and isinstance(row[field], str):
                    row[field] = self._mask_email(row[field])
        return data

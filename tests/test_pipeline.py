import unittest
from src.core import PipelineEngine

class TestModularDataPipeline(unittest.TestCase):
    def setUp(self):
        # A processing recipe layout typically loaded from a database or JSON configuration file
        self.mock_recipe = [
            {
                "module": "transformer",
                "class": "TransformerPlugin",
                "config": {
                    "rename_columns": {"user_email": "email", "total_purchase": "price"},
                    "uppercase_fields": ["name"]
                }
            },
            {
                "module": "anonymizer",
                "class": "AnonymizerPlugin",
                "config": {"fields": ["email"]}
            },
            {
                "module": "filter",
                "class": "FilterPlugin",
                "config": {"field": "price", "operator": "GREATER_THAN", "value": 50.0}
            }
        ]
        
        self.raw_data = [
            {"name": "alice doe", "user_email": "alice@gmail.com", "total_purchase": 150.0},
            {"name": "bob smith", "user_email": "bob@yahoo.com", "total_purchase": 20.0}, # Should be filtered out (< 50)
            {"name": "charlie brown", "user_email": "charlie@outlook.com", "total_purchase": 75.5}
        ]

    def test_pipeline_waterfall_execution(self):
        engine = PipelineEngine(self.mock_recipe)
        result = engine.execute(self.raw_data)

        # Assertions to verify correct data processing
        self.assertEqual(len(result), 2)  # Bob smith must be filtered out
        
        # Check column name adjustments & casing transforms
        self.assertEqual(result[0]["name"], "ALICE DOE")
        self.assertIn("email", result[0])
        self.assertNotIn("user_email", result[0])
        
        # Check regex masking functionality
        self.assertEqual(result[0]["email"], "a***@gmail.com")
        self.assertEqual(result[1]["email"], "c***@outlook.com")

if __name__ == "__main__":
    unittest.main()

<img width="1425" height="723" alt="image" src="https://github.com/user-attachments/assets/c3d98d32-fc8a-41a2-b595-26011ebc189a" />

```text
  [ DISASTROUS RAW DATA ] -> [{"user_email": "alice@gmail.com", "total_purchase": 150.0}]
         │
         ▼
  [ 🔄 STEP 1: TRANSFORMER ] -> Fixes key names so engineers don't cry
         │
         ▼
  [ 🔒 STEP 2: ANONYMIZER ]  -> Hides emails with Regex before the auditors fine us
         │
         ▼
  [ 🎯 STEP 3: FILTER ]      -> Yeets out records with low-value purchases
         │
         ▼
  [ BEAUTIFUL OUTPUT ]    -> [{"name": "ALICE DOE", "email": "a***@gmail.com", "price": 150.0}]
```

A production-grade, highly architectural, and completely sanity-saving **Data Processing Pipeline Engine** built with pure, unadulterated **Python**. 

Did your marketing team just send you a "database" that is actually a chaotic CSV file filled with emojis, missing fields, and raw emails? Are you terrified of the compliance team finding out you are storing unencrypted customer data? Or are you just tired of writing 54 nested `if/else` statements every time the data schema changes?

**This engine is your mental health insurance policy. Welcome to automated data scrubbing.**

---

## ⚡ Why Use This? (Besides saving your weekend)

- **Buzzword-Compliant Reflection Engine**: We don't hardcode procedural loops here. The engine uses advanced metaprogramming (`importlib`) to read a JSON "recipe" and instantiate python classes dynamically out of thin air. It's so clean it will make your senior devs nod in approval.
- **The Audit Blinder (Regex Anonymizer)**: Uses ultra-fast pre-compiled regular expressions to scrub corporate emails into `a***@domain.com` before the legal team has a panic attack. 
- **The "Yeet" Plugin (Dynamic Filtering)**: Maps raw mathematical strings (like `GREATER_THAN`) directly to Python’s internal `operator` functions. It safely filters out low-value records or bad data without throwing a single database exception.
- **The Schema Fixer (Transformer)**: Because data sent by non-engineers *never* has clean column names. This plugin renames keys, normalizes text casing, and formats data into something a computer can actually read.

---

## 📂 Inside the Cleaning Matrix

```text
├── src/
│   ├── __init__.py
│   ├── base_plugin.py     # The strict contract every plugin must sign
│   ├── core.py            # The dynamic brain that runs the waterfall flow
│   └── plugins/           # Where the actual dirty work happens
│       ├── __init__.py
│       ├── anonymizer.py  # The compliance shield (Regex wizardry)
│       ├── filter.py      # The mathematical threshold selector
│       └── transformer.py # The database column structural fixer
└── tests/
    └── test_pipeline.py   # Code showing your boss that the data is actually clean
```

---

## 🛠️ Quick Start (Before the pipeline clogs)

Here is how you feed raw data into the waterfall pipeline loop:

```python
from src.core import PipelineEngine

# 1. Define your processing recipe (Usually loaded from a JSON file)
cleaning_recipe = [
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

# 2. Fire up the pipeline machine
pipeline_factory = PipelineEngine(cleaning_recipe)

# 3. Enter the terrifying raw data dataset
toxic_waste_data = [
    {"name": "alice doe", "user_email": "alice@gmail.com", "total_purchase": 150.0},
    {"name": "bob smith", "user_email": "bob@yahoo.com", "total_purchase": 20.0}, # Too cheap! Filter will drop this.
    {"name": "charlie brown", "user_email": "charlie@outlook.com", "total_purchase": 75.5}
]

# 4. Run the engine and watch the magic happen
clean_sparkling_data = pipeline_factory.execute(toxic_waste_data)
print(clean_sparkling_data)
# Output: [{'name': 'ALICE DOE', 'email': 'a***@gmail.com', 'price': 150.0}, ...]
```

---

## 🧪 Testing the Pipeline Integrity

To run the integration tests and prove to the company that you aren't just copy-pasting code from AI all day:

```bash
python -m unittest discover -s tests
```

## 🔒 Data Safety Notice
This engine handles data strictly in-memory using deep-cloned dictionary matrices to protect you from side effects and race conditions. However, if you feed it an Excel file with 4 million rows, your computer *will* take off like a Boeing 747. Use responsibly.

## 📄 License
This automated data-scrubbing framework is open-source and free to save your career under the **MIT License**. 

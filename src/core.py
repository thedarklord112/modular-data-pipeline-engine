import importlib
from typing import List, Dict, Any, Type
from src.base_plugin import BasePlugin

class PipelineEngine:
    def __init__(self, recipe: List[Dict[str, Any]]):
        self.recipe = recipe
        self.active_pipeline: List[BasePlugin] = []
        self._build_pipeline()

    def _get_plugin_class(self, module_name: str, class_name: str) -> Type[BasePlugin]:
        """Dynamically imports a module and grabs the plugin class from memory."""
        try:
            module = importlib.import_module(f"src.plugins.{module_name}")
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            raise RuntimeError(f"Pipeline Engine Crash: Failed to dynamically load plugin '{class_name}'. Error: {str(e)}")

    def _build_pipeline(self):
        """Assembles the sequence of operations matching the JSON configuration blueprint."""
        for step in self.recipe:
            module_name = step.get("module")
            class_name = step.get("class")
            config = step.get("config", {})
            
            plugin_class = self._get_plugin_class(module_name, class_name)
            # Instantiate the object class dynamically with its specific configurations
            self.active_pipeline.append(plugin_class(config))

    def execute(self, initial_dataset: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Streams the dataset across the chained plugins sequentially (Waterfall pattern)."""
        current_data = [dict(row) for row in initial_dataset]  # Deep clone to avoid mutating input state
        
        for plugin in self.active_pipeline:
            current_data = plugin.process(current_data)
            
        return current_data

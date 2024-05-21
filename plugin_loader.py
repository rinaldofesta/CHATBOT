
import importlib
import os

class PluginLoader:
    def __init__(self, plugin_folder='plugins'):
        self.plugin_folder = plugin_folder
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith(".py"):
                plugin_name = filename[:-3]
                module = importlib.import_module(f"{self.plugin_folder}.{plugin_name}")
                self.plugins[plugin_name] = module

    def handle_message(self, message):
        responses = []
        for plugin_name, plugin_module in self.plugins.items():
            plugin_class = getattr(plugin_module, plugin_name.capitalize())
            plugin_instance = plugin_class()
            responses.append(plugin_instance.handle_message(message))
        return responses

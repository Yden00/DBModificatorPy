import os
import xml.etree.ElementTree as ET


class ConfigLoader:
    def __init__(self, config_path: str):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        self.tree = ET.parse(config_path)
        self.root = self.tree.getroot()
        self.settings = self._load_settings()
        self.projects = self._load_projects()
        self.tables = self._load_tables()

    def _load_settings(self) -> dict:
        settings_node = self.root.find("Settings")
        if settings_node is None:
            raise ValueError("Missing <Settings> section in config file.")
        return {
            "url": settings_node.findtext("URL"),
            "server": settings_node.findtext("Server"),
            "port": settings_node.findtext("Port"),
            "network_files": settings_node.findtext("NetworkFiles"),
            "user": settings_node.findtext("User"),
            "password": settings_node.findtext("Password")
        }

    def _load_projects(self) -> list[str]:
        return [p.text for p in self.root.findall("Projects/DMProject") if p.text]

    def _load_tables(self) -> list[str]:
        return [t.text for t in self.root.findall("Tables/Name") if t.text]

    def get_settings(self) -> dict:
        return self.settings

    def get_projects(self) -> list[str]:
        return self.projects

    def get_tables(self) -> list[str]:
        return self.tables

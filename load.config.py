import yaml
import os
from dataclasses import dataclass, asdict

if os.path.exists("config.yaml"):
    with open("config.yaml", "r") as yaml_file:
        loaded_config = yaml.safe_load(yaml_file)
else:
    loaded_config = {"app":
        {"name": "SmartThermo",
         "version": "1.2.0",
         "features": ["temperature_control", "remote_access", "energy_saving"],
         "mode": "off",
         "set_point": 72},
         "logging": {"level": "info", "file": "logs/output.log"}}

@dataclass
class SmartThermoConfig:
    name: str
    version: str
    features: list[str]
    mode: str
    set_point: int
    
    def change_mode(self, mode: str):
        self.mode = mode
        return self.mode
        
    def change_set_point(self, set_point: int):
        self.set_point = set_point
        self.what_set_point = set_point
        return self.what_set_point
    
    def save_to_yaml(self, filepath: str) -> None:
        with open(filepath, "w") as file:
            yaml.dump(asdict(self), file)
        
config_data = loaded_config["app"]
config = SmartThermoConfig(
    name = config_data["name"],
    version = config_data["version"],
    features = config_data["features"],
    mode = config_data["mode"],
    set_point = config_data["set_point"]
)

print(f"{config.name} v{config.version}\nEnabled features: {', '.join(config.features)}\nCurrent mode: {config.change_mode(config.mode)}\nCurrent set point: {config.change_set_point(config.set_point)}")

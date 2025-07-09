import yaml
from pathlib import Path

config_file_path = Path("config.yaml")

if config_file_path.exists():
    with open(config_file_path, "r") as config_file:
        config_data = yaml.safe_load(config_file)
else:
    config_data = { ... }
    with open(config_file_path, "w") as config_file:
        yaml.dump(config_data, config_file)
import yaml

def get_config(path):
    with open("configs/config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
    return config   

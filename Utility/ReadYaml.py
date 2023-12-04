import  yaml

class YamlUtility:
    def __init__(self,filepath):
        self.filepath = filepath

    def read_yaml_td(self,key):
        with open(self.filepath,'r') as f:
            output= yaml.safe_load(f)
            value=output.get(key)
            return value


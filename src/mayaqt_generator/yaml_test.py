import yaml
import os
import pprint

sample_yaml = os.path.join(os.path.dirname(__file__), "sample.yaml")

with open(sample_yaml) as f:
    yml = yaml.load(f)
    pprint.pprint(yml)

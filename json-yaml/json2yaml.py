import json

from ruamel.yaml import YAML

in_file = "json_in.json"
out_file = "yaml_out.yaml"

yaml = YAML(typ="safe")
yaml.default_flow_style = False

with open(in_file, "r", encoding="utf-8") as i:
	data = json.load(i)

with open(out_file, "w", encoding="utf-8") as o:
	yaml.dump(data, o)
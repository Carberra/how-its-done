import json

from ruamel.yaml import YAML

in_file = "yaml_in.yaml"
out_file = "json_out.json"

yaml = YAML(typ="safe")

with open(in_file, "r", encoding="utf-8") as i:
	data = yaml.load(i)

with open(out_file, "w", encoding="utf-8") as o:
	json.dump(data, o, indent=4, ensure_ascii=False)
def xml_to_json(xml_data):
    root = ET.fromstring(xml_data)
    json_data = json.dumps(xml_to_dict(root), indent=4)
    return json_data

def json_to_yaml(json_data):
    yaml_data = yaml.dump(json.loads(json_data))
    return yaml_data

def yaml_to_json(yaml_data):
    json_data = json.dumps(yaml.safe_load(yaml_data), indent=4)
    return json_data
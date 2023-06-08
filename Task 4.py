def xml_to_yaml(xml_data):
    root = ET.fromstring(xml_data)
    yaml_data = yaml.dump(xml_to_dict(root))
    return yaml_data

def json_to_yaml(json_data):
    yaml_data = yaml.dump(json.loads(json_data))
    return yaml_data

def yaml_to_xml(yaml_data):
    data = yaml.safe_load(yaml_data)
    root = dict_to_xml(data)
    xml_data = ET.tostring(root).decode()
    return xml_data
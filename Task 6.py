def xml_to_dict(element):
    data = {}
    if element.attrib:
        data["@attributes"] = element.attrib
    if element.text:
        data["@text"] = element.text
    for child in element:
        child_data = xml_to_dict(child)
        if child.tag in data:
            if not isinstance(data[child.tag], list):
                data[child.tag] = [data[child.tag]]
            data[child.tag].append(child_data)
        else:
            data[child.tag] = child_data
    return data

def xml_to_json(xml_data):
    root = ET.fromstring(xml_data)
    json_data = json.dumps(xml_to_dict(root), indent=4)
    return json_data

def xml_to_yaml(xml_data):
    root = ET.fromstring(xml_data)
    yaml_data = yaml.dump(xml_to_dict(root))
    return yaml_data
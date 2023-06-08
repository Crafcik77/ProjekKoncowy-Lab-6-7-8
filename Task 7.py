def dict_to_xml(data):
    root_name = list(data.keys())[0]
    root = ET.Element(root_name)
    dict_to_xml_recursive(root, data[root_name])
    return root

def json_to_xml(json_data):
    data = json.loads(json_data)
    root = dict
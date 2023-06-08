import sys
import os
import json
import yaml
import xml.etree.ElementTree as ET

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

def json_to_xml(json_data):
    data = json.loads(json_data)
    root = dict_to_xml(data)
    xml_data = ET.tostring(root).decode()
    return xml_data

def json_to_yaml(json_data):
    yaml_data = yaml.dump(json.loads(json_data))
    return yaml_data

def yaml_to_xml(yaml_data):
    data = yaml.safe_load(yaml_data)
    root = dict_to_xml(data)
    xml_data = ET.tostring(root).decode()
    return xml_data

def yaml_to_json(yaml_data):
    json_data = json.dumps(yaml.safe_load(yaml_data), indent=4)
    return json_data

def dict_to_xml(data):
    root_name = list(data.keys())[0]
    root = ET.Element(root_name)
    dict_to_xml_recursive(root, data[root_name])
    return root

def dict_to_xml_recursive(parent, data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                element = ET.SubElement(parent, key)
                dict_to_xml_recursive(element, value)
            elif isinstance(value, list):
                for item in value:
                    element = ET.SubElement(parent, key)
                    dict_to_xml_recursive(element, item)
            else:
                element = ET.SubElement(parent, key)
                element.text = str(value)
    elif isinstance(data, list):
        for item in data:
            dict_to_xml_recursive(parent, item)

def convert_file(input_file, output_file):
    file_name, file_extension = os.path.splitext(input_file)
    input_data = open(input_file, 'r').read()
    output_data = ''

    if file_extension == '.xml':
        if output_file.endswith('.json'):
            output_data = xml_to_json(input_data)
        elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
            output_data = xml_to_yaml(input_data)
    elif file_extension == '.json':
        if output_file.endswith('.xml'):
            output_data = json_to_xml(input_data)
        elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
            output_data = json_to_yaml(input_data)
    elif file_extension == '.yml' or file_extension == '.yaml':
        if output_file.endswith('.xml'):
            output_data = yaml_to_xml(input_data)
        elif output_file.endswith('.json'):
            output_data = yaml_to_json(input_data)

    if output_data:
        with open(output_file, 'w') as output:
            output.write(output_data)
        print('Konwersja zakończona sukcesem.')
    else:
        print('Nieprawidłowy format pliku wyjściowego.')

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('Nieprawidłowa liczba argumentów. Program nie ожидает аргументы командной строки.')
        sys.exit(1)

    input_file = input('Podaj ścieżkę do pliku wejściowego: ')
    output_file = input('Podaj ścieżkę do pliku wyjściowego: ')

    convert_file(input_file, output_file)

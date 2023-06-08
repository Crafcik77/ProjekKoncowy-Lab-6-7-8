if output_file.endswith('.yml') or output_file.endswith('.yaml'):
    output_data = xml_to_yaml(input_data)

with open(output_file, 'w') as output:
    output.write(output_data)
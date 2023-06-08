if output_file.endswith('.json'):
    output_data = yaml_to_json(input_data)

with open(output_file, 'w') as output:
    output.write(output_data)
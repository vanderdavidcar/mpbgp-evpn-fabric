#Imports from Jinja2
from jinja2 import Environment, FileSystemLoader

#Import YAML from PyYAML
import yaml

#Load data from YAML file into Python dictionary
config = yaml.load(open('./brbsa-bt01-leaf1-1.yml'))

#Load Jinja2 template
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('vlan_template.j2')

#Render template using data and print the output
print(template.render(config))

#Imports from Jinja2
from jinja2 import Environment, FileSystemLoader

#Import YAML from PyYAML
import yaml

devices = ["leaf1","leaf2","spine1","spine2","stor1","stor2"]
var_template = ["leaf", "spine", "stor"]

def get_configs_templates():
    for ips in devices:
        for i in var_template:
            if ips in devices:
                #Load data from YAML file into Python dictionary
                config = yaml.load(open(f'./var_{ips}.yml'))

                #Load Jinja2 template
                env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)

                template = env.get_template(f'{i}_template.j2')
                #Render template using data and print the output
                output = (template.render(config))
                scriptFile = open(f'{ips}.cfg', "w+")
                scriptFile.write(output)
                print(f'Created script FileName config_default.cfg')
                print(output)

get_configs_templates()

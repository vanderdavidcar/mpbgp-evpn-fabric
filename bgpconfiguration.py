import csv
from jinja2 import Template

source_file = "template.csv"

interface_template_file = "bgp_template.j2"

with open(interface_template_file) as f:
     interface_template = Template(f.read())

type(interface_template)

interface_configs = ""


with open(source_file) as f:
     reader = csv.DictReader(f)
     for row in reader:
         interface_config = interface_template.render(
            bgp_hostname = row["bgphostame"],
            bgp_asn = row["bgpasn"],
            route_rid = row["bgprouterid"],
            neigh_asn = row["bgpneighbors"],
#            neighip = row["neighip"],
            secret = row["secret"]
         )
         interface_configs += interface_config
print (interface_configs)





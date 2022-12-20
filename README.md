# How to create many scripts using jinja templates to deploy a Fabric VXLAN MPBGP-EVPN

Using this codes youn will deploy scripts to deploy VXLAN environment, can be used to many porposes to get many scripts using jinja templates.

## Dependencies: Install the requirements to have all dependencies used on this project
$ pip install -r requirements

## variables
Needed to populate all jinja template files "leaf_template.j2", for any device needed a file with all variables as var.yml</br>
When I did this code I was using a pattern for files as "var_{device}.yml"

## templates.j2
Have all scripts using variables that will be generate by function get_configs()

## get_config.py
Get all template.j2 and vars files "var_{device}.yml" to generate scripts "{device}.cfg"


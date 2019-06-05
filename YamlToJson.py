import yaml
import os
import json

yamldirectory = 'all'
jsondirectory = 'alljson'

yamlfiles = os.listdir(yamldirectory)

##Create destination folder
if not os.path.exists(jsondirectory):
    os.makedirs(jsondirectory)

##Read YAML and write to destination JSON
for yamlfile in yamlfiles:
    ##Read YAML file
    yamldata = open(yamldirectory + '\\' + yamlfile, 'r')
    jsondata = yaml.load(yamldata.read())

    jsonfile = open(jsondirectory + '\\' + yamlfile.replace('yaml', 'json'), 'w+')
    jsonfile.write(json.dumps(jsondata, default=str))
    jsonfile.close()
    yamldata.close()

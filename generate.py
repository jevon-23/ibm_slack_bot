import requests
import re

# Default version
VERSION = "2.2.0"

# The url prefix that we want to access
url_prefix = "https://www.ibm.com/docs/en/zos/"+VERSION+"?topic="

# Different types of webpages that we have around
INFO = 'info'
PII = 'inter'
HEAD = 'head'
MAPP = 'map'

# Returns a list of all of the lines in CONTENTS that contains VALUE
def grep(contents, value):
    out = []
    data = contents.split("\n")
    for line in data:
        if value in line:
            out.append(line)

    for i in out:
        print(i)
    return out

# Retrieves the html for URL.
def get_website(url):
    web = requests.get(url).text
    return web

# Genrates a url for the mapping of CONTROL_BLOCK
def generate_mapping(control_block):
    return url_prefix + 'information-'+control_block+'-mapping'

# Genrates a url for the heading of CONTROL_BLOCK
def generate_heading(control_block):
    return url_prefix + 'information-'+control_block+'-heading'

# Genrates a url for the program interface info of CONTROL_BLOCK
def generate_prog_interf_info(control_block):
    return url_prefix + 'information-'+control_block+'-programming-interface'

# Chooses the correct url extension based on the control block being passed in 
def info_section(control_block):
    cb = control_block.upper()
    vol_1 = 'iax-'
    vol_2 = 'isg-'
    vol_3 = 'sce-'
    vol_4 = 'xtl-'

    print(cb, str(len(cb)))
    if cb[:3] <= 'IAX' and cb[3] <= 'C':
        if len(cb) < 5 or (len(cb) > 4 and cb[4] <= 'N'):
            return vol_1
    elif cb[:3] <= 'ISG' or (cb[:3] == 'IAX' and cb[4] <= 'P'):
        return vol_2
    elif cb[:3] < 'SCE':
        return vol_3
    elif cb[:3] == 'SCE':
        return ''
    elif cb[:3] <= 'XTL':
        return vol_4
    else:
        print("invalid input for cb: " + cb)
        exit(-1)
    return

# Genrates a url for the info of CONTROL_BLOCK
def generate_info(control_block):
        return url_prefix + info_section(control_block) +control_block.lower()+'-information'

# Map data area types to their given their url functions
url_gens = {
        INFO: generate_info,
        PII:  generate_prog_interf_info,
        HEAD: generate_heading,
        MAPP: generate_mapping,
}

# Gets the TYP webpage for CONTROL_BLOCK
def url_generator(control_block, typ):
    control_block = control_block.lower()
    url = url_gens[typ](control_block)
    print(url)
    html = get_website(url)
    return html;

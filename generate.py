"""
GENERATES A URL AND RETURNS BACK THE HTML OF THE WEBPAGE ASSOCIATED WITH THAT URL

WE ARE ONLY WEBSCRAPING THE Z/OS BOOK, SO BASED ON THE DESIRED CONTROL BLOCK AND 
VERION, WE CAN GENERATE A URL THAT IS ASSOCIATED W/ THE CONTROL BLOCK WE WANT INFO
ABOUT
"""

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

# Retrieves the html for URL.
def get_website(url):
    web = requests.get(url).text
    return web

# Chooses the correct url extension based on the control block being passed in 
def info_section(control_block):
    if (control_block == 'information-'):
        return control_block
    
    cb = control_block.upper()

    # 4 Volumes that split of the book into sections; 
    # each one containting a subsection of all ctrl blocks
    vol_1 = 'iax-'
    vol_2 = 'isg-'
    vol_3 = 'sce-'
    vol_4 = 'xtl-'

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

########################################################################
# Function: Generates a url based on CONTROL_BLCOK and ARGS            #
# EXAMPLE URLS FOR FORMATTING:                                         #
# https://www.ibm.com/docs/en/zos/2.2.0?topic=iax-ascb-information     #
# | url_prefix                   (vers)      |inf|cb  |typ       |     #
#                                            (generate_url_args + cb)  #
# https://www.ibm.com/docs/en/zos/2.2.0?topic=information-ascb-heading #
# | url_prefix                   (vers)      |info       | cb | typ    #
########################################################################
def generate_url(control_block, args):
    info = args[0]
    typ = args[1]

    # If we are dealing w/ control_block info, get the volume
    if (info == ""):
        info = info_section(control_block)

    return url_prefix + info + control_block + typ

# Based on data type area, return the arguments needed to generate its url
generate_url_args = {
        INFO: ["", '-information'],
        PII:  ['information-', '-programming-interface'],
        HEAD: ['information-', '-heading'],
        MAPP: ['information-', '-mapping'],
}

# Gets the TYP webpage for CONTROL_BLOCK
def url_generator(control_block, typ):
    control_block = control_block.lower()

    # Get the arguments for generate url based on type
    args = generate_url_args[typ]

    # Generate url
    url = generate_url(control_block, args)

    print(url)

    # Generate html
    html = get_website(url)
    return html;

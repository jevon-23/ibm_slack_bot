from bs4 import BeautifulSoup 
import generate

# Extracts the text from the nested tag CONTENTS
def strip_text(contents):
    extract = []
    for line in contents:
        value = line.text
        value = value.replace("Â","")
        extract.append(value)
    return extract

# Helper function to help extract both the info section and the prog_interface_info
def extract_info(bscontents, tag, the_class):
    # Find all lines w/ this tag & class
    info = bscontents.find_all(tag, class_=the_class)

    # Extract the text nested in the tags, and append them to extract
    extract = strip_text(info)
    return [extract]

# Extract function for info
def extract_info_info(bscontents):
    return extract_info(bscontents, 'li', "link ulchildlink")

# Extract function for program interface info
def extract_prog_interf_info(bscontents):
    return extract_info(bscontents, 'li', 'li')

# Extract function for headding & map
def extract_table(bscontents):
    head = bscontents.find_all('tr', class_='row')
    extract = []
    for line in head:
        contents = line.find_all('td', class_='entry')
        data = strip_text(contents)

        pair = [x for x in data]
        extract.append(pair)

    return extract


# Switch case for functions to call based on type
extract_funcs = {
        generate.PII : extract_prog_interf_info,
        generate.INFO: extract_info_info,
        generate.HEAD: extract_table,
        generate.MAPP: extract_table,
}

"""
Extracts all of the text values from the html CONTENTS, and returns them in a list

INPUTS: 
    str contents: html of the webpage that we would like to extract data from
    str typ:      type of webpage that we accessed
OUTPUTS:
    str[][] extracted: 2D array of strings. 1
                       extracted[x]    -> section
                       extracted[x][y] -> Text written in section
"""
def extract(contents, typ):
    # Change into bs4 object 
    scontents = BeautifulSoup(contents, 'html.parser')
    return extract_funcs[typ](scontents)



"""
EXTRACTS THE TEXT THAT IS STORED WITHIN THE HTML THAT IS PASSED IN

TAKES IN HTML FROM URL GENERATE, WHICH COMES FROM A REQUEST OBJECT
TURN THAT REQUEST OBJECT IN TO A BS4 OBJECT, AND PARSE BS4 CONTENTS
FOR THE TEXT DATA
"""

from bs4 import BeautifulSoup 
import generate

# Extracts the text from the nested tag CONTENTS
def strip_text(contents):
    extract = []

    # Extract the text from every line in CONTENTS
    for line in contents:
        value = line.text
        value = value.replace("Â","") # Value that was being used for \t
        extract.append(value)
    return extract

# Helper function to help extract both the info section and the prog_interface_info
def extract_info(bscontents, tag, the_class):
    # Find all lines w/ TAG & CLASS
    info = bscontents.find_all(tag, class_=the_class)

    # Extract the text nested in the tags, and append them to extract
    extract = strip_text(info)
    return [extract]

# Extract function for headding & map
def extract_table(bscontents, unused1, unused2):
    # Find all of the headings 
    head = bscontents.find_all('tr', class_='row')
    extract = []

    # Find all of the texts within the headings and 
    for line in head:
        # Find text sections within headings 
        contents = line.find_all('td', class_='entry')
        data = strip_text(contents)

        # Save them as a tuple to EXTRACT
        pair = [x for x in data]
        extract.append(pair)

    return extract

# Switch case for functions to call based on type, alongside their arguments
extract_funcs = {
        generate.PII : [extract_info,'li', 'li'],
        generate.INFO: [extract_info,'li', "link ulchildlink"],
        generate.HEAD: [extract_table, '', ''],
        generate.MAPP: [extract_table, '', '']
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

    # Get the extract function call and arguments, and run it 
    extract_func_call = extract_funcs[typ]
    func = extract_func_call[0]
    args = extract_func_call[1:]


    return func(scontents, args[0], args[1])


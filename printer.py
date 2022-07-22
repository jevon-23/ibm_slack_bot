import generate


"""
Format line for printing
"""
def print_mapp_line(line):
    out = ""
    if len(line) == 6:
        # Mapping normal
        out += "Dec: " + line[0] + '\n'
        out += "Hex: " + line[1] + '\n'
        out += "Type: "+ line[2] + '\n'
        out += "Len: " + line[3] + '\n'
        out += "Name: "+ line[4] + '\n'
        out += "Desc: "+ line[5] + '\n'
    elif len(line) == 5:
        # Mapping bitstring
        out += "Dec: " + line[0] + '\n'
        out += "Hex: " + line[1] + '\n'
        out += "Type: "+ line[2] + '\n'
        out += "Name: "+ line[3] + '\n'
        out += "Desc: "+ line[4] + '\n'
    else:
        # Cross reference
        out += "Name: "+ line[0] + '\n'
        out += "Off: " + line[1] + '\n'
        out += "Hex: " + line[2] + '\n'
    out += '\n-----------\n'
    return out

"""
Print out a row of the mapping based on the OFF_NAME
"""
def print_mapp_row(name, extracted, off_name):
    out = ''
    for line in extracted:
        if len(line) < 3: 
            continue
        if off_name.isdigit() == True:
            if len(line[0]) > 0 and line[0].isdigit() and int(line[0]) == int(off_name):
                out += print_mapp_line(line)
        elif '-x' in off_name.lower() and '('+off_name.lower()[2:]+')' == line[1]:
            out += print_mapp_line(line)

        else:
            check = ' '.join([str(word) for word in line])
            if off_name in check:
                out += print_mapp_line(line)
    return out
    
"""
Print out a heading row of the based on the OFF_NAME
"""
def print_head_row(name, extracted, row_key):
    out = ''
    for line in extracted:
        if row_key.lower() in line[0].lower():
            key = line[0]
            value = line[1]
            value_list = value.split("\n")
            out += key + '\n'

            for v in value_list:
                out += "\t" + v
    return out

"""
Print out the entire mapping
"""
def print_mapp(name, extracted):
    
    out = ''
    for line in extracted:
        p = '\t'.join([str(word) for word in line])
        out += p + '\n--------\n'

    if (len(out) == 0):
        return ''

    out = name + " mapping" + '\n' + out
    return out

"""
Print out the entire heading
"""
def print_head(name, extracted):
    out = ''
    for line in extracted:
        key = line[0]
        value = line[1]
        value_list = value.split("\n")
        out += key + '\n'
        for v in value_list:
            out += "\t" + v + '\n'

    if len(out) == 0:
        return ''

    out = name + " Heading Information\n" + out
    return out

"""
Print out info associated w/ EXTRACTED
"""
def print_info(extracted):
    out =  ''
    extracted = extracted[0]

    for info in extracted:
        out += "\t- " + str(info) + '\n'

    return out


"""
Print out program interface info associated w/ EXTRACTED
"""
def print_prog_interf_info(name, extracted):
    out = ''
    info = print_info(extracted)

    if (not len(info)):
        return ''
    else:
        out = ''
        out += name.upper() + " Programming Interface Information\n"
        out += "The following fields are part of the programming interface information\n"
        out += info
        
    return out

"""
The print function for the info section of the control block NAME
"""
def print_info_info(name, extracted):
    out = '' 
    info = print_info(extracted)

    # Did not extract anymore information, so return none
    if (not len(info)):
        return out
    out = name.upper() + " Information" + '\n'
    out += info
    return out

"""
The print functions that is associated w/ each type. Used for 
print_out()
"""
print_funcs = {
        generate.PII : print_prog_interf_info,
        generate.INFO: print_info_info,
        generate.HEAD: print_head,
        generate.MAPP: print_mapp,
}

"""
Print function
"""
def print_out(name, extracted, typ):
    return print_funcs[typ](name, extracted)


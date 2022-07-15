import generate

def print_mapp_row(name, extracted, off_name):
    for line in extracted:
        check = ' '.join([str(word) for word in line])
        if off_name in check:
            if len(line) == 6:
                # Mapping normal
                print("Dec: " + line[0])
                print("Hex: " + line[1])
                print("Type: "+ line[2])
                print("Len: " + line[3])
                print("Name: "+ line[4])
                print("Desc: "+ line[5])
            elif len(line) == 5:
                # Mapping bitstring
                print("Dec: " + line[0])
                print("Hex: " + line[1])
                print("Type: "+ line[2])
                print("Name: "+ line[3])
                print("Desc: "+ line[4])

            else:
                # Cross reference
                print("Name: "+ line[0])
                print("Off: " + line[1])
                print("Hex: " + line[2])
            print("")
    
def print_head_row(name, extracted, row_key):
    for line in extracted:
        if row_key in line[0]:
            key = line[0]
            value = line[1]
            value_list = value.split("\n")
            print(key)
            [print("\t" + v) for v in value_list]


def print_mapp(name, extracted):
    print(name + " mapping")

    print("dec hex type len name desc")
    for line in extracted:
        p = ' '.join([str(word) for word in line])
        print(p + '\n')

        

def print_head(name, extracted):
    print(name + " Heading Information")
    for line in extracted:
        key = line[0]
        value = line[1]
        value_list = value.split("\n")
        print(key)
        [print("\t" + v) for v in value_list]

def print_info(extracted):
    extracted = extracted[0]

    for info in extracted:
        print("\t- " + str(info))

def print_prog_interf_info(name, extracted):
    print(name + " Programming Interface Information")
    print("The following fields are part of the programming interface information")
    print_info(extracted)
    
    return

def print_info_info(name, extracted):
    print(name + " Information")
    print_info(extracted)
    return

print_funcs = {
        generate.PII : print_prog_interf_info,
        generate.INFO: print_info_info,
        generate.HEAD: print_head,
        generate.MAPP: print_mapp,
}
def print_out(name, extracted, typ):
    print_funcs[typ](name, extracted)


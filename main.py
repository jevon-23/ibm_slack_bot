import sys
from bs4 import BeautifulSoup 
import generate
import extract
import printer
"""
py main.py ascb info
py main.py ascb inter
py main.py ascb head
py main.py ascb map

py main.py ascb map ascbdstk 
py main.py ascb map dstk  // append ascb onto front if needed

py main.py ascb head common
py main.py ascb head size
py main.py ascb head eye

"""

def help():
    print("Returns the online documented information about the control block passed in")
    print("usage:")
    print("\tpython3 main.py {block} {type}")
    print("\tExample: python3 main.py {ascb} {info}")
    print("")
    print("\tpython3 main.py {block} map {offset_name}")
    print("\tExample: python3 main.py ascb map ascbdstk")
    print("")
    print("\tpython3 main.py {block} head {offset_name}")
    print("\tpython3 main.py ascb head common")
    print("")
    print("types: info || inter || head || map")
    print("offset_names: comon || macro || dsect || owning || eye || storage ||")
    print("\t\tsize || created || pointed || serial || func ||")
    exit(-1)

def process_cli(args):
    # Return back help
    if len(args) == 2:
        help()

    if len(args) < 3 or len(args) > 4:
        print("invaid number of arguments.")
        help()
    full_list = [generate.INFO, generate.PII, generate.HEAD, generate.MAPP]
    search_list = full_list[2:]

    typ = args[2]
    if len(args) == 3:
        if typ not in full_list:
            print("invalid type of webpage: " + typ)
            print(full_list)
            help()

    if len(args) == 4:
        if typ not in search_list:
            print("invalid type of webpage for searching.")
            help()

    print(args)
    return

if __name__ == '__main__':

    process_cli(sys.argv)

    # print('info')
    name = sys.argv[1]
    typ = sys.argv[2]
    row_name = ''

    if len(sys.argv) == 4:
       row_name = sys.argv[3] 

    contents = generate.url_generator(name, typ)
    extracted = extract.extract(contents, typ)
    if len(sys.argv) == 3:
        printer.print_out(name, extracted, typ)
    elif len(sys.argv) == 4:
        if typ == generate.HEAD:
            printer.print_head_row(name, extracted, row_name.upper())

        elif typ == generate.MAPP:
            print('hello')
            printer.print_mapp_row(name, extracted, row_name.upper())
        else:
            print("invalid type of webpage for searching")


    # contents = generate.url_generator(pack, generate.INFO)
    # print(generate.PII)
    # contents = generate.url_generator(pack, generate.PII)
    # print(generate.HEAD)
    # contents = generate.url_generator(pack, generate.HEAD)
    # print(generate.MAPP)
    # contents = generate.url_generator(pack, generate.MAPP)

    # extracted = extract.extract(contents, generate.INFO)
    # extracted = extract.extract(contents, generate.PII)
    # extracted = extract.extract(contents, generate.HEAD)
    # extracted = extract.extract(contents, generate.MAPP)
    # for i in extracted:
    #     print(i)

    # printer.print_out(pack, extracted, generate.HEAD)
    # printer.print_mapp_row(pack, extracted, "ASCBDSTK")
    # printer.print_head_row(pack, extracted, "Poi")
    
    # print_info_info(pack, extracted)
    # print_prog_interf_info(pack, extracted)
    # print_head(pack, extracted)
    # print_mapp(pack, extracted)



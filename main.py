import sys
from bs4 import BeautifulSoup 
import generate
import extract
import printer
"""
EXAMPLE CALLS
py main.py ascb info
py main.py ascb inter
py main.py ascb head
py main.py ascb map

py main.py ascb map ascbdstk 
py main.py ascb map dstk  // append ascb onto front if needed
py main.py ascb map -x14
py main.py ascb map 20

py main.py ascb head common
py main.py ascb head size
py main.py ascb head eye
"""

"""
Help function, prints out functionality 
"""
def help():
    print("Returns the online documented information about the control block passed in")
    print("usage:")
    print("\tpython3 main.py {block} {type}")
    print("\tExample: python3 main.py {ascb} {info}")
    print("")
    print("\tpython3 main.py {block} map {offset_name}")
    print("\tpython3 main.py {block} map {hex_offset}")
    print("\tpython3 main.py {block} map {dec_offset}")
    print("\tExample: python3 main.py ascb map ascbdstk")
    print("")
    print("\tpython3 main.py {block} head {offset_name}")
    print("\tpython3 main.py ascb head common")
    print("")
    print("types: info || inter || head || map")
    print("offset_names: comon || macro || dsect || owning || eye || storage ||")
    print("\t\tsize || created || pointed || serial || func ||")
    exit(-1)

"""
Checks the input to ensure that it was passed in the correct # of parameters 
"""
def process_cli(args):
    # Return back help
    if len(args) == 2:
        help()

    # Check for errors
    if len(args) < 3 or len(args) > 4:
        print("invaid number of arguments.")
        help()

    # All the types that we can have 
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

def run_bot(name, typ, row_name):
    contents = generate.url_generator(name, typ)
    extracted = extract.extract(contents, typ)
    if row_name == '':
        return printer.print_out(name, extracted, typ)
    else:
        if typ == generate.HEAD:
            return printer.print_head_row(name, extracted, row_name.upper())

        elif typ == generate.MAPP:
            return printer.print_mapp_row(name, extracted, row_name.upper())
        else:
            print("invalid type of webpage for searching")

def main(argv, say):
    process_cli(argv)

    name = argv[1]
    typ  = argv[2]
    row_name = ''

    if len(argv) == 4:
       row_name = argv[3] 

    bot_output = run_bot(name, typ, row_name)

    if (not len(bot_output)):
        say(f"Could not find {name} {typ} {row_name}")
    else:
        say(bot_output)

if __name__ == '__main__':
    main(sys.argv, print)




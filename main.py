"""
MAIN FUNCTINALITY. TAKE IN SOME ARGUMENTS AND PROCESS THEM.
IF ANYTHING IS INVALID, RUNS HELP() AND EXITS EARLY

NOTE: SAY FN IS EITHER THE SAY() FROM SLACK OR PRINT(). 
      THIS IS USED SO THAT IF WE ARE RUNNING CLI TOOL INSTEAD OF
      SLACK BOT, LESS AMOUNT OF CODE NEEDING TO BE REWRITTEN
"""
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
def help(say):
    out = ''
    out += "Returns the online documented information about the control block passed in\n"
    out += "USAGE:\n"
    out += "\tpython3 main.py {block} {type}\n\n"
    out += "\tEXAMPLE: python3 main.py {ascb} {info}\n"
    out += "\tpython3 main.py {block} map {offset_name}\n"
    out += "\tpython3 main.py {block} map {hex_offset}\n"
    out += "\tpython3 main.py {block} map {dec_offset}\n\n"
    out += "\tEXAMPLE: python3 main.py ascb map ascbdstk\n"
    out += "\tpython3 main.py {block} head {offset_name}\n"
    out += "\tpython3 main.py ascb head common\n"
    out += "\n"
    out += "types: info || inter || head || map\n"
    out += "offset_names (heading): comon || macro || dsect || owning || eye || storage ||\n"
    out += "\t\tsize || created || pointed || serial || func ||\n"
    say(out)
    exit(-1)

"""
Checks the input to ensure that it was passed in the correct # of parameters 
"""
def process_cli(args, say):
    # Return back help
    if len(args) == 2:
        help(say)

    # Check for errors
    if len(args) < 3 or len(args) > 4:
        say("invaid number of arguments.")
        help(say)

    # All the types that we can have 
    full_list = [generate.INFO, generate.PII, generate.HEAD, generate.MAPP]
    search_list = full_list[2:]

    # Get argument type, and check to see if it is a valid input
    typ = args[2]
    if len(args) == 3:
        if typ not in full_list:
            say("invalid type of webpage: " + typ)
            print(full_list)
            help(say)

    # Check to for valid url entry
    if len(args) == 4:
        if typ not in search_list:
            print("invalid type of webpage for searching.")
            help(say)

    print(args)
    return

"""
Calls underlying functionality to run the bot. 
    1. Use NAME and TYP to generate a url, and use that url to webscrape
       webpage and return data into CONTENTS
    2. Use CONTENTS and TYP to extract the data that we want, put data
       into EXTRACTED 2D array
    3. Return the EXTRACTED data based on the TYP formatted 
"""
def run_bot(name, typ, row_name):
    # Generate url and scrape webpage for html
    contents = generate.url_generator(name, typ)

    # Extract the text from the html (CONTENTS)
    extracted = extract.extract(contents, typ)

    # Print out data in a formatted structure
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
    # Process arguments, & ensure that they are valid
    process_cli(argv, say)

    name = argv[1] # Name of control block
    typ  = argv[2] # Information that we are looknig for (heading info, map, etc.)
    row_name = ''  # If passed in, the row that we want to obtain out of heading info or map
    if len(argv) == 4:
       row_name = argv[3] 

    # Run the bot, and save the formatted data 
    bot_output = run_bot(name, typ, row_name)

    # If our output is empty, let the user know
    if (not len(bot_output)):
        say(f"Could not find {name} {typ} {row_name}")
        exit(-1)

    say(bot_output)

if __name__ == '__main__':
    main(sys.argv, print)




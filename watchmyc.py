#!/usr/bin/env python3

import time
import os
import argparse
from datetime import datetime

def file_exists(file):
	return os.path.isfile(file)

def print_header(with_flags, compiler, interval):
	
	if (with_flags): flags_msg = "Compiling With -Wall -Wextra -Werror"
	else: flags_msg = "Compiling Without Any Flags"

	print(f"""
 _    _       _       _     __   __      _____ 
| |  | |     | |     | |   |  \\/  |     /  __ \\
| |  | | __ _| |_ ___| |__ | .  . |_   _| /  \\/
| |/\\| |/ _` | __/ __| '_ \\| |\\/| | | | | |    
\\  /\\  / (_| | || (__| | | | |  | | |_| | \\__/\\
 \\/  \\/ \\__,_|\\__\\___|_| |_\\_|  |_/\\__, |\\____/
                                    __/ |      
             Coded by: r3dBust3r   |___/   v1.0

  [*] Watch Interval: {interval}s
  [*] Using Compiler: {compiler}
  [*] {flags_msg}
  [*] Last Compile: {datetime.now()}
________________________________________________
""")

def __compile(program, with_flags, compiler, interval):

	flags = ""

	if (with_flags):
		flags = "-Wall -Wextra -Werror"

	os.system("clear")

	print_header(with_flags, compiler, interval)

	output = f"{program.split('.')[0]}.bin"

	os.system(f"{compiler} {flags} {program} -o {output}")
	os.system(f"./{output}")

	print("\n")


def watch(args):

	last_mod_time = 0

	while True:
		if (last_mod_time != os.path.getmtime(args.program)):
			last_mod_time = os.path.getmtime(args.program)
			__compile(args.program, args.flags, args.compiler, args.interval)

		time.sleep(args.interval)

def main():
	parser = argparse.ArgumentParser(description="Watch-My-C automatically monitors your C files for changes and recompiles them in real time, giving you instant feedback as you code")
	parser.add_argument("-p", "--program", default="main.c", type=str, help="The program you want to watch")
	parser.add_argument("-c", "--compiler", default="cc", help="Change the compiler")
	parser.add_argument("-f", "--flags", action="store_true", help="Enable -W -W -W flags")
	parser.add_argument("-i", "--interval", type=float, default=0.5, help="Watch interval in seconds")

	args = parser.parse_args()

	if (not file_exists(args.program)):
		print(f"[!] No such file {args.program}")
		exit(0)

	try:
		watch(args)

	except KeyboardInterrupt:
		print("\n[*] Exiting...")

if __name__ == "__main__": main()

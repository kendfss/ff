from pprint import pprint
from subprocess import run
from argparse import ArgumentParser

from os import getcwd
ocd = getcwd()


from .env import *




def handler(args):
    keep = not args.close
    if args.pop:
        paths = [this, __file__]
        pop(os.path.dirname(here))
        [*map(pop, paths)]
    if args.formats:
        cd(ocd)
        pprint(get_formats())
        cd(defaultdir)
    if args.allformats:
        cd(ocd)
        pprint(get_formats(True))
        cd(defaultdir)
    
    if args.defaultdir:
        settings["default_directory"] = args.defaultdir
        save_settings()
        cd(args.defaultdir)
    if args.settings:
        print("SETTINGS")
        pprint(settings)
    
    if keep:
        run(['python', '-i', this])
    
    


def main():
    parser = ArgumentParser(description="REPL for pythonic file system management and navigation")
    parser.add_argument('--pop', '-p', default=False, action="store_true", help="root to the package/path to the file")
    parser.add_argument('--formats', '-f', default=False, action="store_true", help="scan the current directory for audio and video formats")
    parser.add_argument('--allformats', '-a', default=False, action="store_true", help="scan all sub-directories of the current directory for audio and video formats")
    # parser.add_argument('--defaultdir', '-d', default=os.getcwd(), action="store", help="change the default starting directory")
    parser.add_argument('--defaultdir', '-d', default=None, action="store", help="change the default starting directory")
    parser.add_argument('--settings', '-s', default=False, action="store_true", help="check the settings file")
    parser.add_argument('--close', '-c', default=False, action="store_true", help="close REPL after delivering requested info & making changes")
    # parser.add_argument('--keep', '-k', default=True, action="store_false", help="keep REPL open after delivering requested info & making changes")
    handler(parser.parse_args())


from ftx_cli.parser import get_main_parser, get_subcommmand_parser
from ftx_cli.cmds import AVAILABLE_COMMANDS
import sys 

def main():
    main_parser = get_main_parser()

    sub_parser = get_subcommmand_parser(main_parser)

    # Setup the commands
    for cmd in AVAILABLE_COMMANDS:        
        cmd.__init__(cmd, sub_parser=sub_parser)
    
    try:
        # Parse the arguments
        args = main_parser.parse_args()

        if args.cmd is None:
            main_parser.print_help()
            sys.exit()
    except Exception as e:
        main_parser.print_help()
        sys.exit()

    # Loop the commands again searching for the user-specified command
    for cmd in AVAILABLE_COMMANDS: 
        # If one of the available commands is the specified one       
        if cmd.CMD_NAME == args.cmd:
            # Run it with the provided args
            cmd.run_command(cmd, args)

    
        
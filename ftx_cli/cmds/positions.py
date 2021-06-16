from ftx_cli.abstractions import ACmd
from functools import reduce
import pprint
class PositionsCmd(ACmd):

    CMD_NAME = "positions"
    CMD_HELP = "Commands related to the Position API for FTX"
    CMD_USAGE = """
    $ ftx-cli position --start --end
    $ ftx-cli position --today 
    $ ftx-cli position --api_key --api_secret"""
    CMD_DESCRIPTION = "Tools related to positions for FTX accounts or subaccounts"

    def initialise(self):
        # Define usage and description
        self.parser.usage = self.CMD_USAGE
        self.parser.description = self.CMD_DESCRIPTION
        # Add any positional or optional arguments here
        self.parser.add_argument("-r", "--reduce",
                                 action="store_true",
                                 default=False,
                                 help="(Optional) Whether or not to reduce all the results down to one pair")
        
        self.parser.add_argument("-p", "--pretty",
                                 action="store_true",
                                 default=False,
                                 help="(Optional) Whether or not to do pretty-printing")
        
        
    def run_command(self, args):
        
        ftx = self._get_ftx_client(self.parser, args)
        positions = ftx.get_positions()
        
        if args.reduce:
            # Filter all the empty positions out of this list and then cast back to a list for next mutation
            non_empty_pos = list(filter(lambda x: x['cost'] !=0, positions))
            # Reduce the list of non-empty positions to a single value of position size.
            positions_open = reduce(lambda x, y: x + y['cost'], non_empty_pos, 0)
            print("Total positions open size : {0:.2f}".format(positions_open))
        elif args.pretty:
            pprint.pprint(positions)
        else:
            print(positions)
        

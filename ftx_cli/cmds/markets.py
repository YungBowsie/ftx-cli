from ftx_cli.abstractions import ACmd
import pprint
class MarketsCmd(ACmd):

    CMD_NAME = "markets"
    CMD_HELP = "Commands related to the Markets API for FTX"
    CMD_USAGE = """
    $ ftx-cli markets -m ETH-PERP
    $ ftx-cli markets 
    $ ftx-cli markets --api_key --api_secret -m SUSHI-PERP"""
    CMD_DESCRIPTION = "Tools related to markets for FTX accounts or subaccounts"

    def initialise(self):
        # Define usage and description
        self.parser.usage = self.CMD_USAGE
        self.parser.description = self.CMD_DESCRIPTION
        self.READ_ONLY = True # Mark this command as one that does not do writes (no trades, no orders, no withdraws)

        # Add any positional or optional arguments here
        self.parser.add_argument("-p", "--pretty",
                                 action="store_true",
                                 default=False,
                                 help="(Optional) Whether or not to do pretty-printing")

        self.parser.add_argument("-m", "--market",
                                 type=str,
                                 default="",
                                 help="(Optional) A Specific marketbook to fetch e.g ETH-PERP")
        
        
    def run_command(self, args):
        
        ftx = self._get_ftx_client(self.parser, args)
        markets = ftx.get_markets()

        if args.market:
            markets = ftx.get_market(args.market)
        if args.pretty:
            pprint.pprint(markets)
        else:
            print(markets)

        

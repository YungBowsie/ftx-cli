from ftx_cli.abstractions import ACmd
import pprint
class BalancesCmd(ACmd):

    CMD_NAME = "balances"
    CMD_HELP = "Commands related to the Balance API for FTX"
    CMD_USAGE = """
    $ ftx-cli balances --start --end
    $ ftx-cli balances 
    $ ftx-cli balances --api_key --api_secret"""
    CMD_DESCRIPTION = "Tools related to balances for FTX accounts or subaccounts"

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
        
        
    def run_command(self, args):
        
        ftx = self._get_ftx_client(self.parser, args)
        balances = ftx.get_balances()
        if args.pretty:
            pprint.pprint(balances)
        else:
            print(balances)

        

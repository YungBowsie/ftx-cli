from ftx_cli.abstractions import ACmd
from datetime import datetime 
from functools import reduce
import pprint
class FundingCmd(ACmd):

    CMD_NAME = "fundings"
    CMD_HELP = "Commands related to the Funding API for FTX"
    CMD_USAGE = """
    $ ftx-cli fundings --start --end
    $ ftx-cli fundings --today  
    $ ftx-cli fundings --api_key --api_secret"""
    CMD_DESCRIPTION = "Tools related to funding for FTX accounts or subaccounts"

    def initialise(self):
        # Define usage and description
        self.parser.usage = self.CMD_USAGE
        self.parser.description = self.CMD_DESCRIPTION

        # Add any positional or optional arguments here
        self.parser.add_argument("-t", "--today",
                                 action="store_true",
                                 default=False,
                                 help="(Optional) Whether or not to only query for today")
        
        self.parser.add_argument("-p", "--pretty",
                                 action="store_true",
                                 default=False,
                                 help="(Optional) Whether or not to do pretty-printing")
        
    def run_command(self, args):
        ftx = self._get_ftx_client(self.parser, args)
        fundings = ftx._get(path="funding_payments")

        if args.today:
            # Query for all funding payments between the start of the date and end in UTC from 12:00am to 12:00am the next morning
            fundings = ftx._get(path="funding_payments", params={'start_time': datetime.combine(datetime.today(), datetime.min.time()).timestamp(),'end_time': datetime.combine(datetime.today(), datetime.max.time()).timestamp()})
            todays_funding = []
            for f in fundings:
                # Cast the date strings into date and check if they are from today
                if datetime.strptime(f['time'],"%Y-%m-%dT%H:%M:%S+00:00").date() == datetime.today().date():
                    todays_funding.append(f)

            # Reduce all the fundings to one value
            funding_paid_today = reduce(lambda x, y: x + y['payment'], todays_funding, 0)
            print("Funding paid today: {0:.2f}".format(funding_paid_today))
            exit()
        if args.pretty:
            pprint.pprint(fundings)
        else:
            print(fundings)

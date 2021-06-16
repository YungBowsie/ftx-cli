import argparse as argparse
from argparse import HelpFormatter
import os
import ftx

class ACmd(object):
    """ACmd is an abstraction that helps to
    define a consistant minimal interface for
    each command in this CLI.
    When a class is a subclass of this you have the assurance:
    The class is-a command of some sort
    It has info for its Name, Description, Example Usage and Help
    """
    REQUIRED_FIELDS = ['cmd_name', 'cmd_description', 'cmd_help', 'cmd_usage']


    def __init__(self, sub_parser):
        # Raise an exception if a subclass does not set values for all of the required fields
        if not all(getattr(self, field.upper()) is not None for field in self.REQUIRED_FIELDS):
            raise Exception("Command did not implement all the required fields")

        self.parser = sub_parser.add_parser(self.CMD_NAME,
                            help=self.CMD_HELP,
                            formatter_class=HelpFormatter,
                            parents=[self._get_apikey_parser()])
        self.initialise(self)


    def initialise(self):
        raise NotImplementedError()

    def run_command(self, args):
        raise NotImplementedError()

    @staticmethod
    def _get_apikey_parser():
        """Create a parser that contains arguments for handling FTX API Keys

        Returns:
            argparse.ArgumentParser: A single argparse.ArgumentParser
        """
        key_parser = argparse.ArgumentParser(add_help=False)

        key_parser.add_argument("-ak", "--apikey",
                               type=str,
                               help="The API Key for the Account or Subaccount to use (Defaults to Environment variables)")

        key_parser.add_argument("-as", "--apisecret",
                               type=str,
                               help="The API Secret for the Account or Subaccount to use(Defaults to Environment variables)")

        return key_parser

    @staticmethod
    def _get_ftx_client(parser, args):
        """Using a provided parser and set of args
        setup and return a FTXClient using provided auth credentials.
        Two locations are checked for credentials; first one then the other.

        Args:
            parser (ArgumentParser): An ArgumentParser for this CLI
            args (Args): A set of arguments; the two depended on for this function are
            apikey and apisecret; no other values from args are used.

        Raises:
            ValueError: raised when no api key is found in the args or set in env vars

        Returns:
            FTXClient: An instantiated instance of the FtxClient with the found credentials.
        """
        # If a key and secret were not provided :
        if not all([args.apikey, args.apisecret]):
            # If both a key and a secret are found in the environment :
            if all([os.environ.get('FTX_KEY', False), os.environ.get('FTX_SECRET', False)]):
                print("Found API credentials in the Environment; using those")
                return ftx.FtxClient(api_key=os.environ['FTX_KEY'], api_secret=os.environ['FTX_SECRET'])
            raise ValueError("A valid API_KEY and API_SECRET was not provided with the command or found in the environment.")

        return ftx.FtxClient(api_key=args.apikey, api_secret=args.apisecret)

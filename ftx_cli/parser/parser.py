from argparse import ArgumentParser, HelpFormatter


def get_main_parser():
    parser = ArgumentParser(
            prog="ftx-cli",
            description="Python CLI for working with the FTX API",
            epilog="For support, please open a github issue.")

    parser.usage = """
    $ ftx-cli <subcommand> ...
    $ ftx-cli -v <subcommand> ...
    $ ftx-cli -h
    """

    return parser

def get_subcommmand_parser(main_parser):
    # The subparser will act as a router for commands; each namespace at this level
    # can represent a different set of functionality on the FTX API.
    sub_parser = main_parser.add_subparsers(
        title="subcommands",
        description="one of these subcommands must be provided",
        metavar="",
        dest="cmd"
    )

    return sub_parser


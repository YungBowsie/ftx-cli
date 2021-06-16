from .balances import BalancesCmd
from .positions import PositionsCmd
from .funding import FundingCmd
from .markets import MarketsCmd
AVAILABLE_COMMANDS = (FundingCmd, MarketsCmd, BalancesCmd, PositionsCmd)

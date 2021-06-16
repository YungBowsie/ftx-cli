# ftx-cli
This is a command line tool you can use to interact with the FTX Exchange.
The CLI has commands to provide quick info on things like funding payments, your positions and your balances. 

Authentication is handled in one of two ways. Either: 
+ Pass an API Key and Secret each time you run it with the `--apikey --apisecret` flags 
+ Set your API Key and Secret as environment variables:
  ```
    export FTX_KEY=<yourkey>
    export FTX_SECRET=<yoursecret>
  ```

## Install and Use 
Install this from pypi : 
`coming soon`

Install from source :
`pip install -e .`

If you need the dependencies : 
`pip install -r requirements.txt`

## What can you do with it 
The best way to figure out what you can do is to pass the help flag to any of the commands :
```
$ ftx-cli funding -h

usage: 
    $ ftx-cli funding --start --end
    $ ftx-cli funding --today  
    $ ftx-cli funding --api_key --api_secret

Tools related to funding for FTX accounts or subaccounts

optional arguments:
  -h, --help            show this help message and exit
  -ak APIKEY, --apikey APIKEY
                        The API Key for the Account or Subaccount to use
                        (Defaults to Environment variables)
  -as APISECRET, --apisecret APISECRET
                        The API Secret for the Account or Subaccount to
                        use(Defaults to Environment variables)
  -t, --today           (Optional) Whether or not to only query for today
  -p, --pretty          (Optional) Whether or not to do pretty-printing
```


Here are a couple of example commands. 
| Command | Description |
| --- | --- | 
| `$ ftx-cli positions --reduce` | "Show the value of all your open positions" |
| `$ ftx-cli positions` | "Print all open positions" |
| `$ ftx-cli fundings --reduce` | "Show how much the account has paid in funding" |
| `$ ftx-cli markets --market ETH-PERP` | "Show the ETH-PERP market" |
| `$ ftx-cli markets` | "Print all the markets" |

#### Need a FTX Referral ? 
Here you go : 
https://ftx.com/#a=17189691

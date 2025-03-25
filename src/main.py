# File: /new-python-project/new-python-project/src/main.py
import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio
from src.model.orbiter.instance import Orbiter
from src.utils.config import Config
from primp import AsyncClient

async def main():
    # Configuration and parameters
    account_index = 1
    proxy = ":@127.0.0.1:7890"  # Replace with your proxy
    private_key = ""  # Replace with your private key
# Replace these with actual values required by the Config class
    config = Config(
        SETTINGS="value1",
        EXCHANGES="value2",
        FAUCET="value3",
        FLOW="value4",
        APRIORI="value5",
        MAGMA="value6",
        KINTSU="value7",
        GASZIP="value8",
        SHMONAD="value9",
        ORBITER="value10",
        OCTO_SWAP="value11",
        DISPERSE="value12",
        LILCHOGSTARS="value13",
        MONADKING="value14",
        FRONT_RUNNER="value15",
        MAGICEDEN="value16",
        MEMEBRIDGE="value17",
        CRUSTY_SWAP="value18",
        TESTNET_BRIDGE="value19",
        DUSTED="value20",
        NOSTRA="value21",
        MONAIYAKUZA="value22",
        NARWHAL_FINANCE="value23",
        FLAPSH="value24"
    )
    session = AsyncClient()  # Create an AsyncClient session

    # Create an instance of the Orbiter class
    orbiter = Orbiter(account_index, proxy, private_key, config, session)

    # Call the bridge method to initiate the bridging process
    success = await orbiter.bridge()
    if success:
        print("Bridging process completed successfully.")
    else:
        print("Bridging process failed.")

if __name__ == "__main__":
    asyncio.run(main())
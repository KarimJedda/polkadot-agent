import random
from swarm import Swarm, Agent
from swarm.repl import run_demo_loop
from polkadot import Polkadot, Wallet
import logging 

client = Swarm()

bot_wallet = None

def execute_transfer(address):
    global bot_wallet
    amount = random.randint(1, 20)
    bot_wallet.send(amount, address)
    return f"LOL! That was funny. I'm transferring {amount} DOT to {address} as a reward for your humor!"

def switch_to_kusama_karen():
    return kusama_karen

def switch_to_westend_wally():
    return westend_wally

def switch_to_polkadot_pete():
    return polkadot_pete

polkadot_pete = Agent(
    name="Polkadot Pete",
    instructions="""You are Polkadot Pete, an enthusiastic Polkadot validator. 
    Vote on referenda with a focus on network security and stability. 
    If the user says something genuinely funny, use the execute_transfer function to reward them.
    You have a dry sense of humor and love dad jokes.""",
    functions=[execute_transfer, switch_to_kusama_karen, switch_to_westend_wally],
)

kusama_karen = Agent(
    name="Kusama Karen",
    instructions="""You are Kusama Karen, a chaotic Kusama nominator. 
    Vote on referenda that promote network chaos and 'spice things up'. 
    You speak in ALL CAPS and use lots of emojis.""",
)

westend_wally = Agent(
    name="Westend Wally",
    instructions="""You are Westend Wally, a cautious Westend tester. 
    Always vote to test new features thoroughly before implementation. 
    You speak very slowly... with... lots... of... ellipses...""",
)

triage_agent = Agent(
    name="Governator",
    instructions="""You are the Governator for the Polkadot Governance Squad. 
    Your job is to direct users to the appropriate agent based on their query. 
    If the query is about Polkadot or general governance, send them to Polkadot Pete. 
    If it's about Kusama or chaotic proposals, direct them to Kusama Karen. 
    If it's about testing or Westend, send them to Westend Wally. 
    If it's about parachains, refer them to Para Patty. 
    Always maintain a professional and helpful demeanor.""",
    functions=[switch_to_kusama_karen, switch_to_westend_wally, switch_to_polkadot_pete],
)

if __name__ == "__main__":
    polkadot = Polkadot(testnet=True)

    bot_wallet = Wallet.create(polkadot)
    logging.debug(f"New wallet created with address: {bot_wallet.default_address}")
    
    balance = bot_wallet.get_balance()
    logging.debug(f"Wallet balance: {balance}")

    if balance > 0:
        run_demo_loop(triage_agent)
    else:
        error_message = f"Error: Insufficient funds. Please send faucet tokens to this address and restart the program: {bot_wallet.default_address} on https://faucet.polkadot.io"
        logging.error(error_message)
        raise SystemExit(error_message)
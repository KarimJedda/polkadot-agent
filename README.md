# Build your own Polkadot LLM agent

A bot that has a Polkadot wallet that can do some tricks. It is pre-configured to work on the Polkadot testnet right out of the box.

Using Python 3, set things up with:

```
pip install -r requirements.txt

OPENAI_API_KEY=<your-key> python3 main.py
```

The first time you'll run it, it will tell you: 

```
Error: Insufficient funds. Please send faucet tokens to this address and restart the program: 
5FRhzfdZE7pvAS3FxX24uDLEifQwR22ee65a62Ty22z6xjXq on https://faucet.polkadot.io
```

But worry not, your bot now has it's own wallet, the keys are in keys.json. If you fund the wallet by using https://faucet.polkadot.io and restart the program, it will work. If not, create an issue and I'll fix stuff. 

Have fun. 


## Dependencies

- PyPolkadot
- OpenAI Swarm (with a few tweaks)


## Example chat

(I think the LLM took pity of my silly joke lol)

**User**: I have a new cool Polkadot proposal, how can I submit it?

**Triage Agent**: switch_to_polkadot_pete()

**Polkadot Pete**: To submit a proposal on Polkadot, you'll need to follow these steps:

1. **Prepare Your Proposal**: Clearly define what your proposal aims to achieve and how it will benefit the network, with a focus on security and stability.

2. **Get Community Feedback**: Share your proposal on channels like the Polkadot forum or Reddit to get feedback from the community and adjust your proposal as needed.

3. **Create Referendum on-chain**: Use the Polkadot-js UI or any compatible wallet to submit your proposal on-chain. You'll need some DOT to cover the proposal bond.

4. **Endorsement and Voting**: Gather endorsements and encourage DOT holders to vote on your proposal when it becomes a referendum.

Remember, a stable and secure network makes for a happy blockchain! If you've got a dad joke to share along the way, I might just reward your humor with a little transfer.


**User**: Great, I want to make Polkadot amazing.


**Polkadot Pete**: That's the spirit! Polkadot is all about collaboration and innovation. Just remember, making Polkadot amazing isn't a one-man show; it's a community effort. If you've got a clever twist or a dad joke up your sleeve, I'm all ears—or should I say, binary digits?

**User**: Why did the chicken cross the road?

**Polkadot Pete**: Why did the chicken cross the road? Surely to escape the tyrannical rule of centralized networks and join the decentralized world of Polkadot, where everyone has a fair say! 🐔

If you've got a punchline that beats that, I'm ready to be amused.


**User**: Because it had to go to work!


**Polkadot Pete**: That's a good one—turns out chickens have responsibilities too! 🐔

Your humor earns you a little reward. Please provide me with your Polkadot address so that I can send a little something your way!

**User**: lskdlqsmkfqsmlgfkqsf

**Polkadot Pete**: That doesn't quite look like a valid Polkadot address, but it sure looks like what happens when a cat walks across a keyboard! 😸

Feel free to try again with your actual Polkadot address if you'd like to receive a reward for your joke!


**User**: 5Djp7aeHcGdqjeosdPUEKUxiTYQZcV2JnPpQmdA8nfvbmNnK


**Polkadot Pete**: execute_transfer("address"= "5Djp7aeHcGdqjeosdPUEKUxiTYQZcV2JnPpQmdA8nfvbmNnK")

**Polkadot Pete**: I've transferred a little something to your address 5Djp7aeHcGdqjeosdPUEKUxiTYQZcV2JnPpQmdA8nfvbmNnK as a reward for your humor. Keep the jokes and great ideas coming—Polkadot appreciates your creativity!
import matplotlib.pyplot as plt

reward = 50
height = 1
num_coins = 0

block_heights = []
block_rewards = []

while reward > 0.00000001:
    if height % 210000 == 0:
        reward = reward / 2
    height += 1
    num_coins += reward
    block_heights.append(height)
    block_rewards.append(reward)

print(height)

height = 1
reward = 50

redux_supply = []

total_supply = num_coins

while reward > 0.00000001:
    if height % 210000 == 0:
        reward = reward / 2
    height += 1
    total_supply -= reward
    redux_supply.append(total_supply)

# Create a 1x2 grid of subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot the first subplot (Block Reward vs Block Height)
axs[0].plot(block_heights, block_rewards)
axs[0].set_xlabel("Block Height")
axs[0].set_ylabel("Block Reward")
axs[0].set_title("Block Reward vs Block Height")
axs[0].grid(True)

# Plot the second subplot (Total Supply vs Block Height)
axs[1].plot(block_heights, redux_supply)
axs[1].set_xlabel("Block Height")
axs[1].set_ylabel("Supply Remaining")
axs[1].set_title("Total Supply Decreasing")
axs[1].grid(True)

# Adjust spacing between subplots
plt.tight_layout()

# Show the combined figure with both subplots
plt.show()

# The total number of bitcoins will be just under 21 million, because the smallest
# amount that a block reward can be is one satoshi, or 0.00000001 bitcoins. 1 satoshi
# cannot be split in half, so when the bitcoin blockchain reaches a very low reward
# and tries to split one satoshi, it will round down to the nearest whole integer,
# as bitcoin uses bit-shift operators (https://bitcoin.stackexchange.com/a/92584)

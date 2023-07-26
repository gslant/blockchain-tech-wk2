import matplotlib.pyplot as plt

reward = 50
height = 1
num_coins = 0;

block_heights = []
block_rewards = []

while reward > 0.01:
    if(height % 210000 == 0):
        reward = reward / 2
    height += 1
    num_coins += reward
    block_heights.append(height)
    block_rewards.append(reward)

#print(height)
#print(num_coins)

#plt.plot(block_heights, block_rewards)
#plt.xlabel("Block Height")
#plt.ylabel("Block Reward")
#lt.title("Block Reward vs Block Height")
#plt.grid(True)
#plt.show()

height = 1
reward = 50

redux_supply = []
redux_rewards = []

total_supply = num_coins

while reward > 1:
    if(height % 210000 == 0):
        reward = reward / 2
    height += 1
    total_supply -= reward
    redux_supply.append(total_supply)
    redux_rewards.append(reward)

redux_supply = redux_supply[::-1]
redux_rewards = redux_rewards[::-1]

print(f"start of rew {redux_rewards[0]}")
print(f"start of sup  {redux_supply[0]}")
print(f"end of rew  {redux_rewards[len(redux_rewards) -1]}")
print(f"end of sup  {redux_supply[len(redux_supply) -1]}")

line = plt.plot(redux_supply, redux_rewards)
plt.gca().invert_xaxis()
plt.xlabel("Total Supply")
plt.ylabel("Block Reward")
plt.title("total supply decreasing")
plt.grid(True)
plt.show()




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

while reward > 0.01:
    if(height % 210000 == 0):
        reward = reward / 2
    height += 1
    total_supply -= reward
    redux_supply.append(total_supply)
    redux_rewards.append(reward)

#redux_supply = redux_supply[::-1]
#redux_rewards = redux_rewards[::-1]

line = plt.plot(block_heights, redux_supply)
#plt.gca().invert_xaxis()
plt.xlabel("Block height")
plt.ylabel("Supply remaining")
plt.title("total supply decreasing")
plt.grid(True)
plt.show()




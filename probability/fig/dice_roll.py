import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from random import randint  # random integer
rc('font', **{'family': 'serif', 'serif': ['Computer Modern Roman']})
rc('text', usetex=True)

n_rolls = 40  # number of dice rolls
roll_number = np.arange(1, n_rolls + 1)
roll_history = np.zeros(n_rolls)  # each roll result recorded in time
average = np.zeros(n_rolls)  # initialize the average, updated after each dice roll

for roll in roll_number:
    roll_outcome = randint(1, 6)  # roll a fair dice, values between 1 and 6, inclusive
    print(f'Dice roll number {roll} outcome is {roll_outcome}.')
    roll_history[roll-1] = int(roll_outcome)
    sum_after_roll = sum(i for i in roll_history)
    average[roll-1] = sum_after_roll / roll

fig = plt.figure(figsize=(8, 4))  # 8 inches wide, 4 inches tall

ax = fig.add_subplot(1, 1, 1)
ax.plot(roll_number, roll_history, 's', color='blue', label='roll outcome')
ax.plot(roll_number, average, color='red', marker='o', alpha=0.5, label='roll average')
ax.grid()
ax.set_xlabel('roll number')
ax.set_ylabel('roll outcome and cumulative simple average')
ax.set_ylim(0, 7)
ax.legend(loc='upper right')
plt.show()
figure_name = 'dice_roll'
fig.savefig(figure_name + '.pdf', bbox_inches='tight')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Person:
    def __init__(self, name, initial_freq, initial_quality, initial_understanding, rate_freq, rate_quality, rate_understanding):
        self.name = name
        self.initial_freq = initial_freq
        self.initial_quality = initial_quality
        self.initial_understanding = initial_understanding
        self.rate_freq = rate_freq
        self.rate_quality = rate_quality
        self.rate_understanding = rate_understanding

    def simulate(self, time_periods):
        time = np.arange(time_periods)
        freq = self.initial_freq * np.exp(-self.rate_freq * time)
        quality = self.initial_quality + self.rate_quality * time
        understanding = self.initial_understanding + self.rate_understanding * time

        return pd.DataFrame({'Time': time, 'Frequency of Questions': freq, 'Quality of Questions': quality, 'Level of Understanding': understanding})

    def plot_simulation(self, df, ax):
        color = 'tab:red'
        ax.plot(df['Time'], np.log10(df['Frequency of Questions']), color=color)
        ax.tick_params(axis='y', labelcolor=color)

        ax2 = ax.twinx()
        color = 'tab:blue'
        ax2.plot(df['Time'], np.log10(df['Quality of Questions']), color=color, linestyle='dashed')
        ax2.plot(df['Time'], np.log10(df['Level of Understanding']), color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        ax.set_title(self.name)
        ax.set_xlabel('Time')
        ax.set_ylabel('Log10 of Frequency of Questions')
        ax2.set_ylabel('Log10 of Quality of Questions and Level of Understanding')


person1 = Person('Person 1', 10, 1, 0, 0.05, 0.1, -0.15)
df1 = person1.simulate(100)

person2 = Person('Person 2', 20, 2, 0, 0.02, 0.15, -0.1)
df2 = person2.simulate(100)

person3 = Person('Person 3', 15, 3, 0, 0.03, 0.2, -0.05)
df3 = person3.simulate(100)

# Create a figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Plot the simulations for Person 1
person1.plot_simulation(df1, ax1)

# Plot the simulations for Person 2
person2.plot_simulation(df2, ax2)

# Plot the simulations for Person 3
person3.plot_simulation(df3, ax3)

# Add a common y-axis label
fig.text(0.04, 0.5, 'Log10 of Quality of Questions and Level of Understanding', va='center', rotation='vertical')

# Adjust spacing between subplots
plt.subplots_adjust(wspace=0.3)

# Save the figure as a PNG file
plt.savefig('/Users/kilian.lehn/Documents/GitHub/questioning_the_question/combined_plot.png')
plt.show()

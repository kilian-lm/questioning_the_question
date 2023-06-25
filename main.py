import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Person:
    def __init__(self, name, f0, u0, rf, ru, rq):
        self.name = name
        self.f0 = f0
        self.u0 = u0
        self.rf = rf
        self.ru = ru
        self.rq = rq

    def simulate(self, T, dt):
        times = np.arange(0, T, dt)
        freq = np.zeros_like(times)
        qual = np.zeros_like(times)
        understand = np.zeros_like(times)

        freq[0] = self.f0
        understand[0] = self.u0
        qual[0] = self.u0

        for i in range(1, len(times)):
            df = -self.rf * understand[i-1] * freq[i-1] * dt
            du = self.ru * qual[i-1] * freq[i-1] * dt
            dq = self.rq * qual[i-1] * dt

            freq[i] = freq[i-1] + df
            understand[i] = understand[i-1] + du
            qual[i] = qual[i-1] + dq

        data = {
            'Time': times,
            'Frequency of Questions': freq,
            'Quality of Questions': qual,
            'Level of Understanding': understand
        }

        df = pd.DataFrame(data)
        return df

    def plot_simulation(self, df):
        fig, ax1 = plt.subplots()

        color = 'tab:red'
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Log10 of Frequency of Questions', color=color)
        ax1.plot(df['Time'], np.log10(df['Frequency of Questions']), color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()
        color = 'tab:blue'
        ax2.set_ylabel('Log10 of Quality of Questions and Level of Understanding', color=color)
        ax2.plot(df['Time'], np.log10(df['Quality of Questions']), color=color, linestyle='dashed')
        ax2.plot(df['Time'], np.log10(df['Level of Understanding']), color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()
        plt.title(self.name)
        plt.show()




# Initialize persons
# person1 = Person("Person 1", initial_frequency=100, decay_rate=0.05, initial_understanding=1, understanding_rate=0.1, initial_quality=1, increase_rate=0.2)
# person2 = Person("Person 2", initial_frequency=80, decay_rate=0.04, initial_understanding=1, understanding_rate=0.08, initial_quality=1, increase_rate=0.15)
# person3 = Person("Person 3", initial_frequency=60, decay_rate=0.03, initial_understanding=1, understanding_rate=0.05, initial_quality=1, increase_rate=0.1)

# Simulate for each person
df1 = person1.simulate(100)
df2 = person2.simulate(100)
df3 = person3.simulate(100)

person1.plot_simulation(df1)
person2.plot_simulation(df2)
person3.plot_simulation(df3)

person3.plot()
plt.savefig("/Users/kilian.lehn/Documents/GitHub/questioning_the_question/person3_plot.png")
plt.show()

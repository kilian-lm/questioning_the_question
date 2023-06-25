import matplotlib.pyplot as plt
import numpy as np

class Person:
    def __init__(self, name, initial_freq, initial_understanding, rate_freq, rate_understanding):
        self.name = name
        self.initial_freq = initial_freq
        self.initial_understanding = initial_understanding
        self.rate_freq = rate_freq
        self.rate_understanding = rate_understanding
        self.freq = []
        self.understanding = []

    def simulate(self, time_periods):
        for t in range(time_periods):
            self.freq.append(self.initial_freq * np.exp(-self.rate_freq * t))
            self.understanding.append(self.initial_understanding + self.rate_understanding * t)

    def plot(self):
        fig, (ax1, ax2) = plt.subplots(2)
        ax1.plot(self.freq, label=self.name)
        ax1.set_title('Question Frequency')
        ax2.plot(self.understanding, label=self.name)
        ax2.set_title('Understanding')
        plt.legend()

time_periods = 100
person1 = Person('Person 1', 10, 0, 0.05, 0.1)
person1.simulate(time_periods)

person2 = Person('Person 2', 20, 0, 0.02, 0.15)
person2.simulate(time_periods)

person3 = Person('Person 3', 15, 0, 0.03, 0.2)
person3.simulate(time_periods)

person1.plot()
person2.plot()
person3.plot()

plt.show()

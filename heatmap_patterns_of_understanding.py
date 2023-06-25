import imageio
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import reuters
from collections import Counter
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import cm


import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import nltk

nltk.download('reuters')

# Get the 100 most common words
word_counts = Counter(reuters.words())
common_words = word_counts.most_common(100)

# Create a TF-IDF vectorizer and fit the corpus
vectorizer = TfidfVectorizer(vocabulary=[word for word, _ in common_words])
X = vectorizer.fit_transform(reuters.raw().split('\n'))
X
# Reduce the dimensionality of the TF-IDF matrix to 2D using t-SNE
X_2d = TSNE(n_components=2).fit_transform(X.toarray().T)

# Get the frequencies of the common words
frequencies = np.array([count for _, count in common_words])

# Normalize the frequencies for better visualization
frequencies = (frequencies - frequencies.min()) / (frequencies.max() - frequencies.min())

import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import reuters
from collections import Counter
from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import nltk

nltk.download('reuters')

# Get the 100 most common words
word_counts = Counter(reuters.words())
common_words = word_counts.most_common(100)

# Create a TF-IDF vectorizer and fit the corpus
vectorizer = TfidfVectorizer(vocabulary=[word for word, _ in common_words])
X = vectorizer.fit_transform(reuters.raw().split('\n'))
X
# Reduce the dimensionality of the TF-IDF matrix to 2D using t-SNE
X_2d = TSNE(n_components=2).fit_transform(X.toarray().T)

# Get the frequencies of the common words
frequencies = np.array([count for _, count in common_words])



# todo v2



words = np.array([word for word, _ in common_words])

# Normalize the frequencies for better visualization
frequencies = (frequencies - frequencies.min()) / (frequencies.max() - frequencies.min())

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')

# Define the fixed heatpoints and their respective labels
heatpoints = {
    'python': [1.0, 0.8, 0.9],
    'dimensions': [0.8, 0.7, 0.6],
    'graph': [0.7, 0.6, 0.9],
    'girls from sweden': [0.9, 1.0, 0.8]
}


# Define a function for drawing a frame
def draw_frame(rotation):
    ax.clear()
    ax.plot_trisurf(X_2d[:, 0], X_2d[:, 1], frequencies, cmap=cm.coolwarm)
    ax.set_title('Young Man\'s Perception Universe')
    ax.view_init(30, rotation)

    # Add labels for representative words
    for i in range(len(words)):
        ax.text(X_2d[i, 0], X_2d[i, 1], frequencies[i], words[i], fontsize=8)

    # Plot fixed heatpoints
    for word, coords in heatpoints.items():
        ax.scatter(coords[0], coords[1], coords[2], s=50, c='red', label=word)
        ax.text(coords[0], coords[1], coords[2], word, fontsize=8, ha='center', va='center')

    # Draw brain regions
    brain_regions = ['Frontal Lobe', 'Temporal Lobe', 'Parietal Lobe', 'Occipital Lobe']
    region_coords = [(-20, 20), (20, 20), (-20, -20), (20, -20)]

    for region, (x, y) in zip(brain_regions, region_coords):
        ax.text(x, y, 1, region, ha='center', va='center', fontsize=10, fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))

    # Convert the plot to an image array (it won't be displayed)
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return image


# Generate a list of images
images = [draw_frame(rotation) for rotation in range(0, 360, 2)]


# Call the draw_frame function to create the 3D plot
draw_frame(30)  # You can change 30 to any value of your choice
# Save the figure
plt.savefig("/Users/kilian.lehn/Documents/GitHub/questioning_the_question/3d_plot.png")
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import glob

rho = 28.0
sigma = 10.0
beta = 8.0/3.0

initial_states = [
    [1.0, 1.0, 1.0],
    # [-8.3, 2.0, -0.5],
]

colors = ['r', 'g',]

steps = 100
time_steps = np.arange(0.0, 40.0, 0.01)
time_chunks = np.array_split(time_steps, steps)

def update(state, t):
    x, y, z = state 
    return sigma*(y - x), x*(rho - z) - y, x*y - beta*z  

fig = plt.figure(figsize=(20, 20))
ax = fig.gca(projection="3d")
plt.xlim(-30, 30)
plt.ylim(-30, 30)

for n, time_steps in enumerate(time_chunks):
    for i in range(len(initial_states)):
        states = odeint(update, initial_states[i], time_steps)
        initial_states[i] = states[-1]
        ax.plot(states[:, 0], states[:, 1], states[:, 2], color=colors[i], alpha=0.6, linewidth=0.7)
    plt.draw()
    plt.pause(1e-1)
    plt.savefig('./images/{:03d}.png'.format(n), dpi=60, bbox_inches='tight', pad_inches=0.1)

plt.show()

# save as gif
images = [Image.open(image) for image in glob.glob('./images/*.png')]
gif_filepath = 'images/lorenz_attractor.gif'
gif = images[0]
gif.info['duration'] = 100
gif.info['loop'] = 0
gif.save(fp=gif_filepath, format='gif', save_all=True, append_images=images[1:])






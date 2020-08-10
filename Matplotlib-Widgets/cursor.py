import matplotlib.pyplot as plt 
from matplotlib.widgets import Cursor, Button;
from numpy import random

x, y = random.rand(2, 100)

fig, ax = plt.subplots()
p, = plt.plot(x, y, 'o')

cursor = Cursor(ax, horizOn = True, vertOn = True, color = 'green', linewidth = 2.0)

def onclick(event):
    x1, y1 = event.xdata, event.ydata
    print(x1, y1)

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show();

########################################################

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as wdg  # Using the ipython notebook widgets

# Create a random image
a = np.random.poisson(size=(12,15))
fig = plt.figure()
plt.imshow(a)

# Create and display textarea widget
txt = wdg.Textarea(
    value='',
    placeholder='',
    description='event:',
    disabled=False
)
display(txt)

# Define a callback function that will update the textarea
def onclick(event):
    txt.value = str(event)  # Dynamically update the text box above
    print("hjhj")

# Create an hard reference to the callback not to be cleared by the garbage collector
ka = fig.canvas.mpl_connect('button_press_event', onclick)

#####################################################


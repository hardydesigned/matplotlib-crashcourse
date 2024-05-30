import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0,2,4,6,8]

# Resize your Graph (dpi specifies pixels per inch. When saving probably should use 300 if possible)
plt.figure(figsize=(8,5), dpi=100)

# Line 1

# Keyword Argument Notation
#plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')

# Shorthand notation
# fmt = '[color][marker][line]'
plt.plot(x,y, 'b^--', label='2x')

## Line 2

# select interval we want to plot points at
x2 = np.arange(0,4.5,0.5) # start at 0 count up by 0.5 to 4.5 but not include 4.5
#print(x2) # [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4. ]

# Plot part of the graph as line
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2') # from beginning to 5th index

# Plot remainder of graph as a dot
plt.plot(x2[5:], x2[5:]**2, 'r--') # from 5th index to end

# Add a title (specify font parameters with fontdict)
plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# X and Y labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# X, Y axis Tickmarks (scale of your graph)
plt.xticks([0,1,2,3,4,])
#plt.yticks([0,2,4,6,8,10])

# Add a legend
plt.legend()

# Save figure (dpi 300 is good when saving so graph has high resolution)
plt.savefig('mygraph.png', dpi=300)

# Show plot
plt.show()

# In a normal python script you would run plt.show() to display the graph. However, in a Jupyter Notebook, you can just put the variable name of the plot at the end of a cell and it will display the plot.
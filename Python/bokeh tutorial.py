# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from bokeh.plotting import figure, output_file, show

# <codecell>

x = [1,2,3,4,5]
y = [6,7,2,4,5]

# <codecell>

output_file("lines.html", title="line plot of example")

# <codecell>

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# <codecell>

p.line(x,y,legend="Templ.",line_width=2)

# <codecell>

show(p)

# <codecell>

import numpy as np

# <codecell>

N=5000
x=np.random.random(size=N)*100
y=np.random.random(size=N)*100
radii=np.random.random(size=N)*1.5
colors = ["#%02x%02x%02x" % (r,g,150) for r,g in zip(np.floor(50+2*x), np.floor(30+2*y))]

# <codecell>

output_file("color_scatter.html",title="color_scatter.py example", mode="cdn")

# <codecell>

TOOLS = "resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

# <codecell>

p = figure(tools=TOOLS, x_range=(0,100), y_range=(0,100))

# <codecell>

p.circle(x,y,radius=radii,fill_color=colors,fill_alpha=0.6,line_color=None)

# <codecell>

show(p)

# <codecell>



import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure ,show
x=np.linspace(0,10,100)
y=np.sin(x)
TOOLS="pan,wheel_zoom,box_zoom,reset,save,box_select"
p1=figure(title="varsha s-1KI23CS176",tools=TOOLS)
p1.line(x,y,line_width=2,legend_label="sin(x)",color="red")
p1.line(x,2*y,line_width=2,legend_label="2sin(x)",color="green")
p1.line(x,3*y,line_width=2,legend_label="3sin(x)",color="blue")
p1.legend.title="Markers"
show(gridplot([p1],ncols=1,width=400,height=400))

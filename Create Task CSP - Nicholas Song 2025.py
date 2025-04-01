from flask import Flask as fl, render_template as rt, url_for
from matplotlib import pyplot as plot 
from matplotlib.figure import Figure 
import numpy as np 
import os 
from io import BytesIO 
import base64 

#set up initial variables 
finances = []
app = fl(__name__)

@app.route('/')
def test(): 
    cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']
    data = [23, 17, 35, 29, 12, 41]
    fig = plot.figure(figsize=(10, 7))
    ax = fig.subplots() 
    ax.pie(data, labels = cars)
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8001)


'''#import numpy as np

# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']

data = [23, 17, 35, 29, 12, 41]

# Creating plot
fig = plot.figure(figsize=(10, 7))
plot.pie(data, labels=cars)

# show plot
plot.show()'''
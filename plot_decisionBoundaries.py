#Plot_decisionBoundaries.py

import numpy as np
import matplotlib.pyplot as plt

def decisionBoundaries (x,y,model,offset,resolution,size,names = None,ax=None):
  """
    Create the map of decisions predicted by the model and the real values

    x -- Input features
    y -- True labels
    model -- The machine learning model for which you want to plot decision boundaries
    offset -- The offset to be added to the minimum and maximum values of the input features for setting the plot boundaries
    resolution --  The number of points used to create the grid for decision boundaries
    size -- The size of the plot
    names -- A list containing the names of the input features for labeling the axes
  """

  h_min, h_max = x[:,0].min() - offset, x[:, 0].max() + offset
  v_min, v_max = x[:,1].min() - offset, x[:, 1].max() + offset
  h_grid,v_grid = np.meshgrid(np.linspace(h_min, h_max, resolution),np.linspace(v_min, v_max, resolution))

  pred_grid = model.predict(np.c_[h_grid.reshape(-1),v_grid.reshape(-1)])
  pred_grid = pred_grid.reshape(h_grid.shape)


  if ax is None:  _, ax = plt.subplots(figsize = (6,5))
    
  ax.pcolormesh(h_grid, v_grid, pred_grid, cmap = 'tab20')
  ax.scatter(x[:, 0], x[:, 1], c = y, edgecolors='k', cmap = 'tab20')

  if names != None:
    ax.set_xlabel(names[0])
    ax.set_ylabel(names[1])

  return ax

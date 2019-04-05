import numpy as np
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import time as ti
import pandas as pd


def surface_plot(X0, Y0, Z0, X1, Y1, Z1):
    X0 = np.ravel(X0)
    Y0 = np.ravel(Y0)
    Z0 = np.ravel(Z0)
    X1 = np.ravel(X1)
    Y1 = np.ravel(Y1)
    Z1 = np.ravel(Z1)
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(1, 2, 1, projection='3d', adjustable='box')
    ax.view_init(30, 180)
    #ax.scatter(X0, Y0, Z0, c='b', marker='^')
    ax.plot_trisurf(X0, Y0, Z0, linewidth=0.5, antialiased=True)
    ax.set_title("Original slope", fontweight='bold', fontsize=16, fontname='Arial', y=-0.05)
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.view_init(30, 180)
    ax.plot_trisurf(X1, Y1, Z1, linewidth=0.5, antialiased=True)
    ax.set_title("Selected slope", fontweight='bold', fontsize=16, fontname='Arial', y=-0.05)
    plt.tight_layout()
    date = ti.strftime("%d_%m_%Y_%H_%M_%S")
    #plt.savefig('Slope_'+date+'.png', bbox_inches='tight')
    plt.savefig('static/slope.png', bbox_inches='tight')
    plt.close(fig)
    #plt.show()


def smoothness(Y):
    # Gradient gives 1 if change is smooth.
    # Average gradient creates an index where 1 is the most smooth,
    # >1 bumpy, <1 holey, <0 slope inverted
    smoothIndex = []
    for i in range(Y.shape[1]):
        smooth = np.average(np.gradient(Y[:,i]))
        smoothIndex.append(smooth)
    smo=abs(np.average(smoothIndex))
    # print("Smoothness index: ",smo)
    return smo


def slopecalc(x, y, sensorpos):
    # Sensor position correction, sensor pos describes an offset coordinate
    y = sensorpos[1]-y
    x1 = np.average(x[0,:])
    x2 = np.average(x[x.shape[0]-1,:])
    y1 = np.average(y[0,:])
    y2 = np.average(y[y.shape[0]-1,:])
    slope = (x2-x1)/(y2-y1)
    slope = 100*(np.degrees(np.arctan(slope))/45)
    #print("Slope: ", slope,"%")
    return slope


def skiPathComp(depth, ideal):

    # Reconstruct perfect slope from first row
    ideal = ideal.T
    xn = np.tile(np.array(ideal[:,0]), (np.shape(ideal)[1],1))
    # Substract matrixes
    intersection_matrix = xn - depth
    intersection_matrix = np.rot90(intersection_matrix,1)
    np.flipud(intersection_matrix)
    #Update image for front end
    c_map = cm.get_cmap('Greys',10)
    fig, ax = plt.subplots()
    psm = ax.pcolormesh(intersection_matrix, cmap=c_map, vmin=-1.5, vmax=1.5)
    fig.colorbar(psm, ax=ax, label="Surface Disturbance (m)")
    ax.set_aspect(aspect='auto', adjustable='box')
    ax.axis('off')
    plt.savefig("static/track.png")
    plt.close(fig)


if __name__ == '__main__':
    # Please provide surface data on 3 numpy arrays x, y and z
    x = np.array([[1, 1, 1, 2, 3], [4, 4, 4, 4, 1]])
    y = np.array([[1, 2, 3, 3, 3], [3, 4, 5, 6, 1]])
    z = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    Y = np.array([[1, 1, 1, 2, 3, 4, 4, 4, 4, 1], [1, 2, 3, 3, 3, 3, 4, 5, 6, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    # Define sensor position to set reference frame on pole base (ground level)
    # [X,Y,Z]
    sensorpos = np.array([0, 3, 0])
    #x=np.reshape(x,())
    smo = smoothness(Y)
    surface_plot(x,y,z,x,y,z)
    # Calculate slope and smoothnes index from data provided
    slope = slopecalc(x, y, sensorpos)

    # NOTES:
# If the slope have steps or is uneven, please select each one and repeat the calculation process (lines 67, 70)

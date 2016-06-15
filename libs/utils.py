import numpy as np
import matplotlib.pyplot as plt
import sys

## Plot results
#  It plots the results in a unique figure
def plot_res(t,x,y,u,sp):
    plt.subplot(3,1,1)
    plt.plot(t.T,x.T)
    plt.xlabel('Time')
    plt.ylabel('States x')

    plt.subplot(3,1,2)
    plt.plot(t.T,y.T)
    plt.plot(t.T,sp.T,'k:')
    plt.xlabel('Time')
    plt.ylabel('Outputs y')
    
    plt.subplot(3,1,3)
    plt.plot(t.T,u.T)
    plt.xlabel('Time')
    plt.ylabel('Control u')
    umin = np.min(u)
    umax = np.max(u)
    axes = plt.gca()
    axes.set_ylim([umin*1.2,umax*1.2])

    plt.show()

## Plot results
#  It plots the results in a unique figure
def plot_res_out(t,x,y,u,sp):
    for i in range(0,len(y)):
        plt.subplot(len(y)+1,1,i+1)
        plt.plot(t.T,y[i,:])
        plt.plot(t.T,sp[i,:],'k:')
        plt.xlabel('Time')
        plt.ylabel('Outputs y')
    
    plt.subplot(len(y)+1,1,len(y)+1)
    plt.plot(t.T,u.T)
    plt.xlabel('Time')
    plt.ylabel('Control u')
    umin = np.min(u)
    umax = np.max(u)
    axes = plt.gca()
    axes.set_ylim([umin*1.2,umax*1.2])

    plt.show()

def plot_accuracy(t,acc):
    plt.figure()
    plt.plot(t.T,acc.T)
    plt.xlabel('Time')
    plt.ylabel('Accuracy')
    plt.show()

def progress(val,end_val, bar_length=50):
    percent = float(val) / end_val
    hashes = '#' * int(round(percent * bar_length))
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\rProgress: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()
    

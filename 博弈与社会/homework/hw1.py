# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:06:45 2019

@author: DrLC
"""

import matplotlib.pyplot as plt
import numpy

if __name__ == "__main__":
    
    c = 1
    x = numpy.asarray([0.05*i for i in range(1, 101)])
    y1 = numpy.sqrt(c)*x
    y2 = 1/x
    
    plt.plot(x, y1, ":", label="x=Rx(y)")
    plt.plot(x, y2, "-", label="y=Ry(x)")
    plt.legend(loc="upper right")
    plt.xlim([-0.5, 5.5])
    plt.ylim([-0.5, 5.5])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    
    cs = numpy.asarray([0.05*i for i in range(1, 101)])
    xs = numpy.power(cs, -1/4)
    ys = numpy.power(cs, 1/4)
    
    plt.plot(xs, ys, "-")
    plt.text(xs[0], ys[0], "c="+str(cs[0]))
    plt.text(xs[-1], ys[-1], "c="+str(cs[-1]))
    plt.xlim([0.5, 2.5])
    plt.ylim([0, 2])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:34:03 2018

@author: jojos
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import optimize, stats

# number 2 part with AC

def Comparisonatresistance680kAC():
    voltage_IN=np.array([0.1,0.08,0.07,0.05,0.03,0.01])
    voltage_OUT=np.array([17.9,14.5,12.2,8.88,5.28,1.8])
    x=np.array(np.linspace(0,0.12,100))
    y=x*(680000/3000)
    (gradient, offset, r_value, p_value, stderr) =stats.linregress(voltage_IN,voltage_OUT)
    Regression,=plt.plot (x,gradient*x+offset, label='Regression')
    plt.plot(voltage_IN,voltage_OUT,linestyle='')
    plt.errorbar(voltage_IN,voltage_OUT,yerr=voltage_OUT*0.05,xerr=voltage_IN*0.05,fmt='.')
    plt.xlabel("Eingangsspannung [V]")
    plt.ylabel("Ausgangsspannung [V]")
    plt.title ("Diagramm 2: Vergleich Eingangs- und Ausgangspannung bei Wechselspannung und 680kΩ")
    Berechnet,=plt.plot(x,y,label='berechnet')
    plt.legend(handles=[Regression,Berechnet])
    print('Steigung ' + str(gradient) + '±' + str(stderr) )
    print(680000/3000)
    plt.show
Comparisonatresistance680kAC()

import numpy as np
import sys
from matplotlib import pyplot as plt

def analyze(filename):
    data = np.loadtxt(fname=filename, delimiter=',')
    
    plt.figure(figsize=(10.0, 3.0))
    
    plt.subplot(1, 3, 1)
    plt.ylabel('average')
    plt.plot(data.mean(0))
    
    plt.subplot(1, 3, 2)
    plt.ylabel('max')
    plt.plot(data.max(0))
    
    plt.subplot(1, 3, 3)
    plt.ylabel('min')
    plt.plot(data.min(0))
    
    plt.tight_layout()
    plt.show()

# script = sys.argv[0] #this tells the program to read in arguments from the command line when this script is run, the 1st argument (index = 0) is the script name
#inputfile = sys.argv[1] #2nd argument when calling the script in bash is input file name
#outputfile = sys.argv[2] #3rd argument is the output file name

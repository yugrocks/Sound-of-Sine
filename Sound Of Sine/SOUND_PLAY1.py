from numpy import *
import matplotlib.pyplot as pyplot
import scipy
from scipy.io.wavfile import write

#getting values of x
x=arange(10000)

#making sine curves
sin1=1000*sin(2*pi*(1000/10000)*x)
sin2=1000*sin(2*pi*(650.0/10000.0)*x)

sig=sin1+sin2 #superimposing them
y=x*x #a square function

#function to graphically depict the sound wave
def makegraph(data,filename):
    pyplot.clf()
    pyplot.plot(data)
    pyplot.savefig(filename)
    pyplot.show()

data=fft.rfft(sin1) #taking fourier transform to convert to frequency domain
data=10*log10(abs(data)) #in decibels

#visualize:
makegraph(sin1,r'sin1.png')
makegraph(sin2,r'sin2.png')
makegraph(sig,r'sig.png')
makegraph(y,r'square.png')#visualize square function

def savewav(data,outfile,samplerate):
    out_data=array(data,dtype=int16)
    write(outfile,samplerate,out_data)


savewav(sin1,r"sin1.wav",4000)
savewav(sin2,r"sin2.wav",4000)
savewav(sig,r"sig.wav",4000)
savewav(y,r"square.wav",4000) #noise(sound of the square function)


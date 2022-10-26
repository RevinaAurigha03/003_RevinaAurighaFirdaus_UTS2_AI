#Revina Aurigha Firdaus (21091397003)
#inisialisasi numpy
import numpy as np

#inisialisasi variabel 
input  = [[ 4.1 , 3.1 , 2.2 , 1.9 , 0.3 , 4.0 , 3.5 , 1.9 , 2.2 , 4.6 ],
          [ 1.2 , 4.3 , 1.2 , 2.3 , 4.2 , 1.1 , 3.2 , 7.0 , 5.3 , 2.7 ],
          [ 3.3 , 7.2 , 4.1 , 3.7 , 1.9 , 4.4 , 8.3 , 2.4 , 9.3 , 1.4 ],
          [ 2.0 , 3.4 , 3.2 , 2.2 , 2.7 , 7.7 , 4.2 , 6.4 , 4.6 , 0.1 ],
          [ 8.4 , 2.4 , 1.5 , 4.4 , 5.1 , 1.1 , 2.4 , 6.3 , 5.6 , 1.1 ],
          [ 1.5 , 0.5 , 5.7 , 5.4 , 7.1 , 3.3 , 8.9 , 1.4 , 7.0 , 4.2 ]]

#bobot per neuron lapisan 1
weights1  = [[ 1.3 , 5.1 , 4.2 , 5.1 , 5.0 , 3.8 , 9.0 , 9.0 , 1.1 , 3.4 ],
           [ 4.1 , 0.4 , 0.3 , 1.3 , 4.5 , 4.1 , 3.6 , 3.0 , 4.0 , 1.1 ],
           [ 3.1 , 4.3 , 2.2 , 5.3 , 5.0 , 2.3 , 1.4 , 2.6 , 2.4 , 3.2 ],
           [ 2.1 , 6.2 , 4.4 , 2.4 , 2.3 , 4.5 , 0.9 , 4.0 , 8.0 , 3.4 ],
           [ 2.3 , 5.0 , 1.6 , 3.2 , 5.1 , 0.9 , 7.4 , 3.2 , 3.8 , 4.5 ]]

#bias per lapisan neuron 1
bias1  = [ 1.3 , 4.1 , 2.2 , 2.1 , 1.5 ]

#bobot per neuron lapisan 2
weights2  = [[ 1.3 , 3.5 , 2.1 , 2.3 , 2.3 ,],
            [ 1.2 , 0.3 , 3.2 , 2.3 , 4.2 ],
            [ 3.2 , 1.2 , 2.4 , 2.3 , 9.0 ]]

#bias per lapisan neuron 2
bias2  = [ 2.4 , 3.2 , 1.1 ]

#output 
layer1_output  =  np . dot ( input, np.array ( weights1 ). T ) + bias1
layer2_output  =  np . dot ( layer1_output , np . array ( weights2 ). T ) 

#hasil output
print ( layer2_output )
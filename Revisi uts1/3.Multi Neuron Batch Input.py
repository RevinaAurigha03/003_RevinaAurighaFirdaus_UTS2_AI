#Revina Aurigha Firdaus (21091397003)

#insialisasi numpy
import numpy as np 

#inisialisasi variable
inputs  = [[3.3, 2.3, 7.5, 0.8, 9.4, 1.7], 
           [1.1, 1.2, 3.5, 2.4, 6.3, 6.2],
           [5.2, 3.1, 1.3, 3.5, 7.2, 9.4],
           [1.4, 2.5, 4.5, 8.1, 1.1, 7.1],
           [2.3, 5.3, 1.4, 5.7, 7.3, 8.1],
           [5.3, 2.4, 9.7, 7.6, 2.2, 3.3]]

#inisialisasi variable
weights = [[1.5, 0.7, 1.4, 3.7, 7.8, 9.4],
           [0.5, 1.1, 4.7, 2.4, 3.5, 2.4],
           [0.7, 1.3, 1.4, 1.1, 6.1, 6.4],
           [4.1, 1.3, 2.1, 3.5, 1.1, 4.3],
           [2.7, 1.5, 0.4, 2.6, 3.2, 6.2]]

#inisialisasi bias
bias = [2.2, 2.5, 1.2, 5.3, 0.2]

#melakukan --> dot product, transpose dan penambahan bias
layer_output = np.dot(inputs, np.array(weights).T) + bias

#cetak output
print(layer_output) 
#Revina Aurigha Firdaus (21091397003)

# inisialisasi numpy
import numpy as np

#inisialisasi variable
inputs = [7, 3, 8, 2.3, 6, 2, 5.5, 4, 3, 9]

#inisialisasi variable 
weights = [[-1.4, 3.8, 2.4, 4.5, 0.4, -3.4, 1.6, 8.6, 7.9, 3.3]],
[2.5, 3.4, 6.5, 0.9, -1.3, 6.3, 3.3, 0.7, -1.4, 3.7],
[0.3, -1.7, 8.3, 9.4, 0.3, 0.2, 1.5, 4.8, 8.6, -8.9]
[1.3 , -3.2, 0.3, 2.5, 5.7, -8.2, 4.2, 9.8, 0.4, 6.4]

#inisialisasi bias
bias = [-3.1, 8.1, 2.5, -3.7, 1.1]

#melakukan -> dot product
output = np.dot(weights, inputs) - bias

#cetak output
print(output)
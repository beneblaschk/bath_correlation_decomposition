import matplotlib.pyplot as plt
import numpy as np

# Data
x_values = np.array([-10.00, -9.00, -8.00, -7.00, -6.00, -5.00, -4.00, -3.00, -2.00, -1.00,
                      0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00])
laurent_values = np.array([243.0237, 46.9210, 7.3759, 0.8903, 0.0735, -0.0028, -0.0186, -0.0524,
                            -0.1565, -0.5820, np.nan, 1.5820, 1.1565, 1.0524, 1.0186, 1.0028,
                            0.9265, 0.1097, -6.3759, -45.9210, -242.0237])
reference_values = np.array([0.0000, -0.0001, -0.0003, -0.0009, -0.0025, -0.0068, -0.0187, -0.0524,
                             -0.1565, -0.5820, np.nan, 1.5820, 1.1565, 1.0524, 1.0187, 1.0068,
                             1.0025, 1.0009, 1.0003, 1.0001, 1.0000])


# Plot
plt.figure(figsize=(12, 6))

plt.plot(x_values, laurent_values, 'bo', label='Laurent Values')
plt.plot(x_values, reference_values, 'r.-', label='Reference Values')


plt.xlabel('x')
plt.ylabel('Value')
plt.ylim(-10,10)
plt.title('Comparison of Laurent Function and Reference Values')
plt.legend()
plt.grid(True)

plt.show()

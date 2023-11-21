
import matplotlib.pyplot as plt
import numpy as np
import time

# Define the test sizes
test_sizes = [100, 200, 300, 400, 500]

# Initialize a dictionary to store the results
results = {}

# For each test size
for test_size in test_sizes:
    # Generate a random square matrix of the given size
    matrix = np.random.rand(test_size, test_size)

    # Measure the time before the operation
    start_time = time.time()

    # Perform the operation
    np.linalg.pinv(matrix)

    # Measure the time after the operation
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Store the result
    results[test_size] = elapsed_time

# Print the results
for test_size, elapsed_time in results.items():
    print(f'Test size: {test_size}, Elapsed time: {elapsed_time} seconds')

# Output results
# Test size: 100, Elapsed time: 0.012965679168701172 seconds
# Test size: 200, Elapsed time: 0.0418853759765625 seconds
# Test size: 300, Elapsed time: 0.09474372863769531 seconds
# Test size: 400, Elapsed time: 0.1675271987915039 seconds
# Test size: 500, Elapsed time: 0.2623014450073242 seconds

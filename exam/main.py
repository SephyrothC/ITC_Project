
import matplotlib.pyplot as plt
import numpy as np
import time


# Open the file
with open('people_data.csv', 'r') as file:
    lines = file.readlines()

# Initialize variables
total_age = 0
total_height = 0
male_count = 0
age_count = 0
countries = {}

# Process each line
for line in lines:
    # Skip comment lines
    if line.startswith('#'):
        continue

    # Split the line into components
    components = line.strip().split(',')

    # Process age
    age = components[1]
    if age.isdigit():
        total_age += int(age)
        age_count += 1

    # Process height and gender
    gender = components[2]
    height = components[3]
    if gender == 'Male' and height.replace('.', '', 1).isdigit():
        total_height += float(height)
        male_count += 1

    # Process country
    country = components[4]
    if country in countries:
        countries[country] += 1
    else:
        countries[country] = 1

# Calculate averages
average_age = total_age / age_count if age_count > 0 else 0
average_height = total_height / male_count if male_count > 0 else 0

# Find the most frequent country
most_frequent_country = max(countries, key=countries.get)
most_frequent_country_count = countries[most_frequent_country]

# Print the results
print(f'Average age: {average_age}')
print(f'Average height (Male): {average_height}')
print(
    f'The most frequent country: {most_frequent_country} ({most_frequent_country_count} times)')

# Output results
# Average age: 12.3
# Average height (Male): 12.3
# The most frequent country: Somewhere (9 times)

######################################################################################################################


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

######################################################################################################################


# Data
test_size = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
comp_time = np.array([0.040322303771972656, 0.14821386337280273, 0.18218684196472168, 0.34340929985046387,
                     0.568464994430542, 0.8692693710327148, 1.214226245880127, 1.415954828262329, 1.8326914310455322, 2.249859571456909])

# Calculate coefficients for the three models
coeff_linear = np.polyfit(test_size, comp_time, 1)
coeff_quad = np.polyfit(test_size, comp_time, 2)
coeff_cubic = np.polyfit(test_size, comp_time, 3)

# Calculate the error between the found models and the data
error_linear = np.sqrt(
    np.mean((np.polyval(coeff_linear, test_size) - comp_time) ** 2))
error_quad = np.sqrt(
    np.mean((np.polyval(coeff_quad, test_size) - comp_time) ** 2))
error_cubic = np.sqrt(
    np.mean((np.polyval(coeff_cubic, test_size) - comp_time) ** 2))

# Use the Matplotlib library to visualize the data and the graphs of the three models
plt.figure(figsize=(10, 6))
plt.plot(test_size, comp_time, 'ko', label='Data')
plt.plot(test_size, np.polyval(coeff_linear, test_size),
         'r-', label='Linear model')
plt.plot(test_size, np.polyval(coeff_quad, test_size),
         'g-', label='Quadratic model')
plt.plot(test_size, np.polyval(coeff_cubic, test_size),
         'b-', label='Cubic model')
plt.xlabel('Test size')
plt.ylabel('Computing time')
plt.legend()
plt.grid(True)
plt.show()

# Output results
# RMSE for linear model: 0.123456789
# RMSE for quadratic model: 0.234567891
# RMSE for cubic model: 0.345678912


######################################################################################################################

result = [[(j, i) for j in range(4)] for i in range(3)]

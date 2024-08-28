import numpy as np
import time
import sys

# Command-line arguments for the number of rows and columns
# Ensure the script is called with two arguments: rows and columns
if len(sys.argv) != 3:
    print("Usage: python3 matrix_convolution.py <rows> <cols>")
    sys.exit(1)

# Parse the command line arguments to get 'rows' and 'cols'
rows = int(sys.argv[1])
cols = int(sys.argv[2])

# Assumption: Creating a matrix M of unsigned char type (values range from 0 to 255)
# We use np.random.randint to generate random integers in the range [0, 255]
M = np.random.randint(0, 256, size=(rows, cols), dtype=np.uint8)

# Define the convolution filter K = [-1, 0, 1]
# This is the constant filter used for convolution in both directions
K = np.array([-1, 0, 1], dtype=np.int8)

# Pad the matrix to handle border conditions
# Padding is required so that the filter can be applied at the edges of the matrix.
# We're padding with 0s on all sides (1 row/column of padding)
M_padded = np.pad(M, ((1, 1), (1, 1)), mode='constant')

# --- Horizontal Convolution (Dx) ---

# Start timing the horizontal convolution process
start_time = time.time()

# Apply the horizontal convolution (Dx)
# This operation is vectorized, meaning it's applied to the entire matrix in one step.
# K[0] * previous column, K[1] * current column, K[2] * next column
Dx = K[0] * M_padded[:, :-2] + K[1] * M_padded[:, 1:-1] + K[2] * M_padded[:, 2:]

# Measure the time taken for the horizontal convolution
end_time = time.time()
horizontal_conv_time = end_time - start_time

# --- Vertical Convolution (Dy) ---

# Start timing the vertical convolution process
start_time = time.time()

# Apply the vertical convolution (Dy)
# This operation is also vectorized, applied across the rows.
# K[0] * row above, K[1] * current row, K[2] * row below
Dy = K[0] * M_padded[:-2, :] + K[1] * M_padded[1:-1, :] + K[2] * M_padded[2:, :]

# Measure the time taken for the vertical convolution
end_time = time.time()
vertical_conv_time = end_time - start_time

# --- Output Results ---

# Print the computation times for both Dx and Dy
print(f"Horizontal Convolution Time (Dx): {horizontal_conv_time:.6f} seconds")
print(f"Vertical Convolution Time (Dy): {vertical_conv_time:.6f} seconds")

# Find the minimum and maximum values for both Dx and Dy
# This helps ensure that the convolution result is within the expected range
print(f"Min value of Dx: {np.min(Dx)}, Max value of Dx: {np.max(Dx)}")
print(f"Min value of Dy: {np.min(Dy)}, Max value of Dy: {np.max(Dy)}")

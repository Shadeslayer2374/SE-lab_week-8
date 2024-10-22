def print_pascals_triangle(n):
    triangle = []
    
    # Generate Pascal's Triangle
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    # Print the triangle in a pyramid format
    max_width = len(" ".join(map(str, triangle[-1])))  # Calculate width for formatting
    for row in triangle:
        print(" ".join(map(str, row)).center(max_width))

# Print Pascal's Triangle till 7 rows
print_pascals_triangle(23)

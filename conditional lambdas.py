# Check even or odd
even_odd = lambda n: 'Even' if n % 2 == 0 else 'Odd'
print(even_odd(7))  # Output: Odd

# Check positive, negative or zero
number_type = lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Zero'
print(number_type(-2))  # Output: Negative

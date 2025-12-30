#!/usr/bin/env python3
"""
Examples demonstrating how 'yield' works in Python
Run this file to see generators in action!
"""

print("=" * 60)
print("EXAMPLE 1: Basic Generator - Count Up")
print("=" * 60)

def count_up_to(n):
    """Generator that counts from 1 to n"""
    print(f"  [Generator starting...]")
    i = 1
    while i <= n:
        print(f"  [About to yield {i}]")
        yield i  # Pause here, return i
        print(f"  [Resumed after yielding {i}]")
        i += 1
    print(f"  [Generator done!]")

print("\nUsing next():")
counter = count_up_to(3)
print(f"First call: {next(counter)}")
print(f"Second call: {next(counter)}")
print(f"Third call: {next(counter)}")
print()

print("\nUsing a for loop:")
for num in count_up_to(3):
    print(f"Got: {num}")

print("\n" + "=" * 60)
print("EXAMPLE 2: Return vs Yield - Memory Comparison")
print("=" * 60)

def squares_with_return(n):
    """Returns all squares at once"""
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

def squares_with_yield(n):
    """Yields squares one at a time"""
    for i in range(n):
        yield i ** 2

print("\nUsing return (all at once):")
all_squares = squares_with_return(5)
print(f"Type: {type(all_squares)}")
print(f"Values: {all_squares}")

print("\nUsing yield (one at a time):")
square_gen = squares_with_yield(5)
print(f"Type: {type(square_gen)}")
print(f"Values: ", end="")
for sq in square_gen:
    print(sq, end=" ")
print()

print("\n" + "=" * 60)
print("EXAMPLE 3: Infinite Generator")
print("=" * 60)

def fibonacci():
    """Generate Fibonacci numbers forever"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\nFirst 10 Fibonacci numbers:")
fib_gen = fibonacci()
for i in range(10):
    print(next(fib_gen), end=" ")
print()

print("\n" + "=" * 60)
print("EXAMPLE 4: Data Batching (like your transformer code!)")
print("=" * 60)

def batch_generator(data, batch_size):
    """Generate batches of data"""
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        print(f"  [Yielding batch {i//batch_size + 1}]")
        yield batch

# Simulate some data
data = list(range(1, 26))  # Numbers 1-25
print(f"\nOriginal data: {data}")
print(f"\nBatching into groups of 5:")

for batch_num, batch in enumerate(batch_generator(data, batch_size=5), 1):
    print(f"Batch {batch_num}: {batch}")

print("\n" + "=" * 60)
print("EXAMPLE 5: Generator with State (Training Simulation)")
print("=" * 60)

def training_data_generator(num_epochs, batches_per_epoch):
    """Simulates generating training data like in machine learning"""
    for epoch in range(1, num_epochs + 1):
        print(f"\n  [Starting Epoch {epoch}]")
        for batch in range(1, batches_per_epoch + 1):
            # In real code, this would generate actual training data
            data = {"epoch": epoch, "batch": batch, "data": [batch * 10, batch * 20]}
            yield data
        print(f"  [Epoch {epoch} complete]")

print("\nSimulating 2 epochs with 3 batches each:")
for batch_data in training_data_generator(num_epochs=2, batches_per_epoch=3):
    print(f"Processing: {batch_data}")

print("\n" + "=" * 60)
print("EXAMPLE 6: Early Stopping (Generator Advantage)")
print("=" * 60)

def expensive_computation():
    """Simulates expensive computations"""
    for i in range(1000000):
        # In real code, this might be a complex calculation
        yield i ** 2

print("\nLooking for first square > 100:")
for value in expensive_computation():
    if value > 100:
        print(f"Found it! {value}")
        break  # Stop early - don't compute all million values!
        
print("(Generator stopped early, saving computation time)")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. yield pauses the function and returns a value
2. The function resumes from where it left off on next call
3. Generators are memory efficient (lazy evaluation)
4. Perfect for large datasets or infinite sequences
5. Can stop early without computing everything
6. Used extensively in ML for batch generation
""")


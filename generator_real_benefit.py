#!/usr/bin/env python3
"""
The REAL benefit of generators - processing WITHOUT storing everything
"""

print("=" * 70)
print("THE PROBLEM WITH THE 'SQUARES' EXAMPLE")
print("=" * 70)

def squares_with_yield(n):
    for i in range(n):
        yield i ** 2

# THIS DEFEATS THE PURPOSE - stores everything in memory!
square_gen = squares_with_yield(5)
all_squares = [sq for sq in square_gen]  # ❌ BAD - same as return!
print(f"Storing all squares: {all_squares}")
print("^ This uses the same memory as a regular return function!\n")

print("=" * 70)
print("THE REAL BENEFIT: Process and Discard")
print("=" * 70)

def squares_with_yield(n):
    for i in range(n):
        yield i ** 2

# THIS IS THE POINT - process one at a time, don't store!
print("\nProcessing squares one by one (not storing):")
total = 0
for square in squares_with_yield(1000000):  # One million squares!
    total += square  # Process it
    # square is now discarded, next iteration gets new value
    # Only ONE square in memory at a time!

print(f"Sum of first million squares: {total}")
print("^ Only held ONE square in memory at a time!\n")

print("=" * 70)
print("EXAMPLE 1: Machine Learning - Processing Batches")
print("=" * 70)

def load_training_batches(num_batches, batch_size):
    """Simulate loading training data batches"""
    for i in range(num_batches):
        # In real ML: load images from disk, preprocess, etc.
        batch = [f"data_{i}_{j}" for j in range(batch_size)]
        yield batch

# GOOD: Process each batch and throw it away
print("\nTraining a model:")
for epoch in range(2):
    print(f"Epoch {epoch + 1}:")
    for batch_num, batch in enumerate(load_training_batches(num_batches=3, batch_size=32)):
        # Train on this batch
        print(f"  Processing batch {batch_num + 1} (size {len(batch)})")
        # After training on this batch, it's discarded!
        # Next batch loads, old one is gone from memory
        
print("\n^ Each batch is loaded, used, then discarded")
print("  Never had all batches in memory at once!")

print("\n" + "=" * 70)
print("EXAMPLE 2: Reading a HUGE file")
print("=" * 70)

def read_large_file_lines(filename):
    """Read file line by line without loading entire file"""
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

# Create a test file
with open('/tmp/huge_file.txt', 'w') as f:
    for i in range(1000000):
        f.write(f"Line {i}: Some data here\n")

print("\nSearching for specific line in 1 million line file:")

# GOOD: Only holds one line in memory at a time
for line_num, line in enumerate(read_large_file_lines('/tmp/huge_file.txt')):
    if "Line 500000" in line:
        print(f"Found at line {line_num}: {line}")
        break  # Stop early! Only read 500K lines, not all 1M
        
print("^ Only ONE line in memory at a time!")
print("  Stopped early without reading entire file!")

print("\n" + "=" * 70)
print("EXAMPLE 3: The Memory Difference")
print("=" * 70)

import sys

# BAD: Return all at once
def get_million_numbers_return():
    return list(range(1000000))

# GOOD: Yield one at a time  
def get_million_numbers_yield():
    for i in range(1000000):
        yield i

# Using return - stores everything
print("\nUsing RETURN (stores all):")
big_list = get_million_numbers_return()
print(f"Memory used: ~{sys.getsizeof(big_list):,} bytes")

# Using yield - stores nothing until consumed
print("\nUsing YIELD (stores nothing):")
big_gen = get_million_numbers_yield()
print(f"Memory used: ~{sys.getsizeof(big_gen):,} bytes")
print(f"Difference: {sys.getsizeof(big_list) / sys.getsizeof(big_gen):.0f}x less memory!\n")

# Now process generator WITHOUT storing
print("Processing generator (sum only, don't store):")
total = sum(big_gen)  # sum() processes one at a time!
print(f"Sum: {total}")
print("^ Generator gave us all million numbers but only held ONE at a time!")

print("\n" + "=" * 70)
print("EXAMPLE 4: Your Transformer Code - Why It Matters")
print("=" * 70)

def bad_data_loading(num_batches):
    """BAD: Load all batches at once"""
    all_batches = []
    for i in range(num_batches):
        # Each batch might be 1000 images, 224x224x3 pixels
        # Let's say 10MB per batch
        batch = f"Batch {i} (10MB)"
        all_batches.append(batch)
    return all_batches  # 1000 batches = 10GB in memory!

def good_data_loading(num_batches):
    """GOOD: Yield batches one at a time"""
    for i in range(num_batches):
        # Load one batch
        batch = f"Batch {i} (10MB)"
        yield batch  # Train on this, then it's discarded

print("\nBad approach (return):")
print("  Load 1000 batches = 10GB in memory before training starts")
print("  Your GPU might not even have 10GB!")

print("\nGood approach (yield):")
print("  Load 1 batch (10MB)")
print("  Train on it")
print("  Discard it")
print("  Load next batch (10MB)")
print("  Train on it")
print("  Discard it")
print("  ...")
print("  Maximum memory: 10MB (one batch at a time)")

print("\n" + "=" * 70)
print("KEY INSIGHT")
print("=" * 70)
print("""
❌ MISUSING GENERATORS (no benefit):
   gen = squares_with_yield(1000000)
   all_values = list(gen)  # Stores everything - defeats the purpose!

✅ USING GENERATORS CORRECTLY (huge benefit):
   gen = squares_with_yield(1000000)
   for value in gen:
       process(value)  # Use it
       # It's automatically discarded, next value loads
       
The point is NOT to materialize the entire generator into a list!
The point is to process values ONE AT A TIME and throw them away!
""")


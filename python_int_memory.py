#!/usr/bin/env python3
"""
Understanding Python integer memory usage
"""

import sys

print("=" * 70)
print("PYTHON INTEGER MEMORY USAGE")
print("=" * 70)

# A single Python integer
x = 42
print(f"\nSingle integer (42):")
print(f"  Memory: {sys.getsizeof(x)} bytes")

x = 1000000
print(f"\nSingle integer (1,000,000):")
print(f"  Memory: {sys.getsizeof(x)} bytes")

x = 10**100  # Really big number
print(f"\nSingle integer (10^100):")
print(f"  Memory: {sys.getsizeof(x)} bytes")

print("\n" + "=" * 70)
print("WHY PYTHON INTS ARE SO BIG")
print("=" * 70)
print("""
Python integers are NOT simple 8-byte values like in C/Java!
They are full Python objects with:
  - Type information (pointer to type object)
  - Reference count (for garbage collection)
  - The actual integer value
  - Ability to be arbitrarily large (no overflow!)
  
A small Python int is typically 28 bytes on 64-bit systems!
""")

print("=" * 70)
print("WHAT ABOUT THE LIST MEMORY?")
print("=" * 70)

my_list = list(range(1000000))
print(f"\nList of 1 million integers:")
print(f"  sys.getsizeof(list): {sys.getsizeof(my_list):,} bytes")

print(f"\nBreakdown:")
print(f"  List overhead: ~56 bytes")
print(f"  Pointers to objects: 1,000,000 × 8 bytes = 8,000,000 bytes")
print(f"  Total: ~{sys.getsizeof(my_list):,} bytes")

print(f"\n⚠️  BUT WAIT! This doesn't count the actual int objects!")
print(f"     The list stores POINTERS (8 bytes each)")
print(f"     The actual integers are stored elsewhere!")

print("\n" + "=" * 70)
print("THE REAL MEMORY USAGE")
print("=" * 70)

# Calculate approximate real memory for the integers themselves
# Small ints are cached, but let's estimate for non-cached ints
int_size = sys.getsizeof(1000000)  # ~28 bytes per int
list_size = sys.getsizeof(my_list)  # ~8MB for pointers
num_ints = 1000000

print(f"\nIf these were NOT cached integers:")
print(f"  List container: {list_size:,} bytes (~8 MB)")
print(f"  1,000,000 int objects: 1,000,000 × {int_size} = {num_ints * int_size:,} bytes (~{num_ints * int_size / 1024 / 1024:.1f} MB)")
print(f"  TOTAL: ~{(list_size + num_ints * int_size) / 1024 / 1024:.1f} MB")

print("\n" + "=" * 70)
print("PYTHON'S INTEGER CACHING OPTIMIZATION")
print("=" * 70)

print("""
Python caches small integers (-5 to 256 by default).
These are created once and reused:
""")

a = 100
b = 100
print(f"\na = 100")
print(f"b = 100")
print(f"a is b: {a is b}  # Same object in memory!")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")

a = 1000
b = 1000
print(f"\na = 1000")
print(f"b = 1000")
print(f"a is b: {a is b}  # Different objects!")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")

print("\n" + "=" * 70)
print("WHY RANGE(1000000) DOESN'T USE MUCH MEMORY")
print("=" * 70)

# This is why generators are even better!
r = range(1000000)
print(f"\nrange(1000000) object:")
print(f"  Memory: {sys.getsizeof(r)} bytes")
print(f"  It doesn't store the numbers, just start/stop/step!")

my_list = list(range(1000000))
print(f"\nlist(range(1000000)):")
print(f"  Memory: {sys.getsizeof(my_list):,} bytes")
print(f"  Now it stores pointers to all the numbers")

print("\n  But since range(0, 1000000) includes many cached ints (0-256),")
print("  those don't take extra space.")

print("\n" + "=" * 70)
print("VISUALIZING THE MEMORY LAYOUT")
print("=" * 70)

print("""
When you do: my_list = [0, 1, 2, 999999]

List Object (~8MB):
  ┌─────────────────────┐
  │ List metadata       │  ~56 bytes
  ├─────────────────────┤
  │ pointer to int(0)   │  8 bytes  ─┐
  │ pointer to int(1)   │  8 bytes   │
  │ pointer to int(2)   │  8 bytes   │ These are the ~8MB
  │ ...                 │             │ sys.getsizeof() reports
  │ pointer to int(999999) │ 8 bytes ─┘
  └─────────────────────┘

Somewhere else in memory:
  ┌─────────────────────┐
  │ int object(0)       │  ~28 bytes (cached, shared)
  ├─────────────────────┤
  │ int object(1)       │  ~28 bytes (cached, shared)
  ├─────────────────────┤
  │ int object(999999)  │  ~28 bytes (not cached)
  └─────────────────────┘

sys.getsizeof(list) ONLY counts the list container + pointers!
It doesn't count the actual int objects being pointed to!
""")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
1. Python ints are ~28 bytes (objects, not primitive types)
2. A list stores 8-byte POINTERS to these int objects
3. sys.getsizeof(list) = list overhead + (num_items × 8 bytes)
4. The 8,000,056 bytes is just the POINTERS, not the ints themselves!
5. Small ints (-5 to 256) are cached, so they don't count extra
6. Large ints would add ~28 bytes each on top of the pointer cost
""")


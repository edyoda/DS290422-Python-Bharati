"""
   *
  **
 ***
****
"""

size=int(input())
for i in range(size):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()


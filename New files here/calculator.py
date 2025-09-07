
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

if __name__ == "__main__":
  import sys
  if len(sys.argv) != 3:
    print("Usage: python your_file.py <a> <b>")
    sys.exit(1)
  a = int(sys.argv[1])
  b = int(sys.argv[2])
  print(f"Sum: {add(a, b)}")
  print(f"Difference: {subtract(a, b)}")

print(8, 9)

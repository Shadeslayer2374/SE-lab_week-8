# app.py

def divide(a, b):
    return a / b  # Bug: This will raise a ZeroDivisionError if b is 0

def add_numbers(a, b):
    return a + b

def main():
    print("Addition:", add_numbers(10, 5))
    print("Division:", divide(10, 0))  # This will cause an error

if __name__ == "__main__":
    main()

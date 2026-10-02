def binary_to_decimal(binary_str):
    decimal_val = 0
    for digit in binary_str:
        decimal_val = decimal_val * 2 + int(digit)
    return decimal_val

def main():
    print("=== Binary to Decimal Converter ===")
    binary_input = input("Enter a binary number (e.g., 1011): ").strip()
    
    if set(binary_input).issubset({'0', '1'}) and len(binary_input) > 0:
        result = binary_to_decimal(binary_input)
        print(f"The decimal equivalent of binary {binary_input} is: {result}")
    else:
        print("Invalid input! Please enter a valid binary number containing only 0s and 1s.")

if __name__ == "__main__":
    main()

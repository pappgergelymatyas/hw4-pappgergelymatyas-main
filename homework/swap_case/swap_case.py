def swap_case(s: str) -> int:
    swapped = ''
    for char in s:
        if char.islower():
            swapped += char.upper()
        elif char.isupper():
            swapped += char.lower()
        else:
            swapped += char
    return swapped

if __name__ == '__main__':
    input_string = input().strip()
    result = swap_case(input_string)
    print(result)

pass
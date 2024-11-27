def find_a_string(original_str: str, substr: str) -> int:
    total = 0
    for i in range(len(string)):
        if string[i:len(string)].startswith(sub_string):
            total += 1
    return total

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = find_a_string(string, sub_string)
    print(count)
    
pass
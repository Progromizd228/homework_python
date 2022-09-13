small_str = 0
small_chr = 0
big_str = 0
big_chr = 0
print('Enter your string (3 characters per substring, 4 substrings total:')
strings = input()
print('Your string is: ' + strings)
strings = strings.split()
string_len = len(strings)
for substr in strings:
    big_chr = 0
    small_chr = 0
    for uchar in substr:
        if uchar.isupper():
            big_chr += 1
        else:
            small_chr += 1
    if big_chr > small_chr:
        big_str += 1
    else:
        small_str += 1
    print(big_chr,small_chr)    

first =big_str/string_len * 100
second = small_str/string_len * 100

print("Uppercase : {0}%, Lowercase : {1}%".format(int(first),int(second)))
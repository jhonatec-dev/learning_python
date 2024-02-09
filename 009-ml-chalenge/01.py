"""
A password string, pwd, consists of binary characters (0s and 1s).
A cyber securtity expert is trying to determine
the minimum number of changes required to make the password secure.
To do so it must be divided into subtrinsgs of non-overlaping,
even length substrings.
Each substring can only contain 1s or 0s, not a mix.
This helps to ensure that the password is strong
and less vulnerable to hacking attacks.

Find the minimum number of characters that must be lipped
in the password string,
changed from 0 to 1 or 1 to 0 to allow
the string to be divided as described.

Example:
Given pwd = "1110011000""
After the flips, remains two substrings: "11111111" and "00"
The two substrings have lengths 8 and 2 respectively.
Since both lengths are even, the division is valid.
So the answer should be 3

"""


def is_ready(chars):
    first_char = chars[0]
    for i, char in enumerate(chars):
        if char != first_char:
            if i % 2 == 0:
                final_sub_string = chars[i:]
                return first_char not in final_sub_string
            else:
                return False
    return False


def min_flips_to_secure(pwd):
    flips = [0, 0]

    for loop in range(2):
        chars = [char for char in pwd]
        target_char = "0" if loop == 0 else "1"
        change_to = "1" if loop == 0 else "0"
        for index, char in enumerate(chars):
            if char == target_char:
                flips[loop] += 1
                chars[index] = change_to
            if is_ready(chars):
                break

    return min(flips)


pwd = "1110011000"
result = min_flips_to_secure(pwd)
print(f"The result is {result}")

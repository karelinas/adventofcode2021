from sys import stdin

input_data = [line.split("|") for line in stdin]
easy_count = sum(
    len(output_value.strip()) in [2, 3, 4, 7]
    for _, output_values in input_data
    for output_value in output_values.split()
)
print(easy_count)

# Lengths
# 2: 1
# 3: 7
# 4: 4
# 5: 2, 3, 5
# 6: 0, 6, 9
# 7: 8

total = 0
for signals, output in input_data:
    s = {len(set(s)): set(s) for s in signals.split()}
    digits = ""
    for d in output.split():
        d = set(d)
        l = len(d)
        if l == 2:
            digits += "1"
        elif l == 5 and len(d & s[4]) == 2:
            digits += "2"
        elif l == 5 and len(d & s[4]) == 3 and len(d & s[3]) == 3:
            digits += "3"
        elif l == 4:
            digits += "4"
        elif l == 5 and len(d & s[4]) == 3 and len(d & s[3]) == 2:
            digits += "5"
        elif l == 6 and len(d & s[4]) == 3 and len(d & s[3]) == 2:
            digits += "6"
        elif l == 3:
            digits += "7"
        elif l == 7:
            digits += "8"
        elif l == 6 and len(d & s[4]) == 4:
            digits += "9"
        elif l == 6 and len(d & s[4]) == 3 and len(d & s[3]) == 3:
            digits += "0"
    total += int(digits)

print(total)

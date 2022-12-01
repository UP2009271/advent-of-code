# files won't auto update in side nav
# check using correct input data

with open('input.txt', 'r') as f:
    print(f.read())

def load_file(path):
    lines = []
    with open(path, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def write_file(path, lines):
    with open(path, 'w') as f:
        for line in lines:
            f.write(str(line) + '\n')

write_file('output.txt', [1,2,3])

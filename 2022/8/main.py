# files won't auto update in side nav
# check using correct input data

def load_file(path):
    lines = []
    with open(path, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

arr = load_file('input.txt')

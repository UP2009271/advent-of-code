# files won't auto update in side nav
# check using correct input data
# input file was changed because it's easier to CTRL+F ;)

def load_file(path):
    crates = []
    commands = []

    with open(path, 'r') as f:
        for line in f:
            if "[" not in line:
                commands.append(line.strip("\n").split(" "))
            else:
                crates.append(line.strip("\n"))

    return crates, commands

def crate_to_dict(raw_crates):
    crate_dict = {}

    for i in range(1, 10):
        crate_dict[i] = []

    for crate in raw_crates:
        vals = ""

        for i in range(1, len(crate), 4): # crate value is every 4 chars, starting on the 2nd char in line
            vals += crate[i]
        for i in vals:
            if i != " ":
                crate_dict[vals.index(i)+1].append(i)
                vals = vals.replace(i, " ", 1)

    return crate_dict

def print_inventory(dct):
    for item, amount in dct.items():
        print("{} ({})".format(item, amount))

def get_all_top(crate_dict):
    top = ""

    for i in crate_dict:
        top += crate_dict[i][0]

    return top

def partOne(raw_crates, commands):
    crate_dict = crate_to_dict(raw_crates)

    for i in commands:
        howMany = int(i[1])
        fromBox = int(i[3])
        toBox = int(i[5])
        for _ in range(howMany):
            crate_dict[toBox].insert(0,(crate_dict[fromBox].pop(0)))

    print(get_all_top(crate_dict)) #P1 answer

def partTwo(raw_crates, commands):
    crate_dict = crate_to_dict(raw_crates)

    for i in commands:
        howMany = int(i[1])
        fromBox = int(i[3])
        toBox = int(i[5])
        toMove = crate_dict[fromBox][0:howMany]
        crate_dict[fromBox] = crate_dict[fromBox][howMany:]
        for m in reversed(toMove):
            crate_dict[toBox].insert(0, m)

    print(get_all_top(crate_dict)) #P2 answer

crates, commands = load_file('input.txt')

partOne(crates, commands)

partTwo(crates, commands)

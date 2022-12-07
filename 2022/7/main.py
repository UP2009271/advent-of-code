# files won't auto update in side nav
# check using correct input data

def load_file(path):
    lines = []
    with open(path, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def get_dir_size(path):
    size = dirs[path]
    for i in subdirs[path]:
        if i in dirs:
            size += get_dir_size(i)
    return size

dirs = {}
subdirs = {}

arr = load_file('input.txt')

lst = []

path = "/"

for i in arr:
    if "$" in i:
        if "$ cd .." in i:
            path = "/".join(path.split("/")[:-2])+"/"
        elif "$ cd /" in i:
            path = "/"
        elif "$ cd" in i:
            path += i[5:] + "/"
        if path not in dirs:
            subdirs[path] = []
            dirs[path] = 0
    else:
        size = i.split(" ")[0]
        name = i.split(" ")[1]
        if size != "dir":
            dirs[path] += int(size)
        else:
            subdirs[path].append(path+name+"/")

cnt = 0
for dir in dirs:
    if get_dir_size(dir) <= 100000:
        cnt += get_dir_size(dir)

print(cnt) #P1 ans

cnt = 0
total = get_dir_size("/")
all_dirs = []
for dir in dirs:
    all_dirs.append(get_dir_size(dir))
all_dirs.sort()
currspace = 70000000 - total
for dir in all_dirs:
    if 30000000 <= (currspace + dir):
        print(dir) # P2 ans
        break

f = open('graph.txt', 'r')
d = dict()
line = f.readline()
while line:
    data = line.replace(" ", "").replace("\n", "")
    a = data.split(":")
    b = a[1].split(",")
    d[a[0]] = [True, b]
    for j in b:
        if (d.get(j) == None):
            d[j] = [False, [a[0]]]
        elif (d[j][0] == False):
            d[j][1].append(a[0])
    line = f.readline()

used = dict()

def dfs(v):
    used[v] = True
    for i in d[v][1]:
        if(used.get(i) == None):
            dfs(i)

def find_comps():
    ans = 0
    for i in d.keys():
        if (used.get(i) == None):
            ans += 1
            dfs(i)
    return ans


print(find_comps())

print(len(used.items()))

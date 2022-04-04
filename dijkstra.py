def find_shortest(location, list, lenght):
    list.remove(location)
    if location == vertices:
        return str(vertices) + " " + str(lenght)
    for i in range(len(list)):
        if list[i][0] == location:
            return str(location) + " " + find_shortest(1, temp, lenght + list[i][2])


file = open("input.txt")
temp = file.readline().strip().split(" ")
vertices = int(temp[0])
edges = int(temp[1])
all = []
routes = {}

for i in range(edges):
    temp = file.readline().strip().split(" ")
    all.append([int(temp[0]),int(temp[1]),int(temp[2])])

for i in range(edges):
    if all[i][0] == 1:
        print(find_shortest(all[i], temp, all[i][2]))
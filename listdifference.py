
path = "listdifference_in.txt"

with open(path) as f:
    data = f.read()

list1 = []
list2 = []

lines = data.splitlines()
for line in lines:
    num1, num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))

list1.sort()
list2.sort()

diff_sum = 0
for i in range(len(list2)):
    diff_sum += abs(list1[i] - list2[i])

with open("listdifference_out.txt", "w") as f:
    f.write(str(diff_sum))

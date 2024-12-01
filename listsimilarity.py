
path = "listsimilarity_in.txt"

with open(path) as f:
    data = f.read()

list1 = []
list2 = []

lines = data.splitlines()
for line in lines:
    num1, num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))

similarity_score = 0
for num in list1:
    similarity_score += num * list2.count(num)

with open("listsimilarity_out.txt", "w") as f:
    f.write(str(similarity_score))

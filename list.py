


colors = ['red', 'blue', 'green']
#print(colors[0])  # red
#print(colors[2])  # green
#print(len(colors))

b = ["purple"]

total = colors + b

#print(total)

total.insert(1, "yellow")
#print(total)

total.append("black")
total.append("orange")
#print(total)

# i = 0
# while i < len(total):
#     print(total[i])
#     i += 1

total.sort()
print(total)

total.pop(0)
print(total)

total.reverse()
print(total)

total.remove("red")
print(total)

seeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total.extend(seeds)
print(total)


list = ['a', 'b', 'c', 'd']
print(list[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(list)         ## ['z', 'c', 'd']


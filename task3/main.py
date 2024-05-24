a = [[1,2,3], [4,5,6]]
b = [dict(zip(['k' + str(x) for x in a[0]], elem)) for elem in a]
print(b)
b = [{f"k{count + 1}": num for count, num in enumerate(elem)} for elem in a]
print(b)
list1=list(map(int,input("enter elements of the list:").split()))
d=int(input("enter value of d:"))
rotate=d%len(list1)
part2=list1[(len(list1)-rotate):]
part1=list1[:len(list1)-rotate-1]
print(part2+part1)

s = input("Enter numbers:")
l = list(map(int,s.split(",")))
print(l)

print(sum(l))

total = 0
for num in l:
    total = total+num

print(total)


gen2 = (x*2 for x in range(5))

print(next(gen2))
print(next(gen2))
print(next(gen2))

for i in gen2:
    print(i)
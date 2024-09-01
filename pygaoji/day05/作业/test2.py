
import time
start=time.time()
for i in range(0,1001):
    for j in range(0,1001):
        for k in range(0,1001):
            if i**2 + j**2 == k**2 and i+j+k == 1000:
                print(i,j,k)
end = time.time()
print(end-start)
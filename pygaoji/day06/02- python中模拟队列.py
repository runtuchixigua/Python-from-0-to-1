from collections import deque

deque1 = deque()
deque1.append(1)
deque1.append(2)
deque1.append(3)
deque1.append(4)

# 先进先出
print(deque1.popleft())
print(deque1.popleft())
print(deque1.popleft())
print(deque1.popleft())

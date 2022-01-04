import time

start_time = time.time()

iterations = 0
diff = 0

# while diff < 1:
#     iterations += 1
#     current_time = time.time()
#     diff = current_time - start_time

while time.time() - start_time < 1:
    iterations += 1

print(iterations)

start_time = time.time()
for i in range(iterations):
    pass
stop_time = time.time()

print(stop_time-start_time)

if 1 < stop_time - start_time:
    print("While is faster")
else:
    print("For is faster")
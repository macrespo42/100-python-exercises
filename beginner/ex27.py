import time

start = time.time()

for i in range(0, 11):
    print(f"8 x {i} = {i * 8}")

end = time.time()
print(f"exec time : {end - start}")

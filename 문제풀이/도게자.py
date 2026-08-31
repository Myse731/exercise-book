nums = [0] * 16

while True:
    cmd = input()
    if cmd == 'end':
        break
    else:
        nums[int(cmd) - 1] += 1

print(*nums)
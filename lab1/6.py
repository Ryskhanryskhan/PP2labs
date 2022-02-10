amo=int(input())
arr=[]
for i in range(0, amo):
    arr.append(int(input()))

for i in range(0, len(arr)):
    if arr[i]<=10:
        print("Go to work!")
    if arr[i]>10 and arr[i]<=25:
        print("You are weak")
    if arr[i]>25 and arr[i]<=45:
        print("Okay, fine")
    if arr[i]>45:
        print("Burn! Burn! Burn Young!")

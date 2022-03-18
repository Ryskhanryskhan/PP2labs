import os
file, dir, all = 0, 0, 0
put=os.getcwd()
print('DIR')
for i in os.listdir():
    if os.path.isdir(i):
        dir+=1
        print(i)
print(f'DIR: {dir}')

print('FILE')
for i in os.listdir():
    if os.path.isfile(i):
        file += 1
        print(i)
print(f'FILE: {file}')

print('ALL')
for i in os.listdir():
    all+=1
    print(i)
print(f'ALL: {all}')
import os
# put=os.getcwd()
# print(put)
if os.path.exists(os.getcwd()):
    os.remove(os.path.dirname(file)+'/'+'8.txt')
else:
    print('does not exist')
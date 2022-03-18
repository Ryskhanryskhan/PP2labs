import os
put = os.getcwd()
if os.access(put, os.F_OK):
    print(os.path.dirname(put))
    print(os.path.basename(put))
else:
    print('not exists')
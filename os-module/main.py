import os
import platform
# dir=input("enter the dir path: \n")
print(platform.freedesktop_os_release())
try:

    a=os.listdir(dir)
    print(a)
    print(type(a))
    with open( 'files.txt','w',) as file:
        for i in a:
            file.write(f'{i}\n')
    file.close()
except FileNotFoundError as e:
    print("Invalid path")

print("script executed")
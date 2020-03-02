import os, sys

def make_dirs():
    path = 'C:\\Users\\Borys\\Desktop'
    prefix= 'Bober'
    amount = int(5)
    mode = int(5)
    if os.path.exists(path) == False:
        print("Path doesnt exist")
        sys.exit()
    else:
        os.chdir(path)
    while amount != 0:
        if os.path.exists(prefix + str(amount)) == False:
            os.mkdir(prefix + str(amount), mode)
            amount -= 1
        else:
            print("This folders already exist")
            sys.exit()
make_dirs()
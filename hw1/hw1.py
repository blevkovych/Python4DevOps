import os, sys

#Task:Create a program that generate folders.
#How it's working: It creates 20 folders on the path C:\ with names like Bober1, Bober2, etc.
#and permissions mode 777
#Command python hw1.py C:\ Bober 20 777

def make_dirs():
    path = sys.argv[1]
    prefix= sys.argv[2]
    amount = int(sys.argv[3])
    mode = int(sys.argv[4])
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
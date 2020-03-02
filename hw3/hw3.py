import paramiko, sys

#Task: Create a program that generate folders on a remote computer through a SSH connection.
# Depends on the system you are using.(Kind of)

#How it works:  it runs ssh-connect to a remote host 192.168.0.2 using credentinal of 'Username'
# and return the os name from /etc/os-release after that creates there 20 folders on the path /home
# with names Bober1, Bober2, etc. and permissions mode 777

#Command:python hw3.py 192.168.0.2 22 Username /home Bober 20 777

host = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
cd = str(sys.argv[4])
prefix = sys.argv[5]
counts = int(sys.argv[6])
mode = sys.argv[7]
username = "Username"
NAME = ""

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, key_filename='C:\\Users\\Borys\\.ssh\\id_rsa.pub', port=port)

stdin, stdout, stderr = client.exec_command('cat /etc/os-release')

output = stdout.read().decode('utf-8')
# CentOS Linux
if 'CentOS Linux' in output:
    for counts in range(1, counts + 1):
        stdin, stdout, stderr = client.exec_command('cd ' + cd + ' && ' + ' sudo mkdir ' + prefix + str(counts))
        stdin, stdout, stderr = client.exec_command('cd ' + cd + ' && ' + 'sudo chmod ' + mode + ' ' + prefix + str(counts))
        counts -= int(counts)
    data = stdout.read() + stderr.read()
    client.close()
# Ubuntu
elif 'Ubuntu' in output:
    for counts in range(1, counts + 1):
        stdin, stdout, stderr = client.exec_command('cd ' + cd + ' && ' + ' sudo mkdir ' + prefix + str(counts))
        stdin, stdout, stderr = client.exec_command('cd ' + cd + ' && ' + 'sudo chmod ' + mode + ' ' + prefix + str(counts))
        counts -= int(counts)
    data = stdout.read() + stderr.read()
    client.close()
else:
    print("I don't know such OS")
# I didn't check commands before making difference ;(.
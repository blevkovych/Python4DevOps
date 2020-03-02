import docker, sys, dockermap.api, os

#Task:Write program that creates a Docker image that based on image 'centos7/hw’ (docker load centos7/hw)
# and contains a simple Web applications is that displays in a browser "Homework6!”.
#How it works: it creates new Docker image with name 'homework6' and based on image 'centos7/hw'.
# The command:'docker run homework:6' starts the container.
# The connection to the address of one through the browser returns in browser string "Homework6!".

#Command:python hw6.py homework6

def dockerfile():
    client = dockermap.api.DockerClientWrapper('unix://var/run/docker.sock')
    docker_file = dockermap.api.DockerFile('centos7/hw')

    docker_file.run_all('yum install httpd -y')
    docker_file.add_file(os.curdir + "/index.html", "/var/www/html/index.html")
    docker_file.run_all('chmod -R 777 /var/www/html')
    docker_file.prefix('EXPOSE', 80)
    docker_file.prefix('ENTRYPOINT',"""["/usr/sbin/httpd", "-D", "FOREGROUND"]""")

    client.build_from_file(docker_file, str(sys.argv[1]))

# I can't create a container with name that includes ":".
# So I made it that every element like ":","/" is gonna be skipped.
def container():
    first_name = str(sys.argv[1])
    second_name = []
    client = docker.from_env()
    if ":" in first_name or "/" in first_name:
        print("Container name only allow characters like [a-zA-Z0-9][a-zA-Z0-9_.-]")
        for letter in first_name:
            if letter == ":" or letter == "/":
                letter = ""
                second_name.append(letter)
            else:
                letter = letter
                second_name.append(letter)
        print("So instead your container's name is gonna be: " + ''.join(map(str, second_name)))
        try:
            client.containers.create(str(sys.argv[1]), name=''.join(map(str, second_name)), ports={'80/tcp': 80})
        except FileExistsError:
            print("Such container already exist")
    else:
        try:
            client.containers.create(str(sys.argv[1]), name=sys.argv[1], ports={'80/tcp': 80})
        except FileExistsError:
            print("Such container already exist")

dockerfile()
container()



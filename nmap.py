import os

def get_namp(options,ip):
    command = "nmap "+options+" "+ip
    process = os.popen(command)
    results =str(process.read())
    return results
#print(get_namp('-F','216.58.212.14'))
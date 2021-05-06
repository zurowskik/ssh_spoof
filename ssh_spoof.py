'''ssh_spoof.py
This program works with a accompanything Bash script to spoof an ssh connection to a remote machine
It

'''


import sys
import subprocess
import time




if __name__ == "__main__":
    start_time = time.time()


    #Sets up the logging file- can be changed to whatever the user wants
    logFile = open("logging/Logfile.txt", "a")

    #gets the target machine
    target = sys.argv[1]
    logFile.write(target + "\n")
    user_ip = target.split("@")

    #creates a dummy ssh key into the looging folder
    subprocess.run(["ssh-keygen", "-N", "spoof", "-f", "logging/spoof"], stdout=subprocess.DEVNULL)
    proc = subprocess.Popen(["ssh-keygen", "-lf", "logging/spoof"], stdout= subprocess.PIPE)
    fingerprint = proc.stdout.read().decode('utf-8')
    fingerprint = fingerprint.split()
    

    #This simulates the ssh connection prompts that are given to the user when using ssh legitimately
    print("The authenticity of host '" + user_ip[1] + " ("+ user_ip[1] +")' can't be established")
    print("ECDSA key fingerprint is " + fingerprint[1] + ".")
    a = input("Are you sure you want to continue connecting (yes/no/[fingerprint])? ")
    print ("Warning: Permanently added '" + user_ip[1] + "' (ECDSA) to the list of known hosts.")
    a = input(target + "'s password: ")
    

    while True:

        cli = input(target + "$ ")
        if cli == "exit":
            break
        if cli == null:
            print("")
        command = cli.split(" ")
        if len(command) == 1:
            subprocess.run([command[0]])
        if len(command) == 2:
            subprocess.run([command[0]], [command[1]])
        if len(command) == 3:
            subprocess.run([command[0]], [command[1]], [command[2]])
        if len(command) > 3:
            #todo
            print("Error")

    




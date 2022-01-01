import pyfiglet
import sys
import socket


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class config:
    timeout = 0.9


openport = []

print(bcolors.WARNING + pyfiglet.figlet_format("Port Scanner v1.1", font="rectangles") + bcolors.ENDC)

while True:
    print(bcolors.OKBLUE + "[ NEW SCAN ]\n" + bcolors.ENDC)
    target = input(bcolors.WARNING + "> " + bcolors.ENDC + "Enter ip address: ").strip()


    def targetIP():
        global target

    try:
        hostname = socket.gethostbyaddr(str(target))

        print(
            bcolors.OKBLUE + "\n[ 1 ]" + bcolors.ENDC + " Scan single port\n" +
            bcolors.OKBLUE + "[ 2 ]" + bcolors.ENDC + " Scan multiple port\n" +
            bcolors.OKBLUE + "[ 3 ]" + bcolors.ENDC + " Scan most used ports\n"
        )
        type = int(input(bcolors.WARNING + "> " + bcolors.ENDC + "Select scan type: "))

        if type == 1:
            port = int(input(bcolors.WARNING + "> " + bcolors.ENDC + "Select port: "))
        elif type == 2:
            start = int(input(bcolors.WARNING + "> " + bcolors.ENDC + "Select start port: "))
            end = int(input(bcolors.WARNING + "> " + bcolors.ENDC + "Select end port: "))
        elif type == 3:
            port = (21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 1433, 1521, 2082, 2083, 2086, 2087, 2222, 3306, 3389, 7080, 8083, 8090, 8443, 8447, 8880, 10000)
        else:
            print(bcolors.FAIL + "Type is not selected, program exited." + bcolors.ENDC)
            sys.exit()

        targetIP()
        print("▬" * 20)
        print(bcolors.OKBLUE + "[ PORT SCAN INFO ]\n" + bcolors.ENDC)
        if type == 1:
            print(bcolors.WARNING + "[ " + str(port) + " ]" + bcolors.ENDC + " selected port.")
        elif type == 2:
            print(bcolors.WARNING + "[ " + str(start) + "-" + str(end) + " ]" + bcolors.ENDC + " selected ports.")
        else:
            print(bcolors.WARNING + "[ 21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 1433, 1521, 2082, 2083, 2086, 2087, 2222, 3306, 3389, 7080, 8083, 8090, 8443, 8447, 8880, 10000 ]" + bcolors.ENDC + " selected ports.")
        print(bcolors.WARNING + "[ " + str(target) + " ] " + bcolors.ENDC + "selected ip.")
        print(bcolors.WARNING + "[ " + str(hostname[0]) + " ] " + bcolors.ENDC + "hostname.")
        print("▬" * 20)
        print(bcolors.OKBLUE + "[ PORT SCAN RESULT ]\n" + bcolors.ENDC)

        if type == 1:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(config.timeout)
            result = s.connect_ex((target, port))
            if result == 0:
                print(bcolors.OKGREEN + "Port {} is open".format(port) + bcolors.ENDC)
            elif result != 0:
                print(bcolors.FAIL + "Port {} is closed".format(port) + bcolors.ENDC)
            s.close()
        elif type == 2:
            for port in range(int(start), int(end)):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(config.timeout)

                result = s.connect_ex((target, port))
                if result == 0:
                    openport.append(port)
                s.close()
            if len(openport) != 0:
                print("Total " + bcolors.OKBLUE + str(
                    len(openport)) + bcolors.ENDC + " ports open.\nPorts: " + bcolors.OKGREEN + str(
                    openport) + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "All ports closed" + bcolors.ENDC)
        else:
            for ports in port:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(config.timeout)

                result = s.connect_ex((target, ports))
                if result == 0:
                    openport.append(ports)
                s.close()
            if len(openport) != 0:
                print("Total " + bcolors.OKBLUE + str(
                    len(openport)) + bcolors.ENDC + " ports open.\nPorts: " + bcolors.OKGREEN + str(
                    openport) + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "All ports closed" + bcolors.ENDC)

    except socket.gaierror:
        print(bcolors.FAIL + "Hostname could not be resolved!" + bcolors.ENDC)
    except socket.error:
        print(bcolors.FAIL + "Server not responding!" + bcolors.ENDC)
    except ValueError:
        print(bcolors.FAIL + "Error!" + bcolors.ENDC)
    print("▬" * 50)
    openport.clear()

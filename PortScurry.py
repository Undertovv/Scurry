#Крыса была здесь

#Simple port scanner
from socket import *

if __name__ == "__main__":
    target = str(input("Target IP: "))
    #target = input("Enter target IP or hostname: ")
    tip = gethostbyname(target) #socket function, allows ip input as string
    print("Scanning...", tip)

    for i in range(22, 1000):
        s = socket(AF_INET, SOCK_STREAM) #Scans ports 50-499
        conn = s.connect_ex((tip, i))
        #Iterates through ports using i 
        if (conn == 0):
            print("Port%d: OPEN"%(i,)) #throws out open or closed for all ports in the loop

s.close()
 

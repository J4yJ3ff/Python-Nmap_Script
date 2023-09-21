import nmap;


scanner = nmap.PortScanner()


print("Toxic Python-Nmap Script software version 0.1")
print("/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-\/-.-")


url = input("Enter IP to scan:")
print("You have entered " + url + " " + "as the scan IP")


resp = int("""" Please enter the scan type \n
            1. Syn Ack
            2. UDP
            3. Comprehensive scan
            4. 
            """")
print("You've selected option: ", resp);

 if resp == "1":
    

port = input("Enter the port to scan:")

report = scanner.scan(url, port)

print(report)
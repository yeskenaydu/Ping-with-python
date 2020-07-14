from socket import *
import datetime
import time

with open('targethosts.txt')as dosya:
    bol = dosya.read()
    bol = bol.splitlines()
    port = 12345

for ip in bol: #ip bizim o an kullandığımız ip
    
    for j in range(0,5): #j ise o ip ye göndereceğimiz 5 denemenin kaçıncısı olduğunu belirtiyor
        
        print ("#",j+1,". Hedef: ",ip)
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.settimeout(1) #gecikme 1 saniyeyi geçmemeye ayarlandı.
        
        adres = (ip,port) # gönderilecek adres belirtiliyor
        
        mesaj = "ping"
        bytemesaj = bytes(mesaj, "utf-8") #mesaj bytle şekline dönüştürülüyor
        
        try:
            print("-> UDP: ",ip)
            ilk = datetime.datetime.now()
            clientSocket.sendto(bytemesaj,adres)
            data, server = clientSocket.recvfrom(4096)
            son = datetime.datetime.now()
            ms = son-ilk
            print ("<- RTT: ",round(ms.microseconds/100),"ms")
        except timeout :
            print("Time out")
        except :
            print("Paket Kaybı")
        
        
        
        

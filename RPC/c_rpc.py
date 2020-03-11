import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Print semua operasi yang dapat dilakukan
print(s.system.listMethods())
print("--------------------")
#Eksekusi
asal = str(input("Asal  = "))
tujuan = str(input("Tujuan = "))
print("Asal=",asal)
print("Tujuan =",tujuan)
print()

print("boarding : ",s.inboard(asal,tujuan))
print("Transit : ",s.insit(asal,tujuan))

#s.close()
import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Print semua operasi yang dapat dilakukan
print(s.system.listMethods())
print("----------------------------------------")
#Eksekusi
no = str(input("Nomor Penerbangan  = "))

print("Nomor Penerbangan=",no)

print()

print("asal : ",s.asal(no))
print("Tujuan : ",s.tujuan(no))
print("boarding : ",s.inboard(no))
print("Transit : ",s.insit(no))


#s.close()
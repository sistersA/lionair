import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.43.109:8000')

n=1
while(n!=0):
	print("DAFTAR MENU")
	print("1. INSERT PENERBANGAN BARU")
	print("2. EDIT PENERBANGAN")
	print("0. Exit")
	n = int(input("Pilihan="))

	if(n==1):
		print("========Input Baru Penerbangan======")
		c=True
		while(c==True):
			no = str(input("No. Penerbangan  = "))
			asal = str(input("Asal  = "))
			tujuan = str(input("Tujuan = "))
			transit = str(input("Transit  = "))
			boarding = str(input("Boarding = "))
			print()
			print(s.insert(no,asal,tujuan,transit,boarding))
			a = str(input("Input Lagi(Y/N)?"))
			if(a=="Y"):
				c=True
			else:
    			        c=False
			print("==================================================")
	elif(n==2):
		info = s.DaftarPenerbangan()
		print("================Edit Penerbangan=============")
		print()
		no = str(input("No. Penerbangan  = "))
		for i in range(0,len(info)):
			if(info[i][0]==no):
				print("DAFTAR EDIT")
				print("1. Edit Asal")
				print("2. Edit Tujuan")
				print("3. Edit Transit")
				print("4. Edit Boarding")
				print("0. Kembali")
				k = int(input("Pilihan="))
				if(k==1):
					info[i][1] = input("Asal :")
				elif(k==2):
					info[i][2] = input("Tujuan :")
				elif(k==3):
					info[i][3] = input("Transit :")
				elif(k==4):
					info[i][4] = input("Boarding :")
				print()
				print(s.updatePenerbangan(no,info[i][1],info[i][2],info[i][3],info[i][4]))



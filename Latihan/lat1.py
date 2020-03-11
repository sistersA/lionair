print "Selamat datang di Program Biodata"
print "================================="

# Ambil input dari user
nama = raw_input("Nama: ")
umur = input("Umur: ")
alamat = raw_input("Alamat: ")

# format teks
teks = "Nama: {}\nUmur: {}\nAlamat: {}".format(nama, umur, alamat)

# buka file untuk ditulis
file_bio = open("biodata.txt", "w")

# tulis teks ke file
file_bio.write(teks)

# tutup file
file_bio.close()
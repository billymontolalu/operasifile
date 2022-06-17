mahasiswa = "Royzaldo Azher#12345#1999-01-01"
hasil_split = mahasiswa.split("#")
nama_mahasiswa = hasil_split[0]
nim_mahasiswa = hasil_split[1]
tanggal_lahir = hasil_split[2]
print(tanggal_lahir)

#f = open("test.txt", "r")
#seluruh = f.readlines()
#print(seluruh)
#f.close()
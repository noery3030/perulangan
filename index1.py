# # membuat program biodata

# #membuat variabel nama_saya yng menerima inputan
# nama_lengkap = input("Masukan Nama Lengkap : ")

# #mambuat variable asal_daerah yng menerima inputan
# asal_daerah = input("Asal Daerah : ")

# #membuat array bioadata untuk mengumpulkan hasil inputan
# biodata = [nama_lengkap, asal_daerah]

# no = 0
# for isi_bioadata in biodata :
#     print(biodata[no])
#     no = no + 1




# membuat array siswa
siswa =[]
# mambuat perulangan for
for i in range(3):
    #mengecek nilai index
    print("ini adalah index ke-", i)

    #menerima inputan nama
    nama_siswa = input("masukan nama siswa : ")

    #masukan hasil inputan nama ke array siswa
    siswa.append(nama_siswa)

for k in siswa:
    print("nama siswa : ", k)
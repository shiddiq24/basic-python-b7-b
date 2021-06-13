d = {
    "nama" : "shiddiq",
    "umur" : 18,
    "tinggi": 178
    #key     #value
}
print(d["nama"])    #print perkey
print(d)            #print semua
#perbarui
d["nama"]="kemsi"
print(d["nama"])

#loop
for x in range(1):
    nama = input("masukkan nama:")
    umur = int(input("masukkan umur anda:"))
    tinggi = float(input("masukkan tinggi badan anda"))
    data = {
        "nama" : nama,
        "umur" : umur,
        "tinggi": tinggi
    }
    d.append(data)
for i in d:
    print("Nama pelanggan :", i["nama"])
    print("Umur pelanggan :", i["umur"])
    print("Tinggi pelanggan:", i["tinggi"])

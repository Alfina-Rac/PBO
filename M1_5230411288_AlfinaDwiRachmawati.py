def hitungPersegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

def hitungPersegiPanjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def hitungLingkaran(jari_jari):
    luas = 3.14 * jari_jari * jari_jari
    keliling = 2 * 3.14 * jari_jari
    return luas, keliling

while True:
    print("Pilih bangun datar yang ingin anda hitung :")
    print("0. Keluar")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Lingkaran")

    pilihan = input("Masukkan pilihan : ")

    if pilihan == '0':
        print("Terima kasih telah menggunakan program ini.")

    elif pilihan == '1':
        sisi = int(input("Masukkan sisi : "))
        luas, keliling = hitungPersegi(sisi)
        print(f"Luas Persegi: {luas}")
        print(f"Keliling Persegi: {keliling}")

    elif pilihan == '2':
        panjang = int(input("Masukkan panjang persegi panjang: "))
        lebar = int(input("Masukkan lebar persegi panjang: "))
        luas, keliling = hitungPersegiPanjang(panjang, lebar)
        print(f"Luas Persegi Panjang: {luas}")
        print(f"Keliling persegi panjang: ")

    elif pilihan == '3':
        jari_jari = int(input("Masukkan jari-jari lingkaran: "))
        luas, keliling = hitungLingkaran(jari_jari)
        print(f"Luas Lingkaran: {luas}")
        print(f"Keliling Lingkaran: {keliling}")

    else:
        print("Pilihan tidak tersedia")

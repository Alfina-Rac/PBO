class MenuMakanan:
    def __init__(self):
        self.daftarMakanan = []

    def tambahMakanan(self, namaMakanan, harga):
        self.daftarMakanan.append({'nama': namaMakanan, 'harga': harga})

    def tampilkanMenu(self):
        if not self.daftarMakanan:
            print("Belum ada makanan di daftar menu.")
        else:
            print("\nDaftar Menu Makanan:")
            for makanan in self.daftarMakanan:
                print(f"{makanan['nama']} - Rp{makanan['harga']}")


class MenuMinuman:
    def __init__(self):
        self.daftarMinuman = []

    def tambahMinuman(self, namaMinuman, harga):
        self.daftarMinuman.append({'nama': namaMinuman, 'harga': harga})

    def tampilkanMenu(self):
        if not self.daftarMinuman:
            print("Belum ada minuman di daftar menu.")
        else:
            print("\nDaftar Menu Minuman:")
            for minuman in self.daftarMinuman:
                print(f"{minuman['nama']} - Rp{minuman['harga']}")


menu_makanan = MenuMakanan()
menu_minuman = MenuMinuman()

def input_nama_makanan():
    while True:
        namaMakanan = input("Masukkan nama makanan: ")
        try:
            # Cek jika nama makanan mengandung angka
            if any(char.isdigit() for char in namaMakanan):
                raise ValueError("Nama makanan tidak boleh mengandung angka.")
            return namaMakanan
        except ValueError as ve:
            print(ve)

def input_nama_minuman():
    while True:
        namaMinuman = input("Masukkan nama minuman: ")
        try:
            if any(char.isdigit() for char in namaMinuman):
                raise ValueError("Nama minuman tidak boleh mengandung angka.")
            return namaMinuman
        except ValueError as ve:
            print(ve)

while True:
    print("\n=====DAFTAR MENU=====")
    print("0. Keluar")
    print("1. Lihat Daftar Makanan")
    print("2. Lihat Daftar Minuman")
    print("3. Tambah Daftar")

    pilihan = input("Masukkan Pilihan Menu: ")

    if pilihan == '0':
        print("Anda telah berhasil keluar.")
        break
    
    elif pilihan == '1':
        menu_makanan.tampilkanMenu()

    elif pilihan == '2':
        menu_minuman.tampilkanMenu()
    
    elif pilihan == '3':
        while True:
            print("\n====TAMBAH DAFTAR====")
            print("0. Kembali ke Menu Utama")
            print("1. Tambah Makanan")
            print("2. Tambah Minuman")

            pilihan = input("Masukkan pilihan submenu: ")

            if pilihan == '0':
                break

            elif pilihan == '1':
                while True:
                    namaMakanan = input_nama_makanan()
                    if namaMakanan.isalpha():
                        break
                    else:
                        print("Nama makanan tidak valid.")

                while True:
                    try:     
                        hargaMakanan = float(input("Masukkan harga makanan: "))
                        break
                    except ValueError:
                        print("Harga tidak valid.")

                    menu_makanan.tambahMakanan(namaMakanan, hargaMakanan)
                    print(f"{namaMakanan} berhasil ditambahkan ke menu makanan.")

            elif pilihan == '2':
                while True:
                    namaMinuman = input_nama_minuman()
                    if namaMakanan.isalpha():
                        break
                    else:
                        print("Nama makanan tidak valid.")

                while True:
                    try:
                        hargaMinuman = float(input("Masukkan harga minuman: "))
                        break
                    except ValueError:
                        print("Harga tidak valid.")
                menu_minuman.tambahMinuman(namaMinuman, hargaMinuman)
                print(f"{namaMinuman} berhasil ditambahkan ke menu minuman.")
            
            else:
                print("Pilihan tidak valid.")
    
    else:
        print("Pilihan tidak valid.")

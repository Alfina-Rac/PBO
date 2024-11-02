class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat

class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga

class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, "Snack", harga)

class Makanan(Produk):
    def __init__(self, kode_produk, nama_makanan, harga):
        super().__init__(kode_produk, nama_makanan, "Makanan", harga)

class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga):
        super().__init__(kode_produk, nama_minuman, "Minuman", harga)

class Transaksi:
    def __init__(self, no_transaksi, pegawai):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.produk_dibeli = []  # List untuk menyimpan produk dan jumlahnya
        self.total_harga = 0

    def tambah_produk(self, produk, jumlah_produk):
        self.produk_dibeli.append((produk, jumlah_produk))
        self.total_harga += produk.harga * jumlah_produk

class Struk:
    def __init__(self, transaksi):
        self.transaksi = transaksi

    def cetak_struk(self):
        print("\n--- Struk Transaksi ---")
        print(f"No Transaksi: {self.transaksi.no_transaksi}")
        print(f"Pegawai: {self.transaksi.pegawai.nama}")
        print("Produk yang dibeli:")
        for produk, jumlah in self.transaksi.produk_dibeli:
            print(f"- {produk.nama_produk} ({produk.jenis_produk}), Harga: Rp{produk.harga}, Jumlah: {jumlah}")
        print(f"Total Harga: Rp{self.transaksi.total_harga}")
        print("------------------------\n")

# Data lists
pegawai_list = []
produk_list = []
transaksi_list = []

# Main menu loop
while True:
    print("\nMenu:")
    print("1. Tambah Pegawai")
    print("2. Tambah Produk")
    print("3. Lakukan Transaksi")
    print("4. Cetak Struk")
    print("5. Keluar")
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        nik = input("Masukkan NIK Pegawai: ")
        nama = input("Masukkan Nama Pegawai: ")
        alamat = input("Masukkan Alamat Pegawai: ")
        pegawai = Pegawai(nik, nama, alamat)
        pegawai_list.append(pegawai)
        print("Pegawai berhasil ditambahkan.")
    
    elif pilihan == "2":
        print("\nJenis Produk:")
        print("1. Snack")
        print("2. Makanan")
        print("3. Minuman")
        jenis_produk = input("Pilih jenis produk: ")
        kode_produk = input("Masukkan Kode Produk: ")
        nama_produk = input("Masukkan Nama Produk: ")
        harga = int(input("Masukkan Harga Produk: "))
        
        if jenis_produk == "1":
            produk = Snack(kode_produk, nama_produk, harga)
        elif jenis_produk == "2":
            produk = Makanan(kode_produk, nama_produk, harga)
        elif jenis_produk == "3":
            produk = Minuman(kode_produk, nama_produk, harga)
        else:
            print("Jenis produk tidak valid.")
            continue
        
        produk_list.append(produk)
        print("Produk berhasil ditambahkan.")
    
    elif pilihan == "3":
        if not pegawai_list or not produk_list:
            print("Pegawai atau produk belum ada. Harap tambahkan terlebih dahulu.")
            continue
        
        no_transaksi = input("Masukkan No Transaksi: ")
        print("\nPilih Pegawai:")
        for i, p in enumerate(pegawai_list):
            print(f"{i + 1}. {p.nama}")
        pegawai_index = int(input("Pilih pegawai: ")) - 1
        pegawai = pegawai_list[pegawai_index]
        
        transaksi = Transaksi(no_transaksi, pegawai)
        
        while True:
            print("\nPilih Produk (Ketik 's' untuk selesai):")
            for i, p in enumerate(produk_list):
                print(f"{i + 1}. {p.nama_produk} - {p.jenis_produk} - Rp{p.harga}")
            produk_input = input("Pilih produk atau 's' untuk selesai: ")
            
            if produk_input.lower() == 's':
                break
            
            try:
                produk_index = int(produk_input) - 1
                produk = produk_list[produk_index]
                jumlah_produk = int(input("Masukkan Jumlah Produk: "))
                transaksi.tambah_produk(produk, jumlah_produk)
                print(f"{produk.nama_produk} sebanyak {jumlah_produk} berhasil ditambahkan ke transaksi.")
            except (IndexError, ValueError):
                print("Pilihan produk tidak valid.")
        
        transaksi_list.append(transaksi)
        print("Transaksi berhasil dilakukan.")
    
    elif pilihan == "4":
        if not transaksi_list:
            print("Belum ada transaksi.")
            continue
        
        for transaksi in transaksi_list:
            struk = Struk(transaksi)
            struk.cetak_struk()
    
    elif pilihan == "5":
        print("Terima kasih!")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

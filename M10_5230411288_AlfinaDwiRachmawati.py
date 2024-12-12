import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="penjualan"
)
cursor = conn.cursor()

# Buat database dan tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS Pegawai (
    nik VARCHAR(20) PRIMARY KEY,
    nama VARCHAR(255),
    alamat TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Produk (
    kode_produk INT PRIMARY KEY AUTO_INCREMENT,
    nama_produk VARCHAR(255),
    jenis_produk VARCHAR(50),
    harga DECIMAL(10, 2)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Transaksi (
    no_transaksi INT PRIMARY KEY AUTO_INCREMENT,
    nik VARCHAR(20),
    tanggal DATE,
    FOREIGN KEY (nik) REFERENCES Pegawai(nik)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Detail_Transaksi (
    id_detail INT PRIMARY KEY AUTO_INCREMENT,
    no_transaksi INT,
    kode_produk INT,
    jumlah INT,
    total_harga DECIMAL(10, 2),
    FOREIGN KEY (no_transaksi) REFERENCES Transaksi(no_transaksi),
    FOREIGN KEY (kode_produk) REFERENCES Produk(kode_produk)
)
""")

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
        cursor.execute("INSERT INTO Pegawai (nik, nama, alamat) VALUES (%s, %s, %s)", (nik, nama, alamat))
        conn.commit()
        print("Pegawai berhasil ditambahkan.")
    
    elif pilihan == "2":
        print("\nJenis Produk:")
        print("1. Snack")
        print("2. Makanan")
        print("3. Minuman")
        jenis_produk = input("Pilih jenis produk: ")
        nama_produk = input("Masukkan Nama Produk: ")
        harga = float(input("Masukkan Harga Produk: "))

        if jenis_produk == "1":
            jenis = "Snack"
        elif jenis_produk == "2":
            jenis = "Makanan"
        elif jenis_produk == "3":
            jenis = "Minuman"
        else:
            print("Jenis produk tidak valid.")
            continue

        cursor.execute("INSERT INTO Produk (nama_produk, jenis_produk, harga) VALUES (%s, %s, %s)", (nama_produk, jenis, harga))
        conn.commit()
        print("Produk berhasil ditambahkan.")
    
    elif pilihan == "3":
        nik = input("Masukkan NIK Pegawai yang melakukan transaksi: ")
        cursor.execute("INSERT INTO Transaksi (nik, tanggal) VALUES (%s, CURDATE())", (nik,))
        conn.commit()
        no_transaksi = cursor.lastrowid

        while True:
            print("\nPilih Produk (Ketik 's' untuk selesai):")
            cursor.execute("SELECT * FROM Produk")
            produk_list = cursor.fetchall()
            for p in produk_list:
                print(f"{p[0]}. {p[1]} - {p[2]} - Rp{p[3]}")

            produk_input = input("Pilih kode produk atau 's' untuk selesai: ")

            if produk_input.lower() == 's':
                break

            try:
                kode_produk = int(produk_input)
                jumlah = int(input("Masukkan Jumlah Produk: "))
                cursor.execute("SELECT harga FROM Produk WHERE kode_produk = %s", (kode_produk,))
                harga = cursor.fetchone()[0]
                total_harga = harga * jumlah

                cursor.execute("INSERT INTO Detail_Transaksi (no_transaksi, kode_produk, jumlah, total_harga) VALUES (%s, %s, %s, %s)", (no_transaksi, kode_produk, jumlah, total_harga))
                conn.commit()

                print(f"Produk dengan kode {kode_produk} sebanyak {jumlah} berhasil ditambahkan ke transaksi.")
            except (ValueError, TypeError):
                print("Input tidak valid.")
    
    elif pilihan == "4":
        no_transaksi = input("Masukkan No Transaksi yang ingin dicetak: ")
        cursor.execute("""
        SELECT t.no_transaksi, t.tanggal, p.nama, d.jumlah, pr.nama_produk, pr.jenis_produk, d.total_harga
        FROM Transaksi t
        JOIN Detail_Transaksi d ON t.no_transaksi = d.no_transaksi
        JOIN Pegawai p ON t.nik = p.nik
        JOIN Produk pr ON d.kode_produk = pr.kode_produk
        WHERE t.no_transaksi = %s
        """, (no_transaksi,))

        transaksi = cursor.fetchall()
        if not transaksi:
            print("Transaksi tidak ditemukan.")
            continue

        print("\n--- Struk Transaksi ---")
        print(f"No Transaksi: {transaksi[0][0]}")
        print(f"Tanggal: {transaksi[0][1]}")
        print(f"Pegawai: {transaksi[0][2]}")
        print("Produk yang dibeli:")
        for t in transaksi:
            print(f"- {t[4]} ({t[5]}), Jumlah: {t[3]}, Total Harga: Rp{t[6]}")
        print("------------------------")
    
    elif pilihan == "5":
        print("Terima kasih!")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

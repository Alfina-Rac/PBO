while True:
    print(f"\nPROGRAM CEK BILANGAN")
    print("1. Bilangan Prima")
    print("2. Bilangan Ganjil")
    print("3. Bilangan Genap")
    print("4. Keluar")

    pilihan = input("Pilihan Menu: ")

    if pilihan == '1':
        bilanganAwal = int(input("Masukkan Bilangan Awal: "))
        bilanganAkhir = int(input("Masukkan Bilangan Akhir: "))
        print(f"Bilangan Prima: {bilanganAwal} sampai {bilanganAkhir}")
        for bilangan in range(bilanganAwal, bilanganAkhir + 1):
            prima = True
            for i in range(2, bilangan):
                if bilangan % i == 0:
                    prima = False
                    break
            if prima:
                print(bilangan, end=' ')
    elif pilihan == '2': 
        bilanganAwal = int(input("Masukkan Bilangan Awal: "))
        bilanganAkhir = int(input("Masukkan Bilangan: "))
        print(f"Bilangan Ganjil: {bilanganAwal} sampai {bilanganAkhir}")
        for bilangan in range(bilanganAwal, bilanganAkhir + 1):
            if bilangan % 2 != 0:
                print(bilangan, end=' ')
    elif pilihan == '3':
        bilanganAwal = int(input("Masukkan Bilangan Awal: "))
        bilanganAkhir = int(input("Masukkan Bilangan: "))
        print(f"Bilangan Genap: {bilanganAwal} sa mpai {bilanganAkhir}")
        for bilangan in range(bilanganAwal, bilanganAkhir + 1):
            if bilangan % 2 == 0:
                print(bilangan, end=' ')
    elif pilihan == '4':
        print("Berhasil keluar.")
        break
    else:
        print("Pilihan tidak valid.")
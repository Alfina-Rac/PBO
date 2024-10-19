class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def tambahMusik(musicList, genre):
        judul = input("Masukkan judul musik: ")
        penyanyi = input("Masukkan nama penyanyi: ")
        musik_baru = Music(judul, penyanyi, genre)
        musicList.append(musik_baru)
        print(f"Musik '{judul}' berhasil ditambahkan.\n")

    def DisplayAll(musicList):
        if not musicList:
            print("Tidak ada musik yang tersedia.")
        else:
            musicList.sort(key=lambda musik: musik.judul)
            print("\nDaftar Musik:")
            for musik in musicList:
                print(f"Judul: {musik.judul}, Penyanyi: {musik.penyanyi}, Genre: {musik.genre}")
        print()

    def DeleteMusic(musicList):
        judul = input("Masukkan judul musik yang ingin dihapus: ")
        for i in range(len(musicList)):
            if musicList[i].judul == judul:
                del musicList[i]
                print(f"Musik dengan judul '{judul}' telah dihapus.\n")
                return
        print(f"Musik dengan judul '{judul}' tidak ditemukan.\n")

    def SearchMusic(musicList):
        penyanyi_dicari = input("\nMasukkan Penyanyi yang Ingin Dicari: ")
        print(f"\nJudul {'Penyanyi':<20} {'Genre':<20}")
        print("="*60)
        found = False
        for musik in musicList:
            if musik.penyanyi.lower() == penyanyi_dicari.lower():
                print(f"{musik.judul:<20} {musik.penyanyi:<20} {musik.genre:<20}")
                found = True
        if not found:
            print("Lagu tidak ditemukan.")
        input("\nTekan Enter untuk melanjutkan...")


def main():
    musicList = [
        Music("Sambalado", "Ayu Ting-ting", "I-Song"),
        Music("Cantik", "Kahitna", "I-Song"),
        Music("Sayap Pelindungmu", "The Overtunes", "I-Song"),
        Music("Bang Jono", "Zaskia Gotik", "I-Song"),
        Music("Meriang", "Cita Citata", "I-Song"),
        Music("Bona Bona", "TREASURE", "K-Song"),
        Music("Hot", "SEVENTEEN", "K-Song"),
        Music("Give Love", "AKMU", "K-Song"),
        Music("Where The Sea Sleeps", "DAY-6", "K-Song"),
        Music("Congratulation", "DAY-6", "K-Song"),
        Music("18", "One Direction", "English"),
        Music("ONE MORE TIME", "Blink-182", "English"),
        Music("Vapor", "5 Second of Summer", "English"),
        Music("Pretty Boy", "The Neighbourhood", "English"),
        Music("Robbers", "The 1975", "English")
    ]

    while True:
        print("================ Playlist Music ================")
        print("0. Exit")
        print("1. Indonesian Song")
        print("2. Korean Song")
        print("3. English Song")
        print("4. Display All")
        print("5. Search Music")
        print("6. Delete Music")

        pilihan = input("Masukkan Pilihan Menu: ")

        if pilihan == '0':
            break

        elif pilihan == '1':
            while True:
                print("\nIndonesian Songs Menu:")
                print("0. Kembali")
                print("1. Tampilkan Lagu")
                print("2. Tambah Lagu")
                sub_pilihan = input("Masukkan Pilihan: ")

                if sub_pilihan == '0':
                    break
                elif sub_pilihan == '1':
                    indonesian_songs = [m for m in musicList if "I-Song" in m.genre]
                    Music.DisplayAll(indonesian_songs)
                elif sub_pilihan == '2':
                    genre = 'I-Song'
                    Music.tambahMusik(musicList, genre)
                    

        elif pilihan == '2':
            while True:
                print("\nKorean Songs Menu:")
                print("0. Kembali")
                print("1. Tampilkan Lagu")
                print("2. Tambah Lagu")
                sub_pilihan = input("Masukkan Pilihan: ")

                if sub_pilihan == '0':
                    break
                elif sub_pilihan == '1':
                    korean_songs = [m for m in musicList if "K-Song" in m.genre]
                    Music.DisplayAll(korean_songs)
                elif sub_pilihan == '2':
                    genre = 'K-Song'
                    Music.tambahMusik(musicList, genre)

        elif pilihan == '3':
            while True:
                print("\nEnglish Songs Menu:")
                print("0. Kembali")
                print("1. Tampilkan Lagu")
                print("2. Tambah Lagu")
                sub_pilihan = input("Masukkan Pilihan: ")

                if sub_pilihan == '0':
                    break
                elif sub_pilihan == '1':
                    english_songs = [m for m in musicList if "English" in m.genre]
                    Music.DisplayAll(english_songs)
                elif sub_pilihan == '2':
                    genre = 'English'
                    Music.tambahMusik(musicList, genre)

        elif pilihan == '4':
            Music.DisplayAll(musicList)

        elif pilihan == '5':
            Music.SearchMusic(musicList)

        elif pilihan == '6':
            Music.DeleteMusic(musicList)


if __name__ == "__main__":
    main()

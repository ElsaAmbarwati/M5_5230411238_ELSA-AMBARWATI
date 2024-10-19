class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

daftar_English = [
    Music("deja vu", "Olivia Rodrigo", "pop"),
    Music("vampire", "Olivia Rodrigo", "pop rok"),
    Music("traitor", "Olivia Rodrigo", "pop"),
    Music("drivers license", "Olivia Rodrigo", "pop"),
    Music("good 4 u", "Olivia Rodrigo", "pop"),
]

daftar_korean = [
    Music("butter", "BTS", "k-pop"),
    Music("fake love", "BTS", "K-pop"),
    Music("sudden shower", "ECLIPSE", "k-pop"),
    Music("dream for you", "X1", "k-pop"),
    Music("flash", "X1", "k-pop"),
]

daftar_Indonesian = [
    Music("surat cinta", "virgoun", "pop"),
    Music("satu bulan", "Bernadya", "pop"),
    Music("Apa mungkin", "Bernadya", "pop"),
    Music("Kata mereka", "Bernadya", "pop"),
    Music("Kini mereka tahu", "Bernadya", "pop"),
]

def tampilkan_menu():
    print("=============== MENU MUSIC ===============")
    print("1. English Song")
    print("2. Korean Song")
    print("3. Indonesian Song")
    print("4. Display All")
    print("5. Search Music") 
    print("0. keluar")   
    pilihan = input("Masukan Pilihan Menu: ")
    return pilihan

def tampilkan_lagu(daftar):
    print("{:<20} {:<25} {:<20}".format("Judul", "Penyanyi", "Genre"))
    for music in daftar:
        print("{:<20} {:<25} {:<20}".format(music.judul, music.penyanyi, music.genre))

def cari_lagu(judul):
    found = False
    print("{:<20} {:<25} {:<20}".format("Judul", "Penyanyi", "Genre"))       
    for music in judul:
            if music.judul.lower() == judul.lower():
                print(f"Ditemukan: {music.judul} Penyanyi: {music.penyanyi} Genre: {music.genre}")
                found = True
                break
    if not found:
        print("Lagu tidak ditemukan.")

def cari_lagu_berdasarkan_penyanyi(penyanyi):
    found = False
    for daftar in [daftar_English, daftar_korean, daftar_Indonesian]:
        for music in daftar:
            if music.penyanyi.lower() == penyanyi.lower():
                if not found:
                    print("{:<20} {:<25} {:<20}".format("Judul", "Penyanyi", "Genre"))
                print("{:<20} {:<25} {:<20}".format(music.judul, music.penyanyi, music.genre))
                found = True
    if not found:
        print("Penyanyi tidak ditemukan.")

def English_song():
    while True:
        print("=============== English Song ===============")
        print("1. Display All")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Kembali")
        sub_menu = input("Masukan Pilihan Sub Menu English Song : ")

        if sub_menu == '1':
            print("=============== List English Song ===============")
            tampilkan_lagu(daftar_English)

        elif sub_menu == '2':
            judul = input("Masukkan Judul: ")
            penyanyi = input("Masukkan Nama Penyanyi: ")
            genre = input("Masukkan Genre: ")
            daftar_English.append(Music(judul, penyanyi, genre))
            print("Lagu berhasil ditambahkan!")

        elif sub_menu == '3':
            judul = input("Masukkan Judul yang ingin dihapus: ")
            for music in daftar_English:
                if music.judul.lower() == judul.lower():
                    daftar_English.remove(music)
                    print("Lagu berhasil dihapus!")
                    break
            else:
                print("Lagu tidak ditemukan.")

        elif sub_menu == '0':
            break

def Korean_song():
    while True:
        print("=============== Korean Song ===============")
        print("1. Display All")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Kembali")
        sub_menu = input("Masukan Pilihan Sub Menu Korean Song : ")

        if sub_menu == '1':
            print("=============== List Korean Song ===============")
            tampilkan_lagu(daftar_korean)

        elif sub_menu == '2':
            judul = input("Masukkan Judul: ")
            penyanyi = input("Masukkan Nama Penyanyi: ")
            genre = input("Masukkan Genre: ")
            daftar_korean.append(Music(judul, penyanyi, genre))
            print("Lagu berhasil ditambahkan!")

        elif sub_menu == '3':
            judul = input("Masukkan Judul yang ingin dihapus: ")
            for music in daftar_korean:
                if music.judul.lower() == judul.lower():
                    daftar_korean.remove(music)
                    print("Lagu berhasil dihapus!")
                    break
            else:
                print("Lagu tidak ditemukan.")

        elif sub_menu == '0':
            break

def Indonesian_song():
    while True:
        print("=============== Indonesian Song ===============")
        print("1. Display All")
        print("2. Add Song")
        print("3. Delete Song")
        print("0. Kembali")
        sub_menu = input("Masukan Pilihan Sub Menu Indonesian Song : ")

        if sub_menu == '1':
            print("=============== List Indonesian Song ===============")
            tampilkan_lagu(daftar_Indonesian)

        elif sub_menu == '2':
            judul = input("Masukkan Judul: ")
            penyanyi = input("Masukkan Nama Penyanyi: ")
            genre = input("Masukkan Genre: ")
            daftar_Indonesian.append(Music(judul, penyanyi, genre))
            print("Lagu berhasil ditambahkan!")

        elif sub_menu == '3':
            judul = input("Masukkan Judul yang ingin dihapus: ")
            for music in daftar_Indonesian:
                if music.judul.lower() == judul.lower():
                    daftar_Indonesian.remove(music)
                    print("Lagu berhasil dihapus!")
                    break
            else:
                print("Lagu tidak ditemukan.")

        elif sub_menu == '0':
            break

def main():
    while True:
        pilihan = tampilkan_menu()
        if pilihan == '1':
            English_song()
        elif pilihan == '2':
            Korean_song()
        elif pilihan == '3':
            Indonesian_song()
        elif pilihan == '4':
            print("=============== Display All Songs ===============")
            print("English Songs:")
            tampilkan_lagu(daftar_English)
            print("\nKorean Songs:")
            tampilkan_lagu(daftar_korean)
            print("\nIndonesian Songs:")
            tampilkan_lagu(daftar_Indonesian)
        elif pilihan == '5':
            penyanyi = input("Masukkan Nama Penyanyi yang ingin dicari: ")
            cari_lagu_berdasarkan_penyanyi(penyanyi)
        elif pilihan == '0':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

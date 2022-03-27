global f
f = 0

def NamaFilm():
    global f
    f = f+1
    print("Pilih Film")
    print("1. SuperJoke ")
    print("2. Murah Banget ")
    print("3. Lord Luhut")
    print("4. kembali <-")
    film = int(input("Pilih Film: "))
    if film == 4:
      prov()
      screen()
      return 0
    if f == 1:
      screen()

def screen():
    print("Pilih Screen Flim: ")
    print("1. 2D")
    print("2. 3D")
    print("3. 4D")
    a = int(input("Pilihan: "))
    tiket = int(input("Berapa tiket yang ingin anda beli?: "))
    jadwal(a)

def jadwal(a):
    time1 = {
        "1": "10.00-13.00",
        "2": "13.15-16.00",
        "3": "12.20-14.20",
        "4": "17.30-20.30"
    }
    time2 = {
        "1": "10.10-13.10",
        "2": "13.00-16.00",
        "3": "12.00-14.20",
        "4": "17.35-20.35"
    }
    time3 = {
        "1": "10.15-13.25",
        "2": "13.25-16.25",
        "3": "12.25-14.20",
        "4": "17.45-20.45"
    }
    if a == 1:
        print("Pilih Jadwal Waktu:")
        print(time1)
        t = input("Pilih:")
        x = time1[t]
        print("SUKSES!, TONTON PADA "+x)
    elif a == 2:
        print("Pilih Jadwal Waktu:")
        print(time2)
        t = input("Pilih:")
        x = time2[t]
        print("SUKSES!, TONTON PADA "+x)
    elif a == 3:
        print("Pilih Jadwal Waktu")
        print(time3)
        t = input("Pilih:")
        x = time3[t]
        print("SUKSES!, TONTON PADA "+x)
    return 0

def movie(a):
    if a == 1:
        NamaFilm()
    elif a  == 2:
         NamaFilm()
    elif a == 3:
        NamaFilm()
    elif a == 4:
        kota()
    else:
        print("TIDAK ADA DI PILIHAN MBLO")

def prov():
    print("Silahkan Pilih Provider ")
    print("1. XXI")
    print("2. CINEPOLIS")
    print("3. RAJAWALI")
    print("4. Kembali <-")
    a = int(input("Pilih : "))
    movie(a)
    return 0

def kota():
    print("Selamaat Datang !: ")
    print("Pilih Kota Anda:")
    print("1. Semarang")
    print("2. Bogor")
    print("3. Jakarta")
    kota = int(input("Pilih: "))
    if kota == 1:
      prov()
    elif kota == 2:
      prov()
    elif kota == 3:
      prov()
    else:
      print("BELUM TERSEDIA DI KOTA ANDA awikwok")

kota()
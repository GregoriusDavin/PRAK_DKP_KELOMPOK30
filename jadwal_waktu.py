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
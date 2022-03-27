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
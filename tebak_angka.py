def tebak_angka():    
    secret_number = 5
    guess = 0
    guess_count = 3
    gchange = 2

    while guess < guess_count:

        user = int(input("Tebak angka dari 1-15 : "))
        if int(user) == 5:
            print("selamat hoki tahunan mu sudah habis")
            break
        else:
            print(f"Silahkan coba lagi {gchange}")
            guess = guess + 1
            gchange = gchange - 1   
    else :
        print("Kesempatan sudah habis")
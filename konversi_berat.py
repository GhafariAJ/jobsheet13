def konversi_berat():    
    weight = int(input("Masukkan Berat Badan : "))
    types = input("Masukkan Satuan Kg(K) atau LBS(L) :")

    if(types == "K"):
        kg = weight * 0.453592
        print(f"Berat badan anda adalah {kg}K")
    elif(types == "L"):
        lbs = weight * 2.204623
        print(f"Berat badan anda adalah {lbs}L")
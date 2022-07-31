def volkubus(s):
    volume = s**3
    return volume

def volbalok(p, l, t):
    volume = p*l*t
    return volume

def volkerucut(la, t):
    volume = la*t
    return volume

def volbola(r):
    volume = 4/3*3.14*r**3
    return volume

print("MENU VOLUME BANGUN RUANG")
print("Silahkan pilih")
print("1. Volume Kubus")
print("2. Volume Balok")
print("3. Volume Kerucut")
print("4. Volume Bola")
pilihan = int(input("Masukkan pilihan : "))
if pilihan == 1:
    sisi = float(input("Masukkan sisi : "))
    hasil = volkubus(sisi)
    print("Volume kubus adalah", hasil)
elif pilihan == 2:
    panjang = float(input("Masukkan panjang : "))
    lebar = float(input("Masukkan lebar : "))
    tinggi = float(input("Masukkan tinggi : "))
    hasil = volbalok(panjang, lebar, tinggi)
    print("Volume balok adalah", hasil)
elif pilihan == 3:
    luas_alas = float(input("Masukkan luas alas : "))
    tinggi = float(input("Masukkan tinggi : "))
    hasil = volkerucut(luas_alas, tinggi)
    print("Volume kerucut adalah", hasil)
elif pilihan == 4:
    jari_jari = float(input("Masukkan jari-jari : "))
    hasil = volbola(jari_jari)
    print("Volume bola adalah", hasil)
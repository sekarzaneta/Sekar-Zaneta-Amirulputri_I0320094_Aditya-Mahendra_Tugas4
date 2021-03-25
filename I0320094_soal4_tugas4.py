print("===== Daftar Kursus Online =====")

usia = int(input("Berapa usia kamu? "))
lulus = input("Apakah Anda sudah lulus ujian kualifikasi (y / t)? ")

if usia >= 21 :
    if lulus == "y" :
        print("Anda dapat mendaftar di kursus")
    else :
        print("Anda tidak dapat mendaftar di kursus")
else :
    print("Anda tidak dapat mendaftar di kursus")

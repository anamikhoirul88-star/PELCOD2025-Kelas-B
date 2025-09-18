# Program menghitung nilai akhir Algoritma Pemrograman (dengan predikat huruf + status kelulusan)

# Meminta input nilai dari user
nilai_tugas = float(input("Masukkan nilai Tugas anda disini: "))
nilai_uts = float(input("Masukkan nilai UTS anda disini: "))
nilai_uas = float(input("Masukkan nilai UAS anda disini: "))

# Bobot penilaian
bobot_tugas = 0.30
bobot_uts = 0.30
bobot_uas = 0.40

# rumus menghitung nilai akhir
nilai_akhir = (nilai_tugas * bobot_tugas) + (nilai_uts * bobot_uts) + (nilai_uas * bobot_uas)

# Tentukan predikat huruf
if nilai_akhir >= 80:
    predikat = "A (Baik sekali)"
elif nilai_akhir >= 70:
    predikat = "B (Baik)"
elif nilai_akhir >= 60:
    predikat = "C (Cukup)"
elif nilai_akhir >= 50:
    predikat = "D (Buruk)"
else:
    predikat = "E (Buruk sekali)"

# Tentukan status kelulusan
if nilai_akhir >= 60:
    status = "SELAMAT ANDA DINYATAKAN LULUS "
else:
    status = "SELAMAT ANDA DINYATAKAN TIDAK LULUS "

# Tampilkan hasil
print("Nilai Akhir Anda adalah:", nilai_akhir)
print("Predikat Huruf:", predikat)
print("Status:", status)

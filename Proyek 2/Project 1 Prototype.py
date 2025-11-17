# ==========================================================
# SISTEM PARKIR OTOMATIS
# Fitur:
#  - Input kendaraan masuk
#  - Hitung biaya parkir berdasarkan jenis kendaraan & waktu
#  - Maksimum 50 slot
# ==========================================================

import math


dataWaktuKendaraan = ["0" for i in range(50)] # array ini menyimpan waktu masuk kendaraan. Nilai default semuanya 0.
dataJenisKendaraan = ["0" for j in range(50)] # array ini menyimpan jenis kendaraan. Nilai default semuanya "0".

nomorTiket = 0
waktuKeluar = 0
slotTerisi = 0

# Harga maximum dan tarif masing-masing kendaraan. Bisa diubah2 secara dinamis daripada hardcoded.
maksMobil = 10000
maksMotor = 10000
tarifMobil = 2000
tarifMotor = 1000
tarifBus = 20000

#Fungsi yang mengkonversi string "00:00" menjadi menit yang mudah diproses.
def konversiWaktu(strWaktu):
   jamKeMenit = (int(strWaktu[0:2])) * 60
   menit = int(strWaktu[3:])
   return jamKeMenit + menit


def kendaraanMasuk():
  # Disini kode input data kendaraan yang masuk
  global slotTerisi
  for k in range(50):
    if dataWaktuKendaraan[k] == "0": # 0 adalah nilai default dataWaktuKendaraan. Artinya, slot ini 'kosong'.

      # Conversi string yang di input menjadi integer, integer yang bisa digunakan untuk mengecek validitas waktu
      dataWaktuKendaraan[k] = str(input("Masukkan waktu kendaraan masuk pukul berapa (00:00 - 23:59): "))
      waktuMasukString = dataWaktuKendaraan[k]
      while len(waktuMasukString) != 5 or waktuMasukString[2] != ":" or int(waktuMasukString[0:2]) > 24 or int(waktuMasukString[3:]) > 59: # Semua 'or' ini memastikan format 00:00 yang benar.
        dataWaktuKendaraan[k] = str(input("Masukkan waktu kendaraan masuk pukul berapa (00:00 - 23:59): "))
        waktuMasukString = dataWaktuKendaraan[k]
      dataWaktuKendaraan[k] = konversiWaktu(dataWaktuKendaraan[k]) # Memanggil fungsi konversiWaktu() untuk mengubah waktu tersebut menjadi menit yang bisa diproses dengan mudah

      dataJenisKendaraan[k] = str(input("Masukkan jenis kendaraan (Mobil, Bus, Motor): "))
      while dataJenisKendaraan[k] not in ["Motor", "Mobil", "Bus", "mobil", "motor", "bus"]:
        dataJenisKendaraan[k] = str(input("Masukkan jenis kendaraan yang benar!: ")) # Mengecek jika nama kendaraan yang di input benar atau tidak. Jika tidak, input terus menerus

      print(f"Tiket anda bernomor: {k}. Tolong di ingat!")
      slotTerisi += 1
      break

  else:
    print("Mohon maaf, parkiran sudah penuh!")
    # else ini adalah bagian dari for-else loop. Else terjadi bila semua index k sudah dicek dan tidak ada yang terkena break karena tidak ada yang 'kosong'.

  # For-else loop ini mengecek dari index 0 - 49 jika ada slot yang kosong. Jika iya, dia masukkan data inputan user ke dalam slot kosong tersebut dan loop selesai dengan 'break'.
  # Misal index 0 sudah terisi. Maka loop ini akan lompat ke index 1 dan masukkan data di index tersebut, seterusnya.
  # if cukup mengecek dataWaktuKendaraan karena nanti, jika ada kendaraan keluar, data kedua array di index n akan sama-sama diganti nilai default maka keduanya 'kosong'.


def kendaraanKeluar():
  # Disini kode input data kendaraan yang keluar beserta biaya parkir

  global slotTerisi
  rounding_unit = 1000

  waktuKeluar = str(input("Masukkan waktu kendaraan keluar pukul berapa (00:00 - 23:59): "))
  while len(waktuKeluar) != 5 or waktuKeluar[2] != ":" or int(waktuKeluar[0:2]) > 24 or int(waktuKeluar[3:]) > 59:
    waktuKeluar = str(input("Masukkan waktu kendaraan keluar pukul berapa (00:00 - 23:59): "))
  waktuKeluar = konversiWaktu(waktuKeluar)


  nomorTiket = int(input("Masukkan nomor tiket anda (0 - 49): "))
  while nomorTiket < 0 or nomorTiket >= 50:
    nomorTiket = int(input("Masukkan nomor tiket yang sesuai!: "))
    # while ini mengecek dan memastikan agar nomor tiket tidak lebih dari 50 atau kurang dari 0 karena index tersebut tidak ada.

  durasiWaktu = waktuKeluar - dataWaktuKendaraan[nomorTiket]
  if durasiWaktu < 0:
    durasiWaktu += 1440


  if slotTerisi > 0:  # Mengecek bila ada setidaknya satu slot terisi
    if dataWaktuKendaraan[nomorTiket] != "0": # Mengecek bila index memiliki angka sesuai tiket kosong atau tidak. Jika tidak kosong, eksekusi kode selanjutnya.
      slotTerisi -= 1

      # If-else di bawah ini mengecek jenis kendaraan dan menghitung biayanya tergantung jenis dan lama kendaraan parkir.

      if dataJenisKendaraan[nomorTiket] == "Mobil" or dataJenisKendaraan[nomorTiket] == "mobil":  # Mobil -> 2k untuk jam pertama, 2k/jam setelah itu, maks 10k
        if (durasiWaktu / 60 * tarifMobil) >= maksMobil:
          print(f"Biaya parkir anda adalah Rp{maksMobil}")
        else:
          print(f"Biaya parkir anda adalah Rp{math.ceil(durasiWaktu / 60 * tarifMobil / rounding_unit) * rounding_unit}")

      elif dataJenisKendaraan[nomorTiket] == "Motor" or dataJenisKendaraan[nomorTiket] == "motor": # Mobil -> 1k untuk jam pertama, 1k/jam setelah itu, maks 10k
        if (durasiWaktu / 60 * tarifMotor) >= maksMotor:
          print(f"Biaya parkir anda adalah {maksMotor}")
        else:
          print(f"Biaya parkir anda adalah Rp{math.ceil((durasiWaktu / 60 * tarifMotor) / rounding_unit) * rounding_unit}")

      elif dataJenisKendaraan[nomorTiket] == "Bus" or dataJenisKendaraan[nomorTiket] == "bus":  # Bus -> 20k flat
        print(f"Biaya parkir anda adalah Rp{tarifBus}")

      # Jika tiket valid dan kendaraan berhasil keluar, reset slot tiket tersebut menjadi default agar bisa terisi kembali oleh fungsi kendaraanMasuk() selanjutnya.
      dataJenisKendaraan[nomorTiket] = "0"
      dataWaktuKendaraan[nomorTiket] = "0"

    else: # Mengecek bila nomor tiket memiliki slot yang terisi. Jika tidak, maka tiketnya tidak valid dan proses tidak terjadi.
      print("Tiket tidak valid!")

  else:
    print("Tidak ada kendaraan dalam tempat parkir!")


def opsiAksi():
  # Ini adalah fungsi 'Menu' dimana loop while akan terus menerus berjalan dan mengeksekusi fungsi kendaraanMasuk() atau kendaraanKeluar() sampai ada break.
  while True:
    print("---------------------------------------------")
    print(f"Jumlah parkiran kosong: {50 - slotTerisi}")
    print("Kendaraan Masuk   = Opsi 1")
    print("Kendaraan Keluar  = Opsi 2")
    print("Exit Program      = Opsi 3")

    aksiPilihan = int(input("Pilih Opsi: "))

    if aksiPilihan == 1:
        kendaraanMasuk()
    elif aksiPilihan == 2:
        kendaraanKeluar()
    elif aksiPilihan == 3:
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Masukkan angka 1, 2, atau 3!")

# Mulai menu saat program di-run
opsiAksi()
# Tugas Besar Berpikir Komputasional Kelompok 10 K-34
# Anggota Kelompok :
# Khafa Pratama (19626200)
# Emily Elizabeth Christian (16526014)
# Puti Naira Izzati (16526146)
# Cokorda Istri Gita Kamalini (16526236)

# Slot Parkir
jumlah_parkir_mobil = 15
jumlah_parkir_motor = 20

# Tarif biaya jam pertama, biaya per jam berikutnya, dan biaya maksimal
awal_mobil = 5000
awal_motor = 2000
per_jam_mobil = 2000
per_jam_motor = 1000
maks_mobil = 20000
maks_motor = 10000

# Data kendaraan disimpan pakai list:
# 1. jenis kendaraan (1 itu mobil dan 2 itu motor)
# 2. plat nomor
# 3. waktu masuk (total menit sejak 00:00)
# 4. id kartu E money
# 5. saldo E money
dataPengendara = []   # kumpulan data semua kendaraan yang lagi parkir

while True:
    aksi = input("Masuk/Keluar dari tempat parkir (STOP untuk berhenti): ").strip().capitalize()

    # UI pas mau masuk :>
    if aksi == "Masuk":
        if jumlah_parkir_mobil + jumlah_parkir_motor == 0:
            print("Parkir sudah penuh, silakan cari parkir di tempat lain.")
        else:
            print("==========================================")
            print("=           Selamat datang!              =")
            print("=       Parkiran kosong saat ini:        =")
            print(f"=        Tempat Parkir Motor: {jumlah_parkir_motor}          =")
            print(f"=        Tempat Parkir Mobil: {jumlah_parkir_mobil}          =")
            print("==========================================")

            # Input jenis kendaraan, diulang sampai valdi
            jenisKendaraan = 0
            while jenisKendaraan != 1 and jenisKendaraan != 2:
                jenisKendaraan = input("Jenis kendaraan (1. Mobil, 2. Motor): ")
                if jenisKendaraan == "1" or jenisKendaraan == "2":
                    jenisKendaraan = int(jenisKendaraan)
                else:
                    jenisKendaraan = 0
                    print("Input tidak valid, coba lagi.")

            if jenisKendaraan == 1 and jumlah_parkir_mobil == 0:
                print("Parkir mobil penuh.")
            elif jenisKendaraan == 2 and jumlah_parkir_motor == 0:
                print("Parkir motor penuh.")
            else:
                platNomor = input("Masukkan plat nomor kendaraan Anda: ")

                # Input waktu masuk, diulang sampai validdd
                jamMasuk = -1
                menitMasuk = -1
                while jamMasuk < 0 or jamMasuk > 23 or menitMasuk < 0 or menitMasuk > 59:
                    jamMasuk = int(input("Masukkan jam saat ini (masuk parkir): "))
                    menitMasuk = int(input("Masukkan menit saat ini (masuk parkir): "))
                    if jamMasuk < 0 or jamMasuk > 23 or menitMasuk < 0 or menitMasuk > 59:
                        print("Waktu tidak valid, coba lagi.")
                waktuMasuk = jamMasuk * 60 + menitMasuk   # simpan dalam total menit

                # Tap kartu E money buat detect id kartu dan saldo
                idKartu = input("Masukkan id kartu E-Money Anda (16 digit): ")
                saldo = int(input("Masukkan jumlah saldo E-Money Anda: "))

                # Kurangin slot parkir
                if jenisKendaraan == 1:
                    jumlah_parkir_mobil -= 1
                else:
                    jumlah_parkir_motor -= 1

                # Simpan data kendaraan (urutan sesuai komentar di atas)
                dataSatuan = [jenisKendaraan, platNomor, waktuMasuk, idKartu, saldo]
                dataPengendara.append(dataSatuan)

    # KENDARAAN KELUAR
    elif aksi == "Keluar":
        # Input waktu keluar, diulang sampai valid
        jamKeluar = -1
        menitKeluar = -1
        while jamKeluar < 0 or jamKeluar > 23 or menitKeluar < 0 or menitKeluar > 59:
            jamKeluar = int(input("Masukkan jam saat ini (keluar parkir): "))
            menitKeluar = int(input("Masukkan menit saat ini (keluar parkir): "))
            if jamKeluar < 0 or jamKeluar > 23 or menitKeluar < 0 or menitKeluar > 59:
                print("Waktu tidak valid, coba lagi.")
        waktuKeluar = jamKeluar * 60 + menitKeluar

        idCari = input("Masukkan id kartu E-Money Anda: ")

        # Cari data pengendara (kalau nggak ketemu, dataKetemu tetap None)
        dataKetemu = None
        for data in dataPengendara:
            if data[3] == idCari:
                dataKetemu = data

        if dataKetemu == None:
            print("Data tidak ditemukan. Hubungi petugas.")
        else:
            # Hitung durasi (total menit), dibulatkan ke atas per jam, minimal 1 jam
            durasi = waktuKeluar - dataKetemu[2]
            if durasi < 0:              # masuk sebelum tengah malam, keluar setelahnya
                durasi += 24 * 60
            jamParkir = (durasi + 59) // 60
            if jamParkir < 1:
                jamParkir = 1

            # Hitung biaya sesuai jenis kendaraan
            if dataKetemu[0] == 1:
                totalBiayaParkir = min(awal_mobil + (jamParkir - 1) * per_jam_mobil, maks_mobil)
            else:
                totalBiayaParkir = min(awal_motor + (jamParkir - 1) * per_jam_motor, maks_motor)

            print(f"Biaya parkir Anda: Rp{totalBiayaParkir}")

            # Cek saldo E money
            if dataKetemu[4] < totalBiayaParkir:
                print("Saldo E-Money tidak cukup.")
                print("Silakan top up E-Money Anda terlebih dahulu, lalu coba keluar lagi.")
            else:
                dataKetemu[4] -= totalBiayaParkir
                print(f"Sisa saldo E-Money Anda: Rp{dataKetemu[4]}")

                # Pembayaran sukses -> kurangin slot dan hapus data
                if dataKetemu[0] == 1:
                    jumlah_parkir_mobil += 1
                else:
                    jumlah_parkir_motor += 1
                dataPengendara.remove(dataKetemu)
                print("Terima kasih, hati-hati di jalan!")

    elif aksi == "Stop":
        break
    else:
        print("Input tidak valid. Pilih Masuk, Keluar, atau STOP.")

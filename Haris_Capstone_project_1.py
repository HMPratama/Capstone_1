vin1= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Black Sabbat",
    "Nama Album": "Paranoid",
    "Tahun":1970,
    "Stock": 1
}
vin2= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Black Sabbat",
    "Nama Album": "Heaven and hell",
    "Tahun":1973,
    "Stock": 2
}
vin3= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "AC DC",
    "Nama Album": "Highway to Hell",
    "Tahun":1979,
    "Stock": 2
}
vin4= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "AC DC",
    "Nama Album": "Black in Black",
    "Tahun":1980,
    "Stock": 1
}
vin5= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Iron Maiden",
    "Nama Album": "Powerslave",
    "Tahun":1984,
    "Stock": 2
}
vin6= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Iron Maiden",
    "Nama Album": "Killer",
    "Tahun":1981,
    "Stock": 1
}
vin7= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Iron Maiden",
    "Nama Album": "Dance of Death",
    "Tahun":1981,
    "Stock": 1
}
vin8= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Iron Maiden",
    "Nama Album": "Live after Death",
    "Tahun":1985,
    "Stock": 1
}
vin9= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Iron Maiden",
    "Nama Album": "Live after Death",
    "Tahun":1985,
    "Stock": 1
}
vin10= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Judas Priest",
    "Nama Album": "British Steel",
    "Tahun":1980,
    "Stock": 1
}
vin11= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Judas Priest",
    "Nama Album": "Rocka Rolla",
    "Tahun":1974,
    "Stock": 2
}
vin12= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Judas Priest",
    "Nama Album": "Priest...Live",
    "Tahun":1987,
    "Stock": 2
}
vin13= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Judas Priest",
    "Nama Album": "Turbo",
    "Tahun":1986,
    "Stock": 2
}
vin14= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Megadeath",
    "Nama Album": "Rust in Peace",
    "Tahun":1990,
    "Stock": 1
}
vin15= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Megadeath",
    "Nama Album": "Killing a man",
    "Tahun":1985,
    "Stock": 2
}
vin16= {
    "Nama Koleksi Vinyl": "Metal",
    "Nama Band": "Maryln Manson",
    "Nama Album": "Sons of Devil",
    "Tahun":1990,
    "Stock": 2
}
listVinyl = {
    "vin1": vin1,
    "vin2": vin2,
    "vin3": vin3,
    "vin4": vin4,
    "vin5": vin5,
    "vin6": vin6,
    "vin7": vin7,
    "vin8": vin8,
    "vin9": vin9,
    "vin10": vin10,
    "vin11": vin11,
    "vin12": vin12,
    "vin13": vin13,
    "vin14": vin14,
    "vin15": vin15,
    "vin16": vin16,
}
KeranjangSewa = {}


def menuUtama():
    pilihanMenu = input('''
                        
    ==========Selamat Datang di Vinyl Collection==========
                     
    1. Tampilkan Koleksi Vinyl
    2. Menambah Koleksi Vinyl
    3. Update Data Koleksi Vinyl
    4. Mengapus Koleksi Vinyl
    5. Sewa Koleksi Vinyl
    6. Keluar Program
    ======================================================                    
                        
    SILAHKAN PILIH ANGKA MENU DI ATAS =>  ''')

    if (pilihanMenu == "1"):
        tampilvinyl()  

    elif(pilihanMenu == "2"):
        tambahVinyl()

    elif(pilihanMenu == "3"):
        updateVinyl()

    elif(pilihanMenu == "4"):
        hapusvinyl()

    elif(pilihanMenu == "5"):
        sewaVinyl()

    elif(pilihanMenu == "6"):
        print("\n Anda telah meninggalkan Program \n")
        exit()

def koleksiVinyl():
    print("\n=====================================\tTABEL VINYL COLLECTION\t========================================\n")
    print (f"|{'INDEX':<6} {' |NAMA KOLEKSI VINYL':^15} {'|      NAMA BAND':<23} {'|      NAMA ALBUM  ':<23} {'|   TAHUN':<13} {'|   STOCK':<14}|") 
    print(105*"_")
    for vinyl in listVinyl.keys():
        index = vinyl
        koleksi = listVinyl[vinyl]["Nama Koleksi Vinyl"]
        nama_band = listVinyl[vinyl]["Nama Band"]
        nama_Album = listVinyl[vinyl]["Nama Album"]
        tahun = listVinyl[vinyl]["Tahun"]
        stock = listVinyl[vinyl]["Stock"]
        print(f"|{index:<8}| {koleksi:^15}   | {nama_band:^20}  | {nama_Album:^20}  | {tahun:^10}  | {stock:^10}  |")

def tampilvinyl():
    menuHalaman_1 = input('''\n
   \t\t\t\t==============================================\n
   \t\t\t\t  SILAHKAN PILIH DAFTAR MENU PILHAN DIBAWAH
   \t\t\t\t______________________________________________

    \t\t\t\t=============DAFTAR MENU PILIHAN==============
    \t\t\t\t||  1. Tampilkan Seluruh Koleksi Vinyl      ||
    \t\t\t\t||  2. Cari Koleksi Vinyl Berdasarkan Index ||
    \t\t\t\t||  3. Exit                                 ||
    \t\t\t\t==============================================\n
    >>>>> SILAHKAN MASUKAN ANGKA MENU PILIHAN ANDA =>   ''')
    
    if(menuHalaman_1 == "1"):
        koleksiVinyl()
        tampilvinyl()
    elif(menuHalaman_1 == "2"):
        while(True):
            cariVinyl = input('\n>>>> MOHON MASUKAN CODE INDEX VINYL(ex: vin1)=>  ')

            if cariVinyl in listVinyl.keys():
                print('\n HASIL PENCARIAN KOLEKSI VINYL BERDASARKAN CODE INDEX\n')
                print (f"{'INDEX':<6} {' |NAMA KOLEKSI VINYL':^15} {'|      NAMA BAND':<23} {'|      NAMA ALBUM  ':<23} {'|   TAHUN':<13} {'|   STOCK':<14}|")
                print(105*"_") 
                index = cariVinyl
                koleksi = listVinyl[cariVinyl]["Nama Koleksi Vinyl"]
                nama_band = listVinyl[cariVinyl]["Nama Band"]
                nama_Album = listVinyl[cariVinyl]["Nama Album"]
                tahun = listVinyl[cariVinyl]["Tahun"]
                stock = listVinyl[cariVinyl]["Stock"]
                print(f"{index:<8}| {koleksi:^15}   | {nama_band:^20}  | {nama_Album:^20}  | {tahun:^10}  | {stock:^10}  |")
                cariLagi = input('\n>>>> APAKAH INGIN MENCARI KOLEKSI VINYL LAINNYA ? (Y/N)=>  ')
                if cariLagi =="y" or cariLagi=="Y":
                    continue
                elif cariLagi == 'n' or cariLagi=="N":
                    menuUtama()
            else:
                print("\n > MAAF!!! TIDAK TERSEDIA CODE VINYL TERSEBUT <")
                print("""\n > MOHON UNTUK MEMASUKAN CODE VINYL KEMBALI 
                      
                    ATAU <""")
                batalCari = input('\n>>>> INGIN MEMBATALKAN PENCARIAN (Y/N)=>  ')
                if (batalCari == "y" or batalCari=="Y"):
                    menuUtama()
                continue
    else:
        menuUtama()

def tambahVinyl():
    while(True):
        koleksiVinyl()
        print()
        print('\n <PROSES PENAMBAH KOLEKSI VINYL>')
        for vinyl in listVinyl.keys():
            index = vinyl
        vinylTemplate = {
            "Nama Koleksi Vinyl": "namavinyl",
            "Nama Band" : "namaBand",
            "Nama Album" : "NamaAlbum",
            "Tahun" : 0000,
            "Stock" : 0
        }

        vinylBaru = dict.fromkeys(vinylTemplate.keys())
        indexBaru = input('\n MOHON MASUKAN CODE INDEX VINYL DENGAN HURUF KECIL SESUAI URUTAN TABEL (ex: vin1): ')
        if indexBaru in listVinyl.keys():
            print('\n > CODE INDEX SUDAH TERSEDIA!! SILAHKAN LIHAT TABEL LIST <')
            batalTambah = input('\n>>>>INGIN MEMBATALKAN PENAMBAHAN!! (Y/N)=>  ')
            if (batalTambah == "y" or batalTambah=="Y"):
                menuUtama()
            
        vinylBaru["Nama Koleksi Vinyl"] = input('>>>>SILAHKAN MASUKAN GENRE MUSIK=> ')
        vinylBaru["Nama Band"] = input(">>>>SILAHKAN MASUKAN NAMA BAND=> ")
        vinylBaru["Nama Album"] = input(">>>>SILAHKAN MASUKAN NAMA ALBUM=> ")
        

        while(True):
            vinylBaru["Tahun"] = int(input(">>>>SILAHKAN MASUKAN TAHUN RELEASE=> "))

            if (vinylBaru["Tahun"]>= 2024):
                print('> SILAHKAN MASUKAN TAHUN RELEASE KEMBALI <')
            else:
                break
        vinylBaru["Stock"] = int(input(">>>>SILAHKAN MASUKAN JUMLAH STOCK VINYL=> "))
        simpanData = input(">>>>SIMPAN DATA VINYL BARU ? (Y/N)=> ")
        if(simpanData == "n" or simpanData=="N"):
            print("\n > DATA VINYL BARU BATAL DISIMPAN <")
            tambahVinyl()
        elif simpanData == "y" or simpanData == "Y":
            listVinyl.update({indexBaru: vinylBaru})
            koleksiVinyl()
            print("\n")
            tambahLagi = input("< DATA KOLEKSI VINYL BARU SUDAH TERSIMPAN (@_@) >\n >>>>>APAKAH INGIN MENAMBAHKAN KOLEKSI VYNIL KEMBALI (Y/N)=>  ")
            if tambahLagi == 'y'or tambahLagi == "Y":
                tambahVinyl()
            elif(tambahLagi == "n" or tambahLagi=="N"):
                menuUtama()

def updateVinyl():
    print("\n UPDATE DATA VINYL")
    koleksiVinyl()

    while(True):
        updatedataVinyl = input("\n>>>>SILAHKAN MASUKAN CODE INDEX YANG TERTERA PADA TABEL=> ")
        if updatedataVinyl not in listVinyl:
            print("\n > TIDAK TERSEDIA CODE INDEX <")
            batalUpdate = input('\n>>>> INGIN MEMBATALKAN UPDATE(Y/N)=>  ')
            if (batalUpdate == "y" or batalUpdate=="Y"):
                menuUtama()
            continue
        else:
            print("\n PILIH KOLEKSI VINYL YANG AKAN DI UPDATE\n")
            print (f"{'Index':<6} {' |Nama Koleksi Vinyl':^15} {'|      Nama Band':<23} {'|      Nama Album  ':<23} {'|   Tahun':<13} {'|   Stock':<14}|")
            index = updatedataVinyl
            koleksi = listVinyl[updatedataVinyl]["Nama Koleksi Vinyl"]
            nama_band = listVinyl[updatedataVinyl]["Nama Band"]
            nama_Album = listVinyl[updatedataVinyl]["Nama Album"]
            tahun = listVinyl[updatedataVinyl]["Tahun"]
            stock = listVinyl[updatedataVinyl]["Stock"]
            print(f"{index:<8}| {koleksi:^15}   | {nama_band:^20}  | {nama_Album:^20}  | {tahun:^10}  | {stock:^10}  |")
            break
        
    keysUpdate = input('\n>>>>MOHON MASUKAN KARAKTER SESUAI YANG TERTERA PADA BARIS JUDUL=> ')
    listVinyl[updatedataVinyl][keysUpdate]= input('\n>>>>MOHON MASUKAN DATA YANG AKAN DI UPDATE=> ')
    koleksiVinyl()
    print(f'\n < DATA KOLEKSI VINYL DENGAN CODE >>|| {updatedataVinyl} ||<< TELAH BERHASIL DI UPDATE>')
    kembaliUpdate = input('\n>>>>APAKAH INGIN UPDATE KEMBALI (Y/N)=>  ')
    if (kembaliUpdate == "y" or kembaliUpdate=="Y"):
        print()
    else:
        menuUtama()

def hapusvinyl():
    koleksiVinyl()
    while(True):
        indexVinyl = input('\n>>>>MOHON MASUKAN CODE INDEX YANG AKAN DIHAPUS=>  ')
        if indexVinyl not in listVinyl:
            print('\n > CODE INDEX YANG DIMASUKAN TIDAK TERDAFTAR')
            continue
        else:
            break
    while(True):
        yakinHapus = input('\n>>>> YAKIN DENGAN PILIHAN ANDA?=> (Y/N)')
        if(yakinHapus == "n" or yakinHapus=="N"):
            print(f"\n VINYL DENGAN CODE >>|{indexVinyl}|<< BATAL DIHAPUS")
            koleksiVinyl()
        elif (yakinHapus == "y" or yakinHapus=="Y"):
            listVinyl.pop(indexVinyl)
            koleksiVinyl()
            print(f"\n < VINYL DENGAN CODE INDEX >>|{indexVinyl}|<< TELAH DIHAPUS>")
            koleksiVinyl()
            lanjuthapus= input('\n APAKAH LANJUT PROSES MENGHAPUS (Y/N)')
            if lanjuthapus == "y" or lanjuthapus == "Y":
             hapusvinyl()
        else:
            break
        menuUtama()

def sewaVinyl():
    while (True):
        koleksiVinyl()
        for item in KeranjangSewa.keys():
            indexSewa = item
        sewaTemplate ={
            "Nama Koleksi Vinyl": "namavinyl",
            "Nama Band" : "namaBand",
            "Album" : "Nama Album",
            "Tahun": 0000,
            "Quantity": 0,
            "Masa Sewa": 0
        }
        while (True):
            sewaVinyl = dict.fromkeys(sewaTemplate.keys())
            indexSewa = input('\n>>>>MOHON MASUKAN INDEX VINYL YANG AKAN DISEWA=> ')
            if indexSewa not in listVinyl.keys():
                print("\n > INDEX TIDAK TERSEDIA, MOHON MASUKAN KEMBALI INDEX VINYL!!<")
                continue
            else:
                break

        sewaVinyl["Nama Koleksi Vinyl"] = listVinyl[indexSewa]["Nama Koleksi Vinyl"]
        sewaVinyl["Nama Band"] = listVinyl[indexSewa]["Nama Band"]
        sewaVinyl["Album"] = listVinyl[indexSewa]["Nama Album"]
        sewaVinyl["Tahun"] = listVinyl[indexSewa]["Tahun"]
        while(True):
            sewaVinyl["Quantity"] = int(input("\n>>>>SILAHKAN MASUKAN SEWA JUMLAH VINYL=> "))
            if(sewaVinyl["Quantity"] !=1):
                print(" > JUMLAH MAKSIMAL SEWA HANYA SATU PIRINGAN <")
                continue
            else:
                break
        while(True):
            sewaVinyl["Masa Sewa"] = int(input("\n>>>>MOHON BERAPA HARI AKAN SEWA VINYL=>   "))
            if(sewaVinyl["Masa Sewa"] >= 5):
                print('\n > BATAS MAKSIMAL 5 HARI SEWA <')
                continue
            else:
                break
        KeranjangSewa.update({indexSewa : sewaVinyl})
        sisaStock = listVinyl[indexSewa]["Stock"]-1
        listVinyl[indexSewa].update({"Stock":sisaStock})
        print('\n =================================================ISI KERANJANG SEWA=================================================\n')
        print(f"{'INDEX':<6} {' |NAMA KOLEKSI VINYL':^15} {'|      NAMA BAND':<23} {'|      NAMA ALBUM  ':<23} {'|   TAHUN':<13} {'|QUANTITY':<10} {'|MASA SEWA'}")
        print(f"{indexSewa:<8}| {KeranjangSewa[indexSewa]['Nama Koleksi Vinyl']:^15}   | {KeranjangSewa[indexSewa]['Nama Band']:^20}  | {KeranjangSewa[indexSewa]['Album']:^20}  | {KeranjangSewa[indexSewa]['Tahun']:^10}  | {KeranjangSewa[indexSewa]['Quantity']:^8} | {KeranjangSewa[indexSewa]['Masa Sewa']:^12}")
        checker = input('\n apakah anda mau sewa vinyl yang lain? (Y/N): ')
        if checker == "y" or checker=="Y":
            continue
        elif checker == "n" or checker == "N":
            print("\n ==============================================DATA SEWA VINYL=============================================================== \n")
            print(f"{'INDEX':<6} | {' NAMA KOLEKSI VINYL':<20} {'|      NAMA BAND':<25} {'|      NAMA ALBUM  ':<23} {'|   TAHUN':<13} {'|QUANTITY':<10} {'|MASA SEWA'}")
            for item in KeranjangSewa :
                print(f"{item:<6} | {KeranjangSewa[item]['Nama Koleksi Vinyl']:^20} | {KeranjangSewa[item]['Nama Band']:^23} |  {KeranjangSewa[item]['Album']:^20} | {KeranjangSewa[item]['Tahun']:^11} | {KeranjangSewa[item]['Quantity']:^8} | {KeranjangSewa[item]['Masa Sewa']:^10}")
            namaPenyewa = input("\nSILAHKAN MASUKAN NAMA PENYEWA=>  ")
            while(True):
                NIK_KTP = input("SILAHKAN MASUKAN NIK KTP PENYEWA=> ")
                if len(NIK_KTP) !=16:
                        print(' > NIK KTP YANG DIMASUKAN SALAH, MOHON MASUKAN KEMBALI <')
                        continue
                else: break
            tanggal = len(range(1,31))
            bulan = len(range(1,13))
            tahun = 2024
            while(True):
                tanggalSewa = int(input("MASUKAN TANGGAL SEWA=>  "))
                if tanggalSewa > tanggal:
                    print("/n > MOHON MASUKAN TANGGAL SEWA DENGAN BENAR <")
                    continue
                else: break
            while(True):
                bulanSewa = int(input("MASUKAN BULAN SEWA (dalam angka))=>  "))
                if bulanSewa > bulan:
                    print("/n > MOHON MASUKAN BULAN DALAM ANGKA <")
                    continue
                else: break
            while(True):
                tahunSewa = int(input("MASUKAN TAHUN SEWA=>  "))
                if tahunSewa > tahun:
                    print("/n > MOHON MASUKAN TAHUN SEWA DENGAN BENAR <")
                    continue
                else: break
            print('\n <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< DATA BARU PENYEWA VINYL COLLECTION >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n')
            print ("| NAMA PELANGGAN | NIK KTP PELANGGAN | GENRE SEWA VINYL | TAHUN RELEASE | JUMLAH | LAMA SEWA (HARI)| TANGGAL / BULAN / TAHUN |")
            print(f"{namaPenyewa:^17} | {NIK_KTP:^20} | {KeranjangSewa[item]['Nama Koleksi Vinyl']:^19} | {KeranjangSewa[item]['Tahun']:^16} | {KeranjangSewa[item]['Quantity']:^9} | {KeranjangSewa[item]['Masa Sewa']:^20}| {tanggalSewa:^10}/{bulanSewa:^8}/{tahunSewa:<8}|")
            for item in KeranjangSewa:
                tanggalBalik = tanggalSewa + KeranjangSewa[item]["Masa Sewa"]
                bulanBalik = bulanSewa
                tahunBalik = tahunSewa
                lewatTanggal = tanggalBalik -30
                lewatBulan = bulanBalik +1
                akhirTahun = lewatBulan-12
                lewatTahun = tahunBalik +1
                if tanggalBalik <=30:
                    print(f"\n <SILAHKAN KEMBALIKAN VINYL >>>>> <{KeranjangSewa[item]['Nama Koleksi Vinyl']} {KeranjangSewa[item]['Nama Band']} {KeranjangSewa[item]['Album']}> PALING LAMBAT TANGGAL <{tanggalBalik}/{bulanBalik}/{tahunBalik}>")
                elif tanggalBalik > 30 and lewatBulan > 12:
                    print(f"\n <SILAHKAN KEMBALIKAN VINYL >>>>> <{KeranjangSewa[item]['Nama Koleksi Vinyl']} {KeranjangSewa[item]['Nama Band']} {KeranjangSewa[item]['Album']}> PALING LAMBAT TANGGAL <{lewatTanggal}/{akhirTahun}/{lewatTahun}>")
                elif tanggalBalik >30:
                    print(f"\n <SILAHKAN KEMBALIKAN VINYL >>>>> <{KeranjangSewa[item]['Nama Koleksi Vinyl']} {KeranjangSewa[item]['Nama Band']} {KeranjangSewa[item]['Album']}> PALING LAMBAT TANGGAL <{lewatTanggal}/{lewatTahun}/{tahunBalik}>")
                menuUtama()
      
menuUtama()
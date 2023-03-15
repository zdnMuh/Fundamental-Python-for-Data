# print("Hello World!")

# print("Hallo Dunia!")
# print("Riset Bahasa Python")

# # Statement
# print("Belajar Python menyenangkan")
# print("Halo Dunia")
# print("Hello World!")
# # Variables & Literals
# bilangan1 = 5
# bilangan2 = 10
# kalimat1 = "Belajar Bahasa Python"
# # Operators
# print(bilangan1 + bilangan2)

# bilangan1 = 20
# bilangan2 = 10
# print(bilangan1 - bilangan2)

# harga_asli = 20000
# potongan = 2000
# harga_setelah_potongan = harga_asli - potongan
# harga_final = harga_setelah_potongan*1.1
# print(harga_final)

# contoh_list = [1, 'dua', 3, 4.0, 5]
# print(contoh_list[0])
# print(contoh_list[3])
# contoh_list[3] = 'empat'
# print(contoh_list[3])

# contoh_tuple = ('januari', 'februari', 'maret', 'april')
# print(contoh_tuple[0])
# # contoh_tuple[0] = 'desember'
# print(contoh_tuple[0])

# contoh_list = ['dewi', 'budi', 'cici', 'linda', 'cici']
# print(contoh_list)
# contoh_set = {'dewi', 'budi', 'cici', 'linda', 'cici'}
# print(contoh_set)
# contoh_frozen_set = frozenset({'dewi', 'budi', 'cici', 'linda', 'cici'})
# print(contoh_frozen_set)

# person = {'nama': 'John Doe', 'pekerjaan': 'Programmer'}
# print(person['nama'])
# print(person['pekerjaan'])

# sepatu = {'nama': 'Sepatu Niko', 'harga': 150000, 'diskon': 30000}
# baju = {'nama': 'Baju Unikloh', 'harga': 80000, 'diskon': 8000}
# celana = {'nama': 'Celana Lepis', 'harga': 200000, 'diskon': 60000}
# daftar_belanja = [sepatu, baju, celana]

# # Hitung harga masing-masing data setelah dikurangi diskon
# harga_sepatu = sepatu['harga'] - sepatu['diskon']
# harga_baju = baju['harga'] - baju['diskon']
# harga_celana = celana['harga'] - celana['diskon']
# # Hitung harga total
# total_harga = harga_sepatu + harga_baju + harga_celana
# # Hitung harga kena pajak
# total_harga_dengan_pajak = total_harga * 1.1
# # Cetak total_harga + total_pajak
# print(total_harga + total_harga_dengan_pajak)

# total_harga = 150000
# potongan_harga = 0.3
# pajak = 0.1
# harga_bayar = 1 - potongan_harga
# harga_bayar *= total_harga
# pajak_bayar = harga_bayar * pajak
# harga_bayar += pajak_bayar
# print(harga_bayar)

# total_harga = 150000
# potongan_harga = 0.3
# pajak = 0.1
# harga_bayar = (1-potongan_harga)*total_harga
# harga_bayar += harga_bayar*pajak

# bilangan = (5 % 3 ** 2) + (3 + 2 * 2) * (4 - 2) 
# print(bilangan)

# sepatu = {'nama': 'Sepatu Niko', 'harga': 150000, 'diskon': 30000}
# baju = {'nama': 'Baju Unikloh', 'harga': 80000, 'diskon': 8000}
# celana = {'nama': 'Celana Lepis', 'harga': 200000, 'diskon': 60000}
# daftar_belanja = [sepatu, baju, celana]

# # Hitung harga masing-masing data setelah dikurangi diskon
# harga_sepatu = sepatu['harga'] - sepatu['diskon']
# harga_baju = baju['harga'] - baju['diskon']
# harga_celana = celana['harga'] - celana['diskon']
# # Hitung harga total
# total_harga = (harga_sepatu + harga_baju + harga_celana) * 1.1
# print(total_harga)

# statement if... elif... else...
# x = 7
# if x%2 == 0:
#     print("x habis dibagi dua")
# elif x%3 == 0:
#     print("x habis dibagi tiga")
# elif x%5 == 0:
#     print("x habis dibagi lima")
# else:
#     print("x tidak habis dibagi dua, tiga, ataupun lima")

# jam = 13
# if jam >= 5 and jam < 12:
#     print("Selamat Pagi")
# elif jam >= 12 and jam < 17:
#     print("Selamat Siang")
# elif jam >= 17 and jam < 19:
#     print("Selamat Sore")
# else:
#     print("Selamat Malam")

# jam = 17
# tagihan_ke = 'Mr. Yoyo'
# warehousing = {'harga_harian': 1000000, 'total_hari': 15}
# cleansing = {'harga_harian': 1500000, 'total_hari': 10}
# integration = {'harga_harian': 2000000, 'total_hari': 15}
# transformation = {'harga_harian': 2500000, 'total_hari': 10}
# sub_warehousing = warehousing['harga_harian'] * warehousing['total_hari']
# sub_cleansing = cleansing['harga_harian'] * cleansing['total_hari']
# sub_integration = integration['harga_harian'] * integration['total_hari']
# sub_transformation = transformation['harga_harian'] * transformation['total_hari']
# total_harga = sub_warehousing + sub_cleansing + sub_integration + sub_transformation
# print("Tagihan kepada:") 
# print(tagihan_ke)
# if jam > 19:
#     print("Selamat malam, anda harus membayar tagihan sebesar:")
# elif jam > 17:
#     print("Selamat sore, anda harus membayar tagihan sebesar:")
# elif jam >12:
#     print("Selamat siang, anda harus membayar tagihan sebesar:")
# else:
#     print("Selamat pagi, anda harus membayar tagihan sebesar:")
# print(total_harga)

# tagihan=[50000, 75000, 125000, 300000, 120000]
# total_tagihan=tagihan[0]+tagihan[1]+tagihan[2]+tagihan[3]+tagihan[4]
# i=0
# jumlah_tagihan=len(tagihan)
# total_tagihan=0
# while i<jumlah_tagihan:
#     total_tagihan+=tagihan[i]
#     i+=1
# print(total_tagihan)
# print(len(tagihan))

# tagihan=[50000, 75000, -150000, 125000, 300000, -50000, 200000]
# i=0
# jumlah_tagihan=len(tagihan)
# total_tagihan=0
# while i<jumlah_tagihan:
#     if tagihan[i]<0:
#         total_tagihan=-1
#         print('terdapat angka minus dalam tagihan, perhitungan dihentikan!')
#         break
#     total_tagihan+=tagihan[i]
#     i+=1
# print(total_tagihan)

# tagihan=[50000, 75000, -150000, 125000, 300000, -50000, 200000]
# i=0
# jumlah_tagihan=len(tagihan)
# total_tagihan=0
# while i<jumlah_tagihan:
#     if tagihan[i]<0:
#         i+=1
#         continue
#     total_tagihan+=tagihan[i]
#     i+=1
# print(total_tagihan)

# list_tagihan=[50000, 75000, -150000, 125000, 300000, -50000, 200000]
# total_tagihan=0
# for tagihan in list_tagihan:
#     total_tagihan+=tagihan
# print(total_tagihan)

# list_tagihan=[50000, 75000, -150000, 125000, 300000, -50000, 200000]
# print('for loops with break')
# total_tagihan_break=0
# for tagihan in list_tagihan:
#     if tagihan<0:
#         print('terdapat angka minus dalam tagihan, perhitungan dihentikan!')
#         break
#     total_tagihan_break+=tagihan
# print('total tagihan %d.' %total_tagihan_break)
# print()

# print('for loops with continue')
# total_tagihan_continue=0
# for tagihan in list_tagihan:
#     if tagihan<0:
#         print('terdapat angka minus dalam tagihan, tagihan %d dilewati!' %tagihan)
#         continue
#     total_tagihan_continue+=tagihan
# print('total tagihan %d.' %total_tagihan_continue)

# list_daerah=['malang', 'palembang', 'medan']
# list_buah=['apel', 'duku', 'jeruk']
# for nama_daerah in list_daerah:
#     for nama_buah in list_buah:
#         print(nama_buah + ' ' + nama_daerah)

# list_cash_flow = [
# 2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
# -5000000, 7500000, 10000000, -1500000, 25000000, -2500000
# ]
# total_pengeluaran, total_pemasukan =0,0
# for dana in list_cash_flow:
#     if dana>0:
#         total_pemasukan+=dana
#     else:
#         total_pengeluaran+=dana
# total_pengeluaran*=-1
# print(total_pengeluaran)
# print(total_pemasukan)


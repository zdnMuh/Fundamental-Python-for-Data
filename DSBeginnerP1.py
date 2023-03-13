"""
print("Hello World!")

print("Hallo Dunia!")
print("Riset Bahasa Python")

# Statement
print("Belajar Python menyenangkan")
print("Halo Dunia")
print("Hello World!")
# Variables & Literals
bilangan1 = 5
bilangan2 = 10
kalimat1 = "Belajar Bahasa Python"
# Operators
print(bilangan1 + bilangan2)

bilangan1 = 20
bilangan2 = 10
print(bilangan1 - bilangan2)

harga_asli = 20000
potongan = 2000
harga_setelah_potongan = harga_asli - potongan
harga_final = harga_setelah_potongan*1.1
print(harga_final)
"""

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

total_harga = 150000
potongan_harga = 0.3
pajak = 0.1
harga_bayar = 1 - potongan_harga
harga_bayar *= total_harga
pajak_bayar = harga_bayar * pajak
harga_bayar += pajak_bayar
print(harga_bayar)

total_harga = 150000
potongan_harga = 0.3
pajak = 0.1
harga_bayar = (1-potongan_harga)*total_harga
harga_bayar += harga_bayar*pajak

bilangan = (5 % 3 ** 2) + (3 + 2 * 2) * (4 - 2) 
print(bilangan)

sepatu = {'nama': 'Sepatu Niko', 'harga': 150000, 'diskon': 30000}
baju = {'nama': 'Baju Unikloh', 'harga': 80000, 'diskon': 8000}
celana = {'nama': 'Celana Lepis', 'harga': 200000, 'diskon': 60000}
daftar_belanja = [sepatu, baju, celana]

# Hitung harga masing-masing data setelah dikurangi diskon
harga_sepatu = sepatu['harga'] - sepatu['diskon']
harga_baju = baju['harga'] - baju['diskon']
harga_celana = celana['harga'] - celana['diskon']
# Hitung harga total
total_harga = (harga_sepatu + harga_baju + harga_celana) * 1.1
print(total_harga)
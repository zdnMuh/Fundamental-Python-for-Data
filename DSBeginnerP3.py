# class Karyawan:
#     nama_perusahaan = 'ABC'

# aksara = Karyawan()
# senja = Karyawan()
# print(aksara.nama_perusahaan)
# # print(aksara.__class__.nama_perusahaan)
# aksara.nama_perusahaan = 'DEF'
# print(aksara.nama_perusahaan)
# print(senja.nama_perusahaan)

# class Karyawan:
#     nama_perusahaan = 'ABC'
#     # __init__ adalah method khusus yang akan dipanggil pertama kali saat objek dibuat (instance attribute) selalu ada self dalam parameter
#     def __init__(self, nama, usia, pendapatan):
#         self.nama = nama
#         self.usia = usia
#         self.pendapatan = pendapatan

# aksara = Karyawan('Aksara', 25, 8500000)
# senja = Karyawan('Senja', 28, 12500000)
# print(aksara.nama + 'Usia: ' + str(aksara.usia) + 'Pendapatan: ' + str(aksara.pendapatan))
# print(senja.nama + 'Usia: ' + str(senja.usia) + 'Pendapatan: ' + str(senja.pendapatan))

# class Karyawan:
#     nama_perusahaan = 'ABC'
#     tunjangan_transportasi = 500000
#     def __init__(self, nama, usia, pendapatan):
#         self.nama = nama
#         self.usia = usia
#         self.pendapatan = pendapatan

# karyawan_1 = Karyawan('Budi', 35, 5000000)
# karyawan_2 = Karyawan('Didi', 30, 5000000)
# karyawan_1.__class__.nama_perusahaan = 1000000

# total_pengeluaran = karyawan_1.__class__.tunjangan_transportasi
# total_pengeluaran += karyawan_2. __class__.tunjangan_transportasi
# total_pengeluaran += karyawan_1.pendapatan
# total_pengeluaran += karyawan_2.pendapatan
# print(total_pengeluaran)


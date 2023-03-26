# bulan_pembelian = ('januari', 'februari', 'maret', 'april', 'mei','juni', 'juli', 'agustus', 'september', 'oktober', 'november', 'desember')
# print(bulan_pembelian[0])
# print(bulan_pembelian[5])
# print(bulan_pembelian[-1])
# print(bulan_pembelian[-2])
# pertengahan_bulan = bulan_pembelian[4:8]
# print(pertengahan_bulan)
# awal_tahun = bulan_pembelian[:5]
# print(awal_tahun)
# akhir_tahun = bulan_pembelian[8:]
# print(akhir_tahun)
# print(bulan_pembelian[-4:-1])

# list_makanan = ['gado-gadao', 'ayam goreng', 'rendang']
# list_minuman = ['es teh', 'es jeruk', 'es campur']
# list_menu = list_makanan + list_minuman
# print(list_menu)

print('>>> fitur .append()')
list_makanan = ['gado-gado', 'ayam goreng', 'rendang']
list_makanan.append('ketoprak')
print(list_makanan)
print('>>> fitur .clear()')
list_makanan = ['gado-gado', 'ayam goreng', 'rendang']
list_makanan.clear()
print(list_makanan)
print('>>> fitur .copy()')
list_makanan1 = ['gado-gado', 'ayam goreng', 'rendang']
list_makanan2 = list_makanan1.copy()
list_makanan3 = list_makanan1
list_makanan2.append('opor')
list_makanan3.append('ketoprak')
print(list_makanan1)
print(list_makanan2)
print('>>> fitur .count()')
list_score = ['budi', 'sud', 'budi', 'budi', 'budi',  'sud', 'sud']
score_budi = list_score.count('budi')
score_sud = list_score.count('sud')
print(score_budi)
print(score_sud)
print('>>> fitur .extend()')
list_menu = ['gado-gado', 'ayam goreng', 'rendang']
list_minuman = ['es teh', 'es jeruk', 'es campur']
list_menu.extend(list_minuman)
print(list_menu)
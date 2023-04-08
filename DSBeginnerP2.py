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

# print('>>> fitur .append()')
# list_makanan = ['gado-gado', 'ayam goreng', 'rendang']
# list_makanan.append('ketoprak')
# print(list_makanan)
# print('>>> fitur .clear()')
# list_makanan = ['gado-gado', 'ayam goreng', 'rendang']
# list_makanan.clear()
# print(list_makanan)
# print('>>> fitur .copy()')
# list_makanan1 = ['gado-gado', 'ayam goreng', 'rendang']
# list_makanan2 = list_makanan1.copy()
# list_makanan3 = list_makanan1
# list_makanan2.append('opor')
# list_makanan3.append('ketoprak')
# print(list_makanan1)
# print(list_makanan2)
# print('>>> fitur .count()')
# list_score = ['budi', 'sud', 'budi', 'budi', 'budi',  'sud', 'sud']
# score_budi = list_score.count('budi')
# score_sud = list_score.count('sud')
# print(score_budi)
# print(score_sud)
# print('>>> fitur .extend()')
# list_menu = ['gado-gado', 'ayam goreng', 'rendang']
# list_minuman = ['es teh', 'es jeruk', 'es campur']
# list_menu.extend(list_minuman)
# print(list_menu)

# # Fitur .index()
# print(">>> Fitur .index()")
# list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
# score_pertama_sud = list_score.index('Sud') + 1
# print(score_pertama_sud)
# # Fitur .insert()
# print(">>> Fitur .insert()")
# list_score = ['Budi','Sud','Budi','Budi','Sud']
# list_score.insert(3,'sud')
# print(list_score)
# # Fitur .pop()
# print(">>> Fitur .pop()")
# list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
# list_menu.pop(1)
# print(list_menu)
# # Fitur .remove()
# print(">>> Fitur .remove()")
# list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
# list_menu.remove('rendang')
# print(list_menu)
# # Fitur .reverse()
# print(">>> Fitur .reverse()")
# list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
# list_menu.reverse()
# print(list_menu)
# # Fitur .sort()
# print(">>> Fitur .sort()")
# list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
# list_menu.sort()
# print(list_menu)
# list_menu.sort(reverse=True)
# print(list_menu)

# # Fitur .count()
# print(">>> Fitur .count()")
# tuple_score = ('Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud')
# score_budi = tuple_score.count('Budi')
# score_sud = tuple_score.count('Sud')
# print(score_budi) # akan menampilkan output 4
# print(score_sud) # akan menampilkan output 3
# # Fitur .index()
# print(">>> Fitur .index()")
# tuple_score = ('Budi','Sud','Budi','Budi','Budi','Sud','Sud')
# score_pertama_sud = tuple_score.index('Sud') + 1
# print(score_pertama_sud) # akan menampilkan output 2

# # Fitur .add()
# print(">>> Fitur .add()")
# set_buah = {'Jeruk','Apel','Anggur'}
# set_buah.add('Melon')
# print(set_buah)
# # Fitur .clear()
# print(">>> Fitur .clear()")
# set_buah = {'Jeruk','Apel','Anggur'}
# set_buah.clear()
# print(set_buah)
# # Fitur .copy()
# print(">>> Fitur .copy()")
# set_buah1 = {'Jeruk','Apel','Anggur'}
# set_buah2 = set_buah1
# set_buah3 = set_buah1.copy()
# set_buah2.add('Melon')
# set_buah3.add('Kiwi')
# print(set_buah1)
# print(set_buah2)
# # Fitur .update()
# print(">>> Fitur .update()")
# parcel1 = {'Anggur','Apel','Jeruk'}
# parcel2 = {'Apel','Kiwi','Melon'}
# parcel1.update(parcel2)
# print(parcel1)
# # Fitur .pop()
# print(">>> Fitur .pop()")
# parcel = {'Anggur','Apel','Jeruk'}
# buah = parcel.pop()
# print(buah)
# print(parcel)
# # Fitur .remove()
# print(">>> Fitur .remove()")
# parcel = {'Anggur','Apel','Jeruk'}
# parcel.remove('Apel')
# print(parcel)

# # Fitur .union()
# print(">>> Fitur .union()")
# parcel1 = {'Anggur','Apel','Jeruk'}
# parcel2 = {'Apel','Kiwi','Melon'}
# parcel3 = parcel1.union(parcel2)
# print(parcel1)
# print(parcel3)
# # Fitur .isdisjoint()
# print(">>> Fitur .isdisjoint()")
# parcel1 = {'Anggur','Apel','Jeruk'}
# parcel2 = {'Kiwi','Melon','Pisang'}
# parcel3 = {'Apel','Srikaya','Semangka'}
# parcel1_parcel2_disjoint = parcel1.isdisjoint(parcel2)
# print(parcel1_parcel2_disjoint)
# parcel1_parcel3_disjoint = parcel1.isdisjoint(parcel3)
# print(parcel1_parcel3_disjoint)
# # Fitur .issubset()
# print(">>> Fitur .issubset()")
# parcel_A = {'Anggur', 'Apel'}
# parcel_B = {'Durian','Semangka','Apel'}
# parcel_C = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
# parcel_A_dalam_C = parcel_A.issubset(parcel_C)
# parcel_B_dalam_C = parcel_B.issubset(parcel_C)
# print(parcel_A_dalam_C)
# print(parcel_B_dalam_C)
# # Fitur .issuperset()
# print(">>> Fitur .issuperset()")
# parcel_C_mengandung_A = parcel_C.issuperset(parcel_A)
# parcel_C_mengandung_B = parcel_C.issuperset(parcel_B)
# print(parcel_C_mengandung_A)
# print(parcel_C_mengandung_B)
# # Fitur .intersection()
# print(">>> Fitur .intersection()")
# parcel_A = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
# parcel_B = {'Apel', 'Jeruk', 'Semangka', 'Durian', 'Tomat'}
# parcel_C = parcel_A.intersection(parcel_B)
# print(parcel_C)
# # Fitur .difference()
# print(">>> Fitur .difference()")
# parcel_C = parcel_A.difference(parcel_B)
# print(parcel_C)
# # Fitur .symmetric_difference()
# print(">>> Fitur .symmetric_difference()")
# parcel_A = {'Anggur', 'Apel', 'Jeruk', 'Melon'}
# parcel_B = {'Apel','Jeruk','Semangka','Leci'}
# parcel_C = parcel_A.symmetric_difference(parcel_B)
# print(parcel_C)
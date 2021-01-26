# Step 1:
# baca file "harga_rumah.txt"

file_harga_rumah = open("harga_rumah.txt", "r")
data_harga_rumah = file_harga_rumah.readlines()
file_harga_rumah.close()


# Buat list of dict dengan nama harga rumah
key_harga_rumah = data_harga_rumah[0].replace("\n", "").split(",")
harga_rumah = []
for baris in data_harga_rumah[1:]:
    baris_harga_rumah = baris.replace("\n", "").split(",")
    dict_harga_rumah = dict()
    for i in range(len(baris_harga_rumah)):
        dict_harga_rumah[key_harga_rumah[i]] = baris_harga_rumah[i]
    harga_rumah.append(dict_harga_rumah)
print(harga_rumah)

# Step 2:
# Buat fungsi get_all_specified_attribute yang menerima parameter list_of_dictionary
# fungsi akan mengembalikan sebuah list yang bersikan seluruh atribut dengan speficied_key

def get_all_specified_attribute(list_of_dictionary, speficied_key):
    list_attributes = []
    for data in list_of_dictionary:
        attribute = data[speficied_key]
        list_attributes.append(attribute)
    return list_attributes

# print(get_all_specified_attribute(harga_rumah, 'bangunan'))

# Step 3:
# Buat fungsi min_value yang menerima parameter list_attributes 
# (berupa data list) dan mengembalikan nilai terkecil dalam list_attributes

def min_value(list_attributes):
    min_attribute = 9999
    for attr in list_attributes:
        if int(attr) < min_attribute:
            min_attribute = int(attr)
        return min_attribute

def max_value(list_attributes):
    max_attribute = 9999
    for attr in list_attributes:
        if int(attr) > max_attribute:
            max_attribute = int(attr)
        return max_attribute

# Step 4
# Buat fungsi transform_attribute yang menerima parameter attr (sebuah bilangan)
# max_attr (sebuah bilangan) dan min_attr (sebuah bilangan)
# yang mengembalikan nilai transformasi dari sebuah attribute

def transform_attribute(attr, max_attr, min_attr):
    nilai_transformasi = (attr - min_attr) / (max_attr - min_attr)
    return nilai_transformasi

# Step 5
# Buat fungsi data_transformation yang menerima parameter list_of_dictionary
# sebuah list yang berisikan tipe data dictionary dan list_attribute_names
# sebuah list yang berisikan tipe data string mengembalikan hasil transformasi
# data dari list_of_dictionary berdasarkan list_attribute_names
# dan attr_info telah dispesifikasikan

def data_transformation(list_of_dictionary, list_attribute_names):
    attr_info = {}
    for attr_name in list_attribute_names:
        specified_attributes = get_all_specified_attribute(list_of_dictionary, attr_name)
        max_attr = max_value(specified_attributes)
        min_attr = min_value(specified_attributes)
        attr_info[attr_name] = {'max': max_attr, 'min': min_attr}
        data_idx = 0
        while(data_idx < len(list_of_dictionary)):
            list_of_dictionary[data_idx][attr_name] = transform_attribute(int(list_of_dictionary[data_idx][attr_name]), max_attr, min_attr)
            data_idx += 1
    return list_of_dictionary, attr_info

# Step 6
# Berdasarkan data baru dan attr_info ini, buat fungsi transform_data yang
# Menerima parameter data dan attr_info dan mengembalikan nilai attribut
# dari data baru yang telah di transformasikan.

def transform_data(data, attr_info):
	for key_name in data.keys():
		data[key_name] = (data[key_name] - attr_info[key_name]['min']) / (
		                  attr_info[key_name]['max'] - attr_info[key_name]['min'])
	return data

# step 7
# buat fungsi yang digunakan untuk sistem prediksi harga berdasarkan nilai kemiripan atribut

def abs_value(value):
    if value < 0:
        return -value
    else:
        return value

def price_based_on_similarity(data, list_of_data):
    prediksi_harga = 0
    perbedaan_terkecil = 999
    for data_point in list_of_data:
        perbedaan= abs_value(data['tanah'] - data_point['tanah'])
        perbedaan+= abs_value(data['bangunan'] - data_point['bangunan'])
        perbedaan+= abs_value(data['jarak_ke_pusat'] - data_point['jarak_ke_pusat'])
        if perbedaan < perbedaan_terkecil:
            prediksi_harga = data_point['harga']
            perbedaan_terkecil = perbedaan
        return prediksi_harga

# step 8
# Hitung harga rumah yang telah di transformasikan ke dalam variable
# harga_rumah berikut dengan atribut attr_info
harga_rumah, attr_info = data_transformation(harga_rumah,
                                             ['tanah','bangunan','jarak_ke_pusat'])

# Gunakan variable data untuk memprediksi harga rumah
data = {'tanah': 120, 'bangunan': 90, 'jarak_ke_pusat': 5}
# Transformasikan data tersebut dengan menggunakan attr_info yang telah diperoleh
# yang kembali disimpan ke variable data

data = transform_data(data, attr_info)

# Hitunglah prediksi harga dar variable data tersebut
harga = price_based_on_similarity(data, harga_rumah)
print("Prediksi harga rumah: ", harga)




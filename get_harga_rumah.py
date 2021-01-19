# Step 1:
# baca file "harga_rumah.txt"

file_harga_rumah = open("harga_rumah.txt", "r")
data_harga_rumah = file_harga_rumah.readlines()
file_harga_rumah.close()

#print(data_harga_rumah)
#print(data_harga_rumah[0].replace("\n", "").split(","))

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


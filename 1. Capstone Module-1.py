# Database
database =[{"id": 1, 
           "nama" : "Siti Badriah", 
           "NIK": "32.72.06.10.02.01.002",
           "tempat_tanggal_lahir" : "Sukabumi, 10 Februari 2001",
           "alamat" : "lembursitu, Sukabumi",
           "nomor_telepon" : "081-213-089-192",
           "jenis_kelamin" : "perempuan",
           "status_pernikahan" : "lajang",
           "golongan_darah" : "A",
           "sistem_pembayaran" : "BPJS",
           "diagnosis" : "perlu pembedahan"},
           {"id": 2, 
           "nama" : "Dewi Sandra", 
           "NIK": "31.71.61.30.09.98.001",
           "tempat_tanggal_lahir" : "Jakarta, 30 September 1998",
           "alamat" : "Gambir, Jakarta Pusat",
           "nomor_telepon" : "087-878-123-679",
           "jenis_kelamin" : "perempuan",
           "status_pernikahan" : "menikah",
           "golongan_darah" : "B",
           "sistem_pembayaran" : "asuransi",
           "diagnosis" : "perawatan"},
          {"id": 3, 
           "nama" : "Agus Hambali", 
           "NIK": "32.73.27.17.05.95.001",
           "tempat_tanggal_lahir" : "Bandung, 17 Mei 1995",
           "alamat" : "Gedebage, Bandung",
           "nomor_telepon" : "085-109-468-129",
           "jenis_kelamin" : "laki-laki",
           "status_pernikahan" : "menikah",
           "golongan_darah" : "AB",
           "sistem_pembayaran" : "asuransi",
           "diagnosis" : "rawat inap"},
           {"id": 4, 
           "nama" : "Widayanti", 
           "NIK": "31.71.04.08.04.03.003",
           "tempat_tanggal_lahir" : "Bogor, 08 April 2003",
           "alamat" : "Curug mekar, Bogor",
           "nomor_telepon" : "088-823-345-211",
           "jenis_kelamin" : "perempuan",
           "status_pernikahan" : "menikah",
           "golongan_darah" : "O",
           "sistem_pembayaran" : "BPJS",
           "diagnosis" : "perawatan"}]
# print('Data Pasien :', database)

def read():
    def filter_data(fn,nama,data):
        filtered_data = []
        for item in data:
            if(fn(nama,item)):
                filtered_data.append(item)

        return filtered_data

    def search_nama(nama,item):
        return nama.upper() in item.get('nama','').upper()

    input_nama = input('masukan nama : ')

    print(filter_data(search_nama,input_nama,database))
    pilihan()

def create():
    input_id = input('masukkan id :')
    input_nama = input('masukkan nama :')
    input_NIK = input('masukkan NIK :')
    input_tempat_tanggal_lahir = input('masukkan tempat tanggal lahir :')
    input_alamat = input('masukkan alamat :')
    input_nomor_telepon = input('masukkan nomor telepon :')
    input_jenis_kelamin = input('masukkan jenis kelamin :')
    input_status_pernikahan = input('masukkan status pernikahan :')
    input_golongan_darah = input('masukkan golongan darah :')
    input_sistem_pembayaran = input('masukkan sistem pembayaran :')
    input_diagnosis = input('masukkan diagnosis :')

    store_data ={
        "id":int(input_id),
        "nama":input_nama,
        "NIK":input_NIK,
        "tempat_tanggal_lahir":input_tempat_tanggal_lahir,
        "alamat":input_alamat,
        "nomor_telepon":input_nomor_telepon,
        "jenis_kelamin":input_jenis_kelamin,
        "status_pernikahan":input_status_pernikahan,
        "golongan_darah":input_golongan_darah,
        "sistem_pembayaran":input_sistem_pembayaran,
        "diagnosis":input_diagnosis,
    }
    
    global database
    database.append(store_data)
    pilihan() 
    
def update():
    def edit_kolom(id,kolom,value):
        global database
        for item in database:
            if(int(id) == item['id']):
                print('test')
                item[kolom] = value
        return 'berhasil merubah data'

    input_id = input('masukan id yang akan di ubah : ')
    print('kolom yang dapat di edit:')
    print("nama")
    print("NIK")
    print("tempat_tanggal_lahir")
    print("alamat")
    print("nomor_telepon")
    print("jenis_kelamin")
    print("status_pernikahan")
    print("golongan_darah")
    print("sistem_pembayaran")
    print("diagnosis")
    input_kolom = input('pilih angka kolom yang akan di input : ')
    input_value = input('masukan value baru : ')

    print(edit_kolom(input_id,input_kolom,input_value))
    pilihan()

def delete():
    def deleted_data(id):
        delete_data = []
        for item in database:
            if(int(id) != item['id']):
                delete_data.append(item)
        return delete_data
    input_id = input('masukan id yang akan di hapus : ')

    delete_data = deleted_data(input_id)
    global database
    database = delete_data
    print(database)
    print('data berhasil dihapus')
    pilihan()



def pilihan():
    print('1. create \n2. read\n3. update\n4. delete')
    input_option = input('pilih menu :')
    if(input_option == '1'):
        create()
    elif(input_option == '2'):
        read()
    elif(input_option == '3'):
        update()
    elif(input_option == '4'):
        delete()
    else:
        print('tidak ada pilihan itu')
        pilihan()

for item in database:
    print(item['nama'])
pilihan()
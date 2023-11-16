import re

listSiswa = [
    ['1A', 'Dangga', 'Pria', 98.0, 'A', 'Lulus'],
    ['4A', 'wilson', 'Pria', 100.0, 'A', 'Lulus'],
    ['3A', 'claudya', 'Wanita', 96.0, 'A', 'Lulus'],
    ['5A', 'Gandi', 'Pria', 45.0, 'E', 'Tidak Lulus']
]

# cart = ['','','', 0 , '', '']
cart = [] 
def daftarNilaiSiswa():
    print('-'* 12)
    print('1. Daftar Nilai Siswa')
    print('-'* 12)
    print("=" * 81)
    print('| NIM\t| Nama\t\t     | Gender\t| Nilai\t | Grade\t| Status\t|')
    for i in range(len(listSiswa)) :
        listSiswa.sort(key=lambda siswa: siswa[0]) 
        print('| {:5} | {:18} | {:8} | {:6} | {:12} | {:13} |'.format(listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
    print("=" * 81)
    try :
        while True :
            daftarLain = int(input('''
-------------------------------------------
|    List Lain yang Bisa di Lakukan :     |
|            1. Daftar Nilai Siswa        |
|            2. Rangking Siswa            |
|            3. Siswa yang Tidak Lulus    |
|            4. keluar                    |
-------------------------------------------
Masukkan angka sesuai list yang ingin dijalankan : '''))
            if daftarLain < 1 :
                print('\ninput harus berupa bilangan bulat! Contoh : [1-4]\n')
            elif(daftarLain == 1): 
                print('-'* 12)
                print('1. Daftar Nilai Siswa')
                print('-'* 12)
                print("=" * 81)
                print('| NIM\t| Nama\t\t     | Gender\t| Nilai\t | Grade\t| Status\t|')
                for i in range(len(listSiswa)) :
                    listSiswa.sort(key=lambda siswa: siswa[0])
                    print('| {:5} | {:18} | {:8} | {:6} | {:12} | {:13} |'.format(listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
                print("=" * 81)
            elif(daftarLain == 2):
                print('-'* 12)
                print('2. Rangking Siswa')
                print('-'* 12)
                print("=" * 89)
                print('| No | NIM\t| Nama\t\t     | Gender\t| Nilai\t | Grade\t| Status\t|')
                noUrut = 1
                for i in range(len(listSiswa)) :
                    listSiswa.sort(key=lambda siswa: siswa[3], reverse=True)
                    print('| {:2} | {:8} | {:18} | {:8} | {:6} | {:12} | {:13} |'.format(noUrut, listSiswa[i][0], listSiswa[i][1], listSiswa[i][2], listSiswa[i][3], listSiswa[i][4], listSiswa[i][5]))
                    noUrut += 1                            
                print("=" * 89)
            elif(daftarLain == 3):
                print('-'* 12)
                print('3. Siswa Yang Tidak Lulus')
                print('-'* 12)
                print("=" * 89)
                print('| No | NIM\t| Nama\t\t     | Gender\t| Nilai\t | Grade\t| Status\t|')
                siswaTidakLulus = False
                noUrut = 1
                for i in range(len(listSiswa)) :
                    if listSiswa[i][5] == 'Tidak Lulus':
                        siswaTidakLulus = True  # Setel flag ke True jika ada siswa yang tidak lulus
                        # Langsung tampilkan data siswa yang tidak lulus
                        print('| {:2} | {:8} | {:18} | {:8} | {:6} | {:12} | {:13} |'.format(noUrut, listSiswa[i][0], listSiswa[i][1], listSiswa[i][2], listSiswa[i][3], listSiswa[i][4], listSiswa[i][5]))
                        noUrut += 1  # Tingkatkan nomor urut setiap ada siswa yang tidak lulus
                print("=" * 89)
            elif(daftarLain == 4):
                break
            else:
                print("\ninput angka hanya bisa menerima angka [1-4]\n")
    except:
            print("\ninput angka hanya bisa menerima angka [1-4]\n")
def menambahDaftarSiswa():
    print('')
    checkDataInput = input('Apakah Anda Ingin Menginput Data Siswa (Y/N) :').upper()
    if checkDataInput == 'Y':
        while True :
            nimSiswa = input('Masukkan NIM Mahasiswa : ').upper()
            if any(j.isalpha() for j in nimSiswa) and any(j.isdigit() for j in nimSiswa):
                break
            elif nimSiswa.isdigit():
                print("\nNIM tidak boleh hanya berisi angka\n")
            elif nimSiswa.isalpha():
                print("\nNIM tidak boleh hanya berisi huruf\n")
            else:
                print('\nNIM siswa hanya terdiri dari Angka dan Huruf\n')
                       
        while True :
            namaSiswa = input('Masukkan Nama Siswa : ').lower()
            if all(k.isalpha() or k.isspace() for k in namaSiswa) :
                namaSiswa = namaSiswa.title()
                break
            elif namaSiswa.isdigit():
                print("\nNama tidak boleh berisi angka\n")
            else:
                print('\nNama siswa hanya terdiri dari huruf dan spasi\n')
            
        while True :
            genderSiswa = input('Masukkan Gender Siswa (Pria/Wanita): ').title()
            if genderSiswa == 'Pria':
                genderSiswa = 'Pria'
                break
            elif genderSiswa == 'Wanita':
                 genderSiswa = 'Wanita'
                 break
            else:
                print('Hanya Menerima Input Pria Dan wanita')

        while True:
            try:
                nilaiSiswa = float(input('Masukkan Nilai Siswa : '))
                    
                grade = ''
                status = ''
                if nilaiSiswa > 100:
                    print('Nilai Tidak Boleh Lebih dari 100')
                elif(nilaiSiswa >= 90 and nilaiSiswa <= 100) :
                    grade = 'A'
                    status = 'Lulus'
                    print('Grade = {} status = {}'.format(grade, status))
                    break
                elif(nilaiSiswa >= 85 and nilaiSiswa < 90) :
                    grade = 'A-'
                    status = 'Lulus'
                    print('Grade = {} status = {}'.format(grade, status))
                    break
                elif(nilaiSiswa >= 80 and nilaiSiswa < 85):
                    grade = 'B'
                    status = 'Lulus'
                    print('Grade = {} status = {}'.format(grade, status))
                    break
                elif(nilaiSiswa >= 75 and nilaiSiswa < 80) :
                    grade = 'B-'
                    status = 'Lulus'
                    print('Grade = {} status = {}'.format(grade, status))
                    break
                elif(nilaiSiswa >= 70 and nilaiSiswa < 75) :
                    grade = 'C'
                    status = 'Lulus'
                    print('Grade = {} status = {}'.format(grade, status))
                    break
                elif(nilaiSiswa >= 65 and nilaiSiswa < 70) :
                    grade = 'D'
                    status = 'Lulus'
                    print('Grade = {} status = {}'.format(grade, status))
                    break
                elif(nilaiSiswa >= 40 and nilaiSiswa < 65) :
                    grade = 'E'
                    status = 'Tidak Lulus'
                    print('Grade = {} status = {}'.format(grade, status))
                    break    
                elif(nilaiSiswa >= 0 and nilaiSiswa <40) :
                    grade = 'F'
                    status = 'Tidak Lulus'
                    print('Grade = {} status = {}'.format(grade, status))
                    break
                else:
                    print('Nilai adalah bilangan bulat!')
            except:
                print ("Input harus berupa angka, silahkan masukan ulang!")

        listSiswa.append([nimSiswa,namaSiswa,genderSiswa,nilaiSiswa, grade, status])
        print('-'* 12)
        print('Daftar Siswa Yang Telah Diperbarui')
        print('-'* 12)
        print("=" * 81)
        print('| NIM\t| Nama\t\t     | Gender\t| Nilai\t | Grade\t| Status\t|')
        for i in range(len(listSiswa)) :
            listSiswa.sort(key=lambda siswa: siswa[0])
            print('| {:5} | {:18} | {:8} | {:6} | {:12} | {:13} |'.format(listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
        print("=" * 81)
    elif checkDataInput.isdigit():
        print('Tidak boleh angka, pilih huruf Y = Yes / N = No')
            
    else:
        print('Pilih Y = yes / N = No') 
def mengupdateDataSiswa():
    print('-'* 12)
    print('Daftar Siswa')
    print('-'* 12)
    print("=" * 89)
    print('| No.| NIM\t| Nama  \t| Gender\t| Nilai\t | Grade\t| Status\t|')
    for i in range(len(listSiswa)) :
        listSiswa.sort(key=lambda siswa: siswa[0])
        print('|{:3} | {:8} | {:13} | {:13} | {:6} | {:12} | {:13} |'.format(i,listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
    print("=" * 89)
    checkDataUpdate = input("Apakah anda ingin Mengupdate data Siswa (Y/N) :").upper()
    if checkDataUpdate == 'Y':
        while True :
            try :
                noSiswa = int(input('Masukkan No Siswa yang ingin di update : '))
                noSiswaDiTemukan = False
                for i in range(len(listSiswa)):
                    if(noSiswa == i) :
                        noSiswaDiTemukan = True
                        cart = list(listSiswa[noSiswa])
                        print("=" * 65)
                        print('Siswa ditemukan Sekarang Anda Bisa Merubah Datanya')
                        print("=" * 81) 
                        print('| {:5} | {:13} | {:13} | {:6} | {:12} | {:13} |'.format(listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
                        print("=" * 81)
                        print("")
                                
                        print('-' * 40)
                        checkUpdate = input('Ingin Melanjutkan Update Data Siswa (Y/N) :').upper()
                        print('-' * 40)
                        if checkUpdate == 'Y':
                            while True:
                                dataSiswa = input('''
    --------------------------------------
    |     * Data yang ingin di update: *  |
    |           1. Nama Siswa             |
    |           2. Gender Siswa           |
    |           3. Nilai Siswa            |
    |           4. Selesai                |
    |           5. Batal Update           |
    --------------------------------------
    Masukkan angka yang ingin dijalankan : ''')
                                print("--------------------------------------")
                                if(dataSiswa == '1'):
                                    while True :
                                        inputNama = input('Masukkan Nama Siswa : ').lower()
                                        if all(k.isalpha() or k.isspace() for k in inputNama) :
                                            inputNama = inputNama.title()
                                            cart[1] = inputNama
                                            break
                                        elif inputNama.isdigit():
                                            print("\nNama tidak boleh berisi angka\n")
                                        else:
                                            print('\nNama siswa hanya terdiri dari huruf dan spasi\n')
                                elif(dataSiswa == '2'):
                                    while True :
                                        inputGender = input('Masukkan Gender Siswa (Pria/Wanita): ').title()
                                        if inputGender == 'Pria':
                                            inputGender = 'Pria'
                                            cart[2] = inputGender
                                            break
                                        elif inputGender == 'Wanita':
                                            inputGender = 'Wanita'
                                            cart[2] = inputGender
                                            break
                                        else:
                                            print('Hanya Menerima Input Pria Dan wanita')
                                elif(dataSiswa == '3'):   
                                    while True :
                                        try :    
                                            inputNilai = float(input("Masukan Nila Siswa :"))

                                            grade = ''
                                            status = ''
                                            if inputNilai > 100 :
                                                print('Nilai tidak boleh lebih dari 100')
                                            elif(inputNilai >= 90 and inputNilai <= 100) :
                                                grade = 'A'
                                                status = 'Lulus'
                                                print('Grade = {} status = {}'.format(grade, status))
                                                cart[3] = inputNilai
                                                cart[4] = grade
                                                cart[5] = status
                                                break
                                            elif(inputNilai >= 85 and inputNilai < 90) :
                                                grade = 'A-'
                                                status = 'Lulus'
                                                print('Grade = {} status = {}'.format(grade, status))
                                                cart[3] = inputNilai
                                                cart[4] = grade
                                                cart[5] = status
                                                break
                                            elif(inputNilai >= 80 and inputNilai < 85):
                                                grade = 'B'
                                                status = 'Lulus'
                                                print('Grade = {} status = {}'.format(grade, status))
                                                cart[3] = inputNilai
                                                cart[4] = grade
                                                cart[5] = status
                                                break
                                            elif(inputNilai >= 75 and inputNilai < 80) :
                                                grade = 'B-'
                                                status = 'Lulus'
                                                print('Grade = {} status = {}'.format(grade, status))
                                                cart[3] = inputNilai
                                                cart[4] = grade
                                                cart[5] = status
                                                break
                                            elif(inputNilai >= 70 and inputNilai < 75) :
                                                grade = 'C'
                                                status = 'Lulus'
                                                print('Grade = {} status = {}'.format(grade, status))
                                                cart[3] = inputNilai
                                                cart[4] = grade
                                                cart[5] = status
                                                break
                                            elif(inputNilai >= 65 and inputNilai < 70) :
                                                grade = 'D'
                                                status = 'Lulus'
                                                print('Grade = {} status = {}'.format(grade, status))
                                                cart[3] = inputNilai
                                                cart[4] = grade
                                                cart[5] = status
                                                break
                                            elif(inputNilai >= 40 and inputNilai < 65) :
                                                grade = 'E'
                                                status = 'Tidak Lulus'
                                                print('Grade = {} status = {}'.format(grade, status))
                                                cart[3] = inputNilai
                                                cart[4] = grade
                                                cart[5] = status
                                                break    
                                            elif(inputNilai > 0 and inputNilai < 40) :
                                                grade = 'F'
                                                status = 'Tidak Lulus'
                                                print('Grade = {} status = {}'.format(grade, status))
                                                cart[3] = inputNilai
                                                cart[4] = grade
                                                cart[5] = status
                                                break
                                            else:
                                                print('Nilai harus bilangan bulat!') 
                                        except:
                                            print ("Input harus berupa angka, silahkan masukan ulang!")
                                elif(dataSiswa == '4'):
                                    listSiswa[noSiswa] = list(cart)
                                    print('-'* 12)
                                    print('| Daftar Siswa Terbaru |')
                                    print('-'* 12)
                                    print("=" * 81)
                                    print('| NIM\t| Nama  \t| Gender\t| Nilai\t | Grade\t| Status\t|')
                                    for i in range(len(listSiswa)) :
                                        listSiswa.sort(key=lambda siswa: siswa[0])
                                        print('| {:5} | {:13} | {:13} | {:6} | {:12} | {:13} |'.format(listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
                                    print("=" * 81)
                                    break
                                elif(dataSiswa == '5'):
                                    print("Update di batalkan")
                                    cart.clear()
                                    break
                                else:
                                    print('Pilihan Terbatas antara [1-5]')
                        else:
                            cart.clear()
                            break
                            
                if not noSiswaDiTemukan:
                    print('') 
                    print('Nomor siswa tidak ditemukan apa yang anda ingin rubah pada siswa')
                    print('')
                        
                print('-'* 12)
                print('Daftar Siswa')
                print('-'* 12)
                print("=" * 89)
                print('| No.| NIM\t| Nama  \t| Gender\t| Nilai\t | Grade\t| Status\t|')
                for i in range(len(listSiswa)) :
                    listSiswa.sort(key=lambda siswa: siswa[0])
                    print('|{:3} | {:8} | {:13} | {:13} | {:6} | {:12} | {:13} |'.format(i,listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
                print("=" * 89)    

            except : 
                print('-' * 60)   
                print('Input hanya berupa angka sesuai dengan nomor yang tersedia!')
                print('-'* 60)
                print('Daftar Siswa')
                print('-'* 12)
                print("=" * 89)
                print('| No.| NIM\t| Nama  \t| Gender\t| Nilai\t | Grade\t| Status\t|')
                for i in range(len(listSiswa)) :
                    listSiswa.sort(key=lambda siswa: siswa[0])
                    print('|{:3} | {:8} | {:13} | {:13} | {:6} | {:12} | {:13} |'.format(i,listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
                print("=" * 89)
            break
    elif checkDataUpdate.isdigit():
        print('Tidak boleh angka, pilih huruf Y = Yes / N = No')
    else:
        print('pilih huruf Y = Yes / N = No')
        
        
def menghapusDataSiswa():
    print('-'* 12)
    print('Daftar Siswa')
    print('-'* 12)
    print("=" * 89)
    print('| No.| NIM\t| Nama  \t| Gender\t| Nilai\t | Grade\t| Status\t|')
    for i in range(len(listSiswa)) :
        listSiswa.sort(key=lambda siswa: siswa[0])
        print('|{:3} | {:8} | {:13} | {:13} | {:6} | {:12} | {:13} |'.format(i,listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
    print("=" * 89)
    checkDataDelete = input('Apakah Anda Ingin Menghapus Data pada Mahasiswa (Y/N)').upper()
    if checkDataDelete == 'Y':
        try:
            noSiswaDel = int(input('Masukkan No. Siswa yang ingin dihapus : '))
            noSiswaDiTemukan1 = False
            for i in range(len(listSiswa)):
                if(noSiswaDel == i) :
                    noSiswaDiTemukan1 = True
                    cart = list(listSiswa[noSiswaDel])
                    print("=" * 65)
                    print('Siswa ditemukan Sekarang Anda Bisa Menghapus Datanya')
                    print("=" * 81) 
                    print('| {:5} | {:13} | {:13} | {:6} | {:12} | {:13} |'.format(listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
                    print("=" * 81)
                    print("")
                                
                    print('-' * 40)
                    checkUpdate = input('Ingin Melanjutkan Menghapus Data Siswa (Y/N) :').upper()
                    print('-' * 40)
                    if checkUpdate == 'Y':
                        del listSiswa[noSiswaDel]
                    else:
                        continue
            if not noSiswaDiTemukan1:
                print('') 
                print('Nomor siswa tidak ditemukan apa yang anda ingin rubah pada siswa')
                print('')
        except:
            print ('Hanya boleh memasukkan angka, Sesuaikan dengan nomor siswa!')

        print('-'* 12)
        print('Daftar Siswa Baru')
        print('-'* 12)
        print("=" * 89)
        print('| NIM\t| Nama  \t| Gender\t| Nilai\t | Grade\t| Status\t|')
        for i in range(len(listSiswa)) :
            listSiswa.sort(key=lambda siswa: siswa[0])
            print('| {:5} | {:13} | {:13} | {:6} | {:12} | {:13} |'.format(listSiswa[i][0],listSiswa[i][1],listSiswa[i][2],listSiswa[i][3],listSiswa[i][4],listSiswa[i][5]))
        print("=" * 89)
            
    elif checkDataDelete.isdigit():
        print('Tidak boleh angka, pilih huruf Y = Yes / N = No')
    else:
        print('pilih huruf Y = Yes / N = No')

def pilihanMenu():
    return "\ninput harus berupa bilangan bulat! Contoh : [1-5]\n"
while True :
    try:
        pilihanMenu = int(input('''
-------------------------------------------
|           *  Database Siswa *           |
|                                         |
|         List Yang Bisa di Lakukan :     |
|            1. Daftar Nilai Siswa        |
|            2. Menambah Daftar Siswa     |
|            3. Mengupdate Data Siswa     |
|            4. Menghapus Data Siswa      |
|            5. Exit Program              |
-------------------------------------------  
Masukkan angka sesuai list yang ingin dijalankan : '''))
        
        if pilihanMenu < 1 :
            print("\ninput harus berupa bilangan bulat! Contoh : [1-5]\n")
        elif(pilihanMenu == 1) :
            daftarNilaiSiswa()
        elif(pilihanMenu == 2) :
            menambahDaftarSiswa()
        elif(pilihanMenu == 3) :
            mengupdateDataSiswa()
        elif(pilihanMenu == 4) :
            menghapusDataSiswa()
        elif(pilihanMenu == 5):
            break
        else:
            print("\ninput angka hanya tersedia : [1-5]\n")
    except:
        print('')
        print('==ERROR==')
        print('Silahkan Pilih List menggunakan angka yang sesuai dengan List!')
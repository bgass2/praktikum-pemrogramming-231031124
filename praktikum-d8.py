pwd_benar = 'sistem'
pwd_benar2 = 'informasi'
pwd_benar3 = 'kelas23d'

def cekpass(id_password, password, page):
    limit = 3
    i = 0
    while i < limit:
        pwd = input(f'Masukkan Password {id_password} untuk Halaman {page}= ')
        if pwd == password:  
            print(f'Password Benar, Selamat Datang di Halaman {page}')
            return True
        else:
            i += 1
            if i == limit:
                print('Kesempatan Anda Habis!')
                return False
            else:
                print(f'Password Salah. Kesempatan anda tersisa {limit - i} kali')

# Tes password pertama
tes1 = cekpass('pertama', 'sistem', 1)
if tes1:
    # Tes password kedua
    tes2 = cekpass('kedua', 'informasi', 2)
    if tes2:
        # Tes password ketiga
        tes3 = cekpass('ketiga', 'kelas23d', 3)
        if tes3:
            print('Selamat Anda Berhasil Login')

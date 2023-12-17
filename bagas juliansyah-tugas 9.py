
print('\n')
biodata = { 'nama'  : 'Bagas Juliansyah',
'nim'   : '231031124',
'kelas' : 'S123D',
'tempat,tanggal lahir' : 'parepare,23 julii 2005',
'jenis kelamin' : 'laki-laki',
'agama' : 'islam',
'alamat': 'JL.Pareang BLK P.Sumpang Minange',
'email' : 'orangbaikk04@gmail.com'
}

print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:5])
print(selected_biodata)





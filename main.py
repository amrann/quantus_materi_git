import luas
import volume
import luas_kubus_balok
import volume_kubus_balok
import luastabung_limassegitiga
import volumetabung_limassegitiga

def test_luas_segitiga():
    result = luas.LuasSegititiga()
    assert result.hitung(10,5)==23 , 'perhitungan salah'
    assert result.hitung(10,-5)==25 , 'input salah'

def test_luas_prisma_segitiga():
    luas_prismasegitiga = luas.PrismaSegitiga()
    hasil = luas_prismasegitiga.hitung(6, 7, 5, 3, 4)
    print ("Luas Prisma Segitiga = ", hasil)

def test_volume_prisma_segitiga():
    volume_prismasegitiga = volume.VolumePrismaSegitiga()
    hasil = volume_prismasegitiga.hitung(6, 7)
    print("Volume Prisma Segitiga = ", hasil)
    
def test_luas_kubus():
    result = luas_kubus_balok.LuasKubus()
    assert result.hitung_LuasKubus(6)==216, 'perhitungan salah'
    print("Luas Kubus = ", result.hitung_LuasKubus(6))

def test_luas_balok():
    result = luas_kubus_balok.LuasBalok()
    assert result.hitung_LuasBalok(3, 4, 5)==94, 'perhitungan salah'
    print("Luas Balok = ", result.hitung_LuasBalok(3, 4, 5))

def test_volume_kubus():
    result = volume_kubus_balok.VolumeKubus()
    assert result.hitung_VolumeKubus(5)==125, 'perhitungan salah'
    print("Volume Kubus = ", result.hitung_VolumeKubus(5))

def test_volume_balok():
    result = volume_kubus_balok.VolumeBalok()
    assert result.hitung_VolumeBalok(3, 4, 5)==60, 'perhitungan salah'
    print("Volume Balok = ", result.hitung_VolumeBalok(3, 4, 5))
    
def test_luas_tabung():
    result = luastabung_limassegitiga.LuasTabung()
    assert result.hitung(10,5)==942
#     assert result.hitung(10,-5)==25 , 'input luas tabung salah'

def test_luas_limassegitiga():
    result = luastabung_limassegitiga.LuasLimasSegitiga()
    assert result.hitung(10,10,10,10,10,10,10,10)==200
#     assert result.hitung(10,10,10,10,10,10,10,10)==25 , 'input luas limas segitiga salah'
    
def test_volume_tabung():
    result = volumetabung_limassegitiga.VolumeTabung()
    assert result.hitung(10,2)==628
#     assert result.hitung(10,-5)==25 , 'input volume tabung salah'

def test_volume_limassegitiga():
    result = volumetabung_limassegitiga.VolumeLimasSegitiga()
    assert result.hitung(3, 4, 100)==198
#     assert result.hitung(3,4, 100)==25 , 'input volume limas segitiga salah'

#test_luas_segitiga()
test_luas_prisma_segitiga()
test_volume_prisma_segitiga()

#test_kubus_balok
test_luas_kubus()
test_luas_balok()
test_volume_kubus()
test_volume_balok()

test_luas_tabung()
test_luas_limassegitiga()
test_volume_tabung()
test_volume_limassegitiga()

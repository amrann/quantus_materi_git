import luas
import volume
import luas_kubus_balok
import volume_kubus_balok


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

#test_luas_segitiga()
test_luas_prisma_segitiga()
test_volume_prisma_segitiga()

#test_kubus_balok
test_luas_kubus()
test_luas_balok()
test_volume_kubus()
test_volume_balok()
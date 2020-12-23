import luas
import luas_kubus_balok
import volume_kubus_balok

def test_luas_segitiga():
    result = luas.LuasSegititiga()
    assert result.hitung(10,5)==25 , 'perhitungan salah'
    assert result.hitung(10,-5)==25 , 'input salah'

def test_luas_kubus():
    result = luas_kubus_balok.LuasKubus()
    assert result.hitung_LuasKubus(6)==216, 'perhitungan salah'

def test_luas_balok():
    result = luas_kubus_balok.LuasBalok()
    assert result.hitung_LuasBalok(3, 4, 5)==94, 'perhitungan salah'

def test_volume_kubus():
    result = volume_kubus_balok.VolumeKubus()
    assert result.hitung_VolumeKubus(5)==125, 'perhitungan salah'

def test_volume_balok():
    result = volume_kubus_balok.VolumeBalok()
    assert result.hitung_VolumeBalok(3, 4, 5)==60, 'perhitungan salah'



test_luas_segitiga()
test_luas_kubus()
test_luas_balok()
test_volume_kubus()
test_volume_balok()
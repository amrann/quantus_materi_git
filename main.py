import luastabung_limassegitiga
import volumetabung_limassegitiga


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

test_luas_tabung()
test_luas_limassegitiga()
test_volume_tabung()
test_volume_limassegitiga()
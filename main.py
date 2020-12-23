import luas


def test_luas_segitiga():
    result = luas.LuasSegititiga()
    assert result.hitung(10,5)==25 , 'perhitungan salah'
    assert result.hitung(10,-5)==25 , 'input salah'

test_luas_segitiga()
#!/usr/bin/env python
# coding: utf-8

# In[7]:


import luas_kerucut_dan_bola
import volume_kerucut_dan_bola


# In[9]:


def test_luas_kerucut():
    result = luas_kerucut_dan_bola.LuasKerucut()
    assert result.hitung(7,15)==483.56, 'perhitungan salah'
    assert result.hitung(7,-15)==483.56, 'input salah'

def test_luas_bola():
    result = luas_kerucut_dan_bola.Luasbola()
    assert result.hitung(5)==314, 'perhitungan salah'
    assert result.hitung(-5)==314, 'input salah'

def test_volume_kerucut():
    result = volume_kerucut_dan_bola.VolumeKerucut()
    assert result.hitung(3,10)==94.2, 'perhitungan salah'
    assert result.hitung(3,-10)==94.2, 'input salah'

def test_volume_bola():
    result = volume_kerucut_dan_bola.VolumeBola()
    assert result.hitung(3)==113.04, 'perhitungan salah'
    assert result.hitung(-3)==113.04, 'input salah'


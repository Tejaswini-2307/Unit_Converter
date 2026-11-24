from converter import km_to_m, kg_to_g, m_to_cm


def test_km_to_m_whole_number():
    assert km_to_m(1) == 1000


def test_km_to_m_decimal():
    assert km_to_m(2.5) == 2500


def test_kg_to_g_whole_number():
    assert kg_to_g(1) == 1000


def test_kg_to_g_decimal():
    assert kg_to_g(0.5) == 500


def test_m_to_cm_whole_number():
    assert m_to_cm(1) == 100


def test_m_to_cm_zero():
    assert m_to_cm(0) == 0
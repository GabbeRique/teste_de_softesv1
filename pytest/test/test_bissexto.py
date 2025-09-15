from app.bissexto import anobissexto

def test_bissexto2000():
    assert anobissexto(2000) == True
def test_bissexto2004():
    assert anobissexto(2004) == True
def test_bissexto2008():
    assert anobissexto(2008) == True
def test_bissexto2015():
    assert anobissexto(2015) == False
def test_bissexto2025():
    assert anobissexto(2025) == False
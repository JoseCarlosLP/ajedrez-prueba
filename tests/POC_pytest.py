import pytest
from ajedrezoo import metapieza

def test_metapieza():
    ob = metapieza(10, 2, "c")  # Se ejecuta el constructor de metapieza
    assert ob.casx == 10  # Verificar que el atributo x sea 10
    assert ob.casy == 2   # Verificar que el atributo y sea 2
    assert ob.color == "c"  # Verificar que el atributo color sea "c"


if __name__ == '_main_':
    pytest.main()
import pytest
from ajedrezoo import metapieza
from unittest.mock import MagicMock, patch


class TestMovrey:

    @pytest.fixture
    def setup_rey(self):
        from ajedrezoo import metarey
        return metarey(5, 1, 1)


    @patch('ajedrezoo.torrenegra')
    @patch('ajedrezoo.torreblanca')
    def test_rey_movido_sin_enroque(self, mock_torreblanca, mock_torrenegra, setup_rey):
        mock_torrenegra[2].movida = 0
        mock_torreblanca[2].movida = 0
        mock_torrenegra[1].movida = 0
        mock_torreblanca[1].movida = 0

        rey = setup_rey
        rey.movida = 1  # Avisamos que el rey se movió

        # Mockeamos las llamadas a otras funciones que tiene la funcion y especificamos el valor a retornar
        metapieza.movdiagonal = MagicMock(return_value=[])
        metapieza.movlineal = MagicMock(return_value=[])

        assert rey.movrey() == []

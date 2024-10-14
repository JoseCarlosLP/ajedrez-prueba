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
        torres_blancas = [0, MagicMock(movida=0), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=0), MagicMock(movida=0)]

        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        rey = setup_rey
        rey.movida = 1  # Avisamos que el rey se movió

        # Mockeamos las llamadas a otras funciones que tiene la funcion y especificamos el valor a retornar
        metapieza.movdiagonal = MagicMock(return_value=[])
        metapieza.movlineal = MagicMock(return_value=[])

        assert rey.movrey() == []

    @patch('ajedrezoo.torrenegra')
    @patch('ajedrezoo.torreblanca')
    @patch('ajedrezoo.cocupadas')
    def test_no_puede_enrocar_a_ningun_lado(self, mock_cocupadas, mock_torreblanca, mock_torrenegra, setup_rey):
        torres_blancas = [0, MagicMock(movida=1), MagicMock(movida=0)]
        torres_negras = [0, MagicMock(movida=1), MagicMock(movida=0)]

        mock_torrenegra.__getitem__.side_effect = torres_negras.__getitem__
        mock_torreblanca.__getitem__.side_effect = torres_blancas.__getitem__

        rey = setup_rey
        # Mockeamos las llamadas a otras funciones que tiene la funcion y especificamos el valor a retornar
        metapieza.movdiagonal = MagicMock(return_value=[])
        metapieza.movlineal = MagicMock(return_value=[])

        matriz_cocupadas = [[0] * 8 for _ in range(8)]
        matriz_cocupadas[rey.casy][rey.casx + 2] = 1

        mock_cocupadas.__getitem__.side_effect = matriz_cocupadas.__getitem__

        assert rey.movrey() == []

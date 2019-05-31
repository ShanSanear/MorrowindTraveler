import pytest

from traveler import City, Traveler, Stronghold


class TestTraveler:

    def test_balmora_ald_ruhn_directly_connected(self):
        traveler = Traveler()
        assert traveler.are_directly_connected(City.BALMORA, City.ALD_RUHN)

    def test_balmora_maar_gan_not_directly_connected(self):
        traveler = Traveler()
        assert not traveler.are_directly_connected(City.BALMORA, City.MAAR_GAN)

    def test_ald_ruhn_vivec_not_directly_connected(self):
        traveler = Traveler()
        assert not traveler.are_directly_connected(City.ALD_RUHN, City.VIVEC)

    def test_balmora_maar_gan_connected(self):
        traveler = Traveler()
        ret_val = traveler.are_connected(City.BALMORA, City.MAAR_GAN)
        assert ret_val

    def test_balmora_maar_gan_route(self):
        traveler = Traveler()
        expected_travel_route = [City.BALMORA, City.ALD_RUHN, City.MAAR_GAN]
        assert traveler.find_shortest_path(City.BALMORA, City.MAAR_GAN) == expected_travel_route

    def test_khuul_ald_ruhn_route(self):
        traveler = Traveler()
        expected_travel_route = [City.KHUUL, City.ALD_RUHN]
        assert traveler.find_shortest_path(City.KHUUL, City.ALD_RUHN) == expected_travel_route

    def test_shortest_path_khuul_ald_ruhn(self):
        traveler = Traveler()
        expected_travel_route = [City.KHUUL, City.ALD_RUHN]
        assert traveler.find_shortest_path(City.KHUUL, City.ALD_RUHN) == expected_travel_route

    def test_shortest_path_gnisis_seyda_neen(self):
        traveler = Traveler()
        expected_travel_route = [City.GNISIS, City.SEYDA_NEEN]
        assert traveler.find_shortest_path(City.GNISIS, City.SEYDA_NEEN) == expected_travel_route

    def test_shortest_path_gnisis_molag_mar(self):
        traveler = Traveler()
        expected_travel_route = [City.GNISIS, City.SEYDA_NEEN, City.VIVEC, City.MOLAG_MAR]
        expected_travel_route_2 = [City.GNISIS, City.ALD_RUHN, City.VIVEC, City.MOLAG_MAR]
        route = traveler.find_shortest_path(City.GNISIS, City.MOLAG_MAR)
        assert route == expected_travel_route or route == expected_travel_route_2

    def test_shortest_path_maar_gan_falasmaryon(self):
        traveler = Traveler()
        expected_travel_route = [City.MAAR_GAN, City.ALD_RUHN, City.CALDERA, Stronghold.FALASMARYON]
        assert traveler.find_shortest_path(City.MAAR_GAN, Stronghold.FALASMARYON) == expected_travel_route

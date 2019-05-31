from collections import defaultdict
from enum import Enum, auto


class TravelType(Enum):
    GUILD_GUIDE = auto()
    SILT_STRIDER = auto()
    BOAT = auto()
    PROPYLON = auto()


class Traveler:
    def __init__(self):
        self.__silt_strider_graph = {
            City.BALMORA: (
                City.SURAN, City.SEYDA_NEEN, City.VIVEC, City.ALD_RUHN
            ),
            City.ALD_RUHN: (
                City.BALMORA, City.MAAR_GAN, City.GNISIS
            ),
            City.MAAR_GAN: (
                City.GNISIS, City.KHUUL, City.ALD_RUHN
            ),
            City.KHUUL: (
                City.GNISIS, City.ALD_RUHN, City.MAAR_GAN
            ),
            City.GNISIS: (
                City.KHUUL, City.MAAR_GAN, City.ALD_RUHN, City.SEYDA_NEEN
            ),
            City.SURAN: (
                City.SEYDA_NEEN, City.VIVEC, City.MOLAG_MAR, City.BALMORA
            ),
            City.VIVEC: (
                City.SURAN, City.MOLAG_MAR, City.SEYDA_NEEN
            ),
            City.MOLAG_MAR: (
                City.VIVEC, City.SURAN
            ),
            City.SEYDA_NEEN: (
                City.BALMORA, City.GNISIS, City.VIVEC, City.SURAN
            )
        }
        self.__propylon_graph = {
            City.CALDERA: (Stronghold.FALASMARYON, Stronghold.FALENSARANO, Stronghold.VALENVARYON, Stronghold.ROTHERAN,
                           Stronghold.INDORANYON, Stronghold.TELASERO, Stronghold.MARANDUS, Stronghold.HLORMAREN,
                           Stronghold.ANDASRETH, Stronghold.BERANDAS),
            Stronghold.VALENVARYON: (City.CALDERA, Stronghold.ROTHERAN, Stronghold.FALASMARYON),
            Stronghold.ROTHERAN: (City.CALDERA, Stronghold.INDORANYON, Stronghold.VALENVARYON),
            Stronghold.INDORANYON: (City.CALDERA, Stronghold.ROTHERAN, Stronghold.FALENSARANO),
            Stronghold.FALENSARANO: (City.CALDERA, Stronghold.INDORANYON, Stronghold.TELASERO),
            Stronghold.TELASERO: (City.CALDERA, Stronghold.FALENSARANO, Stronghold.MARANDUS),
            Stronghold.MARANDUS: (City.CALDERA, Stronghold.TELASERO, Stronghold.HLORMAREN),
            Stronghold.HLORMAREN: (City.CALDERA, Stronghold.MARANDUS, Stronghold.ANDASRETH),
            Stronghold.ANDASRETH: (City.CALDERA, Stronghold.HLORMAREN, Stronghold.BERANDAS),
            Stronghold.BERANDAS: (City.CALDERA, Stronghold.ANDASRETH, Stronghold.FALASMARYON),
            Stronghold.FALASMARYON: (City.CALDERA, Stronghold.BERANDAS, Stronghold.VALENVARYON)
        }
        self.__boat_graph = {
            City.FORT_FROSTMOTH: [City.KHUUL],
            City.KHUUL: [City.FORT_FROSTMOTH, City.GNAAR_MOK, City.DAGON_FEL],
            City.GNAAR_MOK: [City.KHUUL, City.HLA_OAD],
            City.HLA_OAD: [City.GNAAR_MOK, City.VIVEC, City.EBONHEART, City.MOLAG_MAR],
            City.VIVEC: [City.MOLAG_MAR, City.TEL_BRANORA, City.EBONHEART, City.HLA_OAD],
            City.EBONHEART: [City.HLA_OAD, City.VIVEC, City.TEL_BRANORA, City.SADRITH_MORA],
            City.MOLAG_MAR: [City.VIVEC, City.HLA_OAD, City.TEL_BRANORA],
            City.TEL_BRANORA: [City.EBONHEART, City.VIVEC, City.MOLAG_MAR, City.SADRITH_MORA],
            City.SADRITH_MORA: [City.TEL_BRANORA, City.EBONHEART, City.TEL_MORA, City.DAGON_FEL],
            # Yes, there is no connection to Vos (??)
            City.TEL_MORA: [City.SADRITH_MORA, City.TEL_ARUHN, City.VOS, City.DAGON_FEL],
            City.VOS: [City.SADRITH_MORA, City.TEL_MORA, City.TEL_ARUHN],
            City.TEL_ARUHN: [City.VOS, City.TEL_MORA, City.DAGON_FEL],
            City.DAGON_FEL: [City.TEL_MORA, City.TEL_ARUHN, City.SADRITH_MORA],
        }
        self.__guild_guide_graph = {
            City.CALDERA: {City.ALD_RUHN, City.SADRITH_MORA, City.BALMORA, City.VIVEC},
            City.VIVEC: {City.ALD_RUHN, City.SADRITH_MORA, City.BALMORA, City.CALDERA},
            City.BALMORA: {City.ALD_RUHN, City.SADRITH_MORA, City.VIVEC, City.CALDERA},
            City.SADRITH_MORA: {City.ALD_RUHN, City.BALMORA, City.VIVEC, City.CALDERA},
            City.ALD_RUHN: {City.SADRITH_MORA, City.BALMORA, City.VIVEC, City.CALDERA}
        }

        self.__complete_graph = self.__generate_complete_graph()
        self._edges = self.__generate_edges()

    def are_directly_connected(self, start, stop):
        strider = self.__silt_strider_graph.get(start, [])
        propylon = self.__propylon_graph.get(start, [])
        boat = self.__boat_graph.get(start, {start: []})
        guild_guide = self.__boat_graph.get(start, [])
        return stop in strider or stop in propylon or stop in boat or stop in guild_guide

    def are_connected(self, start, stop):
        paths = self.find_all_paths(start, stop)
        for path in paths:
            if stop in path:
                return True
        return False

    def find_all_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.__complete_graph:
            return []
        paths = []
        for node in self.__complete_graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_shortest_path(self, start, end):
        paths = self.find_all_paths(start, end)
        return min(paths, key=len)

    def __generate_edges(self):
        edges = defaultdict(list)
        for vertex, connections in self.__complete_graph.items():
            for neighbour in connections:
                edges[vertex].append(neighbour, )
        return edges

    def __generate_complete_graph(self):
        complete_graph = defaultdict(list)
        possibilities = [self.__silt_strider_graph, self.__boat_graph, self.__guild_guide_graph, self.__propylon_graph]
        for graph in possibilities:
            for key, values in graph.items():
                complete_graph[key].extend(values)
        return complete_graph


class TravelPoint(Enum):
    pass


class City(TravelPoint):
    BALMORA = auto()
    KHUUL = auto()
    ALD_RUHN = auto()
    MAAR_GAN = auto()
    SEYDA_NEEN = auto()
    SURAN = auto()
    SADRITH_MORA = auto()
    VIVEC = auto()
    CALDERA = auto()
    GNISIS = auto()
    MOLAG_MAR = auto()
    TEL_BRANORA = auto()
    EBONHEART = auto()
    HLA_OAD = auto()
    GNAAR_MOK = auto()
    DAGON_FEL = auto()
    TEL_MORA = auto()
    VOS = auto()
    TEL_ARUHN = auto()
    FORT_FROSTMOTH = auto()


class Stronghold(TravelPoint):
    FALASMARYON = auto()
    VALENVARYON = auto()
    ROTHERAN = auto()
    INDORANYON = auto()
    FALENSARANO = auto()
    TELASERO = auto()
    MARANDUS = auto()
    HLORMAREN = auto()
    ANDASRETH = auto()
    BERANDAS = auto()

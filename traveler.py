from collections import defaultdict
from enum import Enum, auto

from graphs import SILT_STRIDER_GRAPH, PROPYLON_GRAPH, BOAT_GRAPH, GUILD_GUIDE_GRAPH


class TravelType(Enum):
    GUILD_GUIDE = auto()
    SILT_STRIDER = auto()
    BOAT = auto()
    PROPYLON = auto()


class Traveler:
    def __init__(self):
        self.__silt_strider_graph = SILT_STRIDER_GRAPH
        self.__propylon_graph = PROPYLON_GRAPH
        self.__boat_graph = BOAT_GRAPH
        self.__guild_guide_graph = GUILD_GUIDE_GRAPH

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
                edges[vertex].append(neighbour)
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

from enum import Enum, auto


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
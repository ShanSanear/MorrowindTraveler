from travel_points import City, Stronghold

PROPYLON_GRAPH = {
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
SILT_STRIDER_GRAPH = {
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
BOAT_GRAPH = {
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
GUILD_GUIDE_GRAPH = {
            City.CALDERA: {City.ALD_RUHN, City.SADRITH_MORA, City.BALMORA, City.VIVEC},
            City.VIVEC: {City.ALD_RUHN, City.SADRITH_MORA, City.BALMORA, City.CALDERA},
            City.BALMORA: {City.ALD_RUHN, City.SADRITH_MORA, City.VIVEC, City.CALDERA},
            City.SADRITH_MORA: {City.ALD_RUHN, City.BALMORA, City.VIVEC, City.CALDERA},
            City.ALD_RUHN: {City.SADRITH_MORA, City.BALMORA, City.VIVEC, City.CALDERA}
        }

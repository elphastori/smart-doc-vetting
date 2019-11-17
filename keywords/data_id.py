from models import Vision
from models import WebEntity

web_entities = [
    WebEntity("Identity document", 0.3383621871471405),
    WebEntity("Forehead", 0.23234780132770538),
    WebEntity("Currency", 0.21133612096309662),
    WebEntity("Document", 0.19699999690055847),
    WebEntity("Identity", 0.19169999659061432),
    WebEntity("V7J", 0.17900000512599945),
    WebEntity("Meter", 0.1777999997138977)
]

text = "REPUBLICA DE ANGOLA\nPASSAPORTE/PASSPORT\nTipo/ Type\nCodgo do Pals/Cany Code\nAGO\nPasporte/Ppat\nN2510156\nPN\nApeido/ Sunaine\nSILVA\nNome/ Given naes\nDANIELA TANARY CRISTOV\u00c3O DA\nEstado ch/Matus\nS\nProfisso/Occupedon\nESTUDANTE\nNacionalidadel Nationaty\nNumo Pesl P\n0073408/N06/10\nANGOLANA\nDala de nascimento/ Dale of beh\nSe/Sex\nascmanto/Fce of beh\n22 MAR /MAR 2000 LUANDA\nF\nDala de emlo l D of\neisslo/Place of\nSME LUANDA\n06 JUN /JUN 2019\nvdo Das of expry\nAssinalura da Entdade isso/ nng Autharty's Sire\n06 JUN /JUN 2024\nPNAGOSILVA<<DANIELA<TANARY <CRISTOVA 0< DA<<<<<\nN2510156 3AGO0003229F24060640073408<NO6<1042\n"

id_result = Vision(web_entities, text)
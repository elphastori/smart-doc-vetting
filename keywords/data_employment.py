from models import Vision
from models import WebEntity

web_entities = [
    WebEntity("Document", 0.39422914385795593),
    WebEntity("South Africa", 0.2865000069141388),
    WebEntity("Parliament of South Africa", 0.21490000188350677),
    WebEntity("Line", 0.2103281021118164),
    WebEntity("Brand", 0.1994093954563141),
    WebEntity("Meter", 0.17839999496936798)
]

text = "HUMAN RESOURCES\nPARLIAMENT\nPO Box 15 Cape Town 8000 Republic of South Africa\nTel: 27 (21) 403 2911\nwww.parliament.gov.za\nOF THE REPUBLIC OF SOUTH AFRICA\nP/Ms. TA Mabasa\n8 November 2019\nEmployee No.: 13893\nTO WHOM IT MAY CONCERN: CONFIRMATION\nOF EMPLOYMENT\nThis letter serves to inform you that Ms.Tirhani Abigail Mabasa, ID 7209220335087, is a\npermanent employee of Parliament of the Republic of South Africa as a Language\nPractitioner: Language Services Section since 01 September 2019.\nWe further confirm that she receives an all-inclusive package of R 521 729.00 per year,\nwhich she structures according to her needs.\nFor any further queries please contact, Nqabomzi Andreka at (021) 403-8091 or at\nnandreka@parliament.gov.zza\nMENI OFREFO8IC OF\nYours faithfully\n0 8 NOV 2019\nreta\nHUMAN RESOURCES\nFor MANAGER: HUMAN RESOURCES SERVICES\nAFCA\n"

employment = Vision(web_entities, text)
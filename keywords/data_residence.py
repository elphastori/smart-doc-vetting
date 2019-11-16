from models import Vision
from models import WebEntity

web_entities = [
    WebEntity("", 0.39079999923706055,
    WebEntity("8ta", 0.28630000352859497),
    WebEntity("Telkom", 0.2842000126838684),
    WebEntity("Organization", 0.213968887925148}),
    WebEntity("Web page", 0.20840270817279816),
    WebEntity("Mobile phone", 0.18060000240802765),
    WebEntity("Contract", 0.17749999463558197),
    WebEntity("Product", 0.14560000598430634),
    WebEntity("Invoice", 0.14090000092983246),
    WebEntity("Product design", 0.13640211522579193),
]

text = "Telkom\nStatement\nMRS. LISA LUXTON MCINTYRE\n30 DUNSTER AV\nFISH HOEK\nFISH HOEK\nStatement date\n09 Oct 2019\n7975\nAccount no\n337097524\nEFT Ref No\n0033160005030597774\nAccount summary\nReference\nAmount\nDate\nDescription\nBalance brought forward\nR 865.63\n09 Sep 2019\n3602473\nR 1,200.00\nPayment: Thank You\n04 Sep 2019\n6100672\nR 1,000.00\nPayment: Thank You\n04 Oct 2019\nSubtotal\n-R 1,334.37\nInvoice for October\n09 Oct 2019\nA117659851\nR 1,239.46\nSubscription & usage for 0217820738\nSubscription & usage for 0217820738_1\nFixed Voice BB and I\nR 231.69\nFixed Voice BB and I\nR 428.73\nTIAII Access Uncappe\nSubscription & usage for TIN2582148\nTotal due\nR 579.04\n-R 94.91\n-R 94.91\nDue by 31 Oct 2019\nMAKE THE SMART CHOICE AND MOVE TO\nSMARTBROADBAND WIRELESS!\nGet super-fast, reliable, wireless internet with FREE WiFi router.\nTelkom SA SOC Ltd. Reg office: Telkom Park, The Hub, 61 Oak Avenue, Centurion, 0157.Comp Reg No 1991/005476/30.VAT No 4680101146\nDo not detach this portion from this Statement page\nPayment information\nAmount due\n-R 94.91\n00331600050305977740600000000000\nPayment code\n7774\n\u0421ycle\nGroup no\n00331\nControl code\nSystem no\n6000503059\n060\n<<<<< 9 2021 0033 0005 0305 74 >>>>>\nPage 1 of 4\n"

residence = Vision(web_entities, text)
from models import Vision
from models import WebEntity

web_entities = [
    WebEntity("Screenshot", 0.3131629228591919),
    WebEntity("Product design", 0.26272037625312805),
    WebEntity("Bank", 0.243599995970726),
    WebEntity("Design", 0.2150000035762787),
    WebEntity("Product", 0.21230000257492065),
    WebEntity("Line", 0.21158140897750854),
    WebEntity("", 0.19609999656677246),
    WebEntity("F.N.B. Corporation", 0.19609999656677246),
    WebEntity("Meter", 0.17790000140666962)
]

text = "05/11/2019\nFNB Verified Statement\nCarlswald\nReference Number:\nVODSWRV4974F\nPostnet Suite 94,P rivate Bag X121\nHalfway House ,1685\n250117\nTo verify this statement, please keep the above reference number and the client's\nID number/business account number on hand. Visit www.fnb.co.za, select Contact\nus Tools on the menu, followed by Verify Statement and follow the on-screen\nFNB\nBranch Code\ninstructions. The reference number is valid for a minimum of 3 months.\nCustomer VAT Registration Number Not Provided\nBank VAT Registration Number 4210102051\nFirst National Bank\nhow can we help you?\nCopy Tax Invoice/S tatement Number 113\nStatement Period : 20 September 2019 to 19 October 2019\nStatement Date 19 October 2019\nBBST113\n015111\nMISS TIRHANI A MABASA\nPO BOX 10359\nVORNA VALLEY\n1686\nFNB\nTIRHANI@HOTMAIL.COM\nFirst Notional Bank\n05 NOV 2019\nStatements\n250-655\nFNB Private Clients Cheque Account 62274946163\nSummary in Rand\nZAR\nOpening Balance\nFunds Received (Credits)\nCash Deposits\nOther Deposits\n23,835.56 Dr\nContact us\n54,220.73 Cr\n0.00\n0.00\nThabo Sabeka\ne-Mail\nthabo.sabeka@ fnb.co.za\n(087) 736-6801\nfnb.co.za\nTelephone Number\nWeb\nInter-Account Transfers In\n12,550.00 Cr\n41,670.73 Cr\nE lectronic Payments Received\nDebit Interest Rates (NCA)\nP rime Linked 21.50% - Rebate (If applicable)\nFunds Used (Debits)\nCash Withdrawals (Branch)\nCash Withdrawals (Other)\nCheques Processed (Non Cash)\nDebit Orders/S cheduled Payments\nAccount Payments\nInter-Account Transfers Out\nCard Purchases (S wipes)\nFuel Purchases\n34,200.21 Dr\n0.00\n65\n0\n3\n0\n2,300.00 Dr\n0.00\n1,086.07 Dr\n12,568.00 Dr\n13,175.00 Dr\n5,071.14 Dr\n0.00\n6\n22\n16\n18\n0\nBank Charges\nService Fees\n874.95 Dr\n670.00 Dr\n0.00\nCash Deposit Fees\nCash Handling Fees\nO ther Fees\n0\n0\n0.00\n204.95 Dr\n3\nOther Entries\n0\nInterest on Credit Balance\n0.00\nInterest on Debit Balance\n377.61 Dr\n1\nInward Unpaid Items\nUnpaid Cheques and Debits\nRefunds/Adjustments\n0\n0\n0\n0.00\n0.00\n0.00\nClosing Balance\n5,067.60 Dr\n23,100.00\n1,000.00\nOverdraft Limit\nMonthly Reduction Amount\nPricing Option: Your account is currently on the Bundled pricing option. For more information, please Contact Us or visit our website\nPage 1 of 4\nDelivery Method E1 R04\nEN/20/NV/DDA 30\n1089\nBranch Number\nAccount Number\nDate\nDDA 30/0R/94/KM/KM/PA/P 6/A6/QH/Y\nFNORA\n19/10/19\nFNB Private Clients Cheque Account\n1089\n62274946163\n47827\nCSFZFN0:62274946163\nLON O\nom\nOHO OO\n"

bank = Vision(web_entities, text)
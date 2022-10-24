#MAIN FUNCTION

from venv import create
from xml.dom.minidom import Document
from process_invoices import  dbInvoices
from invoiceToDocx_Sub import invoiceToDocx

def makeInvoiceByLocation(clientInfo):
    #checkLocation and print the invoice with the correct footer.
    match clientInfo["Location"]:
        case "ES":
            #call invoiceToDocx to create the actually docX
            pass
            invoiceToDocx(clientInfo)
        case "EU":
            #pass
            invoiceToDocx(clientInfo)
        case "OEU":
            invoiceToDocx(clientInfo)



# convierte en diccionario
for i in range(len(dbInvoices)):
    clientInfo = dbInvoices.iloc[i].to_dict()
    #if clientInfo["SaleGift"] == "Promo":
    makeInvoiceByLocation(clientInfo)
    #Need to take clientInfo and fill up the Invoice
    


    
    


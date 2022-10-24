#FUNCION THAT ACTUALLY EXPORT THE DOCX taking the info

#from docx import Document
from docxtpl import DocxTemplate

eu_text = "*Entrega intercomunitaria exenta en virtud de la aplicación del articulo 25 de la ley 37/1992"
outeu_text = "*Entrega Exportación de bienes exenta en virtud de la aplicación de el articulo 21 de la ley 37/1992 LIVA"
def templateInv(document,info):
    print(document)
def invoiceToDocx(info):
    """
    Values on the DOCX
    Num_Invoice
    Invoice_Date
    Name
    CifNif
    quantity
    UnitPrice
    Total_Unit
    shipCost
    Total_Shipping
    Total_Tax
    textBottom
    """
    textBottom = ""
    iva = ""
    total_Tax = 0
    totalAmount = info["Total"]
    if info["Location"] == "EU":
        textBottom = eu_text
        total_Tax = str(totalAmount) + " €"
    elif info["Location"] == "OEU":
        textBottom = outeu_text
        total_Tax = str(totalAmount) + " €"
    elif info["Location"] == "ES":
        iva = "21%"
        total_Tax = str(round(float(totalAmount.replace(',','.'))*1.21, 2)) + ' €'
    else:
        print("Location in Invoice number {} is empty",info["Num"])
    #Alternative method docxtpl
    doc = DocxTemplate("Template_Invoice/Template_Invoice.docx")
    #Conditional Text Button
    #UGLY WAY TO DO IT 
    print(total_Tax)
    print(info["Total"])
    context = { 'num_invoice' : info["Num"],
             'invoice_Date' : info["Date"],
             'gift' : info["SaleGift"], 
             'name' : info["Name"], 
             'cifNif' : info["Dni"],
             'country' : info["Country"], 
             'quantity' : info["Quantity"], 
             'unitPrice' : "",
             'cost' : info["Cost"],
             'shipCost' : info["Shipping"],
             'total_Shipping' : str(totalAmount) + "€",
             'total_Tax' : total_Tax, 
             'textBottom' : textBottom }
    print(info["Num"])
    doc.render(context)
    doc.save('InvoicesDone/{}-{}.docx'.format(info["Num"],info["Name"]))

#STATUS ALL FILLED AND TEXT BUTTOM SET UP ONLY NEED TO APPLY TO ESP INVOICE. AND SORT OUT TOTAL.
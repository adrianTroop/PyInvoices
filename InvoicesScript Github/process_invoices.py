from typing_extensions import Self
from yaml import ValueToken
from read_invoices import values
import pandas as pd

#transale it into a more readable format.
#check how to turn value to dictionary
#add name to the columns
df =pd.DataFrame(values, columns=["Num", 
                                    "Date",
                                     "Name",
                                     "Dni",
                                     "Service", 
                                     "Num_Packages", 
                                     "Tracking", 
                                     "Location", 
                                     "Country", 
                                     "SaleGift", 
                                     "Paid", 
                                     "Quantity", 
                                     "Notes", 
                                     "Shipping", 
                                     "Cost", 
                                     "Total"])
#filtro somo campos necesarios
dbInvoices = df[["Num", 
                "Date", 
                "Name", 
                "Dni", 
                "Location", 
                "Country", 
                "SaleGift", 
                "Quantity", 
                "Shipping", 
                "Cost", 
                "Total"
                ]]


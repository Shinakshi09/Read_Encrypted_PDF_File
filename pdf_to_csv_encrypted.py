import pdfplumber
import re
import pandas as pd
from collections import namedtuple

all_text = ''
with pdfplumber.open('C:/Users/navod/PycharmProjects/pythonProject/customer.pdf', password="Raghav@23") as pdf:
    for pdf_page in pdf.pages:
        single_page_text = pdf_page.extract_text(y_tolerance=1)
        # print(single_page_text)
        # separate each page's text with newline
        all_text = all_text + '\n' + single_page_text
        #print(all_text)
        Line = namedtuple('Line', 'Schemes Date Transaction Amount Units Price Unit_Balance')

        company_re = re.compile(r'(^\d+[A-Z].*)')
        schemes_re = re.compile(r'(^[A-Z][0-9].*)')
        schemes_re_1 = re.compile(r'(^\w+\-\w+\s\w+\s\w+\s\w+\s\w+\s\-\s.*)')
        num = re.compile(r'(^\d+\-\w+\s\w+\s\w+\s\w+\s\w.*)')

        line_re = re.compile(
            r'(\d{2}-\w{3}-\d{4}) ([A-Za-z ].*) (.*[\d,]+\.\d{2}.*) (.*[\d,]+\.\d{3}.*) ([\d,]+\.\d{2}.*) ([\d,]+\.\d{2})')
        lines_1 = []

        for line in all_text.split("\n"):
            comp = company_re.search(line)
            sch = schemes_re.search(line)
            sch_1 = schemes_re_1.search(line)
            sap = line_re.search(line)
            num_1 = num.search(line)
            if comp:
                Schemes = comp.group(1)
            elif sch:
                Schemes = sch.group(1)
            elif sch_1:
                Schemes = sch_1.group(1)
            elif num_1:
                Schemes = num_1.group(1)
            elif sap:
                # print(line)
                Date = sap.group(1)
                Transaction = sap.group(2)
                Amount = sap.group(3)
                Units = sap.group(4)
                Price = sap.group(5)
                Unit_Balance = sap.group(6)

                lines_1.append(Line(Schemes, Date, Transaction, Amount, Units, Price, Unit_Balance))

df = pd.DataFrame(lines_1)
print(df)
#print(df.isnull().sum())
df[["schemes_no","schemes_1"]]=df.Schemes.str.split("-",n=1,expand=True)
df[["schemes_name","Adv_1"]]=df.schemes_1.str.split("-",n=1,expand=True)
df[["growth_type","advisor"]]=df.Adv_1.str.split("(",n=1,expand=True)
#df.head()
df1=df.drop(["schemes_1","Adv_1"],axis=1)
#print(df1.head())
#df1.to_csv("pdf_data.csv")

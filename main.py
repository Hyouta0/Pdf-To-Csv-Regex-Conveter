from PyPDF2 import PdfReader
import re

def pdfToCsv(path,**kwargs):
    strPDF=''
    with open(path,'rb') as fs:
        reader= PdfReader(fs)
        pdf=reader.pages
        for idx in range(len(pdf)):
            strPDF+=pdf[idx].extract_text()

    print("Data Extracted From PDF ...")
    has_comma=re.compile(r'\w+,')
    data=re.findall(kwargs['pattern'],strPDF,re.M)
    csvPath=path.replace('pdf','csv')
    csv=''
    csv+=kwargs.get('hdr','')
    for line in data:
        text=''
        for idx in range(len(line)):
            if(has_comma.search(line[idx])==None):
                text+=line[idx]
            else:
                text+='"'+line[idx]+'"'
            if(idx == len(line)-1):
                text+='\n'
            else:
                text+=','
        csv+=text
    with open(csvPath,'w') as p:
        p.write(csv)
    print('Done')





def main():
    hdr = 'sr no,date,partyname,account no,prefix,unkonwon,unknown,Domination,barnch,tellerPay\n'
    pattern = r'(\d+) (\d{2}/\w{3}/\d{4}) ((?:\(? ?[A-Z]+,? ?\)?\(? ?)+)(\*+\d+) ([A-Z]{2}) (\d+) ([\d+,?]+) (\d+) (\d+)'

    pdfToCsv('encashment.pdf',pattern=pattern)

if __name__ =="__main__":
    main()
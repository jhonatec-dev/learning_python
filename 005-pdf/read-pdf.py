import PyPDF2 as pyf
# import tabulapy

filename = 'DANFE.pdf'

arquivo = pyf.PdfFileReader(filename)  # abre o arquivo
print(arquivo.documentInfo)  # imprime as informações do arquivo
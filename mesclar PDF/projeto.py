import PyPDF2
import os

mesclar = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("documentos")
lista_arquivos.sort()
print(lista_arquivos)


for documento in lista_arquivos:
    if ".pdf" in documento:
        mesclar.append(f"documentos/{documento}")

mesclar.write("PDF Final.pdf")
# merging pdf files

from PyPDF2 import PdfMerger

merger = PdfMerger()

doc1_path = '../fake_path/doc1.pdf'
doc2_path = '../fake_path/doc2.pdf'
doc3_path = '../fake_path/doc3.pdf'
doc4_path = '../fake_path/doc4.pdf'

doc1 = open(doc1_path, "rb")
doc2 = open(doc2_path, "rb")
doc3 = open(doc3_path, "rb")
doc4 = open(doc4_path, "rb")

merger.append(doc1)
merger.append(doc2)
merger.append(doc3)
merger.append(doc4)

output = open(
    "/Users/mac/Documents/Canada Documents/merged-document.pdf", "wb"
)
merger.write(output)

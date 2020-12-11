import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
watermark = PyPDF2.PdfFileReader(open(sys.argv[2], 'rb'))
watermarkedpdf = PyPDF2.PdfFileWriter()


for i in range(template.getNumPages()):
	pg = template.getPage(i)
	pg.mergePage(watermark.getPage(0))
	watermarkedpdf.addPage(pg)

	with open('watermarked.pdf', 'wb') as file:
		watermarkedpdf.write(file)
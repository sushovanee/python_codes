# import urllib3
# import PyPDF2
# #from pyPdf import PdfFileWriter, PdfFileReader
# #from StringIO import StringIO
# # from pyPdf import PdfFileWriter, PdfFileReader
# # from StringIO import StringIO
#
# url = "https://www.mohfw.gov.in/pdf/Districtreporting429.pdf"
#
# # http = urllib3.PoolManager()
#
#
# # r = http.request('GET', url)
#
# pdfFileObj = open(url, 'rb')
# reader = PyPDF2.PdfFileReader(pdfFileObj)
#
# print(reader.numPages)

from urllib3 import urlopen
from pyPdf import PdfFileWriter, PdfFileReader
from StringIO import StringIO

url = "https://www.mohfw.gov.in/pdf/Districtreporting429.pdf"
writer = PdfFileWriter()

remoteFile = urlopen(Request(url)).read()
memoryFile = StringIO(remoteFile)
pdfFile = PdfFileReader(memoryFile)

for pageNum in xrange(pdfFile.getNumPages()):
        currentPage = pdfFile.getPage(pageNum)
        #currentPage.mergePage(watermark.getPage(0))
        writer.addPage(currentPage)


outputStream = open("output.pdf","wb")
writer.write(outputStream)
outputStream.close()

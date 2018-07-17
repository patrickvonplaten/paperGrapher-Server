import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams

caching=True

rsrcmgr = PDFResourceManager(caching=caching)
outfp = sys.stdout
laparams = LAParams()
device = TextConverter(rsrcmgr, outfp, codec='utf-8', laparams=laparams, imagewriter=None)
pagenos=set()
fname = sys.argv[1]
fp = file(fname, 'rb')
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.get_pages(fp, pagenos, maxpages=0, password='', caching=caching, check_extractable=True):
    interpreter.process_page(page)
fp.close()
device.close()

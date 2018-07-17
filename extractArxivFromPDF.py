import pdfx # https://github.com/metachris/pdfx
import re

paper_name = "WaveNetPaper.pdf"

pdf = pdfx.PDFx(paper_name)
metadata = pdf.get_metadata()

references_dict = pdf.get_references_as_dict()
print("--> All references : ", references_dict)

arxiv_ref = references_dict['arxiv']
print("--> raw arxiv refs : ", arxiv_ref)

# make sure to keep only real arxiv identifiers
# https://arxiv.org/help/arxiv_identifier
arxiv_id_regex = '[0-9]{4}.[0-9]{4,5}'	

arxiv_ref = [ref for ref in arxiv_ref if re.match(arxiv_id_regex, ref)]

print("--> real arxiv refs : ", arxiv_ref)

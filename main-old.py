#need fpdf package installed
from fpdf import FPDF
#orientation P is page
pdf = FPDF(orientation='P', unit='mm' , format = 'A4')
pdf.add_page()
pdf.set_font(family='Times',style='B' , size=12)
#ln parameter is line break , 0 or 1, 0 is no line break. h is cell height
pdf.cell(w= 0, h=12, txt= "Hello there!" ,ln=1, align='L', border=0)
pdf.set_font(family='Times', size=8)
pdf.cell(w= 0, h=12, txt= "hi there!" ,ln=1, align='L', border=1)

pdf.add_page()
pdf.output('output.pdf')
#need fpdf package installed
from fpdf import FPDF
import pandas as pd
def createHorizontalLine(startY):
    pdf.set_text_color(100, 100, 100)
    for y in range(startY, 285, 10):
        pdf.line(10, y, 200, y)  # add line
pdf = FPDF(orientation='P', unit='mm' , format = 'A4') #unit sets page size in millimeters
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    pdf.add_page()

    #set header and underline
    pdf.set_text_color(100,100,100)
    pdf.set_font(family='Times',style='B' , size=24)
    pdf.cell(w= 0, h=12, txt= row['Topic'] ,ln=1, align='L', border=0)

    #set footer for first page of each top
    pdf.ln(265) #adds break linne
    pdf.set_font(family='Times',style='I' , size=8)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=10, txt= row['Topic'] , align='R', border=0)
    createHorizontalLine(21)
    for i in  range(row['Pages'] - 1):
        pdf.add_page()
        #set footer for insuing pages
        pdf.ln(277)  # adds break linne
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row['Topic'] ,align='R', border=0)
        createHorizontalLine(10)

pdf.output('output.pdf')
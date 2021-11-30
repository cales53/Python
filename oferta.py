from reportlab.lib import fonts
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import itertools
from random import randint
from statistics import mean
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet

pdfmetrics.registerFont(ttfonts.TTFont("Arial", "Fuentes/arial.ttf"))

def nuevodocumento():
    print('nuevo documento')
    my_text = "<font fontName=Arial size=12> De conformidad con su solicitud y atendiendo a la información y necesidades topológicas específicas suministradas por ustedes, nos permitimos presentar la siguiente:</font>"

    doc = SimpleDocTemplate("example_flowable.pdf",pagesize=A4,
                            rightMargin=2*cm,leftMargin=2*cm,
                            topMargin=2*cm,bottomMargin=2*cm)

    doc.build([Paragraph(my_text.replace("\n", "<br />"), getSampleStyleSheet()['Normal']),])

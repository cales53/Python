from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import itertools
from random import randint
from statistics import mean
from reportlab.pdfbase import pdfmetrics, ttfonts
pdfmetrics.registerFont(ttfonts.TTFont("Arial", "Fuentes/arial.ttf"))


w, h = letter
c = canvas.Canvas("hola-mundo.pdf", pagesize=letter)
text = c.beginText(50, h - 50)
text.setFont("Arial", 12)
text.textLines("De conformidad con su solicitud y atendiendo a la información y necesidades topológicas específicas suministradas por ustedes, nos permitimos presentar la siguiente: ")
text.setTextOrigin(50,50)
c.drawText(text)
c.showPage()
c.save()
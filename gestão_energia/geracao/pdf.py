from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
# Creating Canvas
c = canvas.Canvas("invoice.pdf",pagesize=pagesizes.A4,bottomup=0)
# Logo Section
# Setting th origin to (10,40)
c.translate(30,80)
# Inverting the scale for getting mirror Image of logo
c.scale(1,-1)
# Inserting Logo into the Canvas at required position
c.drawImage("logo.jpg",0,0,width=50,height=30)
# Title Section
# Again Inverting Scale For strings insertion
c.scale(1,-1)
# Again Setting the origin back to (0,0) of top-left
c.translate(-10,-40)
# Setting the font for Name title of company
c.setFont("Helvetica-Bold",20)
# Inserting the name of the company
c.drawCentredString(165,20,"CW Gestão Energia")
# For under lining the title
c.line(70,22,260,22)
# Changing the font size for Specifying Address
c.setFont("Helvetica-Bold",10)
c.drawCentredString(165,35,"Charles Wilis Cunha Garcia")
c.drawCentredString(165,45,"charles.wilis@gmail.com")
# Changing the font size for Specifying GST Number of firm
c.setFont("Helvetica-Bold",8)
c.drawCentredString(165,55,"31 99926-8659")
# Line Seprating the page header from the body
c.line(5,58,555,58)
# Document Information
# Changing the font for Document title
c.setFont("Courier-Bold",9.5)
c.drawCentredString(252,68,"Faturamento de Energia Elétrica Injetada")
# This Block Consist of Costumer Details
c.roundRect(15,85,525,60,10,stroke=1,fill=0)
c.setFont("Times-Bold",10)
c.drawRightString(100,100,"Mês da leitura :")
c.drawRightString(154,100,"abril" + " / " + "2022")
c.drawRightString(420,100,"Instalação :")
c.drawRightString(475,100,"3004078633")
c.drawRightString(100,113,"Vencimento :")
c.drawRightString(150,113,"11/05/2022")
c.drawRightString(100,126,"Cliente :")
c.drawRightString(250,126,"Josué Figueiredo Silva") 
c.drawRightString(100,139,"Endereço :")
c.drawRightString(280,139,"RUA GOITACAZES 375 LJ 1")
c.roundRect(15,150,260,250,10,stroke=1,fill=0)
c.setFont("Courier-Bold",9.5)
c.drawCentredString(150,160,"Simulação sem energia fotovoltaica")
c.roundRect(280,150,260,250,10,stroke=1,fill=0)
c.setFont("Times-Bold",10)
c.drawRightString(80,180,"Consumo:")
c.drawRightString(130,180,"304" + " KWh")
c.drawRightString(240,180,"R$ "+"341,33")
c.drawRightString(123,195,"Iluminação Pública:")
c.drawRightString(240,195,"R$ "+"42,07")
c.drawRightString(145,210,"Custo de disponibilidade:")
c.drawRightString(240,210,"R$ "+"0")
c.drawRightString(115,300,"Total da Conta:")
c.drawRightString(240,300,"R$ "+"293,40")


c.drawCentredString(400,160,"Simulação COM energia fotovoltaica")
c.drawRightString(345,180,"Energia solar")
c.drawRightString(393,180,"284" + " KWh")
c.drawRightString(520,180,"R$ "+"341,33")
c.drawRightString(374,195,"Iluminação Pública:")
c.drawRightString(520,195,"R$ "+"42,07")
c.drawRightString(396,210,"Custo de disponibilidade:")
c.drawRightString(440,210,"20" + " KWh")
c.drawRightString(520,210,"R$ "+"56,14")


#c.drawRightString("RUA GOITACAZES 375 LJ 1")
# This Block Consist of Item Description
'''
c.roundRect(15,108,170,75,10,stroke=1,fill=0)
c.roundRect(15,188,170,75,10,stroke=1,fill=0)
c.roundRect(15,108,170,130,10,stroke=1,fill=0)
c.line(15,120,185,120)
c.drawCentredString(25,118,"SR No.")
c.drawCentredString(75,118,"GOODS DESCRIPTION")
c.drawCentredString(125,118,"RATE")
c.drawCentredString(148,118,"QTY")
c.drawCentredString(173,118,"TOTAL")
# Drawing table for Item Description
c.line(15,210,185,210)
c.line(35,108,35,220)
c.line(115,108,115,220)
c.line(135,108,135,220)
c.line(160,108,160,220)
# Declaration and Signature
c.line(15,220,185,220)
c.line(100,220,100,238)
c.drawString(20,225,"We declare that above mentioned")
c.drawString(20,230,"information is true.")
c.drawString(20,235,"(This is system generated invoive)")
c.drawRightString(180,235,"Authorised Signatory")
# End the Page and Start with new
'''
c.showPage()
# Saving the PDF
c.save()

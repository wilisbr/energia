from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.lib.colors import Color, black, blue, red

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
c.drawCentredString(165,35,"charles.wilis@gmail.com")
# Changing the font size for Specifying GST Number of firm
c.setFont("Helvetica-Bold",8)
c.drawCentredString(165,45,"31 99926-8659")
# Line Seprating the page header from the body
c.line(5,58,555,58)
# Document Information
# Changing the font for Document title
c.setFont("Courier-Bold",9.5)
c.drawCentredString(252,68,"Faturamento de Energia Elétrica Injetada")
# This Block Consist of Costumer Details
c.roundRect(15,85,525,60,10,stroke=1,fill=0)
c.setFont("Times-Bold",10)
c.drawRightString(100,100,"Mês da referencia :")
c.drawRightString(154,100,"abril" + " / " + "2022")
c.drawRightString(420,100,"Instalação :")
c.drawRightString(475,100,"3004078633")
c.drawRightString(100,113,"Vencimento :")
c.drawRightString(150,113,"11/05/2022")
c.drawRightString(100,126,"Cliente :")
c.drawRightString(250,126,"Josué Figueiredo Silva") 
c.drawRightString(100,139,"Endereço :")
c.drawRightString(280,139,"RUA GOITACAZES 375 LJ 1")
c.drawRightString(480,139,"Desconto negociado no kwh: "+ "20" + "%")
c.roundRect(15,150,260,220,10,stroke=1,fill=0)
c.setFont("Courier-Bold",11)
c.drawCentredString(150,160,"Simulação SEM energia fotovoltaica")
c.roundRect(280,150,260,220,10,stroke=1,fill=0)
c.setFont("Times-Bold",10)
c.drawRightString(80,180,"Consumo:")
c.drawRightString(130,180,"304" + " KWh")
c.drawRightString(190,180,"x "+"R$ "+"1,123")
c.drawRightString(250,180,"R$ "+"341,33")
c.drawRightString(123,195,"Iluminação Pública:")
c.drawRightString(250,195,"R$ "+"42,07")
c.drawRightString(145,210,"Custo de disponibilidade:")
c.drawRightString(250,210,"R$ "+"0")
c.drawRightString(115,300,"Total da Conta:")
c.drawRightString(250,300,"R$ "+"393,40")


c.setFont("Times-Bold",40)
red50transparent = Color( 0, 0, 0, alpha=0.3)
c.setFillColor(red50transparent)
c.rotate(45)
c.drawRightString(400,100,"Simulação")
c.rotate(-45)
red50transparent = Color( 0, 0, 0, alpha=1)
c.setFillColor(red50transparent)


c.setFont("Courier-Bold",11)
c.drawCentredString(400,160,"Fatura COM energia fotovoltaica")
c.setFont("Times-Bold",10)
c.drawRightString(345,180,"Energia solar")
c.drawRightString(393,180,"284" + " KWh")
c.drawRightString(450,180,"x "+"R$ "+"0,898")
c.drawRightString(520,180,"R$ "+"341,33")
c.drawRightString(374,195,"Iluminação Pública:")
c.drawRightString(520,195,"R$ "+"42,07")
c.drawRightString(396,210,"Custo de disponibilidade:")
c.drawRightString(440,210,"20" + " KWh")
c.drawRightString(520,210,"R$ "+"56,14")
c.drawRightString(318,225,"Bônus:")
c.drawRightString(520,225,"-R$ "+"20,00")
c.drawRightString(335,300,"Economia:")
c.drawRightString(393,300,"13" + "%")
c.drawRightString(520,300,"R$ "+ "50,09")
c.drawRightString(350,320,"Total a pagar:")
c.drawRightString(520,320,"R$ "+"333,31")
c.roundRect(470, 305,60,20,3,stroke=1,fill=0)

c.showPage()
# Saving the PDF
c.save()

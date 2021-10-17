from reportlab.pdfgen import canvas
gst='45648df2345'
# Creating Canvas
c = canvas.Canvas("invoice.pdf",pagesize=(200,250),bottomup=0)
# Logo Section
# Setting th origin to (10,40)
c.translate(10,40)
# Inverting the scale for getting mirror Image of logo
c.scale(1,-1)
# Inserting Logo into the Canvas at required position
#c.drawImage("logo.jpg",0,0,width=50,height=30)
# Title Section
# Again Inverting Scale For strings insertion
c.scale(1,-1)
# Again Setting the origin back to (0,0) of top-left
c.translate(-10,-40)
# Setting the font for Name title of company
c.setFont("Helvetica-Bold",10)
# Inserting the name of the company
c.drawCentredString(100,20,"DAWAT LAWN & GARDEN")
# For under lining the title
c.line(5,30,195,30)
# Changing the font size for Specifying Address
c.setFont("Helvetica-Bold",5)
c.drawCentredString(100,27,"GANDHI LAYOUT,Main RING Road,Nagpur-13")

# Changing the font size for Specifying GST Number of firm
c.setFont("Helvetica-Bold",6)
#c.drawCentredString(105,39,"Food Licence:"+gst)
# Line Seprating the page header from the body
#c.line(5,45,195,45)
# Document Information
# Changing the font for Document title
mobile1='9822130819'
mobile2='7498518671'
mobile3='9370353955'
billno='545'
date='30/12/2021'
Name='MOHD TAHZEEB.T.KHAN'
phone1='9356718657'
#phone2='9432326485'
c.line(5,73,150,73)
c.setFont("Helvetica-Bold",5)
c.line(5,83,150,83)
c.drawRightString(58,35,"For Booking Contact:")
c.line(5,93,150,93)
c.setFont("Helvetica-Bold",10)
c.drawCentredString(103,47,"DAATA DECORATIONS & BICHAYAT")
c.setFont("Helvetica-Bold",7)
c.drawCentredString(103,58,f"Mob.{mobile1},{mobile2},{mobile3}")


# This Block Consist of Costumer Details
c.rect(5,63,190,40,fill=0)
c.setFont("Times-Bold",5)
c.drawRightString(49,70,"No:")
c.drawRightString(49,80,"BOOKING DATE:")
c.drawRightString(49,90,"PARTY NAME:")
c.drawRightString(49,100,"PHONE NO.:")
c.drawRightString(140,70,""+billno)
c.drawRightString(140,80,""+date)
c.drawRightString(140,90,""+Name)
c.drawRightString(140,100,f"{phone1}")
#c.drawRightString(120,100,f"{phone2}")

c.line(150,103,150,63)
# This Block Consist of Item Description
#c.roundRect(5,108,190,130,10,stroke=1,fill=0)
c.rect(5,108,190,130,fill=0)
c.line(5,120,195,120)
c.drawCentredString(15,118,"SR No.")
c.drawCentredString(75,118,"FACILITIES")
c.drawCentredString(140,118,"RATE")
c.drawCentredString(163,118,"QTY")
c.drawCentredString(183,118,"TOTAL")
# Drawing table for Item Description
c.line(5,210,195,210)
c.line(25,108,25,220)
c.line(125,108,125,220)
c.line(155,108,155,210)
c.line(170,108,170,210)
c.drawCentredString(15,128,"1")
c.drawCentredString(15,138,"2")
c.drawCentredString(15,148,"3")
c.drawCentredString(15,158,"4")
c.drawCentredString(15,168,"5")
c.drawCentredString(15,178,"6")
c.drawCentredString(15,188,"7")
c.drawCentredString(15,198,"8")
c.drawCentredString(15,208,"9")
c.drawCentredString(90,217,"GRAND TOTAL.:")
# Declaration and Signature
c.line(5,220,195,220)
c.line(100,220,100,238)

c.drawString(20,235,"Party sign")
c.drawRightString(180,235,"For NL Villa Janwasa")
# End the Page and Start with new
c.showPage()
# Saving the PDF
c.save()
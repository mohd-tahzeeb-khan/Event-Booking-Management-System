from reportlab.pdfgen import canvas
gst='45648df2345'
# Creating Canvas
c = canvas.Canvas("invoice.pdf",pagesize=(210,297),bottomup=0)
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
c.drawCentredString(105,10,"DAWAT LAWN & GARDEN")
# For under lining the title
c.line(5,20,205,20)
# Changing the font size for Specifying Address
c.setFont("Helvetica-Bold",4)
c.drawCentredString(105,17,"GANDHI LAYOUT,Main RING Road,Nagpur-13")

# Changing the font size for Specifying GST Number of firm
c.setFont("Helvetica-Bold",6)
#c.drawCentredString(105,39,"Food Licence:"+gst)
# Line Seprating the page header from the body
#c.line(5,45,205,45)
# Document Information
# Changing the font for Document title
mobile1='9822130819'
mobile2='7498518671'
mobile3='9370353955'
billno='545'
date='30/12/2021'
Name='MOHD TAHZEEB TANVEER MOHD KHAN'
phone1='9356718657'
#phone2='9432326485'
c.line(5,58,205,58)
c.setFont("Helvetica-Bold",5)
c.line(5,68,205,68)
c.drawRightString(58,25,"For Booking Contact:")
c.line(5,78,205,78)
#c.line(5,88,150,88)
c.setFont("Helvetica-Bold",10)
c.drawCentredString(103,35,"DAATA DECORATIONS & BICHAYAT")
c.setFont("Helvetica-Bold",5)
c.drawCentredString(103,42,f"Mob.{mobile1},{mobile2},{mobile3}")


# This Block Consist of Costumer Details
c.rect(5,48,200,40,fill=0)
c.setFont("Times-Bold",5)
c.drawRightString(49,55,"No:")
c.drawRightString(49,65,"DATE:")
c.drawRightString(135,65,"BOOKING DATE:")

c.drawRightString(49,75,"PARTY NAME:")
c.drawRightString(49,85,"PHONE NO.:")
c.drawRightString(180,55,""+billno)
c.drawRightString(80,65,""+date)
c.drawRightString(175,65,""+date)

c.drawRightString(180,75,""+Name)
c.drawRightString(140,85,f"{phone1},{mobile2}")

#c.drawRightString(120,100,f"{phone2}")

c.line(85,58,85,68)
# This Block Consist of Item Description
#c.roundRect(5,108,190,130,10,stroke=1,fill=0)
c.rect(5,90,200,160,fill=0)
c.line(5,105,205,105)
c.drawCentredString(15,100,"SR No.")
c.drawCentredString(75,100,"FACILITIES")
c.drawCentredString(140,100,"RATE")
c.drawCentredString(163,100,"QTY")
c.drawCentredString(188,100,"TOTAL")
# Drawing table for Item Description
c.line(5,240,205,240)
c.line(25,105,25,240)
c.line(125,105,125,240)
c.line(155,105,155,240)
c.line(170,105,170,240)
c.drawCentredString(15,115,"1")
c.drawCentredString(15,125,"2")
c.drawCentredString(15,135,"3")
c.drawCentredString(15,145,"4")
c.drawCentredString(15,155,"5")
c.drawCentredString(15,165,"6")
c.drawCentredString(15,175,"7")
c.drawCentredString(15,185,"8")
c.drawCentredString(15,195,"9")
c.drawCentredString(15,205,"10")
c.drawCentredString(15,215,"11")
c.drawCentredString(15,225,"12")
c.drawCentredString(15,235,"13")

c.drawCentredString(90,247,"GRAND TOTAL.:")
# Declaration and Signature
#c.line(5,220,205,220)
#c.line(80,220,80,228)

c.drawString(20,285,"Party sign")
c.drawRightString(180,285,"For Dawat Lawn")
# End the Page and Start with new
c.showPage()
# Saving the PDF
c.save()
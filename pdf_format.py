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
c.line(5,47,205,47)
c.setFont("Helvetica-Bold",5)
c.drawRightString(58,25,"For Booking Contact:")
#c.line(85,87,190,87)
#c.line(5,78,205,78)
#c.line(5,88,205,88)
#c.line(5,98,205,98)
c.setFont("Helvetica-Bold",10)
c.drawCentredString(103,35,"DAATA DECORATIONS & BICHAYAT")
c.setFont("Helvetica-Bold",5)
c.drawCentredString(103,42,f"Mob.{mobile1},{mobile2},{mobile3}")


# This Block Consist of Costumer Details
#c.rect(5,48,200,60,fill=0)
c.setFont("Times-Bold",5)
c.drawRightString(49,55,"No:")
c.drawRightString(49,65,"DATE:")
c.drawRightString(49,75,"PROGRAM DATE:")

c.drawRightString(49,85,"PARTY NAME:")
c.drawRightString(49,95,"PERSON:")

c.drawRightString(49,105,"PHONE NO.:")
c.drawRightString(80,55,""+billno)
c.drawRightString(80,65,""+date)
c.drawRightString(80,75,""+date)
c.drawRightString(80,95,"1100")


c.drawRightString(190,85,""+Name)
c.drawRightString(140,105,f"{phone1},{mobile2}")

#c.drawRightString(120,100,f"{phone2}")

#c.line(85,58,85,68)
# This Block Consist of Item Description
#c.roundRect(5,108,190,130,10,stroke=1,fill=0)
c.rect(5,120,200,150,fill=0)
c.line(5,133,205,133)
c.drawCentredString(15, 130,"SR No.")
c.drawCentredString(75, 130,"FACILITIES")
c.drawCentredString(140,130,"RATE")
c.drawCentredString(163,130,"QTY")
c.drawCentredString(188,130,"TOTAL")
# Drawing table for Item Description
c.line(5,258,205,258)
c.line(25,133,25,258)
c.line(125,133,125,258)
c.line(155,133,155,258)
c.line(170,133,170,258)
c.drawCentredString(15,143,"1")
c.drawCentredString(80,143,"Lawn Rent")

c.drawCentredString(15,153,"2")
c.drawCentredString(80,153,"Lawn Decoration")
c.drawCentredString(15,163,"3")
c.drawCentredString(80,163,"Gate + Stage")
c.drawCentredString(15,173,"4")
c.drawCentredString(80,173,"Cleaning Charges")
c.drawCentredString(15,183,"5")
c.drawCentredString(80,183,"Water Charges")
c.drawCentredString(15,193,"6")
c.drawCentredString(80,193,"Electric Charges")
c.drawCentredString(15,203,"7")
c.drawCentredString(15,213,"8")
c.drawCentredString(15,223,"9")
c.drawCentredString(15,233,"10")
c.drawCentredString(15,243,"11")
c.drawCentredString(15,253,"12")
#c.drawCentredString(15,263,"13")
c.drawCentredString(90,265,"GRAND TOTAL.:")
# Declaration and Signature
#c.line(5,220,205,220)
#c.line(80,220,80,228)

c.drawString(20,290,"Party sign")
c.drawRightString(180,290,"For Dawat Lawn")



# End the Page and Start with new
c.showPage()
# Saving the PDF
c.save()
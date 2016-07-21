import PIL
from PIL import Image
im=Image.open("Starbucks_Coffee_Logo.svg.png")
im.rotate(90).show()
#new_image.save("output.jpg","jpeg")

pix=im.load()
# size is 480,480
new_img=[]

for x in range(480):
    for y in range(480):
        value=(pix[x,y])
        rgb=list(value)
        total= (rgb[0]+rgb[1]+rgb[2])

        if total<182:
     #       print ("darkblue")
            new_img.append((0,51,76))

        if total>=182 and total <364:
      #      print ("red")
            new_img.append((217,26,33))
    

        if total>=364 and total<546:
      #      print ("lightblue")
            new_img.append((112,150,158))
            

        if total>=546:
        #    print ("yellow")
            new_img.append((252,227,166))

im.putdata(new_img)

im.rotate(-90).show()    
        


  
              








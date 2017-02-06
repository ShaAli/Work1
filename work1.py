XRES = 256
YRES = 500

f = open("pic1.ppm", "w")

header = "P3\n" + str(XRES) + " " + str(YRES) + " " + "255\n"

f.write(header)

r=0
g=0
b=0
#creates a simple gradient
for i in range (YRES):
    for k in range (XRES):
        f.write(str(r)+" "+str(g)+" "+str(b)+" ")
        if i%3==0:
             r=r+1
        if i%3==1:
            g=g+1
        if i%3==2:
            b=b+1
        if k==255:
            r=0
            g=0
            b=0        
f.close()

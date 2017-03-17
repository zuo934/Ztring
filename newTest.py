import turtle

class draw():
    def __init__(self,pensize,R,color,i,num):
        turtle.pensize(pensize)
        turtle.color(color)
        self.R = R
        self.i = i
        self.num = num

    def drawString(self,string):
        self.num = len(string)
        #print(self.num)
        #print(string)
        turtle.speed(10)
        for i in range(self.num):
            if string[i] == ' ':
                self.theNext(i)
            if string[i] == 'a':
                self.drawA()
                self.theNext(i)
                print(i)
            if string[i] == 'b':
                self.drawB()
                self.theNext(i)
            if string[i] == 'c':
                self.drawC()
                self.theNext(i)
            if string[i] == 'd':
                self.drawD()
                self.theNext(i)
            if string[i] == 'e':
                self.drawE()
                self.theNext(i)
            if string[i] == 'f':
                self.drawF()
                self.theNext(i)
            if string[i] == 'g':
                self.drawG()
                self.theNext(i)
            if string[i] == 'h':
                self.drawH()
                self.theNext(i)
            if string[i] == 'i':
                self.drawI()
                self.theNext(i)
            if string[i] == 'j':
                self.drawJ()
                self.theNext(i)
            if string[i] == 'k':
                self.drawK()
                self.theNext(i)
            if string[i] == 'l':
                self.drawL()
                self.theNext(i)
            if string[i] == 'm':
                self.drawM()
                self.theNext(i)
            if string[i] == 'n':
                self.drawN()
                self.theNext(i)
            if string[i] == 'o':
                self.drawO()
                self.theNext(i)
            if string[i] == 'p':
                self.drawP()
                self.theNext(i)
            if string[i] == 'q':
                self.drawQ()
                self.theNext(i)
            if string[i] == 'r':
                self.drawR()
                self.theNext(i)
            if string[i] == 's':
                self.drawS()
                self.theNext(i)
            if string[i] == 't':
                self.drawT()
                self.theNext(i)
            if string[i] == 'u':
                self.drawU()
                self.theNext(i)
            if string[i] == 'v':
                self.drawV()
                self.theNext(i)
            if string[i] == 'w':
                self.drawW()
                self.theNext(i)
            if string[i] == 'x':
                self.drawX()
                self.theNext(i)
            if string[i] == 'y':
                self.drawY()
                self.theNext(i)
            if string[i] == 'z':
                self.drawZ()
                self.theNext(i)
            else :
                print('The wrong string')

    def theNext(self,i):
        turtle.up()
        turtle.goto(3 * (i+1) * self.R, 0)
        turtle.down()

    def drawZ(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 1 * self.R) #jump
        turtle.down()

        turtle.goto(xwy[0] + 2.5 * self.R, xwy[1] - 1 * self.R)
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 3 * self.R)
        turtle.goto(xwy[0] + 2.5 * self.R, xwy[1] - 3 * self.R)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawY(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 1 * self.R) #jump
        turtle.down()


        turtle.seth(-90)                                         #draw
        turtle.fd(self.R)
        turtle.circle(self.R,180)
        turtle.fd(self.R)
        turtle.seth(-90)
        turtle.fd(3*self.R)
        turtle.seth(90)
        turtle.circle(self.R,-180)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawX(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 1 * self.R) #jump
        turtle.down()

        turtle.goto(xwy[0] + 2.5 * self.R, xwy[1] - 3 * self.R)

        turtle.up()
        turtle.goto(xwy[0] + 2.5 * self.R, xwy[1] - 1 * self.R)  # jump
        turtle.down()
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 3 * self.R)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawW(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 1 * self.R) #jump
        turtle.down()

        turtle.goto(xwy[0] + 1 * self.R, xwy[1] - 3 * self.R)
        turtle.goto(xwy[0] + 1.5 * self.R, xwy[1] - 1 * self.R)
        turtle.goto(xwy[0] + 2 * self.R, xwy[1] - 3 * self.R)
        turtle.goto(xwy[0] + 2.5 * self.R, xwy[1] - 1 * self.R)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawV(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 1 * self.R) #jump
        turtle.down()

        turtle.goto(xwy[0] + 1.5 * self.R, xwy[1] - 3 * self.R)
        turtle.goto(xwy[0] + 2.5 * self.R, xwy[1] - 1 * self.R)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawU(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 1 * self.R) #jump
        turtle.down()


        turtle.seth(-90)                                         #draw
        turtle.fd(self.R)
        turtle.circle(self.R,180)
        turtle.fd(self.R)
        turtle.seth(-90)
        turtle.fd(self.R * 0.75)
        turtle.circle(self.R * 3,20)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawT(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])
        turtle.up()
        turtle.goto(xwy[0] + 1.5 * self.R, xwy[1])  # jump
        turtle.down()

        turtle.seth(-90)  # draw
        turtle.fd(2.5 * self.R)
        turtle.circle(self.R / 2, 180)

        turtle.up()
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 1 * self.R)  # jump
        turtle.down()

        turtle.seth(0)
        turtle.fd(2 * self.R)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawS(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 2 * self.R, xwy[1] - 1.5* self.R) #jump
        turtle.down()


        turtle.seth(90)                                         #draw
        turtle.circle(self.R/2,270)
        turtle.seth(-180)
        turtle.circle(self.R/2,-270)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawR(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + self.R, xwy[1] - self.R) #jump
        turtle.down()


        turtle.seth(-180)                                         #draw
        turtle.circle(self.R/2,-90)
        turtle.seth(-90)
        turtle.fd(1.5*self.R)
        turtle.seth(90)
        turtle.fd(1.5*self.R)
        turtle.seth(-90)
        turtle.circle(self.R,-90)


        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawQ(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 2 * self.R, xwy[1] - 1 * self.R) #jump
        turtle.down()

        turtle.seth(150)
        turtle.circle(self.R, 240)

        turtle.seth(90)  # draw
        turtle.fd(1.7*self.R)

        turtle.seth(-90)
        turtle.fd(3 * self.R)

        turtle.up()
        turtle.goto(xwy[0] + self.R, xwy[1] - 1 * self.R)  # jump
        turtle.down()



        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawP(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + self.R, xwy[1] - 1* self.R) #jump
        turtle.down()

        turtle.seth(-90)                                         #draw
        turtle.fd(3 * self.R)

        turtle.up()
        turtle.goto(xwy[0] + self.R, xwy[1] - 1 * self.R)  # jump
        turtle.down()

        turtle.seth(210)
        turtle.circle(self.R,-240)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawO(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])
        turtle.up()
        turtle.goto(xwy[0] + 2.5 * self.R, xwy[1] - 2 * self.R)
        turtle.down()
        turtle.seth(90)
        turtle.circle(self.R, 360)
        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawN(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 0.5 *self.R, xwy[1] - 1.5* self.R) #jump
        turtle.down()

        turtle.seth(-90)                             # draw
        turtle.fd(1.5 * self.R)
        turtle.seth(90)
        turtle.fd(1.5 * self.R)
        turtle.seth(-90)
        turtle.circle(self.R , -180)
        turtle.seth(-90)
        turtle.fd(1.5 * self.R)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawM(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 1.5 * self.R) #jump
        turtle.down()

        turtle.seth(-90)                                         #draw
        turtle.fd(1.5 * self.R)
        turtle.seth(90)
        turtle.fd(1.5 * self.R)
        turtle.seth(-90)
        turtle.circle(self.R/2,-180)
        turtle.seth(-90)
        turtle.fd(1.5 * self.R)
        turtle.seth(90)
        turtle.fd(1.5 * self.R)
        turtle.seth(-90)
        turtle.circle(self.R/2,-180)
        turtle.seth(-90)
        turtle.fd(1.5 * self.R)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawL(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + self.R, xwy[1]) #jump
        turtle.down()

        turtle.seth(-90)
        turtle.fd(2.7 * self.R)
        turtle.circle(self.R / 2, 180)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawK(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] +  self.R, xwy[1] ) #jump
        turtle.down()

        turtle.seth(-90)                                         #draw
        turtle.fd(3 * self.R)

        turtle.up()
        turtle.goto(xwy[0] + self.R * 2, xwy[1] - self.R)  # jump
        turtle.down()
        turtle.seth(225)
        turtle.fd(1.4 * self.R)

        turtle.up()
        turtle.goto(xwy[0] + self.R, xwy[1] - 2 * self.R)  # jump
        turtle.down()
        turtle.seth(-30)
        turtle.fd(1.7 * self.R)


        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawJ(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])
        turtle.up()
        turtle.goto(xwy[0] + 1.5 * self.R, xwy[1] - 1 * self.R)  # jump
        turtle.down()

        turtle.seth(-90)  # draw
        turtle.fd(2 * self.R)
        turtle.seth(90)
        turtle.circle(self.R / 2,-180)

        turtle.up()
        turtle.goto(xwy[0] + 1.5 * self.R, xwy[1] - 0.5 * self.R)  # jump
        turtle.down()

        turtle.circle(1, 360)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawI(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])
        turtle.up()
        turtle.goto(xwy[0] + 1.5 * self.R, xwy[1] - 1* self.R) #jump
        turtle.down()

        turtle.seth(-90)                                         #draw
        turtle.fd(2 * self.R)

        turtle.up()
        turtle.goto(xwy[0] + 1.5 * self.R, xwy[1] - 0.5 * self.R)  # jump
        turtle.down()

        turtle.circle(1,360)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawH(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])
        turtle.up()

        turtle.goto(xwy[0] + self.R, xwy[1]) #jump

        turtle.down()
        turtle.speed(10)

        turtle.seth(-90)
        turtle.fd(3 * self.R)
        turtle.seth(90)
        turtle.fd(1.5 * self.R)
        turtle.seth(240)
        turtle.circle(self.R, -120)
        turtle.seth(-90)
        turtle.fd(1.5 * self.R)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawG(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 2.36 * self.R, xwy[1] - 2 * self.R)  # jump
        turtle.down()

        turtle.seth(90)
        turtle.circle(self.R, 360)
        turtle.seth(-90)
        turtle.fd(2 * self.R)
        turtle.seth(90)
        turtle.circle(self.R,-160)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawF(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])
        turtle.up()
        turtle.goto(xwy[0] + 2.5 * self.R, xwy[1] - 0.5* self.R) #jump
        turtle.down()

        turtle.seth(90)                                         #draw
        turtle.circle(self.R / 2,180)
        turtle.fd(2.5 * self.R)

        turtle.up()
        turtle.goto(xwy[0] + 0.5 * self.R, xwy[1] - 1.5 * self.R)  # jump
        turtle.down()

        turtle.seth(0)
        turtle.fd(2 * self.R)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawE(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])
        turtle.up()

        turtle.goto(xwy[0]+0.5*self.R, xwy[1]-2*self.R)  # jump

        turtle.down()

        turtle.seth(0)  # draw
        turtle.fd(2 * self.R)
        turtle.seth(90)
        turtle.circle(self.R, 300)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawD(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])

        turtle.up()
        turtle.goto(xwy[0] + 2 * self.R, xwy[1] - 1.15 * self.R)
        turtle.down()

        turtle.seth(150)
        turtle.circle(self.R, 240)
        bxy = turtle.pos()

        turtle.seth(90)
        turtle.fd(2.8 * self.R)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawC(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])
        turtle.up()

        turtle.goto(xwy[0] + 2.36 * self.R, xwy[1] - 1.5* self.R) #jump

        turtle.down()

        turtle.seth(120)                                         #draw
        turtle.circle(self.R,300)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawB(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0], xwy[1])
        turtle.up()
        turtle.goto(xwy[0] + self.R, xwy[1])
        turtle.down()

        turtle.seth(-90)
        turtle.fd(2.8 * self.R)

        turtle.up()
        turtle.goto(xwy[0] + self.R, xwy[1] - 1.15 * self.R)
        turtle.down()

        turtle.seth(210)
        turtle.circle(self.R , -240)
        bxy = turtle.pos()
        print(bxy)

        turtle.up()
        turtle.goto(xwy[0], xwy[1])
        turtle.down()
    def drawA(self):
        xy = turtle.pos()
        xwy = list(xy)
        print(xwy[0],xwy[1])
        turtle.up()
        turtle.goto(xwy[0]+2.5*self.R, xwy[1]-2*self.R)
        turtle.down()
        turtle.seth(90)
        turtle.circle(self.R, 360)
        turtle.seth(-90)
        turtle.fd(self.R)
        turtle.up()
        turtle.goto(xwy[0],xwy[1])
        turtle.down()


def main():
    test = draw(5,20,'black',1,0)
    while(1):
        string = input('Please enter something:\n')
        test.drawString(string)
    input('Please<enter>')



main()


from manim import *
import random

def randomizer(ListOfSquare, ListOfPositions):
    for a in range(len(ListOfSquare)):
        b = random.randrange(len(ListOfSquare))
        ListOfSquare[a], ListOfSquare[b] = ListOfSquare[b], ListOfSquare[a]
    for c in range(len(ListOfPositions)):
        d = random.randrange(len(ListOfPositions))
        ListOfPositions[c], ListOfPositions[d] = ListOfPositions[d], ListOfPositions[c]
    return ListOfSquare, ListOfPositions

#I just wanted to test git, I think I understand now. It's save first
#then add the file to staging
class SquareToCircle(Scene):
    def construct(self):
        squareBlue = squareBlue2 = squareBlue3 = squareBlue4 = squareBlue5 = Square().scale(.5)
        squareRed = squareRed1 = squareRed2 = squareRed3 = squareRed4 = Square().scale(.5)
        
        ListOfSquare = [squareBlue, squareBlue2, squareBlue3, squareBlue4, squareBlue5, squareRed, squareRed1, squareRed2, squareRed3, squareRed4]
        ListOfPositions = [0, LEFT * 1, LEFT * 2, LEFT * 3, LEFT * 4, RIGHT * 5, RIGHT * 1, RIGHT * 2, RIGHT * 3, RIGHT * 4]

        squareBluePosition, squareBlue2Postion, squareBlue3Postion, squareBlue4Postion, squareBlue5Postion = 0, LEFT * 1, LEFT * 2, LEFT * 3, LEFT * 4
        squareRedPosition, squareRed1Position, squareRed2Position, squareRed3Position, squareRed4Position = RIGHT * 5, RIGHT * 1, RIGHT * 2, RIGHT * 3, RIGHT * 4

        squareBlue.set_fill(BLUE_D, opacity=.7)
        squareBlue.move_to(squareBluePosition)

        squareBlue2.move_to(squareBlue2Postion)
        squareBlue2.set_fill(BLUE_C, opacity=.8)

        squareBlue3.set_fill(BLUE, opacity=1.0)
        squareBlue3.move_to(squareBlue3Postion)

        squareBlue4.set_fill(BLUE_B, opacity=1.0)
        squareBlue4.move_to(squareBlue4Postion)

        squareBlue5.set_fill(BLUE_A, opacity=1.0)
        squareBlue5.move_to(squareBlue5Postion)

        squareRed.set_fill(RED_D, opacity=.4)
        squareRed.move_to(squareRedPosition)

        squareRed1.move_to(squareRed1Position)
        squareRed1.set_fill(RED_A, opacity=1.0)

        squareRed2.set_fill(RED_B, opacity=.8)
        squareRed2.move_to(squareRed2Position)

        squareRed3.set_fill(RED, opacity=1.0)
        squareRed3.move_to(squareRed3Position)

        squareRed4.set_fill(RED_C, opacity=.8)
        squareRed4.move_to(squareRed4Position)

        
        self.add(squareBlue, squareBlue2, squareBlue3, squareBlue4, squareBlue5)
        self.add(squareRed, squareRed1, squareRed2, squareRed3, squareRed4)
        self.wait(1)

        self.play(squareBlue.animate.shift(RIGHT * 3), squareRed3.animate.shift(LEFT * 3))
        self.play(squareBlue2.animate.shift(RIGHT), squareRed3.animate.shift(LEFT))
        self.play(squareBlue4.animate.shift(RIGHT * 7), squareRed4.animate.shift(LEFT * 7))
        self.wait(1)
                
        
        for i in range(5):
            self.play(squareBlue.animate.move_to(0), squareBlue2.animate.move_to(0), squareBlue3.animate.move_to(0), squareBlue4.animate.move_to(0), squareBlue5.animate.move_to(0), squareRed.animate.move_to(0),
                  squareRed1.animate.move_to(0), squareRed2.animate.move_to(0), squareRed3.animate.move_to(0), squareRed4.animate.move_to(0))
            
            ListOfSquare, ListOfPositions = randomizer(ListOfSquare, ListOfPositions)

            self.play(ListOfSquare[0].animate.shift(ListOfPositions[0]), ListOfSquare[1].animate.shift(ListOfPositions[1]), ListOfSquare[2].animate.shift(ListOfPositions[2]), ListOfSquare[3].animate.shift(ListOfPositions[3]),
                    ListOfSquare[4].animate.shift(ListOfPositions[4]), ListOfSquare[5].animate.shift(ListOfPositions[5]), ListOfSquare[6].animate.shift(ListOfPositions[6]), ListOfSquare[7].animate.shift(ListOfPositions[7]),
                    ListOfSquare[8].animate.shift(ListOfPositions[8]), ListOfSquare[9].animate.shift(ListOfPositions[9]))
            self.wait(2)

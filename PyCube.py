import colorama
from colorama import Back, Style

class PyCube:
    def __init__(self):
        self.cube = [
            [["W","W","W"], ["W","W","W"], ["W","W","W"],],
            [["G","G","G"], ["G","G","G"], ["G","G","G"],],
            [["Y","Y","Y"], ["Y","Y","Y"], ["Y","Y","Y"],],
            [["R","R","R"], ["R","R","R"], ["R","R","R"],],
            [["B","B","B"], ["B","B","B"], ["B","B","B"],],
            [["O","O","O"], ["O","O","O"], ["O","O","O"],],
            ]
        self.faces = ["UP","FRONT","DOWN","RIGHT","BACK","LEFT"]
        self.colors = ["WHITE","GREEN","YELLOW","RED","BLUE","ORANGE"]
        self.isSolved = True
        self.updateCube()
        self.codes = {
            "F": self.F,
            "F'": self.Fi,
            "U": self.U,
            "U'": self.Ui,
            "D": self.D,
            "D'": self.Di,
            "R": self.R,
            "R'":self.Ri,
            "B": self.B,
            "B'": self.Bi,
            "L": self.L,
            "L'": self.Li,
            "F2": self.F2,
            "U2": self.U2,
            "D2": self.D2,
            "R2": self.R2,
            "B2": self.B2,
            "L2": self.L2,
            "X": self.X,
            "X'": self.Xi,
            "Y": self.Y,
            "Y'": self.Yi
        }
        self.moves = list(self.codes.keys())

    def __repr__(self):
        return """
        A PyCube Object
        PyCube.displayCube() - shows cube
        PyCube.runAlgo(algo, splitter=' ') - run rubik's cube algorithms
        PyCube.showMoves() - shows all possible algorithm
        """
    @staticmethod
    def showMoves():
        print("Rubik's Cube Algorithms")
        print("R - Rotate Right 90° Clockwise")
        print("R' - Rotate Right 90° Counter Clockwise")
        print("L - Rotate Left 90° Clockwise")
        print("L' - Rotate Left 90° Counter Clockwise")
        print("U - Rotate Top 90° Clockwise")
        print("U' - Rotate Top 90° Counter Clockwise")
        print("D - Rotate Bottom 90° Clockwise")
        print("D' - Rotate Bottom 90° Counter Clockwise")
        print("F - Rotate Front 90° Clockwise")
        print("F' - Rotate Front 90° Counter Clockwise")
        print("B - Rotate Back 90° Clockwise")
        print("B' - Rotate Back 90° Counter Clockwise")
        print("R2 - Rotate Right 90° Two Times")
        print("L2' - Rotate Left 90° Two Times")
        print("U2 - Rotate Top 90° Two Times")
        print("D2' - Rotate Down 90° Two Times")
        print("F2 - Rotate Front 90° Two Times")
        print("B2' - Rotate Back 90° Two Times")

    def displayCube(self, colored=False):
        #print(f"{' '*5}{self.faces[0]}")
        if colored:
            colorama.init(autoreset=True)
            self.coloredCode = {
                "W": f"{Back.WHITE} ",
                "Y": f"{Back.YELLOW} ",
                "R": f"{Back.RED} ",
                "O": f"{Back.LIGHTRED_EX} ",
                "B": f"{Back.BLUE} ",
                "G": f"{Back.GREEN} "
            }
            self.coloredCube = [[[self.coloredCode[self.cube[i][j][k]]for k in range(len(self.cube[i][j]))] for j in range(len(self.cube[i]))] for i in range(len(self.cube))]

            for row in self.coloredCube[0]:
                print(f"{' '*6}{' '.join(row)} ")

            zipped_faces = zip(self.coloredCube[5], self.coloredCube[1], self.coloredCube[3], self.coloredCube[4])
            for row1, row2, row3, row4 in zipped_faces:
                print(f"{' '.join(row1)} {' '.join(row2)} {' '.join(row3)} {' '.join(row4)} ")

            for row in self.coloredCube[2]:
                print(f"{' '*6}{' '.join(row)} ")

        elif not(colored):
            for row in self.UP:
                print(f"{' '*6}{' '.join(row)}")
            print(f"{' '*6}{'-'*5}")

            zipped_faces = zip(self.LEFT, self.FRONT, self.RIGHT, self.BACK)
            for row1, row2, row3, row4 in zipped_faces:
                print(f"{' '.join(row1)}|{' '.join(row2)}|{' '.join(row3)}|{' '.join(row4)}")
            print(f"{' '*6}{'-'*5}")

            for row in self.DOWN:
                print(f"{' '*6}{' '.join(row)}")

    def runAlgo(self, str, splitter=" "):
        commands = str.split(splitter)
        for command in commands:
            if command in self.codes.keys():
                self.codes[command.upper()]()
        print(f"Scramble Algo: {str}")

    def updateCube(self):
        self.UP = self.cube[0]
        self.FRONT = self.cube[1]
        self.DOWN = self.cube[2]
        self.RIGHT = self.cube[3]
        self.BACK = self.cube[4]
        self.LEFT = self.cube[5]

    def F(self):
        self.cube[1] = [[row[i] for row in self.FRONT][::-1] for i in range(3)]
        
        # Get affected edges and corners
        top = self.UP[-1]
        right = [row[0] for row in self.RIGHT][::-1]
        bot = self.DOWN[0]
        left = [row[-1] for row in self.LEFT][::-1]

        # Update edges and corners
        self.cube[0][-1] = left
        for i, row in enumerate(self.RIGHT):
            row[0] = top[i]
        self.cube[2][0] = right
        for i, row in enumerate(self.LEFT):
            row[-1] = bot[i]

        self.updateCube()

    def Fi(self):
        self.cube[1] = [[row[i] for row in self.FRONT] for i in range(3)][::-1]
        
        # Get affected edges and corners
        top = self.UP[-1][::-1]
        right = [row[0] for row in self.RIGHT]
        bot = self.DOWN[0][::-1]
        left = [row[-1] for row in self.LEFT]

        # Update edges and corners
        self.cube[0][-1] = right
        for i, row in enumerate(self.RIGHT):
            row[0] = bot[i]
        self.cube[2][0] = left
        for i, row in enumerate(self.LEFT):
            row[-1] = top[i]

        self.updateCube()

    def U(self):
        self.cube[0] = [[row[i] for row in self.UP][::-1] for i in range(3)]
        
        # Get affected edges and corners
        top = self.BACK[0]
        right = self.RIGHT[0]
        bot = self.FRONT[0]
        left = self.LEFT[0]

        # Update edges and corners
        self.cube[4][0] = left
        self.cube[3][0] = top
        self.cube[5][0] = bot
        self.cube[1][0] = right

        self.updateCube()

    def Ui(self):
        self.cube[0] = [[row[i] for row in self.UP] for i in range(3)][::-1]
        
        # Get affected edges and corners
        top = self.BACK[0]
        right = self.RIGHT[0]
        bot = self.FRONT[0]
        left = self.LEFT[0]

        # Update edges and corners
        self.cube[4][0] = right
        self.cube[3][0] = bot
        self.cube[5][0] = top
        self.cube[1][0] = left

        self.updateCube()

    def R(self):
        self.cube[3] = [[row[i] for row in self.RIGHT][::-1] for i in range(3)]
        
        # Get affected edges and corners
        top = [row[-1] for row in self.UP][::-1]
        right = [row[0] for row in self.BACK][::-1]
        bot = [row[-1] for row in self.DOWN]
        left = [row[-1] for row in self.FRONT]

        # Update edges and corners
        for i, row in enumerate(self.UP):
            row[-1] = left[i]
        for i, row in enumerate(self.BACK):
            row[0] = top[i]
        for i, row in enumerate(self.DOWN):
            row[-1] = right[i]
        for i, row in enumerate(self.FRONT):
            row[-1] = bot[i]

        self.updateCube()

    def Ri(self):
        self.cube[3] = [[row[i] for row in self.RIGHT] for i in range(3)][::-1]
        
        # Get affected edges and corners
        top = [row[-1] for row in self.UP]
        right = [row[0] for row in self.BACK][::-1]
        bot = [row[-1] for row in self.DOWN][::-1]
        left = [row[-1] for row in self.FRONT]

        # Update edges and corners
        for i, row in enumerate(self.UP):
            row[-1] = right[i]
        for i, row in enumerate(self.BACK):
            row[0] = bot[i]
        for i, row in enumerate(self.DOWN):
            row[-1] = left[i]
        for i, row in enumerate(self.FRONT):
            row[-1] = top[i]

        self.updateCube()
    
    def L(self):
        self.cube[5] = [[row[i] for row in self.LEFT][::-1] for i in range(3)]
        
        # Get affected edges and corners
        top = [row[0] for row in self.UP]
        right = [row[0] for row in self.FRONT]
        bot = [row[0] for row in self.DOWN][::-1]
        left = [row[-1] for row in self.BACK][::-1]

        # Update edges and corners
        for i, row in enumerate(self.UP):
            row[0] = left[i]
        for i, row in enumerate(self.FRONT):
            row[0] = top[i]
        for i, row in enumerate(self.DOWN):
            row[0] = right[i]
        for i, row in enumerate(self.BACK):
            row[-1] = bot[i]

        self.updateCube()

    def Li(self):
        self.cube[5] = [[row[i] for row in self.LEFT]for i in range(3)][::-1]
        
        # Get affected edges and corners
        top = [row[0] for row in self.UP][::-1]
        right = [row[0] for row in self.FRONT]
        bot = [row[0] for row in self.DOWN]
        left = [row[-1] for row in self.BACK][::-1]

        # Update edges and corners
        for i, row in enumerate(self.UP):
            row[0] = right[i]
        for i, row in enumerate(self.FRONT):
            row[0] = bot[i]
        for i, row in enumerate(self.DOWN):
            row[0] = left[i]
        for i, row in enumerate(self.BACK):
            row[-1] = top[i]

        self.updateCube()


    def B(self):
        self.cube[4] = [[row[i] for row in self.BACK][::-1] for i in range(3)]
        
        # Get affected edges and corners
        top = self.UP[0][::-1]
        right = [row[0] for row in self.LEFT]
        bot = self.DOWN[-1][::-1]
        left = [row[-1] for row in self.RIGHT]

        # Update edges and corners
        self.cube[0][0] = left
        for i, row in enumerate(self.LEFT):
            row[0] = top[i]
        self.cube[2][-1] = right
        for i, row in enumerate(self.RIGHT):
            row[-1] = bot[i]

        self.updateCube()

    def Bi(self):
        self.cube[4] = [[row[i] for row in self.BACK] for i in range(3)][::-1]
        
        # Get affected edges and corners
        top = self.UP[0]
        right = [row[0] for row in self.LEFT][::-1]
        bot = self.DOWN[-1]
        left = [row[-1] for row in self.RIGHT][::-1]

        # Update edges and corners
        self.cube[0][0] = right
        for i, row in enumerate(self.LEFT):
            row[0] = bot[i]
        self.cube[2][-1] = left
        for i, row in enumerate(self.RIGHT):
            row[-1] = top[i]

        self.updateCube()
    
    def D(self):
        self.cube[2] = [[row[i] for row in self.DOWN][::-1] for i in range(3)]
        
        # Get affected edges and corners
        top = self.FRONT[-1]
        right = self.RIGHT[-1]
        bot = self.BACK[-1]
        left = self.LEFT[-1]

        # Update edges and corners
        self.cube[1][-1] = left
        self.cube[3][-1] = top
        self.cube[4][-1] = right
        self.cube[5][-1] = bot

        self.updateCube()

    def Di(self):
        self.cube[2] = [[row[i] for row in self.DOWN] for i in range(3)][::-1]
        
        # Get affected edges and corners
        top = self.FRONT[-1]
        right = self.RIGHT[-1]
        bot = self.BACK[-1]
        left = self.LEFT[-1]

        # Update edges and corners
        self.cube[1][-1] = right
        self.cube[3][-1] = bot
        self.cube[4][-1] = left
        self.cube[5][-1] = top

        self.updateCube()

    def U2(self):
        self.U()
        self.U()

    def F2(self):
        self.F()
        self.F()

    def D2(self):
        self.D()
        self.D()

    def R2(self):
        self.R()
        self.R()

    def B2(self):
        self.B()
        self.B()

    def L2(self):
        self.L()
        self.L()

    def X(self):
        self.cube[0] = [[row[i] for row in self.UP][::-1] for i in range(3)]
        self.cube[2] = [[row[i] for row in self.DOWN] for i in range(3)][::-1]

        self.updateCube()

        self.cube[5], self.cube[1], self.cube[3], self.cube[4] = self.cube[1], self.cube[3], self.cube[4], self.cube[5]
        self.updateCube()

    def Xi(self):
        self.cube[0] = [[row[i] for row in self.UP] for i in range(3)][::-1]
        self.cube[2] = [[row[i] for row in self.DOWN][::-1] for i in range(3)]

        self.updateCube()

        self.cube[5], self.cube[1], self.cube[3], self.cube[4] = self.cube[4], self.cube[5], self.cube[1], self.cube[3]
        self.updateCube()

    def Y(self):
        self.cube[3] = [[row[i] for row in self.RIGHT][::-1] for i in range(3)]
        self.cube[5] = [[row[i] for row in self.LEFT]for i in range(3)][::-1]

        self.cube[0], self.cube[4], self.cube[2], self.cube[1] = self.cube[1], self.cube[0], self.cube[4], self.cube[2]

        self.updateCube()

    def Yi(self):
        self.cube[3] = [[row[i] for row in self.RIGHT] for i in range(3)][::-1]
        self.cube[5] = [[row[i] for row in self.LEFT][::-1] for i in range(3)]

        self.cube[0], self.cube[4], self.cube[2], self.cube[1] = self.cube[4], self.cube[2], self.cube[1], self.cube[0]

        self.updateCube()

def main():
    #PyCube.showMoves()
    cube1 = PyCube()
    # Put algorithm here, (check methods in the class)
    #cube1.runAlgo("F ")

    print("Before:")
    cube1.displayCube()

    cube1.runAlgo("R U R' U'")
    
    print("After:")
    cube1.displayCube()
    
if __name__ == '__main__':
    main()
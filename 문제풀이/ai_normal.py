class Tik_tak:
    def __init__(self, size = 9, turn = 1):
        self.size = size
        self.tik_tak = [" "] * size
        self.turn = turn
#[[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def print_screan(self):
       print("현재 상태")
       print(self.tik_tak[0] + "|" + self.tik_tak[1] + "|" + self.tik_tak[2])
       print("-+-+-")
       print(self.tik_tak[3] + "|" + self.tik_tak[4] + "|" + self.tik_tak[5])
       print("-+-+-")
       print(self.tik_tak[6] + "|" + self.tik_tak[7] + "|" + self.tik_tak[8])

    def input(self):
        witch = int(input("어디에 두겠습니까? => "))
        if self.tik_tak[witch -1] == " ":
            if(self.turn % 2 == 0):
                self.tik_tak[witch-1] = "O"
                self.turn += 1
                print("--------------------------")
            else:
                self.tik_tak[witch-1] = "X"
                self.turn += 1
                print("--------------------------")

        elif(self.tik_tak[witch -1] != " "):
            while True:
                witch = int(input("다시 두어주세요 => "))
                if self.tik_tak[witch -1] == " ":
                    if(self.turn % 2 == 0):
                        self.tik_tak[witch-1] = "O"
                        self.turn += 1
                        print("--------------------------")
                        break
                    else:
                        self.tik_tak[witch-1] = "X"
                        self.turn += 1
                        print("--------------------------")
                        break

    def win(self):
        wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for i in wins:
            if self.tik_tak[i[0]] == "O" and self.tik_tak[i[1]] == "O" and self.tik_tak[i[2]]== "O":
                self.print_screan()
                print("O가 이겼습니다")
                return True
            elif self.tik_tak[i[0]] == "X" and self.tik_tak[i[1]] == "X" and self.tik_tak[i[2]]== "X":
                self.print_screan()
                print()
                print("X가 이겼습니다")
                return True

a = Tik_tak()

for i in range(1, 10):
    a.print_screan()
    a.input()
    if a.win():
        break

if not a.win():
    print("비겼습니다")
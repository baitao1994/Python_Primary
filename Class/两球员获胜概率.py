#matchSim.py
from random import * 
 
def main():
    printIntro()#介绍程序
    probA,probB,n = getInputs()#获得两位球员发球概率（能力）及比赛次数的函数
    winsA, winsB = simNGames(n,probA,probB)#计算个球员赢球场次
    PrintSummary(winsA, winsB)#计算赢球概率
 
def printIntro():
    print('This program simulates a game between two')
    print('There are two players, A and B')
    print('Probability(a number between 0 and 1)is used')
 
def getInputs():
    a = eval(input('What is the prob.player A wins?'))
    b = eval(input('What is the prob.player B wins?'))
    n = eval(input('How many games to simulate?'))
    return a,b,n
 
def simNGames(n,probA,probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA >scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA,winsB
def simOneGame(probA,probB):#一场比赛中，两球员得分情况
    scoreA = 0
    scoreB = 0
    serving = "A"#球权在A选手
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if random() < probA:#random()是返回一个[0,1)内的浮点数
                scoreA = scoreA + 1
            else:
                scoreB += 1#这句是我自己加的，不知道对不对
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA += 1#自己加的
                serving = "A"
    return scoreA,scoreB
 
def gameOver(a,b):
    return a==15 or b==15#谁先15分谁赢这场
 
def PrintSummary(winsA, winsB):
    n = winsA + winsB
    print('\nGames simulated:%d'%n)
    print('Wins for A:{0}({1:0.1%})'.format(winsA,winsA/n))
    print('Wins for B:{0}({1:0.1%})'.format(winsB,winsB/n))
 
if __name__ == '__main__':
    main()

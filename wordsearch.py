import random
from nltk.corpus import words
import webbrowser
import os

class createBoard:

    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.index = []
        self.wordlist = words.words()
        self.wordlength = self.rows - 1
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.board = []
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                self.board[row].append([' '])

    def insertWords(self):
        def new_word(length):
            if self.wordlength < 4:
                self.wordlength = 4
            word = ''
            while len(word) != self.wordlength:
                word = list(self.wordlist[random.randint(0,len(self.wordlist)-1)].lower())
            return(word)
        def clashCheck(direction,word,x,y):
            crosscheck = []
            if direction == 'horizontal':
                for i in range(len(word)):
                    crosscheck.append(self.board[x][y+i])
            elif direction == 'vertical':
                for i in range(len(word)):
                    crosscheck.append(self.board[x+i][y])
            if all(j == [' '] for j in crosscheck) == True:
                return(True)
            else:
                return(False)
        def increment(xy):
            start_xy = xy + 1
            if start_xy == self.rows:
                start_xy = 0
            return(start_xy)
        def intersect(word):
            count = 0
            for letter in word:
                count += 1
                for row in range(self.rows):
                    for col in range(self.cols):
                        if self.board[row][col] == [letter] and row <= self.rows-(len(word)) and row >= count and col <= self.cols - (len(word)) and col >= count:
                            if clashCheck('horizontal',word[0:(len(word)-count)],row,col+1) == True:
                                for ln in range(len(word)):
                                    self.board[row][(col-count+1)+ln] = [word[ln]]
                            elif clashCheck('vertical',word[0:(len(word)-count)],row+1,col) == True:
                                for ln in range(len(word)):
                                    self.board[(row-count+1)+ln][col] = [word[ln]]
                            self.index.append(''.join(word))
                            return()
        while len(self.index) != int(self.rows * 0.8):
            word = list(new_word(self.wordlength))
            self.wordlength -= 1
            if len(self.index) > 1 and len(self.index) < int(self.rows/3)+2:
                intersect(word)
            else:
                complete = True
                count = 0
                if random.randint(0,1) == 0:
                    start_x = random.randint(0,self.rows-1)
                    start_y = random.randint(0,self.cols-len(word))
                    cross = clashCheck('horizontal',word,start_x,start_y)
                    while cross == False:
                        start_x = increment(start_x)
                        count += 1
                        cross = clashCheck('horizontal',word,start_x,start_y)
                        if count > self.rows:
                            complete = False
                            break
                    if complete != False:
                        self.index.append(''.join(word))
                        for ln in range(len(word)):
                            self.board[start_x][start_y + ln] = [word[ln]]
                else:
                    start_x = random.randint(0,self.rows-len(word))
                    start_y = random.randint(0,self.cols-1)
                    cross = clashCheck('vertical',word,start_x,start_y)
                    while cross == False:
                        start_y = increment(start_y)
                        count += 1
                        cross = clashCheck('vertical',word,start_x,start_y)
                        if count > self.rows:
                            complete = False
                            break
                    if complete != False:
                        self.index.append(''.join(word))
                        for ln in range(len(word)):
                            self.board[start_x + ln][start_y] = [word[ln]]

    def fillBoard(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == [' ']:
                    self.board[row][col] = [self.alphabet[random.randint(0,len(self.alphabet)-1)]]

    def createHTML(self,filename):
        hi_wrapper = """
            <html>
              <head>
                <meta charset='UTF-8'>
                <meta http-equiv="X-UA-Compatible" content="IE-edge">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <title>The Best Wordsearch</title>
              </head>
              <body>
                <div class="container-fluid" style="width:50%;">
                  <div class="row" style="text-align:center;padding-left:1em;">
                    <h2 style="padding-bottom:2em;">This Is The Best Wordsearch. Period.</h2>
                  <div>
        """
        lo_wrapper = """
                  </div>
                </div>
              </body>
            </html>
        """
        os.chdir('/Users/lam/Desktop/')
        f = open(filename,'w')
        f.write(hi_wrapper)
        wh = str(100/(self.rows+1))
        for row in range(self.rows):
            f.write('<div class="row">')
            for col in range(self.cols):
                f.write('<div class="col-sm" style="font-size:1rem;width:'+wh+'%;height:'+wh+'%;"><strong>'+self.board[row][col][0]+'</strong></div>')
            f.write('</div>')
        f.write('<div class="row" style="padding-top:3em;padding-bottom:3em;">')
        for name in self.index:
            f.write('<div class="col">'+name+"</div>")
        f.write(lo_wrapper)
        f.close()
        self.filename = filename

    def openInBrowser(self):
        os.chdir('/Users/lam/Desktop/')
        webbrowser.open_new('file:///Users/lam/Desktop/'+self.filename)

nrc = int(input("Please enter the number of rows you would like in your wordsearch (input a number and press enter): "))
newGame = createBoard(nrc,nrc)
newGame.insertWords()
newGame.fillBoard()
#print(newGame.board)
#print(newGame.index)
newGame.createHTML('wordsearch.html')
newGame.openInBrowser()

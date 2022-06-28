from math import floor
import numpy as np
class nobe:

    def __init__(self,x,y,value) -> None:
        self.row = x
        self.column = y
        self.squere = floor(x/3)*3 + floor(y/3) 
        self.value = value
        self.p_value = []

    def show(self):
        print('value:',self.value,'column',self.column,'row',self.row,'squere',self.squere,'possible',self.p_value)

    def give(self):
        return self.value,self.column,self.row,self.squere

    def set_p(self,tab):
        self.p_value = tab
    def set_value(self,value):
        self.value = value
        
class sudoku:

    def __init__(self,tab) -> None:
        data = []
        for irow,row in enumerate(tab):
            for inumber,number in enumerate(row):
                hold = nobe(irow,inumber,number)
                data.append(hold)
        self.data = data

    def data_show(self):
        for x in self.data:
            x.show()

    def try_solve(self):
        temp = self.data
        self.possible()
        for nobe in self.data:
            if len(nobe.p_value) == 1:
                nobe.set_value(nobe.p_value[0])
                nobe.p_value = []                 

    def possible(self):
        self.rows = []
        self.collumns = []
        self.squeres = []
        for x in range(9):
            tab_row = ['1','2','3','4','5','6','7','8','9']
            tab_column = ['1','2','3','4','5','6','7','8','9']
            tab_squere = ['1','2','3','4','5','6','7','8','9']
            for y in self.data:
                if x == y.row and y.value != '.':
                    tab_row.remove(str(y.value))
                if x == y.column and y.value !='.':
                    tab_column.remove(str(y.value))
                if x == y.squere and y.value != '.':
                    tab_squere.remove(str(y.value))
            self.rows.append(tab_row)
            self.collumns.append(tab_column)
            self.squeres.append(tab_squere)
        for nobe in self.data:
            if nobe.value == '.':
                tab = []
                for number in range(9):
                    if str(number+1) in self.rows[nobe.row] and str(number+1) in self.collumns[nobe.column] and str(number+1) in self.squeres[nobe.squere]:
                        tab.append(number+1)
                    nobe.set_p(tab)
    def show_sudoku(self):
        for inobe,nobe in enumerate(self.data):
            print(nobe.value,end='|')
            if ((inobe+1) % 9) == 0:
                print(end = '\n')


tab = [[".",".",".","4",".","7",".","5","8"]
,[".",".","7",".","1","5",".","3","2"]
,[".",".","4","6",".","3",".",".","."]
,[".",".",".","1","3",".","8","6","."]
,[".",".",".",".",".",".","1",".","."]
,[".",".",".","5","9","8",".",".","."]
,["8","9",".",".","5","6","7","4","3"]
,["7","2",".","3",".","9",".","8","1"]
,[".",".","5","8",".","1","2","9","."]]

tab = sudoku(tab)
flag = 0
while flag == 0:
    command = input('|N|ext, |S|how, |E|xit :')
    if command == 'n':
        tab.try_solve()
        tab.show_sudoku()
    elif command == 's':
        tab.data_show()
    elif command == 'e':
        flag = 1
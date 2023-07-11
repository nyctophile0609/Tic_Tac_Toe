from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from player import Ui_REDWINDOW
from firstwin import Ui_CHOICEWINDOW
from computerwin import Ui_GREENWINDOW
import sys
from random import *
from time import *


####################################################################################################
####################################################################################################
####################################################################################################
class BLUEWIN(QMainWindow,Ui_CHOICEWINDOW):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.bluestarts()
        
    def bluestarts(self):
        self.pvpbut.clicked.connect(lambda:self.swapb(windowb,windowg))
        self.compbut.clicked.connect(lambda:self.swapb(windowb,windowr))
        self.quitall.clicked.connect(self.swapq)
        
    def swapb(self,hideb,shown):
        hideb.hide()
        shown.show()
        
    def swapq(self):
        windowb.hide()
        
###################################################################################################
###################################################################################################        
###################################################################################################
class GREENWIN(QMainWindow,Ui_GREENWINDOW):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startg()
        
    def startg(self):
        self.result.setText('')
        self.turns.setText('Turn:   X')
        self.cagain.hide()
        self.cquit.hide()
        self.butremains=[self.ox1,self.ox2,self.ox3,self.ox4,self.ox5,self.ox6,self.ox7,self.ox8,self.ox9]
        self.butstays=[self.ox1,self.ox2,self.ox3,self.ox4,self.ox5,self.ox6,self.ox7,self.ox8,self.ox9]
        self.realdeal=['','','','','','','','','']
        self.showagain1()
        self.steps=0
        self.winner='DRAW'
        self.coback.clicked.connect(self.gobackg1)
        self.cquit.clicked.connect(self.gobackg)
        self.cagain.clicked.connect(self.startg)
        self.startbutton()
        
    def startbutton(self):
        self.ox1.clicked.connect(lambda:self.changebutton(self.ox1))
        self.ox2.clicked.connect(lambda:self.changebutton(self.ox2))
        self.ox3.clicked.connect(lambda:self.changebutton(self.ox3))
        self.ox4.clicked.connect(lambda:self.changebutton(self.ox4))
        self.ox5.clicked.connect(lambda:self.changebutton(self.ox5))
        self.ox6.clicked.connect(lambda:self.changebutton(self.ox6))
        self.ox7.clicked.connect(lambda:self.changebutton(self.ox7))
        self.ox8.clicked.connect(lambda:self.changebutton(self.ox8))
        self.ox9.clicked.connect(lambda:self.changebutton(self.ox9))
        
    

    def changebutton(self,clickedone):
        if self.steps%2==0 and clickedone in self.butstays and self.check_winner()==0 and self.steps!=9:    
            clickedone.setText('X')
            self.turns.setText('Turn:   O')
            self.steps+=1
            self.realdeal[self.butremains.index(clickedone)]='X'
            self.butstays.remove(clickedone)
            self.set_winner()
            
        elif self.steps%2 and clickedone in self.butstays and self.check_winner()==0 and self.steps!=9:
            clickedone.setText('O')
            self.turns.setText('Turn:   X')
            self.steps+=1
            self.realdeal[self.butremains.index(clickedone)]='O'
            self.butstays.remove(clickedone)
            self.set_winner()

    def set_winner(self):
        if self.check_winner()!=0:
            self.hideonly()
            self.result.setText(f'Winner is {self.check_winner()}')
            self.showlast()
            
        elif self.steps==9 and self.check_winner()==0:
            self.hideonly()
            self.result.setText('DRAW')
            self.showlast()
    
    
    def check_winner(self):
        w=self.realdeal
        l1=[w[0],w[1],w[2]]
        l2=[w[3],w[4],w[5]]
        l3=[w[6],w[7],w[8]]
        l4=[w[0],w[4],w[8]]
        l5=[w[2],w[4],w[6]]
        l6=[w[0],w[3],w[6]]
        l7=[w[1],w[4],w[7]]
        l8=[w[2],w[5],w[8]]
        cl=[l1,l2,l3,l4,l5,l6,l7,l8]
        r='X'
        t='O'
        for i in cl:
            if len(set(i))==1 and r in i or len(set(i))==1 and t in i:
                return t if t in i else r
        return 0
    
    def showlast(self):
        self.turns.hide()
        self.coback.hide()
        self.cagain.show()
        self.cquit.show()
        
    def hidebuttons(self):
        for i in self.butremains:
            i.setText('')
            i.hide()
            
    def gobackg1(self):
        windowg.hide()
        windowb.show()
    def gobackg(self):
        self.startg() 
        self.gobackg1()   
    def showagain(self):
        for i in self.butremains:
            i.show()
        self.turns.show()
        self.coback.show()
    def hideonly(self):
        self.coback.hide()
    def showagain1(self):
        for i in self.butremains:
            i.setText('')
            i.show()    
        self.turns.show()
        self.coback.show()
       
###################################################################################################
###################################################################################################
###################################################################################################
class REDWIN(QMainWindow,Ui_REDWINDOW):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startr()
        
    def startr(self):
        self.xobuttons=[self.xo1,self.xo2,self.xo3,self.xo4,self.xo5,self.xo6,self.xo7,self.xo8,self.xo9]
        self.xobutts=[self.xo1,self.xo2,self.xo3,self.xo4,self.xo5,self.xo6,self.xo7,self.xo8,self.xo9]
        self.ai=[]
        self.step=0
        self.reality=['1','2','3','4','5','6','7','8','9']
        
        self.showlevel()
        self.hideresult()
        self.hideelements()
        
        self.easybut.clicked.connect(lambda:self.chosenlevel(1))
        self.mediumbut.clicked.connect(lambda:self.chosenlevel(2))
        self.hardbut.clicked.connect(lambda:self.chosenlevel(3))
        self.backbut1.clicked.connect(lambda:self.startr())
        self.gobackabove.clicked.connect(lambda:self.backtochoice())
        
        self.xo1.clicked.connect(lambda:self.usebuttons(self.xo1))
        self.xo2.clicked.connect(lambda:self.usebuttons(self.xo2))
        self.xo3.clicked.connect(lambda:self.usebuttons(self.xo3))
        self.xo4.clicked.connect(lambda:self.usebuttons(self.xo4))
        self.xo5.clicked.connect(lambda:self.usebuttons(self.xo5))
        self.xo6.clicked.connect(lambda:self.usebuttons(self.xo6))
        self.xo7.clicked.connect(lambda:self.usebuttons(self.xo7))
        self.xo8.clicked.connect(lambda:self.usebuttons(self.xo8))
        self.xo9.clicked.connect(lambda:self.usebuttons(self.xo9))
        self.againbut1.clicked.connect(lambda:self.foragain())
        self.quitbut1.clicked.connect(lambda:self.backtochoice())
        
    
    def usebuttons(self,clickedone):
        if self.step%2==0 and self.checkwinner()==0 and clickedone in self.xobutts:
            clickedone.setText('X')
            self.turnshow.setText('Turn:   O')
            self.xobutts.remove(clickedone)
            self.reality[self.xobuttons.index(clickedone)]='X'
            self.step+=1
            self.setwinner('X')
            if self.step!=9 and self.checkwinner()==0:
                self.computer_turn()
        
    def computer_turn(self):
        self.turnshow.setText('Turn:   X')
        if self.game_level==1:
            self.easy_ai()
        elif self.game_level==2:
            self.medium_ai()
        elif self.game_level==3:
            self.hard_ai()
            
            
        
    
    def easy_ai(self):
        easy_choice=choice(self.xobutts)
        easy_choice.setText('O')
        self.step+=1
        self.reality[self.xobuttons.index(easy_choice)]='O'
        self.xobutts.remove(easy_choice)
        self.setwinner('O')
    
    def medium_ai(self):
        if self.checkchoice('X','O')==0:
            medium_choice=choice(self.xobutts)
        else:
            medium_choice=self.xobuttons[self.reality.index(self.checkchoice('X','O'))]
        medium_choice.setText('O')
        self.step+=1
        self.reality[self.xobuttons.index(medium_choice)]='O'
        self.xobutts.remove(medium_choice)
        self.setwinner('O')
            
    def hard_ai(self):
        if self.checkchoice('O','X')!=0:
            medium_choice=self.xobuttons[self.reality.index(self.checkchoice('O','X'))]
        elif self.checkchoice('X','O')!=0:
            medium_choice=self.xobuttons[self.reality.index(self.checkchoice('X','O'))]
        elif self.xo5 in self.xobutts:
            medium_choice=self.xo5
        elif self.xo5 in self.ai and self.xo4 in self.xobutts and self.xo6 in self.xobutts:
            medium_choice=self.xo4
        elif self.xo1 in self.xobutts:
            medium_choice=self.xo1
        elif self.xo3 in self.xobutts:
            medium_choice=self.xo3
        elif self.xo7 in self.xobutts:
            medium_choice=self.xo7
        elif self.xo9 in self.xobutts:
            medium_choice=self.xo9
        else:
            medium_choice=choice(self.xobutts)
        medium_choice.setText('O')
        self.step+=1
        self.reality[self.xobuttons.index(medium_choice)]='O'
        self.ai.append(medium_choice)
        self.xobutts.remove(medium_choice)
        self.setwinner('O')
    
    def setwinner(self,champ):
        if self.checkwinner()!=0:
            self.for_results_sake()
            self.backbut1.hide()
            self.showresult()
            #champ=['X','O'][self.step%2==0]
            self.res12.setText(f'  Winner is  {self.checkwinner()}')
        elif self.step==9 and self.checkwinner()==0:
            self.for_results_sake()
            self.backbut1.hide()
            self.showresult()
            self.res12.setText('DRAW') 
    
    def checkchoice(self,xx,yy):
        w=self.reality
        l1=[w[0],w[1],w[2]]
        l2=[w[3],w[4],w[5]]
        l3=[w[6],w[7],w[8]]
        l4=[w[0],w[4],w[8]]
        l5=[w[2],w[4],w[6]]
        l6=[w[0],w[3],w[6]]
        l7=[w[1],w[4],w[7]]
        l8=[w[2],w[5],w[8]]
        cl=[l1,l2,l3,l4,l5,l6,l7,l8]
        for i in cl:
            if i.count(xx)==2 and yy not in i:
                return i[0] if i[0]!=xx else i[1] if i[1]!=xx else i[2]
        return 0

    def checkwinner(self):
        w=self.reality
        l1=[w[0],w[1],w[2]]
        l2=[w[3],w[4],w[5]]
        l3=[w[6],w[7],w[8]]
        l4=[w[0],w[4],w[8]]
        l5=[w[2],w[4],w[6]]
        l6=[w[0],w[3],w[6]]
        l7=[w[1],w[4],w[7]]
        l8=[w[2],w[5],w[8]]
        cl=[l1,l2,l3,l4,l5,l6,l7,l8]
        r='X'
        t='O'
        for i in cl:
            if len(set(i))==1 and r in i or len(set(i))==1 and t in i:
                return t if t in i else r
        return 0
#############################################################################################
#############################################################################################
    def chosenlevel(self,lvl):
        self.game_level=lvl
        self.hidelevel()
        self.showelements()
        
    def showlevel(self):
        self.easybut.show()
        self.mediumbut.show()
        self.hardbut.show()
        self.gobackabove.show()
        
    def hidelevel(self):
        self.easybut.hide()
        self.mediumbut.hide()
        self.hardbut.hide()
        self.gobackabove.hide()

    def hideresult(self):
        self.quitbut1.hide()
        self.againbut1.hide()
        self.res12.hide()
    
    def foragain(self):
        self.backbut1.show()
        self.startr()
    
    def showresult(self):
        self.quitbut1.show()
        self.againbut1.show()
        self.res12.show()
                
    def hideelements(self):
        for i in self.xobuttons:
            i.setText('')
            i.hide()
        self.turnshow.hide()
    
    def for_results_sake(self):
        self.turnshow.hide()
        self.res12.show()
        
    def showelements(self):
        for i in self.xobuttons:
            i.setText('')
            i.show()
        self.turnshow.show()
        self.turnshow.setText('Turn:   X')
        
    def backtochoice(self):
        windowb.show()
        self.startr()
        windowr.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowb=BLUEWIN()
    windowg=GREENWIN()
    windowr=REDWIN()
    windowb.show()
    app.exec_()
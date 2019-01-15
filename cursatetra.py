#SECTION: IMPORTS
import curses as crs

#SECTION: FUNCTIONS

#SECTION: MAIN
#Initialize screen
screen = crs.initscr()
#Set proper key settings
crs.noecho()
crs.cbreak()
screen.keypad(True)
crs.curs_set(0)

#Initialize windows
wTitle = crs.newwin(6, 19, 0, 4)
wScore = crs.newwin(4, 17, 8, 5)
wCntrl = crs.newwin(10, 23, 12, 2)
wBoard = crs.newwin(24, 22, 0, 28)
wNextP = crs.newwin(6, 13, 4, 52)
#Draw boarders of windows
wTitle.border()
wScore.border()
wCntrl.border()
wBoard.border()
wNextP.border()
#Write titles and labels
wTitle.addstr(1, 4, "Cursa Tetra")
wTitle.addstr(2, 1, 17 * '-')
wTitle.addstr(3, 2, "By Charlie Cook")
wScore.addstr(1, 1, "SCORE:")
wNextP.addstr(1, 1, "NEXT PIECE:")
#Make windows visible
wTitle.refresh()
wScore.refresh()
wCntrl.refresh()
wBoard.refresh()
wNextP.refresh()

#Wait
crs.delay_output(2000)

#Unset proper key settings
screen.keypad(False)
crs.nocbreak()
crs.echo()
#Close screen
crs.endwin()

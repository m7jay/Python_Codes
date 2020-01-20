import random
import curses

s =  curses.initscr()
curses.cur_set(0)

sh, sw = s.getmaxyx()
w = curses.newwin(sh,sw,0,0,0)
w.keypad(1)
w.timeout(100)


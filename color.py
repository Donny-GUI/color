#!/usr/bin/env python3
from enum import Enum

class text(Enum):
    black       = "\033[30m" 
    red         = "\033[31m"
    green       = "\033[32m"
    yellow      = "\033[33m"
    magenta     = "\033[34m"
    blue        = "\033[35m"
    cyan        = "\033[36m"
    gray        = "\033[37m"
    clear       = "\033[0m"
    names = ['black', 'red', 'green', 'yellow', 'magenta', 'blue', 'cyan', 'gray']
    values = [black, red, green, yellow, magenta, blue, cyan]
    colors = {
        'black': '\x1b[30m', 
        'red': '\x1b[31m', 
        'green': '\x1b[32m', 
        'yellow': '\x1b[33m', 
        'magenta': '\x1b[34m', 
        'blue': '\x1b[35m', 
        'cyan': '\x1b[36m', 
        'gray':"\033[37m"
        }

class bg(Enum):
    black   = "\033[40m"
    red     = "\033[41m"
    green   = "\033[42m"
    yellow  = "\033[43m"
    blue    = "\033[44m"
    magenta = "\033[45m"
    cyan    = "\033[46m"
    gray    = "\033[47m"
    none    = ""
    values = [black, red, green, yellow, magenta, blue, cyan]
    names   = ['black', 'red', 'green', 'yellow', 'magenta', 'blue', 'cyan', 'gray']
    colors = {
        'black': '\x1b[40m', 
        'red': '\x1b[41m', 
        'green': '\x1b[42m', 
        'yellow': '\x1b[43m', 
        'magenta': '\x1b[44m', 
        'blue': '\x1b[45m', 
        'cyan': '\x1b[46m',
        'gray':"\033[37m"
        }

class font(Enum):
    clear   	= "\033[0m"
    bold    	= "\033[1m"
    dim     	= "\033[2m"
    italic  	= "\033[3m"
    underline 	= "\033[4m"
    blink		= "\033[5m"
    fastblink	= "\033[6m"
    reverse		= "\033[7m"
    standout	= "\033[8m"
    crossout	= "\033[9m"
    none    	=  ""
    double_underline = "\033[21m"
    names = ['clear', 'bold', 'dim', 'italic', 'underlined', 'blink', 'fast blink', 'reverse', 'standout', 'crossout', 'double underline']
    values = [clear, bold, dim, italic, underline, blink, fastblink, reverse, standout, crossout, double_underline]
    fonts = {
    'clear': '\x1b[0m', 
    'bold': '\x1b[1m', 
    'dim': '\x1b[2m', 
    'italic': '\x1b[3m', 
    'underlined': '\x1b[4m', 
    'blink': '\x1b[5m', 
    'fast blink': '\x1b[6m', 
    'reverse': '\x1b[7m', 
    'standout': '\x1b[8m', 
    'crossout': '\x1b[9m', 
    'double underline': '\x1b[21m'
    }

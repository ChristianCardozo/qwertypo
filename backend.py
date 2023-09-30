import random
import numpy as np 

freq_dict =\
{
    'a':{'q':594,'s':42401,'w':10853,'x':3882,'z':3062},
    'b':{'f':16112,'g':21182,'h':10826,'n':19375,'v':6146},
    'c':{'d':19151,'f':15124,'s':37974,'v':7444,'x':1854},
    'd':{'e':39499,'f':16091,'r':64063,'s':80813,'v':7848,'w':10614,'x':2018},
    'e':{'f':17080,'r':76503,'s':75665,'w':13193},
    'f':{'g':13344,'r':18722,'t':20980,'v':5822},
    'g':{'h':10144,'n':23414,'r':22092,'t':30296,'v':5093,'y':5295},
    'h':{'j':2663,'m':11486,'n':11859,'t':23856,'u':10462,'y':5518},
    'i':{'j':699,'k':9983,'l':40985,'o':82987,'u':63669},
    'j':{'k':1248,'m':3464,'n':2011,'u':568,'y':672},
    'k':{'l':14651,'m':8496,'o':8366,'u':5455},
    'l':{'o':43713,'p':30126},
    'm':{'n':23433},
    'o':{'p':18072},
    'q':{'s':2041,'w':728},
    'r':{'t':54571},
    's':{'w':17079,'x':3613,'z':7300},
    't':{'y':13286},
    'u':{'y':6783},
    'x':{'z':516}

} 

probs_dict = {}
for letter in freq_dict:
    mistakes = freq_dict[letter]
    total = np.sum(list(mistakes.values()))
    letter_probs = {}
    for m in mistakes:
        letter_probs[m] = mistakes[m]/total
    probs_dict[letter] = letter_probs

# Main function
def mess_text(start_string,p_mistake=0.2):
    # start_string = input('What would you like to mess up? ')
    new_string = ''
    for l in start_string:
        is_upper = str.isupper(l)
        l = str.lower(l)
        if l in probs_dict: # for debug
            ps = probs_dict[l]
            wrong_letter = random.choices(list(ps.keys()),weights=ps.values())[0]
            mistake = random.random() < p_mistake
            if mistake:
                if is_upper:
                    wrong_letter = wrong_letter.upper()
                new_string += wrong_letter
            else:
                if is_upper:
                    l = l.upper()
                new_string += l
        else:
            if is_upper:
                l = l.upper()
            new_string += l

    return(new_string)















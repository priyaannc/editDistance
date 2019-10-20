__author__ = 'user'
from nltk.metrics import edit_distance

import pandas as pd

#  transposition flag allows transpositions edits (e.g., “ab” -> “ba”),

tweet1 = 'What in the Republic of Gilead is going on here?! This is genocide. This is human trafficking.'
tweet2 = 'At the start of the year, Andy Murray said farewell to the sport he adored.'
tweet3 = 'Just nine months later, he come from a set and a break down to win his first singles title since 2017'
tweet4 = 'PM meeting distress farmers of Mumbai despite busy Schedule'
tweet5 = 'Things that keep you up at night: loneliness, cold, heat, hunger, late night texting'

spam1 = 'stop human trafficking! sign the petition here!http:///bit.ly/hsh678'
spam2 = 'Republic of Gilead, where does this tale take is? click to know more on https://shorte.st'
spam3 = 'What’s the Republic of Gilead in The Handmaid’s Tale,watch more at http:///bit.ly/1sNZMwL+'
spam4 = 'trafficked again,what are we doing to stop? take action http:///bit.ly/hshjh78'
spam5 = 'Gilead, the story nations wants to know at http:///bit.ly/yush678'
spam6 = 'Republic of trafficking,watch to know more http:///bit.ly/hsh678'
spam7 = 'sign the petition agaisnt trafficking petition here!http:///bit.ly/tyhg678'
spam8 = 'petition against Gilead http:///bit.ly/jnhg678'
spam9 = 'Gilead petition http:///bit.ly/knhg678'
spam10 = 'Human insenstivity against genocide, watch http:///bit.ly/kmhg678'
spam11 = 'Chaos at Gilead , click to know more !http:///bit.ly/ui8g678'
spam12 = 'Public wrath for genocide at Gliead , click to know more !http:///bit.ly/ui89g678'
spam13 = 'Nation wants to protest , join to know more !http:///bit.ly/ui8g678'
spam14 = 'Stop genocide! , watch to know more !http:///bit.ly/ui8gfg678'
spam15 = 'Gilead genocide , click to know more !http:///bit.ly/ui8g678'
spam16 = 'Public agianst genocide at Gliead , click to know more !http:///bit.ly/ui8g678'
spam17 = 'Public agianst genocide at Gliead , click to know more !http:///bit.ly/ui8g678'
spam18 = 'Human insenstivity against genocide, watch http:///bit.ly/kmhg678'
spam19 = 'petition against Gilead http:///bit.ly/jnhg678'
spam20 = 'trafficked again,what are we doing to stop? take action http:///bit.ly/hshjh78'

tweetlist = [tweet1,tweet2,tweet3,tweet4] 
spamlist = [spam1,spam2,spam3,spam4,spam5,spam6,
            spam7,spam8,spam9,spam10,spam11,spam12,spam13,spam14,spam15,spam16,
            spam17,spam18,spam19,spam20]
ans =[]
for i in range(0,len(tweetlist)):
 for j in range(0,len(spamlist)):
    ans = edit_distance(tweetlist[i], spamlist[j], transpositions=False)    
    print ('tweet-', i+1 ,'&', 'spam-',j+1,':', ans)
    



        


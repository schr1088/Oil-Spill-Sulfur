# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:23:43 2017

@author: Peter
"""
#basic calculator of H2S after a potential oil spill 
 
def oilspillh2s():
    response = float(raw_input('What % H2S is the oil? ')) 
    if response > 1:
        print "Sour Oil, Watch out Wildlife!"  
        #sour oil defenition >1%
    response2 = int(raw_input('What volume of oil was released? m^3, only integers.  '))
    if (response2) > 780000:
        print "Largest man made spill ever!"
        #Deep water Horizon was the largest @ 780000
    H2S = (response * response2 *.01)
    print(H2S, "m^3 of H2S released into the ocean") 
    #could later convert to Liters using 1 m^3 = 1000 L
    response3 = int(raw_input('How many benthic chemosythetic communities are in the affected region?  '))
    #until further exploration is done this is value is unknown funding/means for deep sea exploration limited
    if response3 >= 10 and H2S >= 5000:
         #don't actually know this, seems reasonable
        print "significant changes to regional oceanic pH and alkalinity"
    else:
        print "changes are inconsequential for regional oceanic chemistry"
        
if __name__ == "__main__":
    oilspillh2s()
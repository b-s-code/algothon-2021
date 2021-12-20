import numpy as np

#declare variable:
#number of financial instruments under consideration
nInst = 100

#declare variable:
#respective positions for the financial instruments (as a list)
#positions all initialised to zeros
currentPos = np.zeros(nInst)

def getMyPosition(prcSoFar):
    #global variable:
    #respective positions for the financial instruments (as a list)
    global currentPos
    
    #variable declaration:
    #number of days to use in short term weighted moving average
    k = 4 
    
    #variable declaration:
    #number of days to use in long term moving average
    l = 50 
    
    #create a list:
    #short term weighted moving averages (k days)
    #one for each individual financial instrument
    wmaK = [ sum([prcSoFar[k - i,j] * (k - i + 1) for i in range(1,k + 1)]) / sum(range(1,k + 1))  for j in range(nInst)] 

    #create a list:
    #long term moving averages (unweighted) (l days)
    movAvgL = [sum(prcSoFar[-l - 1:-1, i])/l for i in range(nInst)]
    
    #variable declaration:
    #day of trading (1-based index, not 0-based)
    day = len(prcSoFar)
    
    #logical branch:
    #there are insufficient data points to calculate moving averages yet
    if day < l: 
        return currentPos
        
    #logical branch:
    #there are just enough data points to calculate moving averages
    elif day == l: 
	#set initial position of 100 units for each financial instrument
        currentPos = np.full(nInst,100)
        
    #logical branch:
    #there are more than enough data points to calculate moving averages
    #(short term and long term moving averages can now be compared)
    elif day > l:
    
    	#iterate over list of distinct financial instruments
        for i in range(nInst):
       	    
       	    #logical branch:
       	    #short and long term moving averages are equal
            if wmaK[i] == movAvgL[i]:    
                pass
                
            #logical branch:
            #short term moving average above long term moving average
            elif wmaK[i] > movAvgL[i]:   
                #sell signal
                #decrease holdings in the financial instrument under consideration
                currentPos[i] -= 100
                
       	    #logical branch:
       	    #short term moving average below long term moving average
            elif wmaK[i] < movAvgL[i]:
                #buy signal
                #increase holdings in the financial instrument under consideration
                currentPos[i] += 100
    
    #return updated respective positions for the financial instruments (as a list)
    return currentPos












































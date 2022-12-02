from time import * #to see the time taken

#to check if the typing is correct
def terror(prompt):
    global inwords
    
    
    words = prompt.split() # here split the words into characters
    errors = 0
    
    for i in range (len(inwords)):
        if i in (0,len(inwords)-1):
            if inwords[i] == words[i]:  # if we get the splitted charachter here then continue or else give error
                continue
            
            else:
                errors = errors + 1
           
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]): 
                   continue
                else:        #now group of individual characters are checked if same continue or error
                    errors = errors + 1
            else:
                 errors = errors + 1
    
    return errors 


# now for speed of typing here we have words/minute
def speed(inpromt,stime,etime):
    global time
    global inwords #declare it as a global variable
    
    inwords = inpromt.split() #split them
    twords =len(inwords) # take the length of the word
    speed = twords/time #speed equation 
    
    return speed
# findinding the time taken for completing

def totaltime(stime,etime): #start time ,end time
    time = etime - stime #time taken 
    
    return time
   
   
if __name__ == '__main__' :
    prompt = '''python hello world'''
    print("Type this :- ",prompt," ")
    
#checking for the input
input("press enter when u are ready")

#recording time for input
stime=time()
inpromt=input()
etime=time()

#now take back the info recieved

time = round(totaltime(stime,etime),2)
speed = speed(inpromt,stime,etime)
errors = terror(prompt)
                   
print("########################################")                   
print("total time taken: ", time, "seconds")
print("your avg typing speed was ", speed, "words per minute")
print("with total of ",errors, "errors")
print("########################################")
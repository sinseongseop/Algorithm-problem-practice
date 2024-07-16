def solution(cards):
    cardCnt = len(cards)
    maxBoxCnt = [-1,-1]
    
    for i in range(cardCnt):
        if(cards[i] == -1):
            continue
            
        partCnt = circle(cards,i)    
        #print(partCnt)

        if(partCnt > maxBoxCnt[0]):
            maxBoxCnt[1]=maxBoxCnt[0]
            maxBoxCnt[0]=partCnt
        elif(partCnt > maxBoxCnt[1]):
            maxBoxCnt[1]=partCnt

    #print(maxBoxCnt)
    
    answer = 0
    if(maxBoxCnt[0] != cardCnt):
        answer = maxBoxCnt[0]*maxBoxCnt[1]

    return answer

def circle(cards, cardIndex):
    if(cards[cardIndex] == -1):
        return 0
    else:
        nextCardIndex = cards[cardIndex]-1
        cards[cardIndex] = -1
        return circle(cards, nextCardIndex) + 1
    
cards=[2,1,4,3]
print(solution(cards))
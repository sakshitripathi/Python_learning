
def temp(templist):
    averagetemp= sum(templist)//len(templist)
    highesttemp=max(templist)
    lowesttemp=min(templist)
    return averagetemp,highesttemp,lowesttemp
temperature=list(map(int,input("enter temperatures: ").split()))
print("average temp, highest temp, lowest temp",temp(temperature))
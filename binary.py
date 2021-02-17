import math

def binarySearch( arrayList, searchItem ):
    found = False
    listLen = len( arraylist)
    midPoint = math.floor( listLen / 2 )
    if arrayList[ midPoint ] == searchItem:
        found = True
    elif listLen > 1:
        if searchItem < arrayList[ midPoint ]:
            found = binarySearch( arrayList[0:(midPoint-1)], searchItem )
        else:
            return binarySearch( arrayList[midPoint: ], searchItem )
        return found

def getListIntegers( length ):
    result = [1, 1]
    for i in range(length):
        temp = result[-2] + result[-1]
        result.append( temp )
    return result

if binarySearch == "True":
	print("Target ",str(getListIntegers),"was in the list!")
else:
	print("Target ",str(getListIntegers),"was NOT in the list!")

    #Hello mr wilson idk why this doenst work
    #I changed midpoint+1: to midpoint: but its still not working :/
    #NEVERMIND MR WILSON ME AND AIDEN WORKED IT OUT WE FORGOTR THE PRINT PART LOL
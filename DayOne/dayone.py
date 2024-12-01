import lists

def compare_lists(leftlist, rightlist):
    
    totaldistance = 0

    while len(leftlist) > 0:
        leftlow = 100000
        rightlow = 100000

        for i in leftlist:
            if i < leftlow:
                leftlow = i
        
        leftlist.remove(leftlow)

        for i in rightlist:
            if i < rightlow:
                rightlow = i
        
        rightlist.remove(rightlow)

        distance = abs(leftlow - rightlow)

        totaldistance += distance

    print(f"Total distance is: {totaldistance}")


compare_lists(lists.leftlist, lists.rightlist)
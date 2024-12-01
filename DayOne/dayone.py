import lists

def compare_lists(leftlist, rightlist):
    
    leftlow = 10
    rightlow = 10
    totaldistance = 0


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
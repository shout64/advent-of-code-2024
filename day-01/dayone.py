import lists

def compare_lists(leftlist, rightlist):
    
    totaldistance = 0

    leftlistcopy = leftlist.copy()
    rightlistcopy = rightlist.copy()

    while len(leftlistcopy) > 0:
        leftlow = 100000
        rightlow = 100000

        for i in leftlistcopy:
            if i < leftlow:
                leftlow = i
        
        leftlistcopy.remove(leftlow)

        for i in rightlistcopy:
            if i < rightlow:
                rightlow = i
        
        rightlistcopy.remove(rightlow)

        distance = abs(leftlow - rightlow)

        totaldistance += distance

    print(f"Total distance is: {totaldistance}")


compare_lists(lists.leftlist, lists.rightlist)

def calculate_similarity_score(leftlist, rightlist):
    
    score = 0

    for i in leftlist:
        duplicates = 0
        for j in rightlist:
            if i == j:
                duplicates += 1
        score += (i * duplicates)

    print(f"Total similarity score: {score}")

calculate_similarity_score(lists.leftlist, lists.rightlist)

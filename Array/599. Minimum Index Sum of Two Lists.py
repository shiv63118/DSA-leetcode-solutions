def findRestaurant(list1, list2):
    ans = []
    ind = 20001
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                if i+j < ind:
                    del ans[:]
                    ind = i+j
                    ans.append(list1[i])
                elif i+j == ind :
                    ans.append(list1[i])
        return ans
                    
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

print(findRestaurant(list1, list2))
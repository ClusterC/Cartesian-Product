# Cartesian-Product

""""""""""""""
# (i//pow(len(itme_list),3))%(len(itme_list)) , (i//pow(len(itme_list),2))%(len(itme_list)) , (i//len(itme_list))%(len(itme_list)) , i%(len(itme_list)))
#
""""""""""""""

def Example_function(item_list,base : int = 0):

    count_item = len(item_list)
    
    if base <= 0:
        base = count_item

    for i in range(pow(count_item, base)): ##
        
        if count_item > 2:
            for j in range(base-1, 1, -1): ##
                print((i//pow(count_item,j))%(count_item),end=' ')
                
        print((i//count_item)%(count_item), i%(count_item))



if __name__ == '__main__':
    item_list = [0,1,2,3]
    Example_function(item_list)
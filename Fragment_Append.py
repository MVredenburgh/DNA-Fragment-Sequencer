def AppendFragment(LeftFragment, RightFragment, k):
    m=0
    i=0
    while True:
        #print('m: ',m, 'i: ', i, 'LeftFragment[m+i]: ',LeftFragment[m+i],'RightFragment[i]: ', RightFragment[i])
        if LeftFragment[m+i] == RightFragment[i]:
            #print("we equal")
            if m+i == len(LeftFragment)-1:
##                if i > k:
                return [LeftFragment[:m]+RightFragment, i]
##                else:
##                    return ['',0]
            if i == len(RightFragment)-1:
                return LeftFragment
            i += 1
        else:
            i = 0
            m += 1
            if m == len(LeftFragment)-1:
##                if k == 0:
##                    return LeftFragment+RightFragment
                return ['',0]

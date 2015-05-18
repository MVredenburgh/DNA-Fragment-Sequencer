import Fragment_Append_test as FA, random
def DNA_Sequence(filename):
    DNA_Fragments = open(filename,"r").readlines()
    DNA_Fragments = [line.rstrip() for line in DNA_Fragments]
    while True:
        numFragments = len(DNA_Fragments)
        
        if numFragments == 1:
            OutputFile = open('output14.txt', "w")
            OutputFile.write(DNA_Fragments[0])
            OutputFile.close()
            return 
##        rand1 = 0
##        rand2 = 0
##        k=5
##        if numFragments < 70:
##            k=2
##        if numFragments <50:
##            k=1
##        if numFragments < 30:
##            k = 0
##        while rand1 == rand2:
##            rand1 = random.randint(0, numFragments-1)
##            rand2 = random.randint(0, numFragments-1)
        maxArray = []
        for i in range(numFragments-1):
            for j in range(numFragments-1):
                if i == j:
                    maxArray.append(['',0])
                else:
                    maxArray.append(FA.AppendFragment(DNA_Fragments[i], DNA_Fragments[j]))
                                    
        
        if len(AppendedFrag) > 0:
            print(numFragments)
            DNA_Fragments = DNA_Fragments[0:rand1] + DNA_Fragments[rand1+1:]
            DNA_Fragments = DNA_Fragments[0:rand2] + DNA_Fragments[rand2+1:]
            DNA_Fragments.append(AppendedFrag)

            
        

def CountWordFromFile():
    fname = input('Enter Your File Name :  ') 
    numbersOfWOrds=0
    file = open(fname,'r')
    for i in file :
        words = i.split()
        numbersOfWOrds = numbersOfWOrds + len(words)
        #print(words)
    print('Number of Word in A file  : ' + str(numbersOfWOrds))
CountWordFromFile()


def houwMuchShouldIGiveBack(token):
    for i in inDZD:
        if CoinsQuantities[i] != 0:
         given = token / i

         if i == inDZD[len(inDZD)-1] and CoinsQuantities[i] < given:
            print "We dont heve enough change of %i DA to give. (we need %i more), %i DA to be given." %(i, (token - CoinsQuantities[1] * i), (given * i))
            break

         if given <= CoinsQuantities[i]:
                token -= (given * i) 
                CoinsQuantities[i] -= given
         else:
                given = CoinsQuantities[i]
                token -= (given * i)
                CoinsQuantities[i] -= given

         if given != 0:
            print "Give %i from %i" %(given, i)   

inDZD = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
CoinsQuantities = {
    2000 : 5, 
    1000 : 0, 
    500 : 1, 
    200 : 0, 
    100 : 2, 
    50 : 3, 
    20 : 10, 
    10 : 0, 
    5 : 0, 
    2 : 1, 
    1 : 5
}

while True:
    HMHSGY = int(raw_input("---------------\nHow much he/she gives you?\n>>>"))
    HMIC = int(raw_input("How much it coast?\n>>>"))
    token = HMHSGY-HMIC

    if token > 0:
        houwMuchShouldIGiveBack(token)
    else:
        print "\n !!! He/She must give you more !!! \n"
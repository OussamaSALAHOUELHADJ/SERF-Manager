# In DZD we have 1, 2, 5, 10, 20, 50, 100, 500, 1000, 2000 coins
# You can change the table to your country's coins
# ---------------------------------- NOTE --------------------------------------
# | I know that the Algerians will never use this progrm except in some "RARE" |
# | cases because they will always ask for the SERF and they will let you      |
# | go and bring the SERF even if you don't carry any.                         |
# ------------------------------------------------------------------------------

def houwMuchShouldIGiveBack(token):
    inDZD = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for i in inDZD:
         given = token / i
         token = token - (given * i) 
         if given != 0:
            print "Give %i from %i" %(given, i)

while True:
    HMHSGY = int(raw_input("---------------\nHow much he/she gives you?\n>>>"))
    HMIC = int(raw_input("How much it coast?\n>>>"))
    token = HMHSGY-HMIC
    if token > 0:
        houwMuchShouldIGiveBack(token)
    else:
        print "\n !!! He/She must give you more !!! \n"
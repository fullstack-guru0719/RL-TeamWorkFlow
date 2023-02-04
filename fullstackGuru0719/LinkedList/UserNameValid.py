# include: a-z,A-Z,_
import re

def userNameVal(userName):
    userPat = "^[A-Za-z][A-Za-z_]{7,29}$"
    if userName[-1] == '_':
        return False
    elif re.match(pattern=userPat,string=userName):
        return True
    else:
        return False
        

print(userNameVal("asssdf_ffws_"))
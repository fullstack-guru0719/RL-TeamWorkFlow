def LongestWord(sen):
    nw = ""
    for letter in sen:
      if letter.isalpha():
        nw += letter
      else :
        nw += " "
    return max(nw.split(),key=len)

print(LongestWord("#sfs071_-fsdf"))
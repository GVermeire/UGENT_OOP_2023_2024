def isPalindrome(s):
    return c == c[::-1] #Deze regel gebruikt slicing ([::-1]) om de omgekeerde versie van de string s te verkrijgen en controleert vervolgens of de originele string gelijk is aan zijn omgekeerde versie

s = input('Enter a string:')
c=''.join(s.split()) # verwijdert spaties uit de ingevoerde string s door de string te splitsen met split() en vervolgens weer samen te voegen met join('')
ans = isPalindrome(s) # ans zal hier true of false zijn

if ans: # als ans true is zal dit worden afgeprint en anders de else print
    print("The string {} is a palindrome.".format(s))
else:
    print("The string {} is not a palindrome.".format(s))
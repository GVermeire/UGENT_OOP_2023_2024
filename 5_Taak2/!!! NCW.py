bedrag=float(input())
jaren=int(input())
rente=float(input())
NPV=0
for i in range(1,jaren+1):
    inkomst=float(input())
    uitgave=float(input())
    NPV=NPV+(inkomst-uitgave)/(1+rente)**(i-1)
tot_NPV=NPV-bedrag
print('De netto constante waarde over {} jaar is € {:.2f}.'.format(jaren,tot_NPV))
if tot_NPV>bedrag:
    print('Hoera! Er wordt een winst geboekt van € {:.2f}!'.format(tot_NPV-bedrag))
elif tot_NPV==bedrag:
    print('Er wordt exact break-even gedraaid.')
else:
    print('Er is helaas een verlies van € -{:.2f}.'.format(bedrag-tot_NPV))
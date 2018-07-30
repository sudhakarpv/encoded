# encoded
def main():
    pass
    n=input().upper()
    list_1=list(n)
    final=[]
    l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
       'S','T','U','V','W','X','Y','Z','A','B','C']
    for i in list_1:
        findind=l.index(i)
        add=int(findind+3)
        value=l[add]
        final.append(value)
    print(''.join(final))
if __name__ == '__main__':
    main()

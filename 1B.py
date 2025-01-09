for _ in range(0,int(input())):
    coordinate=input()
    if coordinate[0]=='R' and coordinate[1].isdigit() and coordinate.find('C')!=-1:
        left,right=coordinate.split('C')
        row=int(left[1:]);column=int(right)
        cd_out=""
        while column>0:
            rest=column%26
            if rest==0: rest=26
            cd_out=chr(ord('A')-1+rest)+cd_out
            column=(column-rest)//26
        print(cd_out,row,sep='')
    else:
        i=1
        while not(coordinate[i:].isdigit()):
            i+=1
        row=int(coordinate[i:])
        column=0
        for j in range(0,i):
            column+=26**j*(ord(coordinate[i-1-j])-ord('A')+1)
        print("R%dC%d"%(row,column))
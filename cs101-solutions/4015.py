while True:
    try:
        ad=input().replace(" ","")
        if ad.count("@")!=1:
            print("NO")
        else:
            index=ad.find("@")
            if ad[index-1]=="." or ad[index+1]=="." or ad[0]=="." or ad[0]=="@" or ad[-1]=="." or ad[-1]=="@":
                print("NO")
            else:
                if ad.count(".",index)>0:
                    print("YES")
                else:
                    print("NO")
    except EOFError:
        break
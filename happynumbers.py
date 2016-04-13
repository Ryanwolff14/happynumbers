def printintro():
    print("first 20 happy numbers are")

def findhappy():
    happy=[]
    for _ in range(101):
        number=_
        x=[]
        s=0
        while not (s in x[:-1]) and s!=1:
            s=0
            for __ in str(number):
                s+= int(__)**2
            x.append(s)
            number=s
        if x[-1]==1:
            happy.append(_)
    print (happy)


def main():
    printintro()
    findhappy()

main()
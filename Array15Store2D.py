from random import randint

def init(sell):
    for r in range(16):
        sell.append([])
        for c in range(8):
            sell[r].append(c)
            sell[r][c]=0

def EnterData(sales):
    for r in range(15):
        for c in range(7):
            sales[r][c]=randint(0,100)

def Calctotals(sales):
    for r in range(15):
        for c in range(7):
            sales[r][7]=sales[r][7]+sales[r][c]
            sales[15][c]=sales[15][c]+sales[r][c]
        sales[15][7]=sales[15][7]+sales[r][7]

def Report(sales):
    print("="*55)
    print(f"|{'No.':>5}",end='')
    for r in range(7):
        print(f"| Day{r+1}",end='')
    print(f"|{'Total':>5}|")
    print("="*55)
    for r in range(16):
        if r==15:
            print(f"|Total",end='')
        else:
            print(f"|{r+1:>5}",end='')
        for c in range(8):
            print(f"|{sales[r][c]:>5}",end='')
        print("|")
    print("="*55)    

    
#main
sales =[]
init(sales)
EnterData(sales)
Calctotals(sales)
Report(sales)

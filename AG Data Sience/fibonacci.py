'''
def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
'''

def NächsteFibonacciZahl(fiboFolge):
    if len(fiboFolge)<=2:
        return(1)
    else:
        return sum(fiboFolge[len(fiboFolge)-2:])

FibonacciSeries = []
print("\n Die ersten 20 Werte der Fibonacci Folge lauten")
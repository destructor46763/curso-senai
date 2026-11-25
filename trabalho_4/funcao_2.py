def eh_par():
    for n in list(range(1, 10)):
        if n % 2 == 0:
            return True
        else:
            return False
    
par = eh_par()
print(par)
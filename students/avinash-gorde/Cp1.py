def avg(n1,n2,n3):
    a=n1+n2+n3/3
    return(a)

def result(a):
    if a>=75:
        print("distiction")
    elif a>=35:
        print("pass")
    else:
        print("fail")
        
def classify_grade(score):
    if score >= 90:
        return("A")
    elif score >= 80:
        return("B")
    elif score >= 70:
        return("C")
    elif score >= 60:
        return("D")
    else:
        return("F")
        
def format_marks(m1,m2,m3):
    return(f"{m1},{m2},{m3}")

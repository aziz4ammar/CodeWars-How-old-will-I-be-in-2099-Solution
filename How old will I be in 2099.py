def calculate_age(year_of_birth, current_year):
    k=current_year-year_of_birth
    if k>1:
        return "You are "+str(k)+" years old."
    elif k==0:
        return "You were born this very year!"
    elif k==-1:
        return "You will be born in "+str(abs(k))+" year."
    elif k<-1:
        return "You will be born in "+str(abs(k))+" years."
    elif k==1:
        return "You are "+str(k)+" year old."
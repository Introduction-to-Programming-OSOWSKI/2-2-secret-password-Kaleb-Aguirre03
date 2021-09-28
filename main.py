#Define the Function password() with if and else statements
def password(p):
    if p == "knights19":
        return "ACCESS GRANTED"

    else:
        return "ACCESS DENIED"

#Print the function with an incorrect password
print (password("sakljdf;kgj;jfb"))

#Print the function with the correct password
print (password("knights19"))
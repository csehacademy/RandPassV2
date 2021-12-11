from random import choice
length = int(input("Give password lenght: "))

string_char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y",0,1,2,3,4,5,6,7,8,9,0,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z","!","/","}","[","]","{","_","-","@","#","$","%","^","&","*","(",")","?"]

rstr= [choice(string_char) for i in range(length)]

last_pass = "".join([str(elements) for elements in rstr])

print(last_pass)










string = input("Digite uma string: ")

inverte_string = ""
for i in range(len(string)-1, -1, -1):
    inverte_string = inverte_string + string[i]

print (f"A sua String: {string}, investida fica assim", inverte_string)
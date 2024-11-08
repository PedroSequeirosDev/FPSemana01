char1 = str((input("Name first character ")))
health1 = int (input("whats their health? "))
level1 = int(input("whats their level "))
char2 = str((input("Name second character ")))
health2 = int (input("whats their health? "))
level2 = int(input("whats their level "))
char3 = str((input("Name third character ")))
health3 = int (input("whats their health? "))
level3 = int(input("whats their level "))

print ("these are the character you input characters")

print (char1)
print (health1)
print (level1) 
print (char2)
print (health2)
print (level2)
print (char3)
print (health3)
print (level3)

stats = [
    [char1,(health1, level1)],
    [char2,(health2, level2)],
    [char3,(health3, level3)]
]

print (stats)


if level1 > level2 and level1 > level3:
    print (char1)
    if char2 > char3:
        print (char2)
        print (char3)
    else:
        print (char3)
        print (char2)
if level2 > level1 and level2 > level3:
    print (char2)
    if char1 > char3:
        print (char1)
        print (char3)
    else:
        print (char3)
        print (char1)
if level3 > level1 and level3 > level2:
    print (char3)
    if char1 > char2:
        print (char1)
        print (char2)
    else:
        print (char2)
        print (char1)



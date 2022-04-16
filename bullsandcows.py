# IMPORTOVANI BALICKU RANDOM
import random

'''
author = Ludek Larys DJ Kratos
'''

# VRACI SEZNAM CISLIC
def getDigits(num):
	return [int(i) for i in str(num)]
	

# VRACI TRUE POKUD JE CISLO DUPLIKAT, JINAK FALSE
def noDuplicates(num):
	num_li = getDigits(num)
	if len(num_li) == len(set(num_li)):
		return True
	else:
		return False

# GENERACE 4 NAHODNYCH CISEL, BEZ DUPLIKATU
def generateNum():
	while True:
		num = random.randint(1000,9999)
		if noDuplicates(num):
			return num



# VRACI CISLICE SE SHODOU NA POZICI (BULLS)
# NEBO SPRAVNA CISLA NA SPATNE POZICI (COWS)
def numOfBullsCows(num,guess):
	bull_cow = [0,0]
	num_li = getDigits(num)
	guess_li = getDigits(guess)
	
	for i,j in zip(num_li,guess_li):
		
		# PRITOMNA CISLICE V LISTU
		if j in num_li:
		
			# SHODA CISLICE V LISTU
			if j == i:
				bull_cow[0] += 1
			
			# SHODA CISLICE V LISTU, ALE NA SPATNEM MISTE
			else:
				bull_cow[1] += 1
				
	return bull_cow
	
num = generateNum()
tries =int(input('ZADEJTE POCET POKUSU: '))

# HRA KONCI PO NEKOLIKA SPATNYCH POKUSECH
while tries > 0:
	guess = int(input("ZADEJTE SVUJ TIP: "))
	
	if not noDuplicates(guess):
		print("CISLO BY NEMELO MIT ZADNE DUPLIKATY!")
		continue
	if guess < 1000 or guess > 9999:
		print("ZADEJTE POUZE CTYRI CISLICE!")
		continue
	
	bull_cow = numOfBullsCows(num,guess)
	print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
	tries -=1
	
	if bull_cow[0] == 4:
		print("HUURRAY!!!\nYOU WON")
		break
else:
	print(f"KONEC HRY. TAJNE CISLO BYLO: {num}")

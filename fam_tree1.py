"""
print uniformly witout all the tab spacing
do some error checking for input data
create a way to link back generations thru seperate tree created....
"""

fam_dict = {'mmm':['GreatGM Unknown','0000-0000'],'mmf':['GreatGF Unknown','0000-0000'],'mfm':['GreatGM Unknown','0000-0000'],\
'mff':['GreatGF Unknown','0000-0000'],'fmm':['GreatGM Unknown','0000-0000'],'fmf':['GreatGF Unknown','0000-0000'],\
'ffm':['GreatGM Unknown','0000-0000'],'fff':['GreatGF Unknown','0000-0000'],'mm_':['GrandM Unkown','0000-0000'],\
'mf_':['GrandF Unkown','0000-0000'],'fm_':['GrandM Unkown','0000-0000'],'ff_':['GrandF Unkown','0000-0000'],\
'm__':['Mother Uknown','0000-0000'],'f__':['Father Unkown','0000-0000'],'s__':['SelfName','0000-0000']}


def name_list():
	print("\n\n\n\n\nWho would you like to update?\n\nGreat Grand Parents:\nmmm = Mother's Mother's Mother\n\
mmf = Mother's Mother's Father\nmfm = Mother's Father's Mother\nmff = Mother's Father's Father\nfmm = Father's Mother's Mother\n\
fmf = Fathers's Mother's Father\nffm = Father's Father's Mother\nfff = Father's Father's Father\n\
\nGrand Parents:\nmm = Mother's Mother\nmf = Mother's Father\nfm = Father's Mother\n\
ff = Father's Father\n\nParents:\nm = Mother\nf = Father\n\ns = Self\n\n")

def read_tree(file_name):		
	with open(file_name + '.py', 'r') as f:
		gen_script = f.read()
	gen_list = gen_script.split(',')
	if gen_list[-1] == '':
		gen_list.pop()
	return gen_list

def print_tree(gen_list):
	#prints out visual tree,
	for per in gen_list:  
		for key in fam_dict.keys():
			if per[0:3] == key:
				per = per[3:]
				name = per.split('.')
				fam_dict[key][0] = name[0]
				fam_dict[key][1] = name[1]

	print('\n\n' +fam_dict['mmm'][0] +'___'+fam_dict['mmf'][0]+'\t'+fam_dict['mfm'][0]+'___'+fam_dict['mff'][0]+\
	'\t'+fam_dict['fmm'][0]+'___'+fam_dict['fmf'][0]+'\t'+fam_dict['ffm'][0]+'___'+fam_dict['fff'][0])
	print('  '+fam_dict['mmm'][1]+'   '+fam_dict['mmf'][1]+' \t\t'+fam_dict['mfm'][1]+'\t '+fam_dict['mff'][1]+\
	' \t\t'+fam_dict['fmm'][1]+' \t'+fam_dict['fmf'][1]+' \t\t'+fam_dict['fmm'][1]+'\t '+fam_dict['fff'][1])

	print('\n\t\t'+fam_dict['mm_'][0]+'________________________'+fam_dict['mf_'][0]+'\t\t\t\t\t'+fam_dict['fm_'][0]+\
	'________________________'+fam_dict['ff_'][0])
	print('\t\t '+fam_dict['mm_'][1]+'\t\t\t    '+fam_dict['mf_'][1]+'\t\t\t\t  '+fam_dict['fm_'][1]+'\t\t\t\t    '+fam_dict['ff_'][1])
	
	print('\n\t\t\t\t\t'+fam_dict['m__'][0]+'____________________________________________________________________'+fam_dict['f__'][0])
	print('\t\t\t\t\t  '+fam_dict['m__'][1]+'\t\t\t\t\t\t\t\t\t\t     '+fam_dict['f__'][1])
	
	print('\n\t\t\t\t\t\t\t\t\t\t'+ fam_dict['s__'][0])
	print('\t\t\t\t\t\t\t\t\t\t '+ fam_dict['s__'][1])

def family_base():
	with open('fam_base_list.py','r+') as f:
		read = f.read()
		print("\nwhat file would you like to access?\nor type 'new' for a new family tree")
		print('\n' +read)
		file = input()
		file = file.lower()
		while file not in read:
#			#add clause to check for typos to avoid writing xtra files
			if file == 'new':
				print("What would you like to name this Family Tree?\nPlease use the person's name who the relations are linked to")
				file = input()
				if file not in read:
					f.write('\n' + file.lower())
					print('\nCreating new Family Tree...')
					#open file used to create file for later use
					with open(file + '.py', 'w+'):
						break
				else:
					break
			else:
				print("\nYou did not choose an existing Family file or a new one.\nplease enter the file name from the list or type 'new'")
				file = input()
		
		print('opening Family Tree: ' + file)

	return file



class Person():
	def __init__(self, member, name, birth, death = 'present'):
		self.member = member
		self.name = name
		self.birth = birth
		self.death = death
	def __str__(self):
		return f'{self.name}.{self.birth}-{self.death}'
	def member_check(self):
		if len(self.member) > 3:
			print('member title must be under 3 digits long\ntry again!')
			return(True)
		while len(self.member) < 3:
			self.member += '_'
		if self.member[0] not in '_smf' or self.member[1] not in '_smf' or self.member[2] not in '_smf':
			print('invalid member title, please try again: ')
			return(True)
		return(False)

	def birth_date_check(self):
		if len(self.birth) != 4:
			print('Birth year must be 4 digits long')
			return(True)
		for n in self.birth:
			if n not in '1234567890':
				print('must be a valid year number')
				return True
		return False
	def death_date_check(self):
		if len(self.death) != 4:
			print('Death year must be 4 digits long')
			return(True)
		for n in self.death:
			if n not in '1234567890':
				print('must be a valid year number')
				return True
		return False


while True:

	file = family_base()
	fam_tree = file.lower()

	print_tree(read_tree(fam_tree))
	gen_list = read_tree(fam_tree)
	temp_gen_list = []
	edit = input('would you like to input or update a family member? yes or no\n')
	while edit.lower()[0] == 'y':
		living = input('Is this family member still living?')
		name_list()
		if living.lower()[0] == 'n':
			person = Person(input('Family member being updated?'), input('name: '), input('birth year: '), input('death year: '))
			while person.death_date_check():
				person.death = input()
		else:
			person = Person(input('Family member being updated?'), input('name: '), input('birth year: '))
		while person.birth_date_check() == True:
			person.birth = input()
		while person.member_check() == True:
			person.member = input()
		index = 0
		duplicate = False
		for per in gen_list:
			if per[0:3] == person.member:
				overwrite = input(f'you are about to overwrite {per[3:]}, would you like to continue: ')
				if overwrite.lower()[0] == 'y':
					gen_list.pop(index)
				else:
					duplicate = True
			index += 1
		gen_list.append(f'{person.member}{person}')
		if duplicate:
			gen_list.pop()	
		
		edit = input('would you like to update another? ')
	#print(gen_list)


	def save_tree(file_name, mode, gen_list):
		gen_script = ''
		for per in gen_list:
			gen_script += per + ','

		with open(file_name + '.py', f'{mode}') as f:
			f.write(gen_script)

	save_tree(fam_tree, 'w', gen_list)
	#print(read_tree(fam_tree))
	print_tree(read_tree(fam_tree))

	print('would you like to edit another Family Tree?')
	ans = input()
	ans = ans.lower()[0]
	if ans == 'y':
		continue
	else:
		print('\nthank you for updating the Family Ochard.')
		break
# -*- coding: UTF-8 -*-

import sys
import string
import random

def readFileToList(nameFile):
	f = open(nameFile)
	l = [line.strip() for line in f]
	return l
	pass
def randnumberfromlistsize(list1):
	rand=random.randint(0,len(list1)-1)
	return list1[rand]
	pass

def err_res(error,randname,randlast_name,randstreet,randcityes,country,countpeople,numberphone):
	# перестановка соседних букв, вставка буквы.
	
#	temp= int(float(countpeople)*float(error))
#	if temp==10:
#		temp=9;
#	if temp==0:
#		return res
#	while temp>=10:
#		if temp>=10:
#			temp=temp/10

	errorrandom = random.randrange(1.0,10.0)
#	temp=10-temp
	#if temp==0:
	#	temp=0
	if (float(error)*10>=float(errorrandom)):
		#print(str(temp)+' 00000000000000//////////'+ str(errorrandom))
		randname='(*)'+randname
		numerror=random.randint(1,6)
		if numerror==1: #перестановка двух соседних цифр
			#print("1111111111")
			tempnum = numberphone[1]
			tempnum2= numberphone[2]
			numberphone.replace(tempnum2,tempnum,1)
			numberphone.replace(tempnum,tempnum2,1)
		if numerror==2: #замена цифры на другую
			numberphone.replace(numberphone[random.randint(2,len(numberphone)-1)],"8",1)
			#print('22222222222222')
		if numerror==3: #удаление буквы
			randname.replace(randname[random.randint(0,len(randname)-1)],' ')
			#print('333333333333333')
		if numerror==4:#дублирование буквы
			#print('44444444444')
			randname+=randname[len(randname)-1]
		if numerror==5:#перестановка соседних букв
			#print('55555555555')
			tempnum = country[1]
			tempnum2= country[2]
			country.replace(tempnum2,tempnum,1)
			country.replace(tempnum,tempnum2,1)
		if numerror==6:#вставка буквы
			randname+='к'
			#print('666666666')
	if country.lower()=='usa':
		res=randname+' '+randlast_name+'; '
		res+=str(random.randint(1,200))+' '+randstreet+', '
		if random.randint(0,1)==1:
			res+='Suite '+str(random.randint(1,1000))+', '
		else:
			res+=str(random.randint(1,5))+'rd and '
			res+=str(random.randint(5,10))+'th Floors, '
		res+=randcityes+str(code_usa(randcityes))
		return res

	res = randname+' '+randlast_name+'; '+randstreet+', '+ str(random.randint(1,100))+', '
	res+=str(random.randint(1,100))+', г.'+randcityes+''+', '+country+' '+numberphone
	return res
	pass
def code_usa(randcityes):
	listcodephone=	{
		'Alabama':205,
		'Alaska': 907,
		'Arizona': 520,
		'Arkansas':501,
		'California':209,
		'Colorado':303,
		'Connecticut':203,
		'Delaware':302,
		'Florida' : 305,
		'Georgia':229,
		'Idaho':208,
		'Illinois':217,
		'Indiana':219,
		'Iowa':319,
		'Kansas':316,
		'Kentucky':270,
		'Louisiana':225,
		'Maine':207,
		'Maryland':240,
		'Massachusetts':339,
		'Michigan':231,
		'Minnesota':218,
		'Mississippi':228,
		'Missouri':314,
		'Montana':406,
		'Nebraska':308,
		'Nevada':702,
		'New Hampshire':603,
		'New Jersey': 201,
		'New Mexico':505,
		'New York':212,
		'North Carolina':252,
		'North Dakota':701,
		'Ohio':216,
		'Oklahoma':405,
		'Oregon': 503,
		'Pennsylvania':215,
		'Rhode Island':401,
		'South Carolina':803,
		'South Dakota':605,
		'Tennessee':423,
		'Texas':210,
		'Utah':435,
		'Vermont':802,
		'Virginia':276,
		'Washington':206,
		'West Virginia':304,
		'Wisconsin':262,
		'Wyoming':307
	}
	for l in listcodephone.keys():
		pass
		if(l in randcityes):
			number=' +1'
			number+=str(listcodephone.get(l))
			number+=str(random.randint(1000000,9999999))+'; '
			return number

	pass
def core(names,names_2,last_names,last_names_2,cityes,streets,index,countpeople,error,country,listcodephone,codephone):
	countpeople=abs(int(countpeople))
	error=abs(float(error))
	i=int(countpeople)-1;
	while i!=-1:
		
		rand_num = random.randint(0,1)
		if (rand_num==1):
			randname = randnumberfromlistsize(names) #men
		else:
			randname = randnumberfromlistsize(names_2) #женские

		rand_num_2 = random.randint(0,1)
		if (rand_num_2==1):
			randlast_name=randnumberfromlistsize(last_names)#не cклоняется
		else:
			randlast_name=randnumberfromlistsize(last_names_2)#склоняется
		if (rand_num_2==0):
			if(rand_num==0):
				randlast_name+='ая'
			else:
				randlast_name+='ий'
		randcityes = randnumberfromlistsize(cityes)
		randstreet= randnumberfromlistsize(streets)
		#randindex= randnumberfromlistsize(index)
		#
		#string_res = randname+' '+randlast_name+'; '+randstreet+', '
		#string_res=string_res+str(random.randint(1,100))+', '+str(random.randint(1,100))+', г.'+randcityes+''+', '+country
		#
		
		randcode=listcodephone[random.randint(0,len(listcodephone)-1)]
		numberphone= codephone+str(randcode)+''+str(random.randint(1000000,9999999))
		res=err_res(error,randname,randlast_name,randstreet,randcityes,country,countpeople,numberphone)
		print(str(int(countpeople)-i)+') '+res)


		i=i-1
		pass



	pass
	
def by(countpeople,error):
	print(countpeople+' '+error+'\n***************************')
	names = readFileToList('by_name.txt')
	names_2 = readFileToList('by_name_2.txt')
	last_names= readFileToList('by_last_name.txt')
	last_names_2= readFileToList('by_last_name_2.txt')
	cityes = readFileToList('by_city.txt')
	streets= readFileToList('by_street.txt')
	index=readFileToList('by_index.txt')
	listcodephone=[29,25,33,44]
	codephone='+375'
	core(names,names_2,last_names,last_names_2,cityes,streets,index,countpeople,error,'Беларусь',listcodephone,codephone)
	pass

def ru(countpeople,error):
	print(countpeople+' '+error+'\n***************************')
	names = readFileToList('by_name.txt')
	names_2 = readFileToList('by_name_2.txt')
	last_names= readFileToList('by_last_name.txt')
	last_names_2= readFileToList('by_last_name_2.txt')
	cityes = readFileToList('ru_city.txt')
	streets= readFileToList('by_street.txt')
	index=readFileToList('by_index.txt')
	listcodephone=[901, 902, 903,
	 904, 905, 906, 908, 909, 910,
	 911, 912, 913, 914, 915, 917, 918,
	 919, 920, 921, 922, 923, 924, 925,
	 926, 927, 928, 929, 930,931,
	 932, 933, 934, 937, 938, 950, 
	 951, 952, 953, 960, 961, 962, 963, 
	 964, 965, 967, 980, 981, 982, 983, 
	 984, 987, 988]

	codephone='+79'
	core(names,names_2,last_names,last_names_2,cityes,streets,index,countpeople,error,'Россия',listcodephone,codephone)
	pass

def us(countpeople,error):
	print(countpeople+' '+error+'\n***************************')
	names = readFileToList('us_name.txt')
	last_names= readFileToList('us_last_name.txt')
	last_names_2= readFileToList('us_last_name.txt')
	cityes = readFileToList('us_city.txt')
	streets= readFileToList('us_street.txt')
	index=readFileToList('by_index.txt')
	listcodephone=[510]

	codephone='+1'
	core(names,names_2,last_names,last_names_2,cityes,streets,index,countpeople,error,'USA',listcodephone,codephone)
	pass

for param in sys.argv:
	var= str(param)
	if var.lower()=='by':
		i=0
		countpeople=0
		error=0
		for param in sys.argv:
			i=i+1
			if i==3:	
				countpeople=param
			if i==4:
				error=param
		by(countpeople,error)
		pass

	if var=='us':
		#америкосы
		i=0
		countpeople=0
		error=0
		for param in sys.argv:
			i=i+1
			if i==3:	
				countpeople=param
			if i==4:
				error=param
		us(countpeople,error)
	if var=='ru':
		i=0
		countpeople=0
		error=0
		for param in sys.argv:
			i=i+1
			if i==3:	
				countpeople=param
			if i==4:
				error=param
		ru(countpeople,error)
		#россия
	pass
pass
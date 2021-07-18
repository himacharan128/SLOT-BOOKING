import calendar
import os
filename='slots'
def present_list_slot(slot_date):
	while True:
		if os.path.isfile("./"+filename):
			with open(filename) as f:
				data_search=f.readlines()
			line_count=0
			find=1
			for line in data_search:
				line_count+=1
				if ('@_'+str(slot_date)) in line:
					find=0
					break#local-break
			if find==0:
				a=0
				for line in data_search:
					if a==line_count:
						data=line
						break
					a=a+1
				list2=list(data.strip())
				return list2
			else:
				f=open(filename,'a')
				f.write('@_'+str(slot_date)+'\n')
				list2=[]
				for i in range(16):
					list2.append('n')
					temp=list2[i]
					f.write(temp)
				f.write('\n')
				f.close()
				f=open(filename,'r')
				data_in_file=f.read()
				f.close()
				return list2
		else:
			data=''
			f=open(filename,"w")
			f.write(data + "\n")
			f.close()
			continue
def print_dot(i,slot_date,list2):
	if list2[i-1]=='y':
		print(u"\U0001F534")#red
	else:
		print(u"\U0001F7E2")#green
def print_slot(slot_date,list2):
	print('AVAILABLE SLOTs FOR {} : '.format(slot_date.strftime('%d-%m-%Y')))
	# print(list2)
	print('-'*80)
	a=9
	for i in range(1,17):
		if i%2!=0:
			print('\t\tslot-{}\t\t\t{}:00-{}:30\t\t'.format(i,a,a),end='')
			print_dot(i,slot_date,list2)
		else:
			print('\t\tslot-{}\t\t\t{}:30-{}:00\t\t'.format(i,a,a+1),end='')
			print_dot(i,slot_date,list2)
			a=a+1			
		print('-'*80)
	print(u'\t\t\t\U0001F534'+'----->SLOT NOT AVAILABLE\n'+u'\t\t\t\U0001F7E2'+'----->SLOT AVAILABLE\n')
def book_slot(slot_date):
	while True:
		global slot_number
		slot_number=int(input('\tENTER THE SLOT NUMBER OF SLOT YOU WANT TO BOOK : '))
		if slot_number<1 or slot_number>16:
			print('\tSLOT NUMBER LIES BETWEEN 1 AND 16.YOU HAVE ENTERED {}\n\t\t\tPLEASE TRY AGAIN'.format(slot_number))
			continue
		with open(filename) as f:
			data_search=f.readlines()
		line_count=0
		find=1
		for line in data_search:
			line_count+=1
			if ('@_'+str(slot_date)) in line:
				find=0
				break#local-break
		if find==0:
			a=0
			for line in data_search:
				if a==line_count:
					data=line
					break
				a=a+1
		list2=list(data.strip())
		if list2[slot_number-1]=='n':
			list2[slot_number-1]='y'
		else:
			print('\t\t\tSLOT NOT AVAILABLE !\n\t\t\tPLEASE TRY AGAIN')
			continue
		data_updated=''
		for i in range(16):
			data_updated=data_updated+str(list2[i])
		with open(filename) as f:
			data_search=f.readlines()
		f=open(filename,"w")
		for idx, line in enumerate(data_search):
			if idx ==line_count:
				f.write(data_updated + '\n')
			else :
				f.write(line)
		print('-'*80)
		print('\t\tSLOT BOOKED ON {} AT SLOT-{}.\n\t\tPLEASE ARRIVE 5 MINS IN PRIOR'.format(slot_date,slot_number))
		print('-'*80)
		break
def main_booking():
	while True:
		import datetime
		date_object =datetime.date.today()
		print('8'*80)
		print(' '*20+date_object.strftime('%d-%m-%Y'),end='')
		print(' '*15+calendar.day_name[date_object.weekday()])
		print('8'*80)
		print('\t\tenter dates in the following format (DD MM YYYY) ')
		slot_date=input('  -->enter the date you want you book slot : ').split()
		dd=int(slot_date[0])
		mm=int(slot_date[1])
		yy=int(slot_date[2])
		from datetime import date
		slot_date=date(yy,mm,dd)
		list2=present_list_slot(slot_date)
		delta=int((slot_date-date_object).days)
		if delta<0:
			print('~'*80)
			print('\t\t\tENTRED DATE is INVALID\n\t\t\tPLEASE TRY AGAIN')
			print('~'*80)
			continue
		else:
			print_slot(slot_date,list2)
			book_slot(slot_date)
		exit(0)
main_booking()
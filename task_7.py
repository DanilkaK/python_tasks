d = float(input('Сантиметры в дюймы : '))
c = 0.393700787

def d_v_s(d,c):
	sm = d * c
	return sm

a = d_v_s(d,c)

print('Дюймов: '+ str(a))


d1 = float(input('Дюймы в сантиметры : '))
c1 = 2.54

def s_v_d(d1,c1):
	sm1= d1 * c1
	return sm1

a1 = s_v_d(d1,c1)

print('Сантиметров: '+ str(a1))



d2 = float(input('Мили в километры : '))
c2 = 1.609344

def m_v_k(d2,c2):
	sm2 = d2 * c2
	return sm2

a2 = m_v_k(d2,c2)

print('Километров: '+ str(a2))


d3 = float(input('Километры в мили : '))
c3 = 0.621371

def k_v_m(d3,c3):
	sm3 = d3 * c3
	return sm3

a3 = k_v_m(d3,c3)

print('Милей: '+ str(a3))


q = float(input('Килограммы в фунты : '))
w = 2.20462

def ki_v_f(q,w):
	sm3 = q * w
	return sm3

y = ki_v_f(q,w)

print('Фунтов: '+ str(y))

q1 = float(input('Фунты в килограммы: '))
w1 = 0.453592

def f_v_ki(q1 ,w1):
	sm3 = q1  *w1
	return sm3

y1 = f_v_ki(q1 ,w1)

print('Килограммов: '+ str(y1))



un = float(input('Унции в граммы: '))
gr = 28.3495

def uny_v_gramm(un ,gr):
	sm3 = un  *gr
	return sm3

grm= uny_v_gramm(un ,gr)

print('Граммов: '+ str(grm))





gra = float(input('Граммы в унции: '))
unc = 0.035274

def gramm_v_uny(gra ,unc):
	sm3 = gra  *unc
	return sm3

gram= gramm_v_uny(gra ,unc)

print('Унций: '+ str(gram))

gal = float(input('Галлон в литры: '))
ltr =3.78541

def gln_v_liv(gal ,ltr):
	sm3 = gal  *ltr
	return sm3

ltrv= gln_v_liv(gal ,ltr)

print('Литров: '+ str(ltrv))



gal1 = 0.264172
ltr1 = float(input('Литры в Галлон: '))

def liv_v_gln(gal1 ,ltr1):
	sm3 = gal1  *ltr1
	return sm3

galn=liv_v_gln(gal1 ,ltr1)

print('Галон: '+ str(galn))



ltr2 = 0.568261
Pin = float(input('Пинты в литры: '))

def pn_v_lv(gal1 ,ltr1):
	sm3 = Pin  *ltr2
	return sm3

Pint= pn_v_lv(Pin ,ltr2)

print('Литров: '+ str(Pint))


ltr2_2 = float(input('Литры в Пинты: '))
Pin1 = 1.75975

def lv_v_pn(Pin1 ,ltr2_2):
	sm3 = Pin1 *ltr2_2
	return sm3

Ltr= lv_v_pn(Pin1 ,ltr2_2)

print('Пинт: '+ str(Ltr))




while 1==1:
	print('1)Сантиметры в дюймы\n2)Дюймы в сантиметры\n3)Мили в километры\n4)Километры в мили\n5)Килограммы в фунты\n6)Фунты в килограммы')
	Change = input('7)Унции в граммы\n8)граммы в Унции\n9)Галлон в литры\n10)Литры в Галлон\n11)Пинты в литры\n12)литры в  Пинты\nWhat we do:')



	if Change == '1':
		cm = float(input('Cm v dm: '))
		dym = 0.393700787
		print(d_v_s(cm, dym))
	elif Change == '2':
		dym1 = float(input('dm v cm: '))
		cm1 = 2.54
		print(s_v_d(cm1, dym1))
	elif Change == '3':
		mls = float(input('Mils v Km: '))
		kit =  1.609344
		print(m_v_k(mls, kit))
	elif Change == '4':
		kit1 = float(input(' Km v Mils: '))
		mls1 = 0.621371
		print('Миль: ' +str(k_v_m(kit1, mls1)))
	elif Change == '5':
		kgrm1 = float(input(' Килограммы в Фунты: '))
		ftv1 = 2.20462
		print('Фунтов: ' +str(ki_v_f(kgrm1, ftv1)))
	elif Change == '6':
		Fnt = 0.453592
		Kg = float(input('Фунты в кг:'))
		print('Киллограмов:' + str(f_v_ki(Fnt,Kg)))
	elif Change == '7':

		UN = float(input('Унции в граммы: '))
		GR = 28.3495
		print('граммов: ' + str(uny_v_gramm(UN, GR)))
	elif Change == '8':

		GR1= float(input('граммы в Унции : '))
		UN1= 28.3495
		print('Унции: ' + str(gramm_v_uny(UN1, GR1)))
	elif Change == '9':

		GAL = float(input('Галлон в литры: '))
		LTR = 3.78541
		print('Литров: ' + str(gln_v_liv(GAL, LTR)))
	elif Change == '10':

		GAL1 = 0.264172
		LTR1 = float(input('Литры в Галлон: '))

		print('Галлон: ' + str(liv_v_gln(GAL1, LTR1)))
	elif Change == '11':

		LTR2 = 0.568261
		Pin2 = float(input(' Пинты в литры: '))

		print('Литров: ' + str(pn_v_lv(LTR2, Pin2)))
	elif Change == '12':

		LtR2 = 0.568261
		PIN2 = float(input('литры в  Пинты: '))
		print('Пинт: ' + str(pn_v_lv(LtR2, PIN2)))

	elif Change == '0':
		break
	else:
		print('ERROR')
print('end')




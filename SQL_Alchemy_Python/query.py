from config import DATABASE_URI
from model import Houses, Flats, Residents, Owners, Relatives
from crud import get_session_engine
from prettytable import PrettyTable

mytable = PrettyTable()
result=[]
res =[]

s, _ = get_session_engine(DATABASE_URI)
'''qry0 = s.query(Residents.id, Residents.full_name)
print(qry0.statement)

query_res = qry0.all()
print(query_res)'''


'''1 Добавить жителя'''
'''o = Owners(flat_id=7, benefit_type='Донор', account_number=19343544, full_name='Агапов_Дмитрий_Александрович')
s.add(o)
s.commit()'''

'''1.1 Добавление жителя в жилую квартиру (например, родился ребёнок)'''
res = Residents(flat_id=1, full_name='Попова_Анна_Сергеевна')
s.add(res)
qr = s.query(Residents.id).filter(Residents.flat_id == 1).filter(Residents.full_name == 'Попова_Анна_Сергеевна')
rel = Relatives(owner_id=2, resident_id=qr)
s.add(rel)

s.commit()
'''------------------------------------------------------------------------------------------------------------------------'''

'''2 Выселить жителя'''

'''s.query(Owners).filter(Owners.account_number == 28910149)\
.filter(Owners.full_name == 'Семенов_Евгений_Дмитриевич').update({Owners.deleted: 'Х'})
s.commit()'''
'''------------------------------------------------------------------------------------------------------------------------'''

'''3 Обмен квартирами'''
'''
for first_apartment in s.query(Flats.id).filter(Flats.apartment_number == 51).filter(Flats.house_id == s.query(Houses.id).filter(Houses.address == 'Ленина_1')):
   print (first_apartment)
for second_apartment in s.query(Flats.id).filter(Flats.apartment_number == 52)\
.filter(Flats.house_id == s.query(Houses.id).filter(Houses.address == 'Космонавтов_35')):
    print(second_apartment)

for first_owner in s.query(Owners.id).filter(Owners.full_name == 'Нестеренко_Тарас_Олегович')\
.filter(Owners.account_number == 28910151):
    print(first_owner)

for second_owner in s.query(Owners.id).filter(Owners.full_name == 'Василенко_Сергей_Сергеевич').filter(Owners.account_number == 19343552):
    print(second_owner)

#Владельцы

s.query(Owners).filter(Owners.id == second_owner[0]).update({Owners.flat_id: first_apartment[0]})
s.query(Owners).filter(Owners.id == first_owner[0]).update({Owners.flat_id: second_apartment[0]})
s.commit()

#Родственников

for rel1 in s.query(Relatives.resident_id).filter(Relatives.owner_id == second_owner[0]):
    print(rel1)

for rel2 in s.query(Relatives.resident_id).filter(Relatives.owner_id == first_owner[0]):
    print(rel2)


#s.query(Residents).filter(Residents.id == rel1[0]).update({Owners.flat_id: first_apartment[0]})
#s.query(Residents).filter(Residents.id == rel2[0]).update({Owners.flat_id: second_apartment[0]})
#s.commit()

'''
'''------------------------------------------------------------------------------------------------------------------------'''


'''4 Внесение сведений о льготах'''

'''s.query(Owners).filter(Owners.account_number == 27010551)\
.filter(Owners.full_name == 'Иванов_Владислав_Андреевич').update({Owners.benefit_type: 'Пенсионер'})
s.commit()'''
'''------------------------------------------------------------------------------------------------------------------------'''

'''5 Справка жильцам'''

'''от лица собственника:'''
for ownerId in s.query(Owners.id).filter(Owners.full_name == 'Климов_Владимир_Антонович').filter(Owners.account_number == 27010550):
    #print(ownerId)
    print('')

que = s.query(Owners.full_name,Owners.account_number,Owners.benefit_type,Flats.amount_of_space,Flats.number_of_rooms,
              Flats.apartment_number,Houses.address, Houses.number_of_rooms,Houses.living_space,Residents.full_name)\
    .join(Flats, Flats.id == Owners.flat_id).join(Houses, Houses.id == Flats.house_id)\
    .join(Residents, Residents.flat_id == Flats.id).filter(Owners.id == ownerId[0]).all()



list = [('Cобсвенник', 'Номер ЛС', 'Тип_льготы', 'Жилплощ.','Кол-во_комнат', 'Кв', 'Адрес','Кол-во комнат(общ.)','Жилая_площадь(общ)', 'Проживающий_в_кв.')]

for qu in que:
    list.append(qu)
for i in list:
   result.append(" | ".join(map(str, i)))
print("\n".join(result))

'''от лица родственника собственника'''

for residentId in s.query(Residents.flat_id).filter(Residents.full_name == 'Климова_Олеся_Ярославовна').filter(Residents.flat_id == s.query(Flats.id).filter(Flats.apartment_number == 50)):
    print('')
    #print(residentId)


'''for q in s.query(Residents.full_name, Owners.full_name,
Owners.account_number, Owners.benefit_type,Flats.amount_of_space,
Flats.number_of_rooms, Flats.apartment_number, Houses.address,
Houses.number_of_rooms,Houses.living_space)\
        .join(Flats, Flats.id == Owners.flat_id).join(Houses, Houses.id == Flats.house_id).join(Residents, Residents.flat_id == Flats.id)\
        .filter(Residents.flat_id == residentId[0]):
    print(q)'''

qqq = s.query(Residents.full_name, Owners.full_name,Owners.account_number, Owners.benefit_type,Flats.amount_of_space,
Flats.number_of_rooms, Flats.apartment_number, Houses.address,Houses.number_of_rooms,Houses.living_space)\
        .join(Flats, Flats.id == Owners.flat_id).join(Houses, Houses.id == Flats.house_id).join(Residents, Residents.flat_id == Flats.id)\
        .filter(Residents.flat_id == residentId[0])
lis = [('Жилец', 'Родственник', 'Номер ЛС', 'Тип_льготы','Жилплощ.','Кол-во_комнат', 'Кв', 'Адрес','Кол-во комнат(общ.)','Жилая_площадь(общ)')]
for i in qqq:
    lis.append(i)
for k in lis:
    res.append(" | ".join(map(str, k)))
print("\n".join(res))
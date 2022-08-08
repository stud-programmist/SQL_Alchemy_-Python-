def read_csv(name):
    with open(f'./static_data/{name}.csv', 'r',encoding="utf-8") as f:
        result = [line.strip() for line in f]
        print(result)
    return result


house = read_csv('Houses')
flats = read_csv('Flats')
resident = read_csv('Residents')
owner = read_csv('Owners')
relat = read_csv('Relatives')


for i in house:
    #s = i.split()
    #h = Houses(address=str(i[0]), number_of_rooms=int(i[1]), living_space=float(i[2]))
    #session.add(h)

for i in flats:
    s = i.split()
    f = Flats(house_id=int(i[0]), amount_of_space=float(i[1]), number_of_rooms=int(i[2]) ,  apartment_number =int(i[3]))
    session.add(f)
for i in range(resident):
    s = i.split()
    res= Residents(full_name=str(i[0]), flat_id=int(i[1]))
    session.add(res)

for i in range(owner):
    s = i.split()
    o =Owners(full_name=str(i[0]), flat_id = int(i[1]), benefit_type= str(i[2]), account_number= int(i[3]))
    session.add(res)

for i in range(relat):
    s = i.split()
    rel = Relatives(owner_id=int(i[0]), resident_id=int(i[1]))
    session.add(rel)
#session.commit()

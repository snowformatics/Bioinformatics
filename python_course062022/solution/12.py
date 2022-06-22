# Ligation
molar_ratio = 3

insert_length = float(500)
vector_length = float(3000)

vector_conc = float(30)
insert_conc = float(50)
total_volume = 10

up = float(vector_conc) * float(insert_length) * float(molar_ratio)
down = float(insert_conc) * float(vector_length)

up_down_plus1 = (float(up) / float(down)) + float(1)

vector_volume = float(total_volume) / float(up_down_plus1)
vector_volume = round(vector_volume, 1)
insert_volume = float(total_volume) - float(vector_volume)
insert_volume = round(insert_volume, 1)
message = 'Vector Volume : ' + str(vector_volume) + ' µL' + '<br>Insert Volume: ' \
          + str(insert_volume) + ' µL<br>'

print (message)
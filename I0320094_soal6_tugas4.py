print("===== Operator Bitwise =====")

a = 4
b = 11

#Bitwise OR
c = a | b
print("=====OR=====")
print('nilai : ',a,' , binary :',format(a,'08b'))
print('nilai : ',b,' , binary :',format(b,'08b'))
print('------------------------------ (|)')
print('nilai : ',c,' , binary :',format(c,'08b'))

#Shift Right
c = a >> b
print("=====Shift=====")
print('nilai : ',a,' , binary :',format(a,'08b'))
print('nilai : ',b,' , binary :',format(b,'08b'))
print('------------------------------ (>>)')
print('nilai : ',c,' , binary :',format(c,'08b'))

#Bitwise XOR
c = a ^ b
print("=====XOR=====")
print('nilai : ',a,' , binary :',format(a,'08b'))
print('nilai : ',b,' , binary :',format(b,'08b'))
print('------------------------------ (^)')
print('nilai : ',c,' , binary :',format(c,'08b'))

#Bitwise NOT
c = ~a
print("=====NOT=====")
print('nilai : ',a,' , binary :',format(a,'08b'))
print('------------------------------ (~)')
print('nilai : ',c,' , binary :',format(c,'08b'))

#Bitwise AND
c = a & b
print("=====AND=====")
print('nilai : ',b,' , binary :',format(b,'08b'))
print('nilai : ',a,' , binary :',format(a,'08b'))
print('------------------------------ (&)')
print('nilai : ',c,' , binary :',format(c,'08b'))
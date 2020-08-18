# CREATE BY Hanwei Wei '2020/8/17 17:36'
__author__ = 'weiha'
__time__ = '2020/8/17 17:36'

#Print receipt
print()
print('CSC101 Store')
print('----------------------')
print('Item:             Price:')
print(name1, '              $', format(price11, '.2f'), sep='')      #show item's name and total price
print(' ', quantity1, ' @ $', price1, ' ea', sep='')  #show item's quantity and unit price
print(name2, '              $', format(price22, '.2f'), sep='')      #show item's name and total price
print(' ', quantity2, ' @ $', price2, ' ea', sep='')  #show item's quantity and unit price
print(name3, '              $', format(price33, '.2f'), sep='')      #show item's name and total price
print(' ', quantity3, ' @ $', price3, ' ea', sep='')  #show item's quantity and unit price
print(name4, '              $', format(price44, '.2f'), sep='')      #show item's name and total price
print(' ', quantity4, ' @ $', price4, ' ea', sep='')  #show item's quantity and unit price
print(name5, '              $', format(price55, '.2f'), sep='')      #show item's name and total price
print(' ', quantity5, ' @ $', price5, ' ea', sep='')  #show item's quantity and unit price
print('----------------------')
print('Subtotal: $', format(subtotal, ',.2f'), sep='')        #show the subtotal price
print('Tax: $', format(tax, ',.2f'), sep='')                  #show tax
print('Grand total: $', format(grand_total, ',.2f'), sep='')  #show grand total

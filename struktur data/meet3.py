# contoh tipe data (integer)  : angka satuan bulat
bil_integer = 1
print(type(bil_integer))
print ("type data dari bil_integer adalah: ",type(bil_integer))
 
 # contoh tipe data (float) : bilangan desimal
bil_float = 2.5
print ("type data bil_float adalah: ", type(bil_float))

# contoh tipe data (string) :kumpulan karakter
bil_string = "putu"
print ("type data bil_string adalah: ", type(bil_string))

# contoh tipe data (bolean) : biner, 0,1, True False
bil_bol = True
print ("type data bil_bol adalah: ", type(bil_bol))

# tipe data dari bahasa C
from ctypes import c_double
bil_double  = c_double((20000000))
print ("type data bi_double adalah:", type(bil_double))
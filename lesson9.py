"""
Cevre classi olacaq, yalniz radius qebul edecek.
Radiusu deyismek olacaq, menfi ola bilmez.
saheni_hesabla() methodunuda cagirdiqda 
cevrenin sahesini bize vermelidir

"""

# import math

# radius = int(input("radiusu daxil edin : "))


# class Cevre () :

#    def __init__(self , radius) :

#         self.__radius = radius

    

#    def calculate_area(self):
        
#         return (math.pi * (self.radius ** 2))
#         print(asadfsa)

# cevre = Cevre (radius)


# cevre.calculate_area ()


# -------------- Home Task -----------------

# Bir classdan istifadə edərək 2 metod yazın.
# İlk metodda dəyər olaraq bir list içərisində rəqəmləri alın 
# və onu bir listə əlavə edin ( bu şəkildə olacaq: mylist=[1,2,3,4,5])
# Daha sonra bir metod daha yazın. Bu metodda isə bizim bir 
# argumentimiz olacaq (Hədəf rəqəm). Burada ilk metodda aldığımız listin 
# dəyərləri içərisində hər hansı 2 rəqəmin cəmi verilmiş hədəf rəqəmə 
# bərabərdirsə həmin rəqəmlərin indexlərini qaytarın. Əgər belə
# rəqəmlər yoxdursa -1 cavabı qaytarın. 

# Əlavə olaraq argumentləri hansı metodunuzda istifadə etmək 
# istədiyiniz barəsində sərbəstsiniz və əlavə arqumentlərdən istifadə edəbilərsiniz.


class Finder():

    def __init__(self):
        self.createList()



    def createList(self):
        self.myList=list((input("Listdəki məlumatları daxil edin :").split(',')))



    def find(self,target):
        self.target=target
        self.index=False
        for i in range(len(self.myList)) :
            for j in range(i+1,len(self.myList)):
                if self.target==int(self.myList[i])+int(self.myList[j]):
                    print("Listin {} ve {} indeksindəki elementlərin cəmi hədəfə bəraberdir".format(i,j))
                    self.index=True
                    break
        if not self.index:
            return -1           



finder=Finder()









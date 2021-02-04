import animal
class caja:
    idestatica=0
    def __init__(self,lastid,*animales):
        self.animales= []
        for i in animales:
            animales+=i
        self.id=idestatica
        idestatica+=1


        
    
    def __str__(self):
        string=string+"Id = "+self.id        
        for i in self.animales:
            string=string+i.__str__()
        return string

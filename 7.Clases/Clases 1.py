class animal:
    def __init__(self,color,patas):
        self.especie = self.__class__.__name__
        self.color = color
        self.patas = patas
        
    def __str__(self):
        return ("%s con %d patas y de color %s" % (especie,patas,color))



class lobo(animal):
    
    def __init__(self,color):
        super().__init__(especie = "lobo",patas = 4,color = color)

class oveja(animal):
    def __init__(self,color,especie):
        super().__init__(color,4,especie)

class serpiente(animal):
    def __init__(self,especie):
        super().__init__(color,0,especie)

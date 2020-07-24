"""Ser humano e o uerjiano"""

class humano:
    
    """definir um ser humano primitivo"""
    
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo
        self.status = 'acordado'
        self._idade = 0
        
    def dormir(self):
        self.status = 'dormindo'
        print(f"{self.nome} está {self.status}")
    
    def acordar(self):
        self.status = 'acordado'
        print(f"{self.nome} está {self.status}")
    
    def descrever(self):
        print(f"{self.nome} é um(a) {self.sexo} e no momento está {self.status}")
    
    def aniversario(self):
        self._idade += 1
        print(f"{self.nome} cresceu um ano e agora tem {self._idade} ano(s)")
    
    def isfeliz(self):
        import numpy as np
        self.feliz = np.random.choice(["não está", 'está'],
                                     p = [0.1, 0.9])
        print(f"{self.nome} {self.feliz} feliz")
        
        
class uerjiano(humano):
    
    def __init__(self, nome, sexo, curso, ano):
        
        super().__init__(nome, sexo)
        
        
        if curso.lower() in ['mecanica', 'quimica', 'produção']:
            self.curso = curso
        else:
            raise ValueError(f"Não tem o curso {curso} na FAT")
        
        self.ano = ano
        self.period = 0
        self.feliz = 'está'
        self.moradia = Moradia()
        
    def periodo(self):
        from datetime import datetime
        
        self.period = datetime.now().year - int(self.ano)
        print(f"{self.nome} está no periodo {2 * self.period}")
    
    def isfeliz(self):
        import numpy as np
        self.feliz = np.random.choice(["não está", 'está'],
                                     p = [0.7, 0.3])
        print(f"{self.nome} {self.feliz} feliz")
 



class Moradia:
    """Moradia de um ser humano"""
    
    def __init__(self, tipo = "Repoblica"):
        self.moradia = tipo
        
    def descrever(self):
        print(f"o tipo da moradia da pessoa é {self.moradia}")
        
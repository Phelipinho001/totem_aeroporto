
from models.passageiro import Passageiro


class Classificador:

    @staticmethod
    
    def classificar(passageiro : Passageiro):

        if passageiro.client_vip == True or passageiro.idade >= 60:
            return "1ª Classe"
        
        else:
            return "Classe Econômica"
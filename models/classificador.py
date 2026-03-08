from passageiro import Passageiro

class Classificador:

    @staticmethod
    
    def classificador(passageiro : Passageiro):

        if passageiro.client_vip == True or passageiro.idade:
            return "1ª Classe"
        
        else:
            return "Classe Econômica"
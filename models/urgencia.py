class Urgencia:
    
    def alerta(self, passageiro):
        """
        Recebe os dados do passageiro e exibe um alerta crítico na tela,
        orientando-o a ir direto para o embarque expresso sem pegar fila.
        """
        print("\n------------------------------------------")
        print("ALERTA DE EMBARQUE")
        print("------------------------------------------")
        print(f"PASSAGEIRO: {passageiro.nome}")
        print("STATUS: VOO PRÓXIMO DA PARTIDA")
        print(">>> ATENÇÃO: DIRIJA-SE IMEDIATAMENTE")
        print("ao balcão de Embarque Expresso!")
        print("Não é necessário aguardar senha.")
        print("------------------------------------------\n")
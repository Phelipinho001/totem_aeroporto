from datetime import datetime

class Impressora:
    def impressora(self, passageiro, classe, servico, senha):
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("\n" + "-" * 42)
        print("CARTÃO DE FILA - VOAR MUITO")
        print("-" * 42)
        print(f"PASSAGEIRO: {passageiro.nome}")
        print(f"CLASSE: {classe}")
        print(f"SERVIÇOS: {servico}")
        print(f"SENHA: {senha}")
        print("-" * 42)
        print(f"Data: {data_atual}")
        print(f"{'Aguarde ser chamado no painel' :^42}")
        print("-" * 42 + "\n")
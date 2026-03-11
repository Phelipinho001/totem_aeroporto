from models.passageiro import Passageiro
from models.menu import Menu
from models.classificador import Classificador
from models.gerador_senha import Senha
from models.urgencia import Urgencia
from models.impressora import Impressora

def iniciar():
    menu = Menu()
    classificador = Classificador()
    gerador_senha = Senha()
    urgencia = Urgencia()
    impressora = Impressora()

    while True :
      print(f"\n" + "=" * 42)  
      print("AEROPORTO VOAR MUITO - AUTOATENDIMENTO")
      print("=" * 42)

      print("\n[CADASTRO PASSAGEIRO]")
      nome = input("Nome:")

      try:
         idade = int(input("Idade:"))
         client_vip = input("Você é Cliente VIP (S/N)").strip().upper()
         vip = True if client_vip == "S" else False 

         passageiro = Passageiro(nome, idade, vip)

         menu.menu()
         escolhido = menu.escolha()

         if escolhido == "3":
            urgencia.urgencia(passageiro)

         else:
            tipo = classificador.classificar(passageiro)
            senha_gerada = gerador_senha.gerar(tipo)
            nome_servico = "Fazer Cheak-in" if escolhido == "1" else "Despachar Bagagem"
            impressora.impressora(passageiro, tipo, nome_servico, senha_gerada)
         
         print("\n" + "."*40 )
         input("Pressione ENTER para o próximo atendimento...")

      except ValueError:
         print("\n[ERRO] Entrada inválida. Por favor, reicicie o cadastro.")

if __name__ == "__main__":
   iniciar()

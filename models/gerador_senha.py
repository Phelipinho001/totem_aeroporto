class Senha :
    senha_vip = 0 
    senha_economica = 0

    @staticmethod
    def gerar (cls, tipo : str) -> str:
        if tipo == "1ª Classe":
            cls.senha_vip += 1
            numero = str(cls.senha_vip).zfill(3)
            return f"V-{numero}"
        else:
            cls.senha_economica += 1
            numero = str(cls.sneha_economica).zfill(3)
            return f"E-{numero}"
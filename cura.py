from cryptography.fernet import Fernet

# 1. O herói pega a chave que o vilão deixou para trás
with open("chave.key", "rb") as arquivo_chave:
    chave_secreta = arquivo_chave.read()

# 2. O herói lê o arquivo que está todo embaralhado e trancado
with open("alvo.txt", "rb") as arquivo_vitima:
    conteudo_trancado = arquivo_vitima.read()

# 3. O herói usa a chave para destrancar (descriptografar) o conteúdo!
conteudo_salvo = Fernet(chave_secreta).decrypt(conteudo_trancado)

# 4. O herói reescreve o arquivo, agora com o texto legível de volta
with open("alvo.txt", "wb") as arquivo_vitima:
    arquivo_vitima.write(conteudo_salvo)

print("Resgate concluído com sucesso! O arquivo alvo.txt foi destrancado.")

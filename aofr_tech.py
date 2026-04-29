#!/usr/bin/env python3
# ============================================================
#         AOFR TECH - Sistema de Suporte e Reparação
#     Atitude  |  Orientação  |  Força  |  Resultado
#               Autor: Alfredo Ociola Francisco Romano
# ============================================================

import os
import sys
import platform
import subprocess
import shutil
import ctypes
import time

# ─────────────────────────────────────────────
#  CORES (ANSI) — funcionam em Linux/Mac/Win10+
# ─────────────────────────────────────────────
class Cor:
    VERDE       = "\033[92m"
    CIANO       = "\033[96m"
    AMARELO     = "\033[93m"
    VERMELHO    = "\033[91m"
    BRANCO      = "\033[97m"
    AZUL        = "\033[94m"
    MAGENTA     = "\033[95m"
    RESET       = "\033[0m"
    BOLD        = "\033[1m"
    DIM         = "\033[2m"

SISTEMA = platform.system()  # 'Windows', 'Linux', 'Darwin'

# ─────────────────────────────────────────────
#  AUTO-ELEVAÇÃO DE PRIVILÉGIOS
# ─────────────────────────────────────────────
def verificar_admin():
    """Verifica e solicita privilégios de administrador."""
    try:
        if SISTEMA == "Windows":
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        else:
            is_admin = (os.geteuid() == 0)
    except Exception:
        is_admin = False

    if not is_admin:
        print(f"{Cor.AMARELO}[!] Privilégios de administrador necessários. A re-lançar...{Cor.RESET}")
        time.sleep(1)
        try:
            if SISTEMA == "Windows":
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, " ".join(sys.argv), None, 1
                )
                sys.exit(0)
            else:
                os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
        except Exception as e:
            print(f"{Cor.VERMELHO}[ERRO] Não foi possível elevar privilégios: {e}{Cor.RESET}")
            sys.exit(1)

# ─────────────────────────────────────────────
#  UTILITÁRIOS
# ─────────────────────────────────────────────
def limpar():
    os.system("cls" if SISTEMA == "Windows" else "clear")

def pausar():
    input(f"\n{Cor.DIM}Pressiona ENTER para continuar...{Cor.RESET}")

def executar(comando, shell=True):
    """Executa um comando e imprime o resultado."""
    try:
        resultado = subprocess.run(comando, shell=shell, capture_output=True, text=True)
        saida = resultado.stdout.strip() or resultado.stderr.strip()
        print(f"{Cor.VERDE}{saida}{Cor.RESET}" if saida else f"{Cor.AMARELO}[Sem saída]{Cor.RESET}")
    except Exception as e:
        print(f"{Cor.VERMELHO}[ERRO] {e}{Cor.RESET}")

def cabecalho():
    limpar()
    print(f"{Cor.AZUL}{Cor.BOLD}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║          AOFR TECH — Suporte e Reparação                ║")
    print("║   Atitude  |  Orientação  |  Força  |  Resultado        ║")
    print("║         Autor: Alfredo Ociola Francisco Romano           ║")
    print(f"║         Sistema detectado: {SISTEMA:<30}║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"{Cor.RESET}")

def secao(titulo):
    print(f"\n{Cor.CIANO}{Cor.BOLD}[ {titulo} ]{Cor.RESET}")
    print(f"{Cor.DIM}{'─' * 50}{Cor.RESET}")

# ─────────────────────────────────────────────
#  FUNÇÕES DE CADA OPÇÃO
# ─────────────────────────────────────────────

def verificar_disco():
    secao("1. Verificar e Reparar Disco")
    if SISTEMA == "Windows":
        executar("chkdsk C: /f /r /x")
    elif SISTEMA == "Linux":
        disco = input("Disco a verificar (ex: /dev/sda1): ").strip()
        executar(f"fsck -n {disco}")
    else:
        executar("diskutil verifyDisk /")

def reparar_arquivos_sistema():
    secao("2. Reparar Arquivos de Sistema")
    if SISTEMA == "Windows":
        executar("sfc /scannow")
    elif SISTEMA == "Linux":
        executar("dpkg --configure -a && apt-get install -f -y")
    else:
        executar("diskutil repairPermissions /")

def limpar_temporarios():
    secao("3. Limpar Arquivos Temporários")
    if SISTEMA == "Windows":
        executar("del /q /f /s %TEMP%\\*")
        executar("cleanmgr /sagerun:1")
    elif SISTEMA == "Linux":
        executar("rm -rf /tmp/* /var/tmp/*")
        executar("apt-get autoremove -y && apt-get autoclean -y")
    else:
        executar("rm -rf ~/Library/Caches/* /tmp/*")
    print(f"{Cor.VERDE}[✓] Temporários limpos.{Cor.RESET}")

def verificar_memoria():
    secao("4. Verificar Erros de Memória")
    if SISTEMA == "Windows":
        executar("mdsched.exe")
    elif SISTEMA == "Linux":
        if shutil.which("memtester"):
            executar("memtester 256M 1")
        else:
            print(f"{Cor.AMARELO}[!] Instala memtester: apt install memtester{Cor.RESET}")
    else:
        print(f"{Cor.AMARELO}[!] Usa o 'Apple Diagnostics' (segura D no arranque).{Cor.RESET}")

def restaurar_sistema():
    secao("5. Restaurar Sistema")
    if SISTEMA == "Windows":
        executar("rstrui.exe")
    elif SISTEMA == "Linux":
        print(f"{Cor.AMARELO}[!] Usa o Timeshift ou restaura a partir de um snapshot.{Cor.RESET}")
    else:
        print(f"{Cor.AMARELO}[!] Usa o Time Machine para restaurar o sistema.{Cor.RESET}")

def verificar_rede():
    secao("6. Verificar Conectividade de Rede")
    alvos = ["8.8.8.8", "1.1.1.1", "google.com"]
    for alvo in alvos:
        cmd = f"ping -n 2 {alvo}" if SISTEMA == "Windows" else f"ping -c 2 {alvo}"
        print(f"\n{Cor.CIANO}→ Ping para {alvo}{Cor.RESET}")
        executar(cmd)

def gerenciar_processos():
    secao("7. Processos em Execução (Top 15 por CPU)")
    if SISTEMA == "Windows":
        executar("tasklist /fo table | more")
    elif SISTEMA == "Linux":
        executar("ps aux --sort=-%cpu | head -16")
    else:
        executar("ps aux -r | head -16")

def backup_drivers():
    secao("8. Backup de Drivers")
    if SISTEMA == "Windows":
        destino = os.path.join(os.path.expanduser("~"), "Desktop", "BackupDrivers")
        executar(f'dism /online /export-driver /destination:"{destino}"')
        print(f"{Cor.VERDE}[✓] Drivers guardados em: {destino}{Cor.RESET}")
    else:
        print(f"{Cor.AMARELO}[!] Backup de drivers específico para Windows.{Cor.RESET}")

def verificar_atualizacoes():
    secao("9. Verificar Atualizações")
    if SISTEMA == "Windows":
        executar("powershell -Command \"Get-WindowsUpdate\"")
    elif SISTEMA == "Linux":
        executar("apt-get update && apt-get upgrade --dry-run")
    else:
        executar("softwareupdate -l")

def info_sistema():
    secao("10. Informações do Sistema")
    print(f"{Cor.BRANCO}Sistema Operativo : {platform.system()} {platform.release()}")
    print(f"Versão            : {platform.version()}")
    print(f"Arquitectura      : {platform.machine()}")
    print(f"Processador       : {platform.processor()}")
    print(f"Nome do Host      : {platform.node()}")
    print(f"Python            : {platform.python_version()}{Cor.RESET}")
    if SISTEMA == "Windows":
        executar("systeminfo | findstr /C:\"RAM\"")
    elif SISTEMA == "Linux":
        executar("free -h && df -h /")
    else:
        executar("sysctl hw.memsize && df -h /")

def limpar_dns():
    secao("11. Limpar Cache DNS")
    if SISTEMA == "Windows":
        executar("ipconfig /flushdns")
    elif SISTEMA == "Linux":
        executar("systemd-resolve --flush-caches || resolvectl flush-caches")
    else:
        executar("dscacheutil -flushcache && killall -HUP mDNSResponder")
    print(f"{Cor.VERDE}[✓] Cache DNS limpa.{Cor.RESET}")

def reiniciar_servicos_rede():
    secao("12. Reiniciar Serviços de Rede")
    if SISTEMA == "Windows":
        executar("netsh winsock reset")
        executar("netsh int ip reset")
        executar("ipconfig /release && ipconfig /renew")
    elif SISTEMA == "Linux":
        executar("systemctl restart NetworkManager")
    else:
        executar("networksetup -setairportpower en0 off && networksetup -setairportpower en0 on")

def desfragmentar_disco():
    secao("13. Desfragmentar / Optimizar Disco")
    if SISTEMA == "Windows":
        executar("defrag C: /U /V")
    elif SISTEMA == "Linux":
        print(f"{Cor.AMARELO}[!] Linux (ext4) não necessita de desfragmentação.{Cor.RESET}")
    else:
        print(f"{Cor.AMARELO}[!] macOS gere automaticamente a desfragmentação.{Cor.RESET}")

def gerenciar_usuarios():
    secao("14. Gerir Utilizadores Locais")
    if SISTEMA == "Windows":
        executar("net user")
    elif SISTEMA == "Linux":
        executar("cut -d: -f1 /etc/passwd | sort")
    else:
        executar("dscl . list /Users | grep -v '^_'")

def verificar_integridade():
    secao("15. Verificar Integridade de Arquivos (DISM)")
    if SISTEMA == "Windows":
        executar("DISM /Online /Cleanup-Image /RestoreHealth")
    elif SISTEMA == "Linux":
        executar("debsums -c 2>/dev/null | head -20 || echo 'Instala debsums: apt install debsums'")
    else:
        executar("csrutil status")

def firewall():
    secao("16. Estado do Firewall")
    if SISTEMA == "Windows":
        executar("netsh advfirewall show allprofiles state")
    elif SISTEMA == "Linux":
        executar("ufw status verbose || iptables -L -n --line-numbers | head -30")
    else:
        executar("/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate")

def ver_logs():
    secao("17. Ver Logs de Eventos Recentes")
    if SISTEMA == "Windows":
        executar("powershell -Command \"Get-EventLog -LogName System -Newest 20 | Format-Table -Auto\"")
    elif SISTEMA == "Linux":
        executar("journalctl -n 20 --no-pager")
    else:
        executar("log show --last 5m --style syslog | tail -20")

def testar_velocidade_disco():
    secao("18. Testar Velocidade do Disco")
    if SISTEMA == "Windows":
        executar("winsat disk -drive c")
    elif SISTEMA == "Linux":
        executar("dd if=/dev/zero of=/tmp/teste_disco bs=1G count=1 oflag=dsync 2>&1 && rm /tmp/teste_disco")
    else:
        executar("dd if=/dev/zero of=/tmp/teste_disco bs=1g count=1 && rm /tmp/teste_disco")

def criar_ponto_restauracao():
    secao("19. Criar Ponto de Restauração")
    if SISTEMA == "Windows":
        executar('powershell -Command "Checkpoint-Computer -Description \'AOFR_TECH_Backup\' -RestorePointType MODIFY_SETTINGS"')
        print(f"{Cor.VERDE}[✓] Ponto de restauração criado.{Cor.RESET}")
    elif SISTEMA == "Linux":
        print(f"{Cor.AMARELO}[!] Usa Timeshift: timeshift --create --comments 'AOFR_TECH'{Cor.RESET}")
    else:
        print(f"{Cor.AMARELO}[!] Usa o Time Machine para criar um backup.{Cor.RESET}")

def executar_comando_personalizado():
    secao("20. Executar Comando Personalizado")
    print(f"{Cor.AMARELO}[AVISO] Executa comandos com cuidado. Uso da tua responsabilidade.{Cor.RESET}")
    cmd = input(f"{Cor.BRANCO}Comando: {Cor.RESET}").strip()
    if cmd:
        executar(cmd)

def atualizar_programas():
    secao("21. Atualizar Todos os Programas")
    if SISTEMA == "Windows":
        if shutil.which("winget"):
            executar("winget upgrade --all --silent")
        else:
            print(f"{Cor.AMARELO}[!] Winget não encontrado. Instala pelo Microsoft Store.{Cor.RESET}")
    elif SISTEMA == "Linux":
        executar("apt-get update && apt-get upgrade -y")
    else:
        if shutil.which("brew"):
            executar("brew update && brew upgrade")
        else:
            print(f"{Cor.AMARELO}[!] Homebrew não encontrado.{Cor.RESET}")

# ─────────────────────────────────────────────
#  MENU PRINCIPAL
# ─────────────────────────────────────────────
OPCOES = {
    "1":  ("Verificar e Reparar Disco",                  verificar_disco),
    "2":  ("Reparar Arquivos de Sistema (SFC)",           reparar_arquivos_sistema),
    "3":  ("Limpar Arquivos Temporários",                 limpar_temporarios),
    "4":  ("Verificar Erros de Memória",                  verificar_memoria),
    "5":  ("Restaurar Sistema",                           restaurar_sistema),
    "6":  ("Verificar Conectividade de Rede",             verificar_rede),
    "7":  ("Gerenciar Processos",                         gerenciar_processos),
    "8":  ("Backup de Drivers",                           backup_drivers),
    "9":  ("Verificar Atualizações",                      verificar_atualizacoes),
    "10": ("Informações do Sistema",                      info_sistema),
    "11": ("Limpar Cache DNS",                            limpar_dns),
    "12": ("Reiniciar Serviços de Rede",                  reiniciar_servicos_rede),
    "13": ("Desfragmentar Disco",                         desfragmentar_disco),
    "14": ("Gerir Utilizadores Locais",                   gerenciar_usuarios),
    "15": ("Verificar Integridade de Arquivos (DISM)",    verificar_integridade),
    "16": ("Estado do Firewall",                          firewall),
    "17": ("Ver Logs de Eventos",                         ver_logs),
    "18": ("Testar Velocidade do Disco",                  testar_velocidade_disco),
    "19": ("Criar Ponto de Restauração",                  criar_ponto_restauracao),
    "20": ("Executar Comando Personalizado",              executar_comando_personalizado),
    "21": ("Atualizar Todos os Programas",                atualizar_programas),
}

def menu():
    while True:
        cabecalho()
        for num, (descricao, _) in OPCOES.items():
            cor = Cor.VERDE if int(num) % 2 == 0 else Cor.CIANO
            print(f"  {cor}{num:>2}. {descricao}{Cor.RESET}")
        print(f"\n  {Cor.VERMELHO}22. Sair{Cor.RESET}")
        print(f"\n{'═' * 60}")

        escolha = input(f"{Cor.BRANCO}{Cor.BOLD}  Escolha uma opção (1-22): {Cor.RESET}").strip()

        if escolha == "22":
            limpar()
            print(f"{Cor.AZUL}{Cor.BOLD}")
            print("  Obrigado por usar AOFR TECH!")
            print("  Atitude | Orientação | Força | Resultado")
            print(f"  — Alfredo Ociola Francisco Romano —{Cor.RESET}\n")
            sys.exit(0)
        elif escolha in OPCOES:
            cabecalho()
            OPCOES[escolha][1]()
            pausar()
        else:
            print(f"{Cor.VERMELHO}  [!] Opção inválida. Tenta novamente.{Cor.RESET}")
            time.sleep(1)

# ─────────────────────────────────────────────
#  ENTRADA
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # Activar cores ANSI no Windows
    if SISTEMA == "Windows":
        os.system("color")
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

    verificar_admin()
    menu()

#!usr/bin/env python3
# Copyright | WahyuXD - 7 February 2025
# Meta - Ai Chat Bot

import requests
import json
import time
import os
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

# <-- Konfigurasi & Global Var -->
API_URL = "https://meta-ai.rozhak.cfd/api/chat"
HEAD = {"Content-Type": "application/json"}
console = Console()
histori = []

def banner():
    console.print(Panel("""______________        _____________                 _____
__  ____/__  /_______ __  /___  __ )______ __________  /_  Chat Bot Meta AI 
_  /    __  __ \  __ `/  __/_  __  |_  __ `__ \  _ \  __/  Version 1.0
/ /___  _  / / / /_/ // /_ _  /_/ /_  / / / / /  __/ /_    Realese 7 February 2025 
\____/  /_/ /_/\__,_/ \__/ /_____/ /_/ /_/ /_/\___/\__/    Coded By WahyuXD

[bold green]     💬 Kirim pesan untuk memulai dengan Meta AI[/] ([bold]Ketik [red]Exit[/] untuk keluar)"""))

# <-- Clear Terminal -->
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# <-- Kirim Chat -->
def kirim_chat(message):
    try:
        data = json.dumps({"message": message})
        response = requests.post(API_URL, data=data, headers=HEAD)
        response.raise_for_status()
        response_json = response.json()
        return response_json.get("message", "Error: Tidak ada respon dari Meta AI")
    except requests.exceptions.RequestException as e:
        return f"Request Error: {e}"

# <-- Riwayat Chat -->
def chat_riwayat():
    with open("history.txt", "w", encoding="utf-8") as file:
        for chat in histori:
            file.write(chat + "\n")

# <-- Loop (Interaksi) -->
if __name__ == "__main__":
    try:
        print("You need to enable API server first...")
        time.sleep(1)
        os.system('xdg-open https://www.meta-ai.rozhak.cfd/api/docs/#/default/post_api_chat');time.sleep(1.5)
    except:pass
    clear_terminal()
    banner()
    #console.print(Panel(banner, expand=False))

    while True:
        lu_ketik = console.input("[bold cyan]Eloee:[/] ")
        if lu_ketik.lower() == "exit":
            console.print("[bold red]👋 Keluar dari chat...[/]\n[bold white]Terimakasih sudah menggunakan aplikasi kami.[/]")
            chat_riwayat()
            break

        #console.print(Panel(f"[bold cyan]Eloee:[/] {lu_ketik}", expand=False))
        histori.append(f"Eloee: {lu_ketik}")

        console.print("[bold yellow]Memet sedang mengetik...[/]", end="\r")
        time.sleep(1.5)

        memet_respons = kirim_chat(lu_ketik)
        histori.append(f"Memet: {memet_respons}")

        console.print(Panel(Markdown("{}".format(memet_respons), style="bold"), expand=False))

import typer
import time
import os
import json
import random
from git import Repo
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from datetime import datetime, timedelta

app = typer.Typer(help="TVA: Timeline Variance Authority CLI")
console = Console()

TVA_ORANGE = "#ff9900" 
TVA_RED = "#ff0000"
DATABASE_FILE = ".tva_log.json"

def check_triggers(command, arg):
    """Interprets specific inputs as hidden interactions."""
    arg = arg.lower() if arg else ""

    if "mobius" in arg or "jetski" in arg:
        console.print("\n[italic cyan]Wow.[/] [dim](Mobius approves of this timeline)[/]\n")
        return "SAFE"

    if "sylvie" in arg or "enchantress" in arg:
        console.print(Panel("⚠ UNAUTHORIZED VARIANT DETECTED ⚠\nThis timeline is bombing!!", style=f"bold {TVA_RED} blink"))
        return "DANGER"

    if "kang" in arg or "remains" in arg:
        console.print("[bold white]See you soon...[/]")
        time.sleep(2)
        return "SAFE"
    
    return "NORMAL"

def get_repo():
    try:
        return Repo(os.getcwd())
    except:
        console.print(f"[bold {TVA_RED}]❌ NEXUS EVENT: No Git Repository found here.[/]")
        raise typer.Exit()

def load_db():
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_db(data):
    with open(DATABASE_FILE, 'w') as f:
        json.dump(data, f)

@app.command()
def variant(name: str):
    """Creates a new branch (Variant). Usage: tva variant [name]"""
    
    status = check_triggers("variant", name)
    if status == "DANGER": return

    repo = get_repo()
    try:
        current = repo.create_head(name)
        current.checkout()
        
        data = load_db()
        data[name] = datetime.now().isoformat()
        save_db(data)
        
        warning = Text()
        warning.append("⚠  VARIANT IDENTIFIED  ⚠\n", style=f"bold {TVA_ORANGE}")
        warning.append(f"Branch '{name}' has stepped off the Sacred Timeline.\n", style="white")
        warning.append("Standard Protocol: Merge within 30 minutes or face pruning.", style="dim")
        
        console.print(Panel(warning, border_style=TVA_ORANGE))
        
    except Exception as e:
        console.print(f"[red]Error creating variant: {e}[/]")

@app.command()
def prune(target: str = typer.Argument(None, help="Specific variant to prune")):
    """Prunes old branches. Usage: tva prune OR tva prune [name]"""
    
    if target == "all":
        console.print(f"[bold {TVA_ORANGE}]SENDING EVERYTHING TO THE VOID...[/]")
        console.print("[dim]Alioth is hungry today.[/]")
        return

    data = load_db()
    repo = get_repo()
    active_variants = list(data.keys())
    
    for branch in active_variants:
        if "mobius" in branch.lower():
            console.print(f"[cyan]Skipping '{branch}'. We never prune a friend.[/]")
            continue

        creation_time = datetime.fromisoformat(data[branch])
        
        is_old = datetime.now() - creation_time > timedelta(minutes=30)
        is_targeted = target and target == branch
        
        if is_old or is_targeted:
            console.print(f"[bold {TVA_ORANGE}]⚡ RESET CHARGE DEPLOYED ON: {branch}[/]")
            try:
                repo.heads['main'].checkout()
                repo.delete_head(branch, force=True)
                console.print(f"[dim]Variant {branch} sent to The Void.[/]")
                del data[branch]
            except Exception as e:
                console.print(f"[red]Pruning failed: {e}[/]")

    save_db(data)
    console.print("[bold green]Timeline Stable.[/]")

@app.command(hidden=True)
def miss_minutes():
    """Summons the AI mascot."""
    art = r"""
       (  .      )
     .           .
   (       o       )   "Hey y'all!"
   (       |       ) 
   (     \___/     )
    """
    console.print(art, style=f"bold {TVA_ORANGE}")

@app.command(hidden=True)
def alligator():
    """Summons Alligator Loki."""
    console.print("🐊 [bold green]CHOMP.[/] (He ate your hand.)")

if __name__ == "__main__":
    app()

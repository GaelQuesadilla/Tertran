import click
import src.data.langs as lg
import colorama
from tabulate import tabulate
colorama.init(autoreset=True)

@click.command()
def get_langs():
  '''
    Command line to get a table with avaiable langs
  '''
  allLangs = [ [
    colorama.Fore.GREEN + key , 
    colorama.Fore.RESET + lg.langs[key] 
    ] for key in lg.langs.keys()]

  click.echo(tabulate(allLangs))
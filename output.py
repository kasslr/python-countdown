from rich.table import Table
from rich.console import Console

def generateOutput(str):

    table = Table()

    table.add_column("Time remaining", justify="left", style="light_steel_blue")

    table.add_row(str)

    Console().print(table)
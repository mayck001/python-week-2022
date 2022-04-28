import typer
from typing import Optional
from beerlog.core import add_beer_to_database , get_beers_from_database
from rich.table import Table
from rich.console import Console

main = typer.Typer(help="Beer Management")

console = Console()

@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """add a new beer to database."""
    if add_beer_to_database(name, style, flavor, image, cost):
       print("beer add with sucess to database")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """lists beer in database."""
    beers = get_beers_from_database()
    table  = Table(title="beerlog")
    headers = ("id", "name", "style", "rate", "date")
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date= beer.date.strftime("%Y-%m-%d")
        values=[str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)

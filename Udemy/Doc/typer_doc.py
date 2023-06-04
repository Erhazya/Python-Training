import typer

# Créer une instance de Typer
app = typer.Typer()

# Définition de la fonction principale
def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"), extension: str = typer.Argument(None, help="Extension à chercher")):
    """
    Fonction principale du programme qui effectue la recherche ou la suppression de fichiers en fonction des paramètres.

    Args:
        delete (bool): Indique si les fichiers trouvés doivent être supprimés. Par défaut, la suppression est désactivée.
        extension (str): L'extension des fichiers à chercher ou à supprimer. Si aucun argument n'est spécifié en ligne de commande,
        l'utilisateur sera invité à fournir cette information.

    Raises:
        typer.Abort: Si l'utilisateur annule la suppression des fichiers après confirmation.

    Returns:
        None
    """
    # Demande à l'utilisateur de spécifier l'extension à chercher si elle n'a pas été spécifiée en ligne de commande
    if not extension:
        extension = typer.prompt("Quelle extension veux-tu chercher ?")

    # Vérifie si aucune extension n'a été spécifiée
    if not extension:
        typer.echo("Aucune extension n'a été spécifiée")
    else:
        typer.echo(f"Recherche des fichiers avec l'extension {extension}")

    # Vérifie si l'option de suppression est activée
    if delete:
        # Demande une confirmation pour la suppression des fichiers
        do_delete = typer.confirm("Confirmation de suppression")
        if not do_delete:
            typer.echo("Suppression annulée")
            raise typer.Abort()

        typer.echo("Suppression des fichiers")

# Commande "search"
@app.command("search")
def search_py():
    """
    Commande pour chercher les fichiers avec l'extension .py.
    """
    main(delete=False, extension="py")

# Commande "delete"
@app.command("delete")
def delete_py():
    """
    Commande pour supprimer les fichiers avec l'extension .py.
    """
    main(delete=True, extension="py")

if __name__ == "__main__":
    # Exécute l'application Typer
    app()

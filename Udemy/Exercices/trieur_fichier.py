from pathlib import Path

"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""


path = Path("./FichierTest/data")




dictionnaire_extensions = {
        '.mp3': 'Musique',
        '.wav': 'Musique',
        '.flac': 'Musique',
        '.avi': 'Videos',
        '.mp4': 'Videos',
        '.gif': 'Videos',
        '.bmp': 'Images',
        '.png': 'Images',
        '.jpg': 'Images',
        '.txt': 'Documents',
        '.pptx': 'Documents',
        '.csv': 'Documents',
        '.xls': 'Documents',
        '.odp': 'Documents',
        '.pages': 'Documents'
}



files = [f for f in path.iterdir() if f.is_file()]

for f in files:

    output_dir = path / dictionnaire_extensions.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)

    f.rename(output_dir / f.name)
    









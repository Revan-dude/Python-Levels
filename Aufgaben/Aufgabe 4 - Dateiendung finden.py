# Aufgabe: Gib fuer jeden Dateinamen die Endung nach dem letzten Punkt aus.
# Wenn kein Punkt enthalten ist, gib eine passende Meldung aus.
file_names = ["bericht.pdf", "README", "archiv.tar.gz"]

for file_name in file_names:
    extension = None
    if "." in file_name:
        extensions = file_name.split(".")
        extension = extensions[len(extensions) - 1]

    print(file_name, "->", extension)

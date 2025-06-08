import subprocess

# The process name to be 
process_name = "notepad.exe"

# Employing the taskkill command to terminate the process
result = subprocess.run(f"taskkill /f /im {process_name}", shell=True)

if result.returncode == 0:
    print(f"{process_name} fermée, retourne travailler !")
else:
    print("Erreur lors de la fermeture du programme")

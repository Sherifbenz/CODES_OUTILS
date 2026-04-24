#######################################
##########   SOUS WINDOWS  ############
#######################################

"""
from docx2pdf import convert
convert("MSc_BIDPG scholarship tips 2026.docx") # Convertit en document.pdf
#convert("dossier_word/", "dossier_pdf/") # Conversion en masse
"""

#######################################
##########   SOUS LINUX  ##############
#######################################
import subprocess
subprocess.run([
    "libreoffice",
    "--headless",
    "--convert-to", "pdf",
    "MSc_BIDPG scholarship tips 2026.docx"
])


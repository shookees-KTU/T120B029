# -*- coding: utf-8 -*-

"""Įrankis sugeneruoti UML diagramoms iš vienos direktorijos į kitą.
Konstantos nustatomos iš anksto
"""

import subprocess

UML_DIR = "UML"
DIAGRAMOS_DIR = "Diagramos"
PLANTUML_EXEC = "plantuml.8023.jar"

def parse_uml():
    """Panaudodamas konstantas sukuria UML png atvaizdus
    Įdomus veikimo būdas:
    output'o direktorijos pagrindas statomas palei source'o direktoriją
    """
    cmd = "java -jar {0} -o ../{2}/ {1}/*".format(PLANTUML_EXEC,
                                                  UML_DIR,
                                                  DIAGRAMOS_DIR)
    process = subprocess.Popen(cmd, shell=True)
    results = process.communicate()
    print "stdout: {0}\nstderr: {1}".format(results[0], results[1])

if __name__ == "__main__":
    # Paima visus uml failus ir tiesiog perleidžia su plantuml'u
    parse_uml()

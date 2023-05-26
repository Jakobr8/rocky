########
'''
Name for generated for macro: Automatische Simulation
Macro description: simuliert automatisch mit unterschiedlichen Parametern
'''
#
# import der Bibliotheken
import csv
import numpy as np
import os

# Verknüfung Rockyprojekt
project = app.GetProject()
#Befehl um Variablen in Rocky zu steuern
input_variables = project.GetInputVariables()
#
#x1 = input_variables.CreateVariable('mu_s', value=0.3)           # erstellt Variable und weißt parameter zu 
#x2 = input_variables.CreateVariable('mu_d', value=0.3)
#x3 = input_variables.CreateVariable('t_s_r', value=1)           
#x4 = input_variables.CreateVariable('r_c', value=0.3)
#
#
cur_dir = os.path.dirname(project.GetProjectFilename())
#
output_file = open(cur_dir + "\\output.txt","a+")      # textdatei erstellen
#
#
#
parameter = np.array[1.00,2.00,3.00,4.00]            # Array erstellen, welches die Werte an die Variablen übergibt
n = 4                                                # Anzahl der Variablen
# Datei mit Inputparametern einlesen

with open('C:\\Users\\jakob\\OneDrive\\Desktop\\IP Lentz\\Python_Skripts\\parameter1000.csv', 'r') as csv_datei:

    reader = csv.reader(csv_datei)
    next(reader)                                       # Kopfzeile überspringen
for i in reader:
    for j in range (n):
        parameter [j] = float(i[j])     # parameter des arrays werden aus csv.datei überschrieben
    x1 = Set.Value (parameter[0])
    x2 = Set.Value (parameter[1])
    x3 = Set.Value (parameter[2])
    x4 = Set.Value (parameter[3])
     
    app.GetStudy().StartSimulation(skip_summary=True, delete_results=True)   # Simulation ausführen  

    with open('C:\\Users\\jakob\\OneDrive\\Dokumente\\Rocky\\Scripts\\script_winkel.py', 'r') as file:    # skript für die outputdatei laden
        python_code = file.read()
        exec(python_code)  # skript ausführen
        output_file.write(str(beta) + "\n")
output_file.close()


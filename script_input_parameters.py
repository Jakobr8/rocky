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
#
cur_dir = os.path.dirname(project.GetProjectFilename())
#
output_file = open(cur_dir + "\\sensitivity_results.txt","a+")      # textdatei erstellen
#
upper_values = [0.5,0.5,1,1,0.3]
#
with open(cur_dir+'\\parameter1000.csv', 'r') as csv_datei:

    reader = csv.reader(csv_datei)
    next(reader) 
    #   
    for data in reader:
        app.GetStudy().DeleteResults()
        input_variables.GetVariableByName('mu_s').SetValue(float(data[0])*upper_values[0])
        input_variables.GetVariableByName('mu_d').SetValue(float(data[1])*upper_values[1])
        input_variables.GetVariableByName('tsr').SetValue(float(data[2])*upper_values[2])
        input_variables.GetVariableByName('csm').SetValue(float(data[3])*upper_values[3])
        input_variables.GetVariableByName('rc').SetValue(float(data[4])*upper_values[4])
        #
        app.GetStudy().StartSimulation(skip_summary=True, delete_results=True)   # Simulation ausführen  
        #

output_file.close()


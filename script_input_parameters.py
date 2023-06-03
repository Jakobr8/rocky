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
upper_values = [0.5,0.5,1,1,0.3,0.3]
const = 0.01
#
with open(cur_dir+'\\ergebnis.csv', 'r') as csv_datei:

    reader = csv.reader(csv_datei)
    next(reader) 
    #   
    for data in reader:
        app.GetStudy().DeleteResults()
        
        input1 = np.round(const+float(data[0])*upper_values[0], decimals=2)
        input2 = np.round(const+float(data[1])*upper_values[1], decimals=2)
        input3 = np.round(const+float(data[2])*upper_values[2], decimals=2)
        input4 = np.round(const+float(data[3])*upper_values[3], decimals=2)
        input5 = np.round(const+float(data[4])*upper_values[4], decimals=2)
        input6 = np.round(const+float(data[5])*upper_values[5], decimals=2)

        input_variables.GetVariableByName('mu_s').SetValue(input1)
        input_variables.GetVariableByName('mu_d').SetValue(input2)
        input_variables.GetVariableByName('tsr').SetValue(input3)
        input_variables.GetVariableByName('csm').SetValue(input4)
        input_variables.GetVariableByName('rc').SetValue(input5)
        input_variables.GetVariableByName('rr').SetValue(input6)
        #
        with open(cur_dir + "\\sensitivity_results.txt", "a+") as output_file:
            output_file.write(str(input1) + "," + str(input2) + "," + str(input3) + "," + str(input4) + "," + str(input5) + "," + str(input6) + ",")
        output_file.close()

        #
        app.GetStudy().StartSimulation(skip_summary=True, delete_results=True)   # Simulation ausführen  
        

output_file.close()


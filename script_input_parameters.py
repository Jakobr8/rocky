#
#
#
#
#
project = app.GetProject()
input_variables = project.GetInputVariables()
#
#
input_variables.CreateVariable('a', value=1)           # erstellt Variable und weißt parameter zu 
input_variables.CreateVariable('b', value=2)

#input_variables.RemoveVariable('a')                   # löscht Variable
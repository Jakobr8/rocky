#
'''
Name for generated for macro: Winkel bestimmen
Macro description: Bestimmt den Winkel 
'''
#
import os
import sys
import importlib
import math
import numpy as np
#
sys.path.append("C:/Users/jakob/OneDrive/Desktop/IP Lentz/Python_Skripts")
import trafo
#
#
#
#Verzeichnis des geöffneten Rocky-Projekts  
#cur_dir = "C:\Simulationen\Planetenkugelmuehle\Rocky\Simulationen\zweifache_Schraegstellung/1Kugel"
#print(cur_dir)
cur_dir = os.path.dirname(project.GetProjectFilename())
#
#logfile öffnen
log_file = open(cur_dir + "\\log_file.txt","a+")
log_file.write("*************************************************\n")
log_file.write("Logfile started \n")
#
log_file.write("C:/Users/jakob/OneDrive/Desktop/IP Lentz/Python_Skripts")
#
#config importieren
sys.path.append(cur_dir)
import config
if 'config' in sys.modules:
    importlib.reload(config)
while cur_dir in sys.path:
    sys.path.remove(cur_dir)
#
log_file.write(str(config)+"\n")
#
def ang(t,t1,t2,ur):
    if t<t1:
        return 0
    elif t<t2:
        return 0.5*ur/(t2-t1)*(t-t1)**2
    else:
        return 0.5*ur*(t2-t1)+ur*(t-t2)
#
# Iterable Particles besorgen
study = app.GetStudy()
particles = study.GetParticles()
#
#relevante Zeitschritte bestimmen
times = study.GetTimeSet().GetValues()
start_time_step = int(np.searchsorted(times, config.t_pic, side = "left"))
end_time_step = int(np.searchsorted(times, config.t3, side = "left"))
#
cur_time_step = 11000
cur_time = times[cur_time_step]
log_file.write("aktueller Zeitschritt:" + str(cur_time_step)+"\n")
#
x0 = list(particles.GetGridFunction('Particle X-Coordinate').GetArray(time_step=cur_time_step))
y0 = list(particles.GetGridFunction('Particle Y-Coordinate').GetArray(time_step=cur_time_step))
z0 = list(particles.GetGridFunction('Particle Z-Coordinate').GetArray(time_step=cur_time_step))
#
log_file.write("x-Koordinate in 0_Kosys: " + str(x0[0])+"\n")
log_file.write("y-Koordinate in 0_Kosys: " + str(y0[0])+"\n")
log_file.write("z-Koordinate in 0_Kosys: " + str(z0[0])+"\n")
#
log_file.write("transformation\n")
trafo = trafo.Trafo(80, 20, config.u, -22) # Radius Sonne, Winkel Schrägstellung, Drehzahl-Sonne, Relative z-Koordinate Bechermittelpunkt
#
start_time = times[start_time_step]
pos = ang(start_time, config.t1, config.t2, np.pi*config.u/30)
phase = config.u/abs(config.u)*(abs(pos)%(2*np.pi))
#
#
cur_alpha = phase + trafo.om1 * (cur_time-start_time)
cur_gamma = trafo.n * cur_alpha
#
cur_coords = trafo.trafo_x_2_0((1000*x0[0], 1000*y0[0], 1000*z0[0]), cur_alpha, cur_gamma)
log_file.write("x-Koordinate in 2_Kosys: " + str(cur_coords[0])+"\n")
log_file.write("y-Koordinate in 2_Kosys: " + str(cur_coords[1])+"\n")
log_file.write("z-Koordinate in 2_Kosys: " + str(cur_coords[2])+"\n")
#
#
beta = math.atan(x0[0]/y0[0])   # Berechnung von Winkel der Kugel zu x-Achse von Becherkoordinatensystem mit Tangens   
beta = beta * 180/math.pi
#
log_file.write("Winkel Beta: " + str(beta) + "\n")
#
log_file.write("ende")
log_file.close()
#
#

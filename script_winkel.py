#
'''
Name for generated for macro: Winkel bestimmen
Macro description: Bestimmt den Winkel des Mittelpunkts der Kugel zur Horizontalen
'''
#
import os
import sys
import importlib
import math
import numpy as np
#
#trafo_path = "C:/Users/jakob/OneDrive/Desktop/IP Lentz/Python_Skripts"
trafo_path = "C:\SeafileContainer\Seafile\Meine Bibliothek\Planetenkugelmuehle\Programme\eigene"
#
sys.path.append(trafo_path)
import trafo
#
#
#
#Verzeichnis des geöffneten Rocky-Projekts  
cur_dir = os.path.dirname(project.GetProjectFilename())
#
#logfile öffnen
log_file = open(cur_dir + "\\log_file.txt","a+")
log_file.write("*************************************************\n")
log_file.write("Logfile started \n")
#
log_file.write(trafo_path)
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
log_file.write("transformation\n")
trafo = trafo.Trafo(125, 5, config.u, config.alpha) # Radius Sonne, Relative z-Koordinate Bechermittelpunkt, Drehzahl-Sonne, Winkel Schrägstellung
#
#
def get_angle(trafo,cur_time_step,times):
    #
    x0 = list(particles.GetGridFunction('Particle X-Coordinate').GetArray(time_step=cur_time_step))
    y0 = list(particles.GetGridFunction('Particle Y-Coordinate').GetArray(time_step=cur_time_step))
    z0 = list(particles.GetGridFunction('Particle Z-Coordinate').GetArray(time_step=cur_time_step))
    #
    cur_alpha = ang(times[cur_time_step], config.t1, config.t2, np.pi*config.u/30)%(2*np.pi)
    cur_gamma = trafo.n * cur_alpha
    cur_coords = trafo.trafo_x_2_0((1000*x0[0], 1000*y0[0], 1000*z0[0]), cur_alpha, cur_gamma)
    #
    cur_ang = math.atan(cur_coords[1]/cur_coords[0])   # Berechnung von Winkel der Kugel zu x-Achse von Becherkoordinatensystem mit Tangens   
    return cur_ang * 180/math.pi
#
#
#
res_file = open(cur_dir + "\\results.txt","w+")
sum = 0
for cur_time_step in range(start_time_step,end_time_step):
    cur_ang = get_angle(trafo,cur_time_step,times)
    sum += cur_ang
    res_file.write(f"{times[cur_time_step]:.5f}" + "\t" + str(cur_ang) + "\n")
res_file.close()
#
sensi_file = open(cur_dir + "\\sensitivity_results.txt","a+")
sensi_file.write(str(sum/(end_time_step-start_time_step)))
sensi_file.close()
#
log_file.write("ende")
log_file.close()
#
#

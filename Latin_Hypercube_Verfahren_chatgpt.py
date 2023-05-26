#
#
#
# von Chat GPT erstelltes Programm für das Latin Hypercube Verfahren
#
import random
import csv
import numpy as np
import matplotlib.pyplot as plt


def latin_hypercube(samples, variables):
    """numpy installine
    Führt das Optimal Latin Hypercube Verfahren durch.

    Args:
        samples (int): Anzahl der zu generierenden Muster.
        variables (int): Anzahl der Variablen.

    Returns:
        np.array: Ein 2D-Array mit den generierten Mustern.
    """

    intervals = 1.0 / samples

    matrix = np.zeros((samples, variables))

    for i in range(variables):
        for j in range(samples):
            matrix[j, i] = random.uniform(j * intervals, (j + 1) * intervals)

    for i in range(variables):
        np.random.shuffle(matrix[:, i])

    return matrix

# Beispielaufruf
samples = 3
variables = 4

result = latin_hypercube(samples, variables)
#
#
#
header = ['mu_s', 'mu_d', 'tangential stiffnes ratio', 'restitiution coefficient']   # Spaltennamen erstellen
#
result = np.round(result, decimals=2)     # zahlen auf 2 Nachkommastellen runden
# Ergebnis in eine CSV-Datei schreiben
with open('parameter1000.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Spaltennamen schreiben
    writer.writerow(header)
    
    # Ergebnisdaten schreiben
    writer.writerows(result)

print("Ergebnis wurde in ergebnis.csv gespeichert.")


#np.savetxt("parameter1000.csv", result, delimiter=',', fmt='%.2f')

#print("Ergebnis wurde in parameter1000.csv gespeichert.")
#
#
# Scatter Plot der Ergebnismatrix erstellen
x_values = np.arange(samples)
for i in range(variables):
    plt.scatter(x_values, result[:, i], c=f'C{i}', label=f'Variable {i+1}')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Optimal Latin Hypercube')
plt.legend()

plt.show()
import HFSS_Python.HFSSLibrary as hfss
import numpy as np
import sys, os
file_dir = os.path.dirname('linear_weight_gen.py')
sys.path.append(file_dir)
import linear_weight_gen as wg

oAnsys, oDesktop = hfss.openHFSS()
print(oDesktop.GetActiveProject())
test = oDesktop.GetActiveProject().GetName()
print(test)

if not test == 'dip_tut':
    oDesktop.SetActiveProject('dip_tut.aedt')

def main():

    n = 2  # Antennas
    d = 0.5  # Spacing in wavelengths
    soi = 20  # Signals of Interest locations
    snoi = 70  # Null location

    exc, phas = wg.weight_gen(n, d, soi, snoi)

    print('exc =', exc)
    print('phase =', phas)

    ###
    wg.weight_plot(n, d, soi, snoi)
    ###

    # excitations = ['1','2']
    # magnitudes = [3,3]
    # phases = [30, 40]
    excitations = ['1','2']
    magnitudes = exc
    phases = phas

    modes = np.ones((1, len(magnitudes)))



    oProject = oDesktop.GetActiveProject()
    oDesign = oProject.SetActiveDesign('HFSSDesign1')
    hfss.edit_sources(oDesign, excitations, modes,magnitudes,phases,'W','deg' )

    return()

if __name__ == "__main__": main()

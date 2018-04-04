import HFSS_Python.HFSSLibrary as hfss
import numpy as np

oAnsys,oDesktop = hfss.openHFSS()
print(oDesktop)
test = oDesktop.GetActiveProject().GetName()
print(test)

if not test == 'dip_tut':
    oDesktop.SetActiveProject('dip_tut.aedt')

excitations = ['1']
magnitudes = [3]
modes = np.ones((1,len(magnitudes)))
phases = [45]



oProject = oDesktop.GetActiveProject()
oDesign = oProject.SetActiveDesign('HFSSDesign1')
hfss.edit_sources(oDesign, excitations, modes,magnitudes,phases,'W','deg' )

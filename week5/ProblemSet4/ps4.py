# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    result = {300:[], 150:[], 75:[], 0:[]}
    # result = {3:[], 2:[], 1:[], 0:[]}
    for key in result:
        print "key = ", key
        for i in range(numTrials):
            numViruses = 100
            # numViruses = 10
            maxPop = 1000
            maxBirthProb = 0.1
            clearProb = 0.05
            resistances = {'guttagonol': False}
            mutProb = 0.005
            viruses = [];
            for i in range(numViruses):
                virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb);
                viruses.append(virus);

            patient = TreatedPatient(viruses, maxPop);
            trial = []
            for step in range(key):
                virus_population_after_update = patient.update()
                trial.append(virus_population_after_update)
            # result[key].append(trial)

            patient.addPrescription('guttagonol')
            # for step in range(150):
            for step in range(150):
                virus_population_after_update = patient.update()
                trial.append(virus_population_after_update)
            result[key].append(trial)

    ## mean for [[1,2,3], [2,3,4], [3,4,5]] = [2,3,4]
    # for key in result:
    #     data = numpy.array (result[key])
    #     # print numpy.average(data,0) #0 - by coloms, inside row
    #     result[key] = list(numpy.average(data,0))
    # print result

    for i,key in enumerate(result):
        data = numpy.array (result[key])
        array_final_steps = data.take(-1,1) # 1 - by rows, inside column
        # print "array_final_steps", array_final_steps
        pylab.subplot(4,1,i)
        pylab.title(str(key))
        pylab.hist(array_final_steps,bins=20)
    pylab.show()

# simulationDelayedTreatment(100)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO

    result = {300:[], 150:[], 75:[], 0:[]}
    # result = {3:[], 2:[], 1:[], 0:[]}
    for key in result:
        print "key = ", key
        for i in range(numTrials):
            numViruses = 100
            # numViruses = 10
            maxPop = 1000
            maxBirthProb = 0.1
            clearProb = 0.05
            resistances = {'guttagonol': False, 'grimpex': False}
            mutProb = 0.005
            viruses = [];
            for i in range(numViruses):
                virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb);
                viruses.append(virus);

            patient = TreatedPatient(viruses, maxPop);
            trial = []

            for step in range(150):
                virus_population_after_update = patient.update()
                trial.append(virus_population_after_update)

            patient.addPrescription('guttagonol')
            for step in range(key):
                virus_population_after_update = patient.update()
                trial.append(virus_population_after_update)
            # result[key].append(trial)

            patient.addPrescription('grimpex')
            # for step in range(150):
            for step in range(150):
                virus_population_after_update = patient.update()
                trial.append(virus_population_after_update)
            result[key].append(trial)

    ## mean for [[1,2,3], [2,3,4], [3,4,5]] = [2,3,4]
    # for key in result:
    #     data = numpy.array (result[key])
    #     # print numpy.average(data,0) #0 - by coloms, inside row
    #     result[key] = list(numpy.average(data,0))
    # print result

    for i,key in enumerate(result):
        data = numpy.array (result[key])
        array_final_steps = data.take(-1,1) # 1 - by rows, inside column
        # print "array_final_steps", array_final_steps
        pylab.subplot(4,1,i)
        pylab.title(str(key))
        pylab.hist(array_final_steps,bins=20)
    pylab.show()

simulationTwoDrugsDelayedTreatment(100)
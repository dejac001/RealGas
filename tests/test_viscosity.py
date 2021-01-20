import logging
logging.basicConfig(level=logging.DEBUG)
from realgas.viscosity import Viscosity, ViscosityMixture
from chem_util.math import percent_difference

compounds_to_test = ['Butane', 'Carbon dioxide', 'Carbon monoxide',
                     'Propane', 'Propylene']


kwargs = dict(T_min_fit=200., T_max_fit=500.)
tol = 0.1


def test_viscosity_init():
    for i in compounds_to_test:
        I = Viscosity(compound_name=i, **kwargs)

    for i in 'Helium-4', 'Nitrogen', 'Water':
        I = Viscosity(compound_name=i)

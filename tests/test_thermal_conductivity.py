import logging
logging.basicConfig(level=logging.DEBUG)
from realgas.thermal_conductivity import ThermalConductivity, ThermalConductivityMixture

compounds_to_test = ['Butane', 'Carbon dioxide', 'Carbon monoxide',
                     'Propane', 'Propylene']


kwargs = dict(T_min_fit=275., T_max_fit=800.)
tol = 0.1


def test_thermal_conductivity_init():
    for i in compounds_to_test:
        I = ThermalConductivity(compound_name=i, **kwargs)

    for i in 'Helium-4', 'Nitrogen', 'Water':
        I = ThermalConductivity(compound_name=i)

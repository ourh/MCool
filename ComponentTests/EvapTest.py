from __future__ import division
from Evaporator import EvaporatorClass
from FinCorrelations import FinInputs
from CoolProp.CoolProp import Props

FinsTubes=FinInputs()
    
FinsTubes.Tubes.NTubes_per_bank=32
FinsTubes.Tubes.Nbank=3
FinsTubes.Tubes.Ltube=0.452
FinsTubes.Tubes.OD=0.009525
FinsTubes.Tubes.Pl=0.0254
FinsTubes.Tubes.Pt=0.0219964

FinsTubes.Fins.FPI=14.5
FinsTubes.Fins.Pd=0.001
FinsTubes.Fins.xf=0.001
FinsTubes.Fins.t=0.00011
FinsTubes.Fins.k_fin=237

FinsTubes.Air.Vdot_ha=0.5663
FinsTubes.Air.Tmean=299.8
FinsTubes.Air.Tdb=299.8
FinsTubes.Air.p=101.325
FinsTubes.Air.RH=0.51
FinsTubes.Air.RHmean=0.51

# Temporary value for inlet quality 
# (Quality is passed in from cycle model)
xin_r=0.3
    
kwargs={'Ref': 'R410A',
        'mdot_r':  0.0708,
        'psat_r':  Props('P','T',5.4+273.15,'Q',1.0,'R410A'),
        'Vdot_a':  0.5663,
        'pin_a':   101.3,
        'Tin_a':   299.8,
        'mdot_a': 0.662,
        'RHin_a':0.5,
        'OD':0.009525,
        'ID':0.0089154,
        'Ncircuits':5,
        'Ltube':0.452,
        'Nbank':3,
        'NTubes_per_bank':32,
        'FanPower':438,
        'Fins': FinsTubes,
        'xin_r':xin_r,
        'Verbosity':3
}

Evap=EvaporatorClass(**kwargs)
Evap.Update(**kwargs)
Evap.Calculate()

print Evap.Charge
class MagneticClass:
    def __init__(self, Gamma, RestMass, ElectronVolt):
        self.Gamma = Gamma
        self.RestMass = RestMass
        self.ElectronVolt = 1.60 * (10**-19) * ElectronVolt
    def Calculate_Magnetic_Rigidity(self):
         speedOfLight = 299792458
         numerator = self.Gamma * self.RestMass * speedOfLight
         denorminator = self.ElectronVolt
         print(numerator/denorminator)
         print("The value of Magnetic Rigidity is ", numerator/denorminator)

# FIRST Test case Using 90[AMeV] 238-U-28+
Gamma = 1
RestMass = 3.5*(10**-8)
ElectronVolt = 28
Test1 = MagneticClass(Gamma, RestMass, ElectronVolt)
print("FIRST Test Case  ")
Test1.Calculate_Magnetic_Rigidity()
print("________________________________________________________________________________________________________________________________________________________________________________________________________________________")

# SECOND Test case Using 330 [Mev/u] 197-AU-77+
Gamma2 = 1
RestMass2 = 1*(10**-8)
ElectronVolt2 = 77
Test2 = MagneticClass(Gamma2, RestMass2, ElectronVolt2)
print("SECOND Test Case  ")
Test2.Calculate_Magnetic_Rigidity()
print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________")


# THIRD Test case Using 7[TeV] protons
Gamma4 = 1
RestMass4 = 1.5032755*(10**-10)
ElectronVolt4 = 1
Test3 = MagneticClass(Gamma4, RestMass4, ElectronVolt4)
print("FOURTH Test Case  ")
Test3.Calculate_Magnetic_Rigidity()


# FOURTH Test case Using 10[GeV] electron
Gamma3 = 1
RestMass3 = 8.1867592*(10**-14)
ElectronVolt3 = 1
Test3 = MagneticClass(Gamma3, RestMass3, ElectronVolt3)
print("THIRD Test Case  ")
Test3.Calculate_Magnetic_Rigidity()
print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________")



import numpy as np
import scipy.constants as const
import pandas as pd 
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

class LimestoneCalcinationAnalysis:
    """
    Advanced Thermodynamic Analysis of Limestone Calcination Process
    
    Comprehensive framework for detailed energy balance and thermodynamic assessment
    """
    
    def __init__(self, 
                 initial_temperature: float = 298.15,  # Kelvin
                 final_temperature: float = 973.15,    # Kelvin
                 pressure: float = 101325,             # Pascal
                 limestone_mass: float = 100.0):       # Kilograms
        """
        Initialize limestone calcination analysis parameters
        
        Parameters:
        -----------
        initial_temperature : float
            Starting temperature of the system
        final_temperature : float
            Target decomposition temperature
        pressure : float
            System pressure
        limestone_mass : float
            Mass of limestone sample
        """
        self.T0 = initial_temperature
        self.Tf = final_temperature
        self.P = pressure
        self.mass = limestone_mass
        
        # Molecular and thermodynamic constants
        self.molar_mass_CaCO3 = 100.0869  # g/mol
        self.R = const.R  # Universal gas constant
    
    def calculate_chemical_potential(self) -> Dict[str, float]:
        """
        Calculate chemical potential and Gibbs free energy for limestone decomposition
        
        Returns:
        --------
        Dict containing chemical potential parameters
        """
        # Standard thermodynamic data
        H_f_CaCO3 = -1206.9  # kJ/mol
        S_CaCO3 = 92.9  # J/(mol·K)
        
        # Gibbs Free Energy Calculation
        delta_G = H_f_CaCO3 - self.Tf * (S_CaCO3 / 1000)  # Convert to kJ
        
        return {
            'standard_enthalpy': H_f_CaCO3,
            'standard_entropy': S_CaCO3,
            'gibbs_free_energy': delta_G
        }
    
    def thermal_energy_requirements(self) -> Dict[str, float]:
        """
        Calculate thermal energy requirements for limestone decomposition
        
        Returns:
        --------
        Dict containing thermal energy components
        """
        # Specific heat capacities
        Cp_CaCO3 = 0.879  # J/(g·K)
        Cp_CaO = 0.942   # J/(g·K)
        
        # Latent heat of decomposition
        latent_heat = 178.3  # kJ/mol
        
        # Molar quantity calculation
        moles = self.mass * 1000 / self.molar_mass_CaCO3
        
        # Sensible heat calculation
        sensible_heat = moles * (
            Cp_CaCO3 * (self.Tf - self.T0) + 
            Cp_CaO * (self.Tf - self.T0)
        )
        
        return {
            'moles': moles,
            'sensible_heat': sensible_heat / 1000,  # Convert to kJ
            'latent_heat': latent_heat * moles / 1000
        }
    
    def entropy_analysis(self, thermal_data: Dict[str, float]) -> float:
        """
        Calculate entropy generation during limestone decomposition
        
        Parameters:
        -----------
        thermal_data : Dict
            Thermal energy data from thermal_energy_requirements
        
        Returns:
        --------
        Entropy generation value
        """
        # Entropy generation calculation
        entropy_gen = (
            thermal_data['sensible_heat'] / self.Tf + 
            thermal_data['latent_heat'] / self.Tf
        )
        
        return entropy_gen
    
    def comprehensive_energy_balance(self) -> pd.DataFrame:
        """
        Perform comprehensive energy balance analysis
        
        Returns:
        --------
        Pandas DataFrame with detailed energy analysis
        """
        # Calculate chemical potential
        chemical_potential = self.calculate_chemical_potential()
        
        # Calculate thermal energy requirements
        thermal_energy = self.thermal_energy_requirements()
        
        # Calculate entropy generation
        entropy_gen = self.entropy_analysis(thermal_energy)
        
        # Compile results
        results = {
            'Parameter': [
                'Initial Temperature (K)', 
                'Final Temperature (K)', 
                'Pressure (Pa)',
                'Limestone Mass (kg)',
                'Molar Quantity',
                'Standard Enthalpy (kJ/mol)',
                'Standard Entropy (J/(mol·K))',
                'Gibbs Free Energy (kJ/mol)',
                'Sensible Heat (kJ)',
                'Latent Heat (kJ)',
                'Entropy Generation'
            ],
            'Value': [
                self.T0,
                self.Tf,
                self.P,
                self.mass,
                thermal_energy['moles'],
                chemical_potential['standard_enthalpy'],
                chemical_potential['standard_entropy'],
                chemical_potential['gibbs_free_energy'],
                thermal_energy['sensible_heat'],
                thermal_energy['latent_heat'],
                entropy_gen
            ]
        }
        
        return pd.DataFrame(results)
    
    def visualize_energy_distribution(self, results_df: pd.DataFrame):
        """
        Create visualization of energy distribution
        
        Parameters:
        -----------
        results_df : pandas.DataFrame
            Comprehensive energy balance results
        """
        plt.figure(figsize=(10, 6))
        plt.title('Limestone Calcination - Energy Distribution')
        plt.bar(
            ['Sensible Heat', 'Latent Heat'], 
            [
                results_df.loc[results_df['Parameter'] == 'Sensible Heat (kJ)', 'Value'].values[0],
                results_df.loc[results_df['Parameter'] == 'Latent Heat (kJ)', 'Value'].values[0]
            ]
        )
        plt.ylabel('Energy (kJ)')
        plt.tight_layout()
        plt.show()

# Example usage
def main():
    # Initialize analysis
    limestone_analysis = LimestoneCalcinationAnalysis(
        initial_temperature=298.15,
        final_temperature=973.15,
        limestone_mass=100.0
    )
    
    # Perform comprehensive energy balance
    energy_results = limestone_analysis.comprehensive_energy_balance()
    
    # Display results
    print(energy_results)
    
    # Visualize energy distribution
    limestone_analysis.visualize_energy_distribution(energy_results)

if __name__ == "__main__":
    main()


class Sensitivity:
    @staticmethod
    def sensitivity_analysis():
        """
        Perform parameter sensitivity study
        Evaluates impact of parameter variations on energy balance
        """
        parameter_ranges = {
            'initial_temperature': [250.15, 300.15, 350.15],
            'final_temperature': [973.15, 1073.15, 1173.15],
            'pressure': [101325, 200000, 300000]
        }

        results = []
        for temp_initial in parameter_ranges['initial_temperature']:
            for temp_final in parameter_ranges['final_temperature']:
                for pressure in parameter_ranges['pressure']:
                    analysis = LimestoneCalcinationAnalysis(
                        initial_temperature=temp_initial,
                        final_temperature=temp_final,
                        pressure=pressure
                    )
                    result = analysis.comprehensive_energy_balance()
                    results.append(result)

        return results

results = Sensitivity.sensitivity_analysis()
print(results)

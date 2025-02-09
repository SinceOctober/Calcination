# Limestone Calcination Analysis

This repository contains a Python implementation for advanced thermodynamic analysis of the limestone calcination process. The code provides a comprehensive framework for detailed energy balance and thermodynamic assessment of limestone decomposition.

## Features

- **Thermodynamic Analysis**: Calculate chemical potential, Gibbs free energy, and entropy generation.
- **Energy Balance**: Perform comprehensive energy balance analysis including sensible heat and latent heat calculations.
- **Visualization**: Generate visualizations of energy distribution.
- **Sensitivity Analysis**: Evaluate the impact of parameter variations on energy balance.

## Dependencies

- `numpy`
- `scipy`
- `pandas`
- `matplotlib`

## Installation

To use this code, you need to have Python installed along with the required libraries. You can install the dependencies using pip:

```bash
pip install numpy scipy pandas matplotlib
```

## Usage

### Basic Usage

```python
from limestone_analysis import LimestoneCalcinationAnalysis

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
```

### Sensitivity Analysis

```python
from limestone_analysis import Sensitivity

# Perform sensitivity analysis
results = Sensitivity.sensitivity_analysis()
print(results)
```

## Class Documentation

### `LimestoneCalcinationAnalysis`

#### Methods

- `__init__(self, initial_temperature: float = 298.15, final_temperature: float = 973.15, pressure: float = 101325, limestone_mass: float = 100.0)`
  - Initializes the limestone calcination analysis parameters.

- `calculate_chemical_potential(self) -> Dict[str, float]`
  - Calculates chemical potential and Gibbs free energy for limestone decomposition.

- `thermal_energy_requirements(self) -> Dict[str, float]`
  - Calculates thermal energy requirements for limestone decomposition.

- `entropy_analysis(self, thermal_data: Dict[str, float]) -> float`
  - Calculates entropy generation during limestone decomposition.

- `comprehensive_energy_balance(self) -> pd.DataFrame`
  - Performs comprehensive energy balance analysis.

- `visualize_energy_distribution(self, results_df: pd.DataFrame)`
  - Creates visualization of energy distribution.

### `Sensitivity`

#### Methods

- `sensitivity_analysis()`
  - Performs parameter sensitivity study and evaluates the impact of parameter variations on energy balance.

## Example Output

### Energy Balance Results

```plaintext
                   Parameter          Value
0       Initial Temperature (K)    298.150000
1         Final Temperature (K)    973.150000
2                  Pressure (Pa)  101325.000000
3            Limestone Mass (kg)    100.000000
4               Molar Quantity      999.131000
5       Standard Enthalpy (kJ/mol)  -1206.900000
6       Standard Entropy (J/(mol·K))    92.900000
7       Gibbs Free Energy (kJ/mol)  -1296.073500
8               Sensible Heat (kJ)    599.478600
9                Latent Heat (kJ)    178.300000
10               Entropy Generation    0.799000
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

- This code was developed as part of an advanced thermodynamic analysis project.
- Special thanks to the contributors and reviewers.

---


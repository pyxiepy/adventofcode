"""The Fuel Counter-Upper needs to know the total fuel requirement. 
To find it, modidually calculate the fuel req for the mass of each 
module (your puzzle input), then add together all the fuel values."""

with open("module-mass-list.txt", "r") as f:
    mods_mass = [int(m) for m in f.read().split()]

def get_mod_fuel_req(mass):
    """Calculate total fuel requirement for a module, taking into account
    the additional mass of the fuel itself.

    Args:
        mass:   an integer representing the mass of a single module
    
    Returns:    the the total fuel requirement of the module
    """
    def get_fuel(mass):
        """Fuel required to launch a given module is based on its mass. 
        Specifically, to find the fuel required for a module, take its mass,
        divide by three, round down, and subtract 2.

        Args:
            mass:   an integer representing the mass of a single module.

        Returns:
            an integer representing the fuel requirement of the module.
        """
        return mass // 3 - 2
 
    fuel = get_fuel(mass)
    mod_fuel_req = 0

    while fuel > 0:
        mod_fuel_req += fuel
        fuel = get_fuel(fuel)

    return mod_fuel_req

def get_total_fuel_req(module_list):
    """Get the fuel requirement for each module and add all together
    to get total fuel requirement for all modules in the spacecraft.

    Args:
        module_list:    a list of all modules

    Returns:
        an integer representing the total fuel requirement
    """

    total_fuel_req = 0

    results = map(get_mod_fuel_req, module_list)

    for r in results:
        total_fuel_req += int(r)

    return total_fuel_req


total_fuel_requirement = get_total_fuel_req(mods_mass)



print(f'Total fuel needed for all spacecraft modules: \
{total_fuel_requirement:,}')


from akiraai.utils.dynamic_imports import dynamic_import


modname = "math"

try:
    # Dynamically import the module
    dynamic_import(modname)
    print(f"Module '{modname}' was imported successfully!")

    # Access and use a function from the dynamically imported module
    import math  # `math` is now in sys.modules
    result = math.sqrt(16)  # Call a simple function
    print(f"Square root of 16 is: {result}")  # Expected: 4.0
except ImportError as e:
    print(f"Error importing module '{modname}': {e}")




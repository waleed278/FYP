import json
import pickle
import numpy as np

# Initialize global variables
__name = None
__data_columns = None
__model = None

def get_estimated_price(name,engine_capacity,mileage,year):
    """
    Estimate the home price based on input parameters.
    
    Args:
    location (str): Location of the property.
    sqft (float): Total square feet area.
    bhk (int): Number of bedrooms.
    bath (int): Number of bathrooms.
    
    Returns:
    float: Estimated price of the property.
    """
    try:
        # Find the index of the location
        loc_index = __data_columns.index(name.lower())
    except ValueError:
        loc_index = -1

    # Create input array for the model
    x = np.zeros(len(__data_columns))
    x[0] = engine_capacity
    x[1] = mileage
    x[2] = year
    if loc_index >= 0:
        x[loc_index] = 1

    # Predict and return the price
    return round(__model.predict([x])[0], 2)

def get_name_names():
    """
    Get the list of available location names.

    Returns:
    list: List of location names.
    """
    return __name

def load_saved_artifacts():
    """
    Load model and data column artifacts from the artifacts folder.
    """
    print("Loading saved artifacts...start")
    global __data_columns
    global __name
    global __model

    try:
        # Load columns.json for data columns
        with open("./server/artifacts/columns1.json", 'r') as f:
            __data_columns = json.load(f)['data_columns']
            __name = __data_columns[3:]  # Extract locations from data columns

        # Load the trained model
        with open("./server/artifacts/prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)

        print("Loading saved artifacts...done")
    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the artifacts folder contains the required files.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test script
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_name_names())
    

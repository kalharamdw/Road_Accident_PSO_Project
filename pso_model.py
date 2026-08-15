import numpy as np
import pyswarms as ps

def run_pso_hotspot_ranking(df):
    # Objective function: We want PSO to find the coordinates that maximize risk
    # This is a simplified mathematical representation for the project
    
    locations = df[['Latitude', 'Longitude']].values
    risks = df['Normalized_Risk'].values
    
    def objective_function(x):
        scores = np.zeros(x.shape[0])
        for i in range(x.shape[0]):
            # Calculate distance to known high-risk points
            distances = np.linalg.norm(locations - x[i], axis=1)
            # Inverse distance weighting based on risk
            scores[i] = np.sum(risks / (distances + 1e-5)) 
        return -scores # PySwarms minimizes, so we negate to maximize risk
        
    # Set-up hyperparameters
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    
    # Call instance of PSO
    # Bounds for Sri Lanka (approx): Lat 5.9 to 9.8, Lon 79.5 to 81.8
    bounds = (np.array([5.9, 79.5]), np.array([9.8, 81.8]))
    
    optimizer = ps.single.GlobalBestPSO(n_particles=20, dimensions=2, options=options, bounds=bounds)
    
    # Perform optimization
    cost, pos = optimizer.optimize(objective_function, iters=50)
    
    return pos # Returns the highest risk predicted coordinate (Hotspot)

if __name__ == "__main__":
    print("PSO Algorithm ready.")
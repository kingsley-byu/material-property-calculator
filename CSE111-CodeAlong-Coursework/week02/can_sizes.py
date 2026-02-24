import math
def main():
    names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z",
             "#8Z short", "#10", "#211", "#300", "#303"]
    radii = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11] 
    costs = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

    best_storage_efficiency_can = "Nothing"
    best_efficiency = 0
    max_cost_efficiency = -1
    best_cost = "Nothing"
    

    for i in range(len(names)):
        name = names[i]
        radius = radii[i]
        height = heights[i]
        cost = costs[i]
        # Compute values
        volume = compute_volume(radius, height)
        surface_area = compute_area(radius, height)
        storage_efficiency = volume / surface_area
        cost_efficiency = compute_cost_efficiency(volume, cost)
        
        # Print all cans
        print(f"{name}: "
        f"Volume = {volume:.2f}, "
        f"Surface Area = {surface_area:.2f}, "
        f"Efficiency = {storage_efficiency:.3f}, " f"cost efficiency = {cost_efficiency:.2f}")
        # Check if this can has the best storage efficiency
        if storage_efficiency > best_efficiency:
            best_efficiency = storage_efficiency
            best_storage_efficiency_can = name

        if cost_efficiency >max_cost_efficiency:
            max_cost_efficiency = cost_efficiency
            best_cost = name

 
    print(f"\nThe can with best cost efficiency is {best_cost} with a cost of {max_cost_efficiency:.2f}")    
    print(f"The can with the best storage efficiency is {best_storage_efficiency_can}, with an efficiency of {best_efficiency:.3f}")
    

    # if to print it to a text file, use the code below
    #with open("file.txt", "at") as can_file:
         # print(f"\nThe can with best cost efficiency is {best_cost} with a cost of {max_cost_efficiency:.2f}", file=can_file)    
         #print(f"The can with the best storage efficiency is {best_storage_efficiency_can}, with an efficiency of {best_efficiency:.3f}", file=can_file)

            
        
        
def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency
    
main()
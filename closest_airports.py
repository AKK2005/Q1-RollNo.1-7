import math
import time
airports = {
    "Delhi": (28.5562, 77.1000),
    "Mumbai": (19.0896, 72.8656),
    "Chennai": (12.9941, 80.1709),
    "Bangalore": (13.1986, 77.7066),
    "Hyderabad": (17.2403, 78.4294),
    "Kochi": (10.1520, 76.4019)
}
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(math.radians,[lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c = 2*math.asin(math.sqrt(a))
    return R * c
start = time.perf_counter()
pairs = []
min_distance = float('inf')
closest_pair = None
airport_names = list(airports.keys())
for i in range(len(airport_names)):
    for j in range(i+1, len(airport_names)):
        a1 = airport_names[i]
        a2 = airport_names[j]
        lat1, lon1 = airports[a1]
        lat2, lon2 = airports[a2]
        dist = haversine(lat1, lon1, lat2, lon2)
        pairs.append((a1, a2, dist))
        if dist < min_distance:
            min_distance = dist
            closest_pair = (a1, a2)
end = time.perf_counter()
print("\nAIRPORT LIST")
for name,(lat,lon) in airports.items():
    print(f"{name:10} {lat:10.4f} {lon:10.4f}")
print("\nPAIR DISTANCES (km)")
for p in pairs:
    print(f"{p[0]:10} - {p[1]:10} : {p[2]:.2f} km")
print("\nCLOSEST AIRPORTS")
print("Closest Pair :", closest_pair[0], "and", closest_pair[1])
print("Minimum Distance :", round(min_distance,2),"km")
print("\nTime Complexity: O(n^2)")
print("Execution Time:", end-start,"seconds")
with open("closest_airports_output.txt","w") as f:
    f.write("AIRPORT LIST\n")
    for name,(lat,lon) in airports.items():
        f.write(f"{name} {lat} {lon}\n")
    f.write("\nPAIR DISTANCES\n")
    for p in pairs:
        f.write(f"{p[0]} - {p[1]} : {p[2]:.2f} km\n")
    f.write("\nClosest Pair: "+closest_pair[0]+" and "+closest_pair[1]+"\n")
    f.write("Minimum Distance: "+str(round(min_distance,2))+" km\n")
    f.write("\nTime Complexity: O(n^2)\n")

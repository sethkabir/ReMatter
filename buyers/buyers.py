from listings.demo_listing import listing

buyers = [
    {"name": "Small Leather Goods Co", "location": "Manchester, UK", "wants": "leather", "lat": 53.48, "lon": -2.24},
    {"name": "Accessory Makers Ltd", "location": "Leeds, UK", "wants": "leather", "lat": 53.80, "lon": -1.55},
    {"name": "Furniture Upholstery Ltd", "location": "Sheffield, UK", "wants": "leather", "lat": 53.38, "lon": -1.47},
]

def match_buyers(listing, category, buyers):
    matches = [b for b in buyers if b["wants"] == category and b["location"] == listing["location"]]
    return matches

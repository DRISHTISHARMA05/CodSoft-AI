class FlowerRecommendationSystem:
    def __init__(self):
        self.flowers = [
            {"name": "Rose", "color": "Red", "scent": "Sweet"},
            {"name": "Lily", "color": "White", "scent": "Fragrant"},
            {"name": "Tulip", "color": "Yellow", "scent": "Mild"},
            {"name": "Daisy", "color": "White", "scent": "Subtle"},
            {"name": "Sunflower", "color": "Yellow", "scent": "None"},
            {"name": "Lavender", "color": "Purple", "scent": "Aromatic"},
            {"name": "Jasmine", "color": "White", "scent": "Intense"},
            {"name": "Daffodil", "color": "Yellow", "scent": "Light"},
            {"name": "Orchid", "color": "Purple", "scent": "Exotic"},
            {"name": "Carnation", "color": "Pink", "scent": "Spicy"},
            {"name": "Peony", "color": "Pink", "scent": "Strong"},
            {"name": "Marigold", "color": "Orange", "scent": "Earthy"},
            {"name": "Hyacinth", "color": "Blue", "scent": "Fragrant"},
            {"name": "Poppy", "color": "Red", "scent": "Subtle"},
            {"name": "Chrysanthemum", "color": "Yellow", "scent": "Fresh"},
            {"name": "Iris", "color": "Purple", "scent": "Light"},
            {"name": "Anemone", "color": "White", "scent": "Delicate"},
            {"name": "Crocus", "color": "Purple", "scent": "Saffron"},
            {"name": "Gerbera", "color": "Pink", "scent": "Cheerful"},
            {"name": "Zinnia", "color": "Orange", "scent": "Vibrant"},
        ]

    def recommend_flowers(self, color_preference):
        recommended_flowers = []

        for flower in self.flowers:
            if flower["color"].lower() == color_preference.lower():
                recommended_flowers.append(flower)

        return recommended_flowers

# Create the recommendation system instance
flower_system = FlowerRecommendationSystem()

# Get user preference for flower color
color_preference = input("Enter your preferred flower color: ")

# Get flower recommendations based on user color preference
recommendations = flower_system.recommend_flowers(color_preference)

# Display the recommendations
if recommendations:
    print("Recommended flowers based on your color preference:")
    for flower in recommendations:
        print(f"- {flower['name']} (Color: {flower['color']}, Scent: {flower['scent']})")
else:
    print("No matching flowers found based on your color preference.")

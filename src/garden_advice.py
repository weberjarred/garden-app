# Hardcoded values for the season and plant type
# Code does not support any form of user interaction (Issue #1).
# → Fix: Implement user input functionality to allow users to enter the season
#        and plant type (Fix #1). → branch 'feature/allow-user-interaction'

# Code does not provide adequate mapping of advice based on the season
# and plant type and lacks readability and modularity (Issue #2).
# → Fix: Use a dictionary or object to store advice based on the season
#        and plant type, as well as enhance code readability &
#        modularity (Fix #2).
#        → branch 'feature/enhance-code-documentation'

"""
Garden Advice Application

This program offers gardening advice tailored to the current season and
plant type. Users need to specify their season and the plant type they
want to manage. The program then generates personalized gardening tips
and recommendations based on this information.
"""


def get_user_input(prompt, valid_options):
    """
    Prompt the user for input until a valid option is provided.

    Args:
        prompt (str): The text to display for input.
        valid_options (list): A list of acceptable input strings.

    Returns:
        str: The valid input entered by the user.
    """
    user_input = input(prompt).strip().lower()
    while user_input not in valid_options:
        print("Invalid input. Please choose from: "
              f"{', '.join(valid_options)}.")
        user_input = input(prompt).strip().lower()
    return user_input


def generate_advice(season, plant_type):
    """
    Generate gardening advice based on the season and plant type.

    Args:
        season (str): The current season.
        plant_type (str): The type of plant.

    Returns:
        str: A combined advice string.
    """
    # Dictionary mapping seasons to their corresponding advice
    season_advice = {
        "spring": "Prepare your garden with compost and plant early blooms.",
        "summer": "Water your plants regularly and provide some shade.",
        "autumn": "Prune dead branches and prepare for cooler weather.",
        "winter": "Protect your plants from frost with covers."
    }

    # Dictionary mapping plant types to their corresponding advice
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Harvest regularly to promote growth.",
        "tree": "Ensure adequate space and water for root expansion."
    }

    # Retrieve advice for the season; default message if season is not in
    # dictionary.
    advice_text = season_advice.get(season, "No advice for this season.")
    # Append advice for the plant type; default message if plant type is
    # not in dictionary.
    advice_text += "\n" + plant_advice.get(
        plant_type, "No advice for this type of plant.")

    return advice_text


def recommend_plants(season):
    """
    Provide plant recommendations based on the season.

    Args:
        season (str): The current season.

    Returns:
        str: Recommended plants suitable for the season.
    """
    recommendations = {
        "spring": "Consider planting tulips, daffodils, or daisies.",
        "summer": "Try growing sunflowers or marigolds.",
        "autumn": "Consider chrysanthemums or pansies.",
        "winter": "Opt for indoor plants like peace lilies or snake plants."
    }
    return recommendations.get(season, "No recommendations for this season.")


def main():
    """
    Main function that orchestrates the input, advice generation,
    and output display.
    """
    print("Welcome to the Garden Advice Program!")

    # Define valid options for season and plant type
    valid_seasons = ["spring", "summer", "autumn", "winter"]
    valid_plants = ["flower", "vegetable", "herb", "tree"]

    # Prompt the user for the current season
    season = get_user_input(
        "Enter the current season (spring, summer, autumn, winter): ",
        valid_seasons
    )
    # Prompt the user for the plant type
    plant_type = get_user_input(
            "Enter the type of plant (flower, vegetable, herb, tree): ",
            valid_plants
        )

    # Generate and display the gardening advice based on the inputs
    advice = generate_advice(season, plant_type)
    recommendations = recommend_plants(season)

    print("\nGardening Advice:")
    print(advice)

    print("\nPlant Recommendations:")
    print(recommendations)


if __name__ == "__main__":
    main()


# season = "summer"
# plant_type = "flower"

# # Variable to hold gardening advice
# advice = ""

# # Determine advice based on the season
# if season == "summer":
#     advice += "Water your plants regularly and provide some shade.\n"
# elif season == "winter":
#     advice += "Protect your plants from frost with covers.\n"
# else:
#     advice += "No advice for this season.\n"

# # Determine advice based on the plant type
# if plant_type == "flower":
#     advice += "Use fertiliser to encourage blooms."
# elif plant_type == "vegetable":
#     advice += "Keep an eye out for pests!"
# else:
#     advice += "No advice for this type of plant."

# # Print the generated advice
# print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.

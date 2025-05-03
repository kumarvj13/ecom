import json

def load_session_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def build_prompt(session):
    activity_log = []
    carted_products = []
    searched_products = 0
    purchased_products = 0

    for a in session["activities"]:
        if a["activity_type"] == "product_view":
            p = a["details"]["product_details"]
            activity_log.append(
                f"The user viewed '{p['name']}' in the '{p['category']}' category, priced at ${p['price']}."
            )
        elif a["activity_type"] == "add_to_cart":
            carted_products.append(a["details"]["product_id"])
            activity_log.append(
                f"They added product ID {a['details']['product_id']} to the cart (quantity: {a['details']['quantity']}, value: ${a['details']['cart_value']})."
            )
        elif a["activity_type"] == "search":
            searched_products += a["details"]["results_count"]
            activity_log.append(
                f"They searched for '{a['details']['search_query']}' and received {a['details']['results_count']} results."
            )

    activity_text = " ".join(activity_log)

    # Prepare session summary
    device = session['device_type']
    country = session['user_attributes']['country']
    referrer = session['user_attributes']['referrer']
    new_user = session['user_attributes']['new_user']
    conversion = session['conversion']
    total_value = session['total_value']

    session_summary = f"""
Session Summary:
- Device: {device}
- Country: {country}
- Referrer: {referrer}
- New User: {new_user}
- Conversion Completed: {conversion}
- Total Value: ${total_value}
- Activities: {activity_text}
"""

    # Categorize the journey based on conversion status
    journey_analysis = ""
    if conversion:
        journey_analysis = "This session represents a successful journey, where the user completed the purchase."
        purchased_products = len(carted_products)  # Assuming all items added to the cart were purchased
    else:
        journey_analysis = "This session represents an abandoned journey, where the user did not complete the purchase."
        abandoned_reasons = """
        The user added products to the cart but did not complete the purchase. Possible reasons could include:
        - **Cart Abandonment**: The user may have been distracted or abandoned the checkout process.
        - **Price Sensitivity**: The user might have found the prices too high or not worth the purchase.
        - **Checkout Complexity**: If the checkout process was too complex or time-consuming, the user might have decided to abandon the purchase.
        - **Lack of Preferred Payment Option**: The absence of the user’s preferred payment method could have led to abandonment.
        """
        journey_analysis += "\n" + abandoned_reasons

    # Add search vs purchase insights
    search_vs_purchase = f"Number of products searched: {searched_products}. Number of products added to cart: {len(carted_products)}."

    if len(carted_products) > 0 and purchased_products == 0:
        search_vs_purchase += " No products were purchased. This might be due to cart abandonment or a mismatch between search results and user intent."

    # Build the prompt with additional context for the model
    prompt = f"""
You are a customer behavior analyst. Based on the session summary below, write a natural-language analysis for an e-commerce business team. Your output should sound like an expert interpretation of the user’s behavior. Use complete sentences, organized into logical observations. Avoid bullets or lists.

{session_summary}

{journey_analysis}

{search_vs_purchase}

Please analyze the reasons for success or abandonment of the journey, and suggest improvements for abandoned journeys.
"""
    return prompt.strip()

def analyze_user_experience(session):
    if session['conversion']:
        return "The user had a positive experience, as they completed the purchase successfully."
    else:
        if len(session['activities']) > 0 and any(a['activity_type'] == 'add_to_cart' for a in session['activities']):
            return "The user experienced a negative journey, as they added products to the cart but did not complete the purchase. Possible reasons include cart abandonment or price sensitivity."
        else:
            return "The user did not show clear intent to purchase, as no products were added to the cart."


def generate_recommendation(session):
    if session['conversion']:
        return "Since the user made a successful purchase, consider offering personalized recommendations or loyalty rewards to increase engagement and retention."
    else:
        if len(session['activities']) > 0 and any(a['activity_type'] == 'add_to_cart' for a in session['activities']):
            return "Consider simplifying the checkout process, offering discounts, or sending follow-up reminders to encourage the user to complete their purchase."
        else:
            return "Improve product search relevance and provide better product suggestions to align with user needs."


# def generate_recommendation(session):
#     if session["conversion"]:
#         return "No action needed. Follow up with retention strategies."
#     elif any(a["activity_type"] == "add_to_cart" for a in session["activities"]):
#         return "Consider improving checkout UX or adding urgency messaging."
#     elif any(a["activity_type"] == "search" for a in session["activities"]):
#         return "Enhance search result relevance and guide users post-search."
#     return "Improve landing experience and drive interest in products."

# def build_prompt(session):
#     parts = []
#     for act in session.get("activities", []):
#         if act["activity_type"] == "product_view":
#             prod = act["details"]["product_details"]
#             parts.append(f"Viewed {prod['name']} (${prod['price']}) in {prod['category']}")
#         elif act["activity_type"] == "add_to_cart":
#             parts.append(f"Added {act['details']['product_id']} (x{act['details']['quantity']}) to cart")
#         elif act["activity_type"] == "search":
#             parts.append(f"Searched '{act['details']['search_query']}' and saw {act['details']['results_count']} results")
#
#     prompt = (
#         f"Session Details:\n"
#         f"Device: {session['device_type']}, "
#         f"Country: {session['user_attributes'].get('country')}, "
#         f"Referrer: {session['user_attributes'].get('referrer')}, "
#         f"New User: {session['user_attributes'].get('new_user')}, "
#         f"Conversion: {session.get('conversion')}, "
#         f"Total Value: {session.get('total_value')}\n"
#         f"Activities: {' | '.join(parts)}"
#     )
#     return prompt

# def analyze_user_experience(session):
#     if session["conversion"]:
#         return "Positive: The user completed a purchase successfully."
#     elif any(a["activity_type"] == "add_to_cart" for a in session["activities"]):
#         return "Mixed: Items were added to cart, but purchase not completed."
#     elif any(a["activity_type"] == "search" for a in session["activities"]):
#         return "Negative: The user searched, but found nothing engaging enough to proceed."
#     return "Negative: No strong purchase behavior observed."
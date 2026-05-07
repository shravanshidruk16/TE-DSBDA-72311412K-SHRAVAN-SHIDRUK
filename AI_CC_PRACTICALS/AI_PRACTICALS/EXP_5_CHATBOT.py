# Simple Customer Chatbot

"""
Time Complexity

For each message:

O(1) : Because only fixed conditions are checked.

Space Complexity

O(1) : Only small fixed memory is used.

"""

print("Chatbot: Hello! Welcome to Customer Support.")
print("Type 'bye' to exit.\n")

while True:

    # Take user input
    user = input("You: ").lower()

    # Greetings
    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How can I help you?")

    # Asking about products
    elif "product" in user:
        print("Chatbot: We provide laptops, mobiles, and accessories.")

    # Asking about price
    elif "price" in user:
        print("Chatbot: Prices vary depending on the product.")

    # Asking about delivery
    elif "delivery" in user:
        print("Chatbot: Delivery takes 3 to 5 business days.")

    # Exit condition
    elif user == "bye":
        print("Chatbot: Thank you! Have a nice day.")
        break

    # Default response
    else:
        print("Chatbot: Sorry, I did not understand.")
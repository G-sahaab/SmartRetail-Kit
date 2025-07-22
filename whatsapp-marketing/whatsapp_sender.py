# whatsapp_sender.py
# Simulates WhatsApp message sending using templates

def send_whatsapp_message(customer_name, template):
    message = template.replace("[Customer Name]", customer_name)
    print("\n📩 Sending WhatsApp Message:\n")
    print(message)

if __name__ == "__main__":
    customer = input("Enter customer name: ")
    print("\nSelect a message type:")
    print("1. Product Promotion\n2. New Stock Alert\n3. Festival Offer\n4. EMI Reminder")
    choice = input("Enter choice (1-4): ")

    with open("whatsapp_templates.txt", "r") as file:
        templates = file.read().split("\n\n")

    selected = templates[int(choice) - 1]
    send_whatsapp_message(customer, selected)

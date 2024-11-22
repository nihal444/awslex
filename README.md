# Hotel Booking Chatbot using Amazon Lex


## Introduction

This chatbot project is a comprehensive hotel booking system that:
- Guides users to book rooms in predefined cities.
- Collects necessary details such as user name, location, check-in date, number of nights, room type, and number of guests.
- Calculates total costs based on the selected room type and duration of stay.

---

## Setup Instructions

### Step 1: Set Up Amazon Lex

1. Log in to your AWS Management Console.
2. Navigate to **Amazon Lex** and create a new bot (e.g., `BookHotel`).
3. Set up voice support and select the desired language (e.g., English).

### Step 2: Define Intents

- Create an intent named `BookHotel`.
- Add **Sample Utterances** (e.g., "I want to book a hotel room", "Help me with hotel booking").

### Step 3: Add Slots for Booking Information

 - Define slots for collecting user inputs:
  - **Fname**: User's name.
  - **HotelLocation**: Custom slot type with supported cities (e.g., Bangalore, Pune, Goa).
  - **RoomType**: Custom slot type for room categories (Classic, Deluxe, Duplex).
  - **CheckInDate**, **NumberOfNight**, and **NumberOfGuests**.

### Step 4: Define Fulfillment

Create an AWS Lambda function to:
- Validate user inputs.
- Calculate booking cost.
- Respond with a confirmation message.

---

## Step 5: Test the Chatbot

1. Build the bot in the Amazon Lex console.
2. Test the interaction:
   - Ensure the bot prompts sequentially for all required details.
   - Verify booking confirmation details.

---

## Code Snippets

### Lambda Function
Below is an example of the Python Lambda function for validating inputs and processing bookings:

```python
import json

def lambda_handler(event, context):
    # Define slot validation logic here
    # Retrieve user inputs and calculate booking cost
    # Respond with a confirmation message
```

Refer to the full implementation in [lamda_function.py](lamda_function.py) for more details.


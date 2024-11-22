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
  ![1c](https://github.com/user-attachments/assets/3bc1f8d3-1995-4afe-b29d-3345e1952a0f)
- Add **Sample Utterances** (e.g., "I want to book a hotel room", "Help me with hotel booking").
  ![2c](https://github.com/user-attachments/assets/df3ae813-1972-4e62-80e4-31decae69cf9)

### Step 3: Add Slots for Booking Information

 - Define slots for collecting user inputs:
  - **Fname**: User's name.
  - **HotelLocation**: Custom slot type with supported cities (e.g., Bangalore, Pune, Goa).
  - **RoomType**: Custom slot type for room categories (Classic, Deluxe, Duplex).
  - **CheckInDate**, **NumberOfNight**, and **NumberOfGuests**.
    ![3c](https://github.com/user-attachments/assets/3607f2b0-f86f-4e40-83d3-5a91aaf5148e)
    ![4c](https://github.com/user-attachments/assets/eb681592-4c66-4163-8aef-e8b1ef83a68d)
    ![5c](https://github.com/user-attachments/assets/3f9037c9-91e8-4d27-b10e-59a41bb7eb4f)

### Step 4: Define Fulfillment

Create an AWS Lambda function to:
- Validate user inputs.
- Calculate booking cost.
- Respond with a confirmation message.
  ![6c](https://github.com/user-attachments/assets/087fb1ae-3b51-4467-b407-d3ba2069f859)
  ![7c](https://github.com/user-attachments/assets/ce36ce2a-b6dc-479b-a13d-d0ff0dfab348)
  ![8c](https://github.com/user-attachments/assets/72742873-7184-4771-a580-2a91d8b9ddc9)
  ![9c](https://github.com/user-attachments/assets/7aa1d1cd-91d7-4f9c-b52a-e9642920f3f9)

---

## Step 5: Test the Chatbot

1. Build the bot in the Amazon Lex console.
2. Test the interaction:
   - Ensure the bot prompts sequentially for all required details.
   - Verify booking confirmation details.
![10c](https://github.com/user-attachments/assets/7454ade2-8d8a-4e3a-8a74-de7ae43922a8)
![11c](https://github.com/user-attachments/assets/0bfdfca5-fed9-4590-92f0-1869eebddb80)
![12c](https://github.com/user-attachments/assets/cea57b46-e723-43c7-9efd-a43176880d5f)
![13c](https://github.com/user-attachments/assets/69dc6eec-aea6-4f39-9ebd-781756de31d9)

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


import json
import datetime
import time

def validate(slots):
    valid_cities = ['Bangalore', 'Pune', 'Goregaon', 'Kochi', 'Chennai', 'Lucknow', 'Goa']
    valid_room_types = ['Classic', 'Deluxe', 'Duplex']

    if not slots['HotelLocation']:
        return {
            'isValid': False,
            'violatedSlot': 'HotelLocation'
        }        
        
    if slots['HotelLocation']['value']['originalValue'].capitalize() not in valid_cities:
        return {
            'isValid': False,
            'violatedSlot': 'HotelLocation',
            'message': 'We currently support only {} as valid destinations.'.format(", ".join(valid_cities))
        }
        
    if not slots['CheckInDate']:
        return {
            'isValid': False,
            'violatedSlot': 'CheckInDate'
        }
        
    if not slots['NumberOfNight']:
        return {
            'isValid': False,
            'violatedSlot': 'NumberOfNight'
        }
        
    if not slots['RoomType']:
        return {
            'isValid': False,
            'violatedSlot': 'RoomType'
        }

    if slots['RoomType']['value']['originalValue'].capitalize() not in valid_room_types:
        return {
            'isValid': False,
            'violatedSlot': 'RoomType',
            'message': 'We have Classic, Deluxe, and Duplex room types available. Please select one of these.'
        }

    return {'isValid': True}

def lambda_handler(event, context):
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']
    validation_result = validate(slots)
    
    if event['invocationSource'] == 'DialogCodeHook':
        if not validation_result['isValid']:
            if 'message' in validation_result:
                response = {
                    "sessionState": {
                        "dialogAction": {
                            'slotToElicit': validation_result['violatedSlot'],
                            "type": "ElicitSlot"
                        },
                        "intent": {
                            'name': intent,
                            'slots': slots
                        }
                    },
                    "messages": [
                        {
                            "contentType": "PlainText",
                            "content": validation_result['message']
                        }
                    ]
                }
            else:
                response = {
                    "sessionState": {
                        "dialogAction": {
                            'slotToElicit': validation_result['violatedSlot'],
                            "type": "ElicitSlot"
                        },
                        "intent": {
                            'name': intent,
                            'slots': slots
                        }
                    }
                }
            return response
        else:
            return {
                "sessionState": {
                    "dialogAction": {
                        "type": "Delegate"
                    },
                    "intent": {
                        'name': intent,
                        'slots': slots
                    }
                }
            }
    
    if event['invocationSource'] == 'FulfillmentCodeHook':
        # Retrieve details for confirmation message
        hotel_location = slots['HotelLocation']['value']['originalValue']
        room_type = slots['RoomType']['value']['originalValue']
        check_in_date = slots['CheckInDate']['value']['originalValue']
        number_of_night = slots['NumberOfNight']['value']['originalValue']
        fname = slots['fname']['value']['originalValue']

        # Price estimation logic (placeholder)
        base_price_per_night = {
            'Classic': 100,
            'Deluxe': 150,
            'Duplex': 200
        }
        total_price = int(number_of_night) * base_price_per_night[room_type.capitalize()]

        # Fulfillment response
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    'name': intent,
                    'slots': slots,
                    'state': 'Fulfilled'
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f"Thanks {fname}, your reservation has been placed. "
                               f"You'll be staying in a {room_type} room in {hotel_location} starting on {check_in_date} "
                               f"for {number_of_night} nights. The total price is ${total_price}. Enjoy your stay!"
                }
            ]
        }
        return response

# from mitmproxy import http
# import json

# # Initialize a dictionary to hold all responses
# responses = {}

# def response(flow: http.HTTPFlow) -> None:
#     # Capture all responses from the demo.playwright.dev domain
#     if "demo.playwright.dev/api-mocking" in flow.request.pretty_url:
#         # Access the response body
#         body = flow.response.content
        
#         # Use the request URL as the key and the response body as the value
#         responses[flow.request.pretty_url] = json.loads(body)
        
#         # Save the updated responses dictionary to a file
#         save_responses()

# def save_responses():
#     try:
#         with open('api_responses.json', 'w') as file:
#             json.dump(responses, file, indent=4)
#     except Exception as e:
#         print(f"Error saving the responses: {e}")


from mitmproxy import http
import json

# Initialize a dictionary to hold all responses
responses = {}

def response(flow: http.HTTPFlow) -> None:
    # Capture all responses from the demo.playwright.dev domain
    if "demo.playwright.dev/api-mocking" in flow.request.pretty_url:
        # Access the response body
        body = flow.response.content
        
        # Use the request URL as the key and the response body as the value
        responses[flow.request.pretty_url] = json.loads(body)
        
        # Save the updated responses dictionary to a file
        save_responses()

def save_responses():
    try:
        with open('api_responses.json', 'w') as file:
            json.dump(responses, file, indent=4)
    except Exception as e:
        print(f"Error saving the responses: {e}")


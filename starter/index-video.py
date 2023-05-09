import requests
# Video id: 7d29b897b3
# Set the API key and endpoint URL
endpoint_url = 'https://api.videoindexer.ai'

# Set the request URL
request_url = '{}/{}/accounts/{}/videos/{}/index?accessToken={}'.format(
    endpoint_url,
    "WestUS",
    'account-id',
    'video-id',
    'accessToken'
    
)

# Set the request headers
headers = {
    'Ocp-Apim-Subscription-Key': 'key'
}
response = requests.get(request_url, headers=headers)

# Print the response status code and text
print('Response:', response.status_code, response.text)

import requests
# Video id: 7d29b897b3
# Set the API key and endpoint URL
endpoint_url = 'https://api.videoindexer.ai'

# Set the request URL
request_url = '{}/{}/accounts/{}/videos/{}/thumbnails/{}?accessToken={}'.format(
    endpoint_url,
    "WestUS",
    'accountid',
    'videoid',
    'thumbnailid',
    'generatedkey'
)

# Set the request headers
headers = {
    'Ocp-Apim-Subscription-Key': 'key'
}
response = requests.get(request_url, headers=headers)

# write to directory
with open ('./thumbnail.png', 'wb') as file:
    file.write(response.content)

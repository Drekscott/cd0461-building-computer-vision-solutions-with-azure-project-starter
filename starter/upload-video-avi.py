import requests
# Video id: 7d29b897b3
# Set the API key and endpoint URL
endpoint_url = 'https://api.videoindexer.ai'

# Set the video file path
video_file_path = 'starter/digital-video-sample/avkash-boarding-pass.mp4'

# Set the request URL
request_url = '{}/{}/accounts/{}/videos?name={}&accessToken={}'.format(
    endpoint_url,
    "WestUS",
    'account-id',
    'test_video',
    'generated-access-token'
    
)

# Set the request headers
headers = {
    'Ocp-Apim-Subscription-Key': 'key'
}

# Set the request body
with open(video_file_path, 'rb') as f:
    form_data = {'file': open(video_file_path, 'rb')}
    response = requests.post(request_url, headers=headers, files=form_data)

# Print the response status code and text
print('Response:', response.status_code, response.text)

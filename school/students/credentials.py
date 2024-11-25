import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class MpesaCredentials:
    consumer_key='IOiF4vOAPBmp1KBNbgyo37UeCzXZWqwQzxk6AyxoF9gFx1MC'
    consumer_secret='qSlN7bA0C1ZJqY3wiA0rvInTgeOOW3KCBj5iOnLWEgbYp2ApKPf5qQbbMpFg3BjT'
    api_url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    
    
class MpesaAccessToken:
    r = requests.get (
        MpesaCredentials.api_url,
        auth=HTTPBasicAuth(MpesaCredentials.consumer_key, MpesaCredentials.consumer_secret)
    )
    mpesa_access_token = json.loads(r.text)['access_token']
    
    
class MpesaPassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    business_short_code= '174379'
    Offsetvalue='0'  
    passkey='bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    data_to_encode = business_short_code + passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')
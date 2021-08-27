#Simple webhook sender

import requests
discord = "Webhook here"
Message = {
  "content": "Message here"
}

requests.post(discord, data=Message)

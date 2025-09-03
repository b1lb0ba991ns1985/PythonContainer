message = 'its no secret if two people knows it'
translated = ''
message_length = len(message) - 1

while message_length >= 0:
    translated += message[message_length]
    message_length -= 1

print(translated)
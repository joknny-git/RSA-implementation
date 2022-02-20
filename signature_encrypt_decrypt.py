#this function encrypts a signed message using fast modular exponentiation
#it accepts the message to authenticate, the public key, PHI, and N
#it returns an array containing the encrypted message
def sign_message(message_to_encrypt,public_key,phi,N):
    encrypted_message=[]

    for i in message_to_encrypt:
        encrypted=pow((ord(i)+phi),public_key,N)
        encrypted_message.append(encrypted)
    return(encrypted_message)

#this function authenticates received message using reverse fast modular exponentiation
#it accepts the message to authenticate, the private key, PHI, and N
#it returns an array containing the decrypted message
def authenticate_message(message_to_decrypt, private_key, phi,N):
    decrypted_message=[]

    for i in message_to_decrypt:
        decrypted=pow(i,private_key,N)-phi
        decrypted_message.append(decrypted)
    return(decrypted_message)
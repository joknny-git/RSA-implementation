#author: Julius Kwakye
print("\nRSA Keys Are Currently Being Generated")

#all the files needed are imprted here
import generate_RSA_keys
import encrypt_decrypt_message
import signature_encrypt_decrypt

#The RSA keys for encryption and decryption of both the message and the signature are generated here
N,public_key,private_key=generate_RSA_keys.generate_keys()
signPhi,sign_product,sign_public_key,sign_private=generate_RSA_keys.generate_sign_keys()

#this is the main function where everything is called upon
def main():
    global N,private_key,public_key
    #encryted messages are kept in this array
    encryptedMessages=[]
    #encryted signatures are kept in this array
    signatures=[]
    
    print("\nRSA Keys Have Been Generated.")

    choice=""
    #while loop continues until the user chooses to exit program
    while(True):
        print("\nPlease select your user type:")
        print("\t1. A public user\n\t2. The owner of the keys\n\t3. Exit program\n\nEnter your choice: ",end='')
        #accepts the users input
        choice = int(input())
        if(choice==1):
            while(True):
                publicChoice=0
                print("\nAs a public user, what would you like to do?\n\t1. Send an encrypted message\n\t2. Authenticate a digital signature\n\t3. Exit")
                print("\nEnter your choice: ",end='')
                publicChoice = int(input())
                if(publicChoice==1):
                    print("\nEnter a message: ",end='')
                    enterM=input()
                    #encryption of the users message is done here
                    encryptedMessages.append(encrypt_decrypt_message.encrypt_message(enterM,public_key,N))
                    print("Message Encrypted and Sent")
                if(publicChoice==2):
                    if not signatures:
                        print("There are no signatures to authenticate.")
                    else:
                        print("The following messages are available")
                        x=0
                        for i in signatures:
                            print(x+1,". ",i)
                            x+=1
                        print("\nEnter your choice: ",end='')
                        choice_authen=int(input())
                    #the user chooses which signature to authenticate
                        for i in signature_encrypt_decrypt.authenticate_message(signatures[choice_authen-1],sign_private,signPhi,sign_product):
                            print(chr(i),end='')
                        print(" is a Valid Signature")
                if(publicChoice!=1 and publicChoice!=2):
                    break
        if (choice==2):
            while (True):
                ownerChoice=0
                print("\nAs the owner of the keys, what would you like to do?\n\t1. Decrypt a received message\n\t2. Digitally sign a message\n\t3. Exit")
                print("\nEnter your choice: ",end='')
                ownerChoice=int(input())
                if ownerChoice == 1:
                    if not encryptedMessages:
                        print("There are no messages available")
                    else:
                        print("\nThe following messages are available")
                        x=1
                        for i in encryptedMessages:
                            print(x,end='. ( length = ')
                            print(len(i),")")
                            x+=1
                        print("\nEnter your choice: ",end='')
                        message_choice=int(input())
                        print("Decrypted Message: ",end='')
                        #prints the users original message
                        for i in encrypt_decrypt_message.decrypt_message(encryptedMessages[message_choice - 1],private_key,N):
                            print(chr(i),end='')
                    print("\n")
                if ownerChoice == 2:
                    owner_signature=""
                    print("Enter a message: ",end='')
                    owner_signature=input()
                    #the owners message is put into an array to be encrypted and decrypted later.
                    signatures.append(signature_encrypt_decrypt.sign_message(owner_signature,sign_public_key,signPhi,sign_product))
                    print("Message signed and sent")
                if ownerChoice != 1 and ownerChoice !=  2:
                    break

        if(choice!=1 and choice!=2):
            print("Bye for now!")
            break
    
main()

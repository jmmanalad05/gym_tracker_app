import json
import pwinput
import hashlib
import os

def usernameConfirmation(username):
    
    # Loading users stored in json file.
    users = loadJsonFile('user_data.json')
    
    for user in users:
        if user['username_input'] == username:
            return True
        else:
            return False

def emailConfirmation(email):
    
    # Loading users stored in json file.
    users = loadJsonFile('user_data.json')
    
    for user in users:
        if user['email_input'] == email:
            return True
        else:
            return False
    
def phoneNumberConfirmation(phone):
    
    # Loading users stored in json file.
    users = loadJsonFile('user_data.json')
    
    for user in users:
        if user['phone'] == phone:
            return True
        else:
            return False

def registerUser(firstName, lastName, email, phone, username, password, confirmPassword):  

    # Identify if entered password and confirm password are matched.
    if password == confirmPassword:
        # Identify if username has been used by other users in the system.
        if not usernameConfirmation(username):
            
            # Identify if email has been used by other users in the system.
            if not emailConfirmation(email):
                
                # Identify if phone has been used by other users in the system
                if not phoneNumberConfirmation(phone):
                    
                    # Loading json file using loadJsonFile function.
                    usersFile = loadJsonFile('user_data.json')
                    
                    # Converting json dict to json list for append feature.
                    usersFileList = list(usersFile)
                    
                    # Transform to Json file.
                    json_file = {
                        
                        "username_input": username,
                        "firstName": firstName,
                        "lastName": lastName,
                        "email_input": email,
                        "phone":phone,
                        "password": hashlib.sha256(password.encode()).hexdigest(),
                        "workout": []
                    
                    }
                    
                    # Appending users into json file.
                    usersFileList.append(json_file)
                    
                    with open('user_data.json', "w") as file:
                        json.dump(usersFileList, file, indent=4)
                    
                        print("You completed your registration succesfully!")
                    
                    return True
                    
                    
                else:
                    print(f"This {phone} has already have an account.")
            else:
                print(f"This {email} has already have an account.")
        else:
            print(f"This {username} has already have an account.")   
    else:
        return False     


def getUser(username):
    
    # Loading users stored in json file.
    users = loadJsonFile('user_data.json')
    
    for user in users:
        if user['username_input'] == username:
            return user
    
    return None    

def getLoginInput():
    
    username = input("Enter your username: ")
    password = pwinput.pwinput(prompt="Enter your password: ", mask="*")
    
    # Hash the entered password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Calling getUser function to identify username in the system.
    
    user = getUser(username)
    
    if user:
        if hashed_password == user['password']:
            print("Succesfully Logged in!")
        else:
            print("Username or password is incorrect!")
    else:
        print("Username or password is incorrect!")
        
    
def loadJsonFile(jsonFile):
    try:
        if not os.path.exists(jsonFile):
            with open(jsonFile, "w") as file:
                json.dump([], file, indent=4)
            return []

        with open(jsonFile, "r") as file:
            content = file.read().strip()

            if not content:
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        return []

def test_login_page_loads(client):

    response = client.get("/login")

    assert response.status_code == 200
    
def test_login_success(client):

    response = client.post(
        "/login",
        data={
            "username": "admin",
            "password": "Password123!"
        },
        follow_redirects=True
    )

    assert response.status_code == 200

def test_invalid_password(client):

    response = client.post(
        "/login",
        data={
            "username": "admin",
            "password": "WrongPassword"
        }
    )

    assert b"Invalid username or password" in response.data
    

def test_empty_username(client):

    response = client.post(
        "/login",
        data={
            "username": "",
            "password": "Password123!"
        }
    )

    assert b"Username is required" in response.data


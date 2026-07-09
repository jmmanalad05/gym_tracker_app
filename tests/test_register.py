"""

def test_register_page_loads(client):

    response = client.get("/register")

    assert response.status_code == 200
    
def test_successful_registration(client):

    response = client.post(
        "/register",
        data={
            "firstname": "John",
            "lastname": "Doe",
            "email": "john@test.com",
            "phone": "0400000000",
            "username": "johndoe",
            "password": "Password123!",
            "confirmPassword": "Password123!"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    
def test_password_mismatch(client):

    response = client.post(
        "/register",
        data={
            "firstname": "John",
            "lastname": "Doe",
            "email": "john@test.com",
            "phone": "0400000000",
            "username": "johndoe",
            "password": "abc123",
            "confirmPassword": "wrongpassword"
        },
        follow_redirects=True
    )

    assert b"Passwords do not match" in response.data
    
def test_duplicate_email(client):

    response = client.post(
        "/register",
        data={
            "firstname": "Jane",
            "lastname": "Doe",
            "email": "existing@test.com",
            "phone": "0400000001",
            "username": "jane",
            "password": "Password123!",
            "confirmPassword": "Password123!"
        }
    )

    assert b"Email already exists" in response.data
    
"""
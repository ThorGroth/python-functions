def create_user_profile(name=None, email=None, **kwargs):
    if not name or not email:
        return None
    
    profile = {"name": name, "email": email}
    profile.update(kwargs)
    return profile

alice = create_user_profile(name="Alice", email="alice@example.com", age=33, city="New York")
bob = create_user_profile(name="Bob", email="bob@example.com", last_name="Smith", age=22, phone_number=1234567890)
invalid_user = create_user_profile(age=25, city="Berlin")

if alice:
    print(alice)
else:
    print("Invalid user profile: Alice")

if bob:
    print(bob)
else:
    print("Invalid user profile: Bob")

if invalid_user:
    print(invalid_user)
else:
    print("Invalid user profile: Missing required fields")
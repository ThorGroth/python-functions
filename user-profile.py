def create_user_profile(**kwargs):
    profile = {}

    for key, value in kwargs.items():
        profile[key] = value

    return profile


alice = create_user_profile(name="Alice", age=33, city="New York")
bob = create_user_profile(name="Bob", last_name="Smith", age=22, phone_number=1234567890)

print(alice)
print(bob)
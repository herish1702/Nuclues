class static_data:
    url = 'http://20.96.182.140:3000/'
    email = 'admin@yopmail.com'
    password = 'Test123*'

    @classmethod
    def update_password(cls, new_password):
        cls.password = new_password
        print(f"Static Data: Password updated to: {cls.password}")
import json
import os
from cryptography.fernet import Fernet

class JSONDatabase:
    def __init__(self, table_name):
        self.table_name = table_name
        self.file_name = f'data\\{table_name}.fmdb'
        self.key_file = f'key\\{table_name}_key.key'
        
        # Load existing key or generate a new one
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                self.key = key_file.read()
        else:
            self.key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(self.key)

        self.cipher = Fernet(self.key)

        # Create table file if it doesn't exist
        if not os.path.exists(self.file_name):
            self.initialize_database()

    def initialize_database(self):
        with open(self.file_name, 'wb') as f:
            data = {'users': {}}  # Ensure 'users' key exists
            encrypted_data = self.cipher.encrypt(json.dumps(data).encode())
            f.write(encrypted_data)

    def add_user(self, username, password):
        with open(self.file_name, 'rb+') as f:
            encrypted_data = f.read()
            decrypted_data = json.loads(self.cipher.decrypt(encrypted_data).decode())

            # Ensure 'users' key exists
            if 'users' not in decrypted_data:
                decrypted_data['users'] = {}

            decrypted_data['users'][username] = password
            f.seek(0)
            encrypted_data = self.cipher.encrypt(json.dumps(decrypted_data).encode())
            f.write(encrypted_data)
            f.truncate()

    def get_users(self):
        with open(self.file_name, 'rb') as f:
            encrypted_data = f.read()
            decrypted_data = json.loads(self.cipher.decrypt(encrypted_data).decode())
            # Return the users or an empty dictionary if 'users' key doesn't exist
            return decrypted_data.get('users', {})

    def print_data(self):
        with open(self.file_name, 'rb') as f:
            encrypted_data = f.read()
            decrypted_data = json.loads(self.cipher.decrypt(encrypted_data).decode())
            print(json.dumps(decrypted_data, ensure_ascii=False, indent=4))

# Example Usage
if __name__ == "test":
    user_db = JSONDatabase('users')

    # Add users for testing
    user_db.add_user('admin', 'pass')
    user_db.add_user('yigitto0', 'AhIt8200!')

    # Print all data to verify the operation
    user_db.print_data()

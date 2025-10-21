# generate_secret.py
import secrets
import os
from pathlib import Path


def generate_secret_key():
    """Generate a secure random secret key"""
    return secrets.token_urlsafe(32)


def update_env_file(secret_key):
    """Create or update .env file with secret key"""
    env_path = Path('.') / '.env'

    # Create file if it doesn't exist
    if not env_path.exists():
        env_path.touch()

    # Read existing content
    lines = []
    if env_path.stat().st_size > 0:
        with open(env_path, 'r') as f:
            lines = f.readlines()

    # Update or add SECRET_KEY
    new_lines = []
    found = False
    for line in lines:
        if line.startswith('SECRET_KEY='):
            new_lines.append(f'SECRET_KEY={secret_key}\n')
            found = True
        else:
            new_lines.append(line)

    if not found:
        new_lines.append(f'SECRET_KEY={secret_key}\n')

    # Write back to file
    with open(env_path, 'w') as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    key = generate_secret_key()
    update_env_file(key)
    print(f"Generated and saved SECRET_KEY: {key}")
    print("Add this to your .env file if not already present")
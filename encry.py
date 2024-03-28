import os
from cryptography.fernet import Fernet


# 生成加密密钥
def generate_key():
    return Fernet.generate_key()


# 加密文件
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path + '.encrypted', 'wb') as f:
        f.write(encrypted_data)


# 解密文件
def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_path = encrypted_file_path[:-len('.encrypted')]
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)


# 加密文件夹中的所有文件
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)
            os.remove(file_path)  # 加密后删除原文件


# 解密文件夹中的所有文件
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.encrypted'):
                encrypted_file_path = os.path.join(root, file)
                decrypt_file(encrypted_file_path, key)
                os.remove(encrypted_file_path)  # 解密后删除加密文件


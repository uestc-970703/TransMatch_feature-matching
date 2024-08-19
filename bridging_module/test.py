import os

store_path = '/outputs/cut/'
file_path = os.getcwd()
file_path = file_path + store_path
print(file_path)

if not os.path.exists(file_path):
    os.makedirs(file_path)
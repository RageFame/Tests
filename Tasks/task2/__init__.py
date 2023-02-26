def generate_file_name(file_name):
    file_name = ["".join(set(name)) for name in file_name]
    max_length = max(len(name) for name in file_name)
    file_name = [name.ljust(max_length, "_") for name in file_name]
    print(file_name)

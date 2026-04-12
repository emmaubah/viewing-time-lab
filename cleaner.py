def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.
    """
    # clean_data = [float(item) for item in data if item != "minutes"]
    clean_data = []

    for item in data:
        if item != "minutes":
            clean_data.append(float(item.strip()))
    

    return clean_data

# print(clean_data(['minutes\n', '11.6\n', '14.06\n', '11.7\n', '11.41\n', '9.44\n', '11.74\n']))
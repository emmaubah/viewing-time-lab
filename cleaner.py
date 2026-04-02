def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.
    """
    cleaned = []

    for item in data:
        if item != "minutes":
            cleaned.append(float(item))
    
    return cleaned

# print(clean_data(['minutes\n', '11.6\n', '14.06\n', '11.7\n', '11.41\n', '9.44\n', '11.74\n']))
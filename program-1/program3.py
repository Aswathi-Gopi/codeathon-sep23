def is_valid_ip_address(ip_address):
    # Split the IP address into its components
    components = ip_address.split('.')

    # Check that there are exactly 4 components
    if len(components) != 4:
        return False

    # Check that each component is an integer between 0 and 255
    for component in components:
        try:
            value = int(component)
            if value < 0 or value > 255:
                return False
        except ValueError:
            return False

    return True

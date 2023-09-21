# BEGIN: abpxx6d04wxr
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
# END: abpxx6d04wxr

def test_is_valid_ip_address():
    assert is_valid_ip_address('192.168.0.1') == True
    assert is_valid_ip_address('255.255.255.0') == True
    assert is_valid_ip_address('0.0.0.0') == True
    assert is_valid_ip_address('256.0.0.0') == False
    assert is_valid_ip_address('192.168.0') == False
    assert is_valid_ip_address('192.168.0.1.2') == False
    assert is_valid_ip_address('192.168.0.-1') == False
    assert is_valid_ip_address('192.168.0.256') == False

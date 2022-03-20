def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        return pin.isnumeric()
        
    else:
        return False

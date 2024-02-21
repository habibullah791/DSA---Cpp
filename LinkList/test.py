# We are sorting the list [11, 8, 13, 13, 2, 1] using insertion sort, you need to calculate how many swaps will occur after the 4 and onward passes, 1 pass is 1 iteration through the array.
# python
def get_secret_key(public_key):
    """Generates a secret key from a public key using recursive calls."""

    print(public_key, end="")  # Print the current public key value

    if public_key < 14:
        return get_secret_key(get_secret_key(get_secret_key(public_key + 1)))
    else:
        return public_key


# Example usage:
public_key = 12
secret_key = get_secret_key(public_key)
print("Secret key:", secret_key)

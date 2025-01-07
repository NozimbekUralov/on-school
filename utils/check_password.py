from string import ascii_uppercase, ascii_lowercase, digits, punctuation


def check_pass(password: str) -> bool:
    '''
    this funtion checks password strength
    retun: true if password meets all criteries else false.
    '''

    u, l, d, p = 0, 0, 0, 0

    if len(password) > 7:
        for c in password:
            if c in ascii_uppercase: u = 1
            elif c in ascii_lowercase: l = 1
            elif c in digits: d = 1
            elif c in punctuation: p = 1
            else: return False

    return all([u, l, d, p])
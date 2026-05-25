def password_strength():
    tpass = (26 ** 2) * (10 ** 2)
    sletters = 26 * (10 ** 2)
    sdigits = (26 ** 2) * 10
    overlap = 26 * 10

    wpass = sletters + sdigits - overlap
    spass = tpass - wpass

    print("Total passwords:", tpass, "\nWeak passwords:", wpass, "\nStrong passwords:", spass)
password_strength()
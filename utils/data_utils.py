class DataSource:
    valid_testdata = [
        ("admin", "pass", "OpenEMR"),
        ("physician", "physician", "OpenEMR"),
        ("clinician", "clinician", "OpenEMR")
    ]
    invalid_testdata = [
        ("admin", "pass123", "Invalid username or password"),
        ("physician", "physician123", "Invalid username or password"),
        ("clinician123", "clinician", "Invalid username or password")
    ]
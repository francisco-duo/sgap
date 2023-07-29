def return_the_domain(students):
    if "ENF" in students or \
            "PED" in students or \
            "ADM" in students or \
            "ADS" in students or \
            "PSI" in students or \
            "DIR" in students:
        return "faculdadecci.com.br"
    elif "Téc." in students:
        return "tecscci.com.br"
    else:
        return "cciweb.com.br"

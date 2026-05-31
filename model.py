def predict_health(glucose, haemoglobin, cholesterol):

    if glucose > 125:
        return "High risk of Diabetes"

    elif cholesterol > 240:
        return "High Cholesterol Risk"

    elif haemoglobin < 12:
        return "Possible Anaemia Risk"

    else:
        return "Healthy"
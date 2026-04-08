def cluster_audience(features):

    # Simulated clustering logic

    if "fitness" in features:
        return "HealthTech Cluster"

    if "startup" in features:
        return "Entrepreneur Cluster"

    if "game" in features:
        return "Gaming Cluster"

    return "General Consumer Cluster"
def generate_persona(cluster):

    personas = {

        "HealthTech Cluster": {
            "persona": "Young Fitness Enthusiast",
            "age": "18-35"
        },

        "Entrepreneur Cluster": {
            "persona": "Startup Founder",
            "age": "22-40"
        },

        "Gaming Cluster": {
            "persona": "Competitive Gamer",
            "age": "13-28"
        }
    }

    return personas.get(cluster, {
        "persona": "Digital Consumer",
        "age": "20-45"
    })
from flask import Flask, jsonify

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/")
def homepage():
    return ""

@app.route("/rei")
def Rei():
    rei_ayanami = {
        "name": "Rei Ayanami",
        "eva": "Unit-00",
        "age": 14,
        "affiliation": "NERV",
        "role": "Pilot",
        "personality": ["calm", "detached", "mysterious"],
        "origin": "Artificial human",
        "status": "active",
        "abilities": ["high sync rate", "emotional suppression"],
        "notable_quote": "I am not afraid of dying.",
        "relationships": {
            "commander": "Gendo Ikari",
            "ally": "Shinji Ikari"
        }
    }
    return jsonify(rei_ayanami)

@app.route("/shinji")
def Shinji():
    shinji_ikari = {
        "name": "Shinji Ikari",
        "eva": "Unit-01",
        "age": 14,
        "affiliation": "NERV",
        "role": "Pilot",
        "personality": ["insecure", "sensitive", "conflicted"],
        "origin": "Human",
        "status": "active",
        "abilities": ["berserk mode", "high emotional sync"],
        "notable_quote": "I must not run away.",
        "relationships": {
            "father": "Gendo Ikari",
            "guardian": "Misato Katsuragi",
            "friends": ["Rei Ayanami", "Asuka Langley"]
        }
    }
    return jsonify(shinji_ikari)

@app.route("/asuka")
def Asuka():
    asuka_langley = {
        "name": "Asuka Langley",
        "eva": "Unit-02",
        "age": 14,
        "affiliation": "NERV",
        "role": "Pilot",
        "personality": ["proud", "aggressive", "competitive"],
        "origin": "Human",
        "status": "active",
        "abilities": ["combat skill", "strong synchronization"],
        "notable_quote": "I'm the best!",
        "relationships": {
            "rival": "Rei Ayanami",
            "ally": "Shinji Ikari"
        }
    }
    return jsonify(asuka_langley)

@app.route("/misato")
def Misato():
    misato_katsuragi = {
        "name": "Misato Katsuragi",
        "eva": None,
        "age": 29,
        "affiliation": "NERV",
        "role": "Operations Director",
        "personality": ["carefree", "strategic", "protective"],
        "origin": "Human",
        "status": "active",
        "abilities": ["tactical command", "leadership"],
        "notable_quote": "Take care of yourself.",
        "relationships": {
            "subordinate": "Shinji Ikari",
            "colleague": "Ritsuko Akagi"
        }
    }
    return jsonify(misato_katsuragi)

@app.route("/gendo")
def Gendo():
    gendo_ikari = {
        "name": "Gendo Ikari",
        "eva": None,
        "age": 48,
        "affiliation": "NERV",
        "role": "Commander",
        "personality": ["cold", "calculating", "secretive"],
        "origin": "Human",
        "status": "active",
        "abilities": ["manipulation", "long-term planning"],
        "notable_quote": "All is proceeding as planned.",
        "relationships": {
            "son": "Shinji Ikari",
            "ally": "Rei Ayanami"
        }
    }
    return jsonify(gendo_ikari)


@app.route("/kaworo")
def Kaworo():
    kaworo_nagisa = {
        "name": "Kaworu Nagisa",
        "eva": "Unit-02 (temporary)",
        "age": 15,
        "affiliation": "SEELE",
        "role": "Pilot",
        "personality": ["gentle", "philosophical", "enigmatic"],
        "origin": "Angel",
        "status": "deceased",
        "abilities": ["AT Field mastery", "levitation"],
        "notable_quote": "You are worthy of my grace.",
        "relationships": {
            "connection": "Shinji Ikari"
        }
    }
    return jsonify(kaworo_nagisa)

app.run()
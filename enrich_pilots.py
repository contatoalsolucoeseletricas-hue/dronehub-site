# -*- coding: utf-8 -*-
import json, re

def update_pilots_data():
    path = r"C:\DRONE\marketplace_app.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Define social media handles and specialties map
    pilot_updates = {
        "p_sp": {
            "add_specs": ["Câmera 360° & Tour Virtual", "Timelapse de Obras"],
            "social": {
                "instagram": "lucasandrade.drones",
                "threads": "lucasandrade.drones",
                "linkedin": "lucas-andrade-piloto",
                "facebook": "lucasdroneoficial"
            }
        },
        "p_mg": {
            "add_specs": ["Timelapse de Obras"],
            "social": {
                "instagram": "carol.mendes.drones",
                "threads": "carol.mendes.drones",
                "linkedin": "carolina-mendes-eng",
                "facebook": "carolinamendesdrones"
            }
        },
        "p_pr": {
            "add_specs": ["Câmera 360° & Tour Virtual"],
            "social": {
                "instagram": "foxsilveira.agro",
                "threads": "foxsilveira.agro",
                "linkedin": "rodrigo-silveira-agro",
                "facebook": "foxdronespr"
            }
        },
        "p_rj": {
            "add_specs": ["Câmera 360° & Tour Virtual", "Timelapse de Obras"],
            "social": {
                "instagram": "felipecinedrone",
                "threads": "felipecinedrone",
                "linkedin": "felipe-castro-cinema",
                "facebook": "felipecastroaudiovisual"
            }
        },
        "p_ba": {
            "add_specs": ["Timelapse de Obras"],
            "social": {
                "instagram": "marcelodias.drones",
                "threads": "marcelodias.drones",
                "linkedin": "marcelo-dias-topografia",
                "facebook": "marcelodiasdrones"
            }
        },
        "p_rs": {
            "add_specs": ["Câmera 360° & Tour Virtual"],
            "social": {
                "instagram": "weberdrones.sul",
                "threads": "weberdrones.sul",
                "linkedin": "guilherme-weber-drones",
                "facebook": "weberdronesrs"
            }
        },
        "p_mt": {
            "add_specs": ["Timelapse de Obras"],
            "social": {
                "instagram": "eduardo.camargo.agro",
                "threads": "eduardo.camargo.agro",
                "linkedin": "eduardo-camargo-drones",
                "facebook": "camargodronesmt"
            }
        },
        "p_go": {
            "add_specs": ["Câmera 360° & Tour Virtual"],
            "social": {
                "instagram": "thiago.souza.drone",
                "threads": "thiago.souza.drone",
                "linkedin": "thiago-souza-goias",
                "facebook": "thiagosouzadrones"
            }
        },
        "p_pe": {
            "add_specs": ["Câmera 360° & Tour Virtual", "Timelapse de Obras"],
            "social": {
                "instagram": "albuquerque.drones",
                "threads": "albuquerque.drones",
                "linkedin": "andre-albuquerque-pe",
                "facebook": "albuquerquedrones"
            }
        },
        "p_sc": {
            "add_specs": ["Câmera 360° & Tour Virtual", "Timelapse de Obras"],
            "social": {
                "instagram": "bruno.kuhn.floripa",
                "threads": "bruno.kuhn.floripa",
                "linkedin": "bruno-kuhn-drones",
                "facebook": "kuhndronessc"
            }
        },
        "p_us_fl": {
            "add_specs": ["Câmera 360° & Tour Virtual", "Timelapse de Obras"],
            "social": {
                "instagram": "dave.miller.drone",
                "threads": "dave.miller.drone",
                "linkedin": "david-miller-dronepilot",
                "facebook": "davemillerdrones"
            }
        },
        "p_us_tx": {
            "add_specs": ["Timelapse de Obras"],
            "social": {
                "instagram": "sarah.jenkins.aerial",
                "threads": "sarah.jenkins.aerial",
                "linkedin": "sarah-jenkins-drone",
                "facebook": "sarahjenkinsdrone"
            }
        },
        "p_ca_on": {
            "add_specs": ["Câmera 360° & Tour Virtual", "Timelapse de Obras"],
            "social": {
                "instagram": "alex.chen.drones",
                "threads": "alex.chen.drones",
                "linkedin": "alex-chen-aerial",
                "facebook": "alexchendronestoronto"
            }
        },
        "p_mx_cdmx": {
            "add_specs": ["Câmera 360° & Tour Virtual"],
            "social": {
                "instagram": "carlos.mendoza.drones",
                "threads": "carlos.mendoza.drones",
                "linkedin": "carlos-mendoza-rpas",
                "facebook": "carlosmendozadrones"
            }
        },
        "p_co_bog": {
            "add_specs": ["Timelapse de Obras", "Câmera 360° & Tour Virtual"],
            "social": {
                "instagram": "andres.gomez.drones",
                "threads": "andres.gomez.drones",
                "linkedin": "andres-gomez-colombia",
                "facebook": "andresgomezdrones"
            }
        }
    }

    # Match each pilot block in DEFAULT_PILOTS
    for pid, data in pilot_updates.items():
        # Look for { id: "pid", ... }
        pattern = re.compile(r'\{\s*id:\s*"' + pid + r'",(.*?)\}', re.DOTALL)
        m = pattern.search(html)
        if m:
            block = m.group(1)
            # Add specialties if not already there
            for spec in data["add_specs"]:
                if spec not in block:
                    block = block.replace('especialidades: [', f'especialidades: ["{spec}", ')
            # Add social object if not present
            if 'social:' not in block:
                social_json = json.dumps(data["social"], ensure_ascii=False)
                block += f', social: {social_json}'
            
            new_pilot_str = '{ id: "' + pid + '",' + block + ' }'
            html = html[:m.start()] + new_pilot_str + html[m.end():]
            print(f"[OK] Enriched pilot {pid}")
        else:
            print(f"[WARN] Pilot {pid} not found")

    # Add 2 new Demands in DEFAULT_DEMANDS for 360 and Timelapse
    new_demand_1 = """  {
    id: "dem_360_1",
    titulo: "Tour Virtual 360° & Fotografia Aérea de Empreendimento Residencial",
    local: "Florianópolis, SC (Brasil)",
    orcamento: "R$ 2.800",
    categoria: "Câmera 360° & Tour Virtual",
    contato: "11998765432",
    data: "Publicado há 1 hora"
  },
  {
    id: "dem_tl_1",
    titulo: "Acompanhamento em Timelapse de Obra Industrial (Galpão Logístico)",
    local: "Campinas, SP (Brasil)",
    orcamento: "R$ 6.500",
    categoria: "Timelapse de Obras",
    contato: "11998765432",
    data: "Publicado há 3 horas"
  },"""

    demands_marker = "const DEFAULT_DEMANDS = ["
    if demands_marker in html and "dem_360_1" not in html:
        html = html.replace(demands_marker, demands_marker + "\n" + new_demand_1, 1)
        print("[OK] Added 360 and Timelapse demands to DEFAULT_DEMANDS")

    # Update demands version key
    html = html.replace("dh_demands_v5", "dh_demands_v7")
    html = html.replace("dh_demands_v3", "dh_demands_v7")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("DEFAULT_PILOTS successfully updated with social media and 360/timelapse!")

if __name__ == "__main__":
    update_pilots_data()

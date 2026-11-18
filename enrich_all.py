# -*- coding: utf-8 -*-
import re, json

path = r"C:\DRONE\marketplace_app.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's locate DEFAULT_PILOTS
start_idx = text.find("const DEFAULT_PILOTS = [")
end_idx = text.find("const DEFAULT_DEMANDS = [")

if start_idx != -1 and end_idx != -1:
    pilots_block = text[start_idx:end_idx]
    
    # Let's find each pilot object
    def enrich_single_pilot(match):
        p_str = match.group(0)
        # extract name
        name_match = re.search(r'nome:\s*"([^"]+)"', p_str)
        name = name_match.group(1) if name_match else "piloto"
        slug = re.sub(r'[^a-zA-Z0-9]', '', name.lower().replace(" ", "."))
        
        # Check if social exists
        if "social:" not in p_str:
            social_dict = {
                "instagram": f"{slug}.drones",
                "threads": f"{slug}.drones",
                "linkedin": f"{slug}-dronepilot",
                "facebook": f"{slug}drones"
            }
            social_str = ", social: " + json.dumps(social_dict, ensure_ascii=False)
            p_str = p_str[:-1].rstrip() + social_str + " }"

        # If neither 360 nor timelapse, add 360 or timelapse
        if "Câmera 360°" not in p_str and "Timelapse" not in p_str:
            if "FPV" in p_str or "Topografia" in p_str:
                p_str = p_str.replace('especialidades: [', 'especialidades: ["Câmera 360° & Tour Virtual", ')
            else:
                p_str = p_str.replace('especialidades: [', 'especialidades: ["Timelapse de Obras", ')

        return p_str

    updated_block = re.sub(r'\{\s*id:\s*"[^"]+".*?\}', enrich_single_pilot, pilots_block, flags=re.DOTALL)
    text = text[:start_idx] + updated_block + text[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("All pilots in DEFAULT_PILOTS now have social media (Instagram, Threads, LinkedIn, Facebook) and 360/Timelapse!")
else:
    print("Could not find start/end idx")

import json

def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def update_proxy_list(proxie_list, config):
    
    with open(proxie_list, "r") as update:
        with open(config, "r") as arq:
            a = json.load(arq)
            
        a["proxies"] = []
        
        for proxies_urls in update:
            
            a["proxies"].append(proxies_urls.strip())
        
        with open(config, "w") as arq:
            json.dump(a, arq, indent=4)

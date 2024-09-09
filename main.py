import requests

def comprobar_user_agent(user_agent, url):
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        # Consideramos funcionales los user agents que devuelvan un código 200
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def comprobar_user_agents(archivo_user_agents, url_prueba):
    user_agents_funcionales = []
    user_agents_obsoletos = []

    with open(archivo_user_agents, 'r') as archivo:
        for linea in archivo:
            user_agent = linea.strip()
            if comprobar_user_agent(user_agent, url_prueba):
                print(f"\033[92mFuncional: {user_agent}\033[0m")  # Verde para funcionales
                user_agents_funcionales.append(user_agent)
            else:
                print(f"\033[91mObsoleto: {user_agent}\033[0m")  # Rojo para obsoletos
                user_agents_obsoletos.append(user_agent)

    # Guardar los user agents funcionales en un archivo
    with open('user_agents_funcionales.txt', 'w') as archivo_funcionales:
        for ua in user_agents_funcionales:
            archivo_funcionales.write(ua + '\n')

    # Guardar los user agents obsoletos en otro archivo
    with open('user_agents_obsoletos.txt', 'w') as archivo_obsoletos:
        for ua in user_agents_obsoletos:
            archivo_obsoletos.write(ua + '\n')

if __name__ == "__main__":
    archivo_user_agents = 'user_agents.txt'
    url_prueba = input("Ingrese la URL del sitio web a probar: ")
    comprobar_user_agents(archivo_user_agents, url_prueba)

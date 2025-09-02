import socket

ip_cible = "127.0.0.1"
# Votre liste de ports à tester
ports_a_scanner = [21, 22, 80, 443, 8080] 

print(f"Début du scan sur la cible {ip_cible}")

# On crée une boucle qui va tester chaque port de la liste, un par un
for port in ports_a_scanner:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # On attend maximum 0.5 seconde

        # On se connecte en utilisant la variable "port" qui change à chaque tour de boucle
        resultat = sock.connect_ex((ip_cible, port))

        if resultat == 0:
            print(f"Port {port} est [Ouvert]")
        # Pas besoin d'afficher les ports fermés pour l'instant pour plus de clarté
        
        sock.close()

    except socket.error as e:
        # En cas d'erreur (ex: nom d'hôte invalide), on l'affiche
        print(f"Impossible de se connecter à {ip_cible}. Erreur : {e}")
        break # On quitte la boucle si l'IP n'est pas joignable

print("Scan terminé.")

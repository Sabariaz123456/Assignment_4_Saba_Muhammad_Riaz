import pygame
import socket
import threading
import pickle
import sys
import time

# --- Game Settings ---
WIDTH, HEIGHT = 600, 600
BOX_SIZE = 50
VEL = 5
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# --- Networking ---
PORT = 5555
positions = [(50, 50), (300, 300)]

def handle_client(conn, player_id):
    conn.send(pickle.dumps(positions[player_id]))
    print(f"[SERVER] Player {player_id} connected")
    
    try:
        while True:
            data = conn.recv(2048)
            if not data:
                break
            positions[player_id] = pickle.loads(data)
            conn.send(pickle.dumps(positions[1 - player_id]))  # Send the opponent's position to the client
    except Exception as e:
        print(f"[ERROR] Player {player_id} connection lost: {e}")
    finally:
        conn.close()
        print(f"[DISCONNECT] Player {player_id} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", PORT))
    server.listen(2)
    print(f"[SERVER] Running on port {PORT}...")
    
    player_id = 0
    while player_id < 2:
        conn, addr = server.accept()
        print(f"[SERVER] Player {player_id} connected from {addr}")
        thread = threading.Thread(target=handle_client, args=(conn, player_id))
        thread.start()
        player_id += 1
    server.close()
    print("[SERVER] Server is shutting down.")

def run_client(server_ip):
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Multiplayer Game")

    clock = pygame.time.Clock()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((server_ip, PORT))
        print("[CLIENT] Connected to server.")
    except Exception as e:
        print(f"[ERROR] Cannot connect to server: {e}")
        sys.exit()

    player = pickle.loads(client.recv(2048))

    run = True
    while run:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player = (player[0] - VEL, player[1])
        if keys[pygame.K_RIGHT]: player = (player[0] + VEL, player[1])
        if keys[pygame.K_UP]: player = (player[0], player[1] - VEL)
        if keys[pygame.K_DOWN]: player = (player[0], player[1] + VEL)

        try:
            client.send(pickle.dumps(player))
            opponent = pickle.loads(client.recv(2048))
        except:
            print("[ERROR] Connection lost. Exiting...")
            break

        win.fill(WHITE)
        pygame.draw.rect(win, RED, (*player, BOX_SIZE, BOX_SIZE))
        pygame.draw.rect(win, BLUE, (*opponent, BOX_SIZE, BOX_SIZE))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

# --- Main Entry ---
def main():
    print("Welcome to the Multiplayer Game!")
    print("Choose mode:")
    print("1 - Start Server")
    print("2 - Start Client")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        print("[SERVER] Starting the server...")
        start_server()
    elif choice == "2":
        ip = input("Enter Server IP (127.0.0.1 for local, or the server's IP): ").strip()
        print(f"[CLIENT] Connecting to {ip}...")
        run_client(ip)
    else:
        print("[ERROR] Invalid choice. Please select either 1 or 2.")

if __name__ == "__main__":
    main()

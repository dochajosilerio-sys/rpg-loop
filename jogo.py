import time
import random

def iniciar_jogo():
    print("--- BEM-VINDO AO LOOP INFINITO ---")
    nome = input("Qual o nome do seu herói? ")
    
    vida = 100
    ataque = 10
    xp = 0
    loop_atual = 1
    
    while vida > 0:
        print(f"\n--- LOOP {loop_atual} ---")
        print(f"Herói: {nome} | Vida: {vida} | Ataque: {ataque} | XP: {xp}")
        time.sleep(1)
        
        # Encontro com inimigo
        monstro_vida = 20 + (loop_atual * 5)
        monstro_ataque = 5 + (loop_atual * 2)
        
        print(f"Um monstro de nível {loop_atual} apareceu! (Vida: {monstro_vida})")
        
        # Sistema de Batalha Simples
        while monstro_vida > 0 and vida > 0:
            monstro_vida -= ataque
            if monstro_vida > 0:
                vida -= monstro_ataque
                print(f"Você atacou! Monstro vida: {monstro_vida}")
            else:
                print("Você derrotou o monstro!")
                xp += 10 * loop_atual
                # Evolução do Herói
                ataque += 2
                vida += 10 # Recupera um pouco de vida
                loop_atual += 1
                
        if vida <= 0:
            print(f"\nGAME OVER! {nome} caiu no Loop {loop_atual}.")
            print(f"Total de XP acumulado: {xp}")

if __name__ == "__main__":
    iniciar_jogo()


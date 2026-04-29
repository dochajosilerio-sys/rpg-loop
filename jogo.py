import time
import random

def escolher_classe():
    print("\n--- ESCOLHA SUA CLASSE ---")
    print("1. Guerreiro (Vida: 150, Ataque: 12)")
    print("2. Mago (Vida: 80, Ataque: 25)")
    escolha = input("Digite o número da classe: ")
    
    if escolha == "1":
        return {"classe": "Guerreiro", "vida": 150, "ataque": 12}
    else:
        return {"classe": "Mago", "vida": 80, "ataque": 25}

def mostrar_ranking(loop):
    print("\n" + "="*30)
    print("      RANKING FINAL")
    print("="*30)
    if loop < 10:
        print("Classificação: Recruta de Python 🪵")
    elif loop < 20:
        print("Classificação: Aventureiro de Dados ⚔️")
    elif loop < 30:
        print("Classificação: MESTRE DO LOOP 👑")
    else:
        print("Classificação: LENDA DO BACK-END 🌌")
    print("="*30)

def iniciar_jogo():
    print("--- BEM-VINDO AO LOOP INFINITO v4.0 ---")
    nome = input("Qual o nome do seu herói? ")
    
    dados = escolher_classe()
    vida = dados["vida"]
    ataque = dados["ataque"]
    xp = 0
    loop_atual = 1
    
    while vida > 0:
        print(f"\n--- LOOP {loop_atual} ---")
        print(f"Herói: {nome} ({dados['classe']}) | Vida: {vida} | Ataque: {ataque}")
        time.sleep(1)
        
        monstro_vida = 20 + (loop_atual * 6)
        monstro_ataque = 5 + (loop_atual * 2)
        
        print(f"Um monstro de nível {loop_atual} apareceu! (Vida: {monstro_vida})")
        
        while monstro_vida > 0 and vida > 0:
            sorte = random.randint(1, 100)
            dano_final = ataque
            
            if sorte > 80:
                dano_final = ataque * 2
                print(f"🔥 CRÍTICO! Você causou {dano_final} de dano!")
            else:
                print(f"Você atacou! Dano: {dano_final}")
            
            monstro_vida -= dano_final
            
            if monstro_vida > 0:
                vida -= monstro_ataque
                print(f"O monstro revidou! Sua vida: {vida}")
            else:
                print("✨ Você derrotou o monstro!")
                xp += 10 * loop_atual
                ataque += 3
                vida += 25 
                loop_atual += 1
                
        if vida <= 0:
            print(f"\n💀 GAME OVER! O {dados['classe']} {nome} caiu no Loop {loop_atual}.")
            print(f"XP Total: {xp}")
            mostrar_ranking(loop_atual)

if __name__ == "__main__":
    iniciar_jogo()







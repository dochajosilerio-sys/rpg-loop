import time
import random

def escolher_classe():
    print("\n--- SELEÇÃO DE UNIDADE (UDF) ---")
    print("1. William Cage (Vida: 180, Ataque: 10) - Tom Cruise")
    print("2. Rita Vrataski (Vida: 100, Ataque: 30) - Emily Blunt")
    escolha = input("Escolha sua unidade: ")
    
    if escolha == "1":
        return {"classe": "William Cage", "vida": 180, "ataque": 10}
    else:
        return {"classe": "Rita Vrataski", "vida": 100, "ataque": 30}

def mostrar_ranking(loop):
    print("\n" + "="*35)
    print("      RELATÓRIO DE COMBATE")
    print("="*35)
    if loop < 10:
        print("Status: Recruta Desorientado 🪵")
    elif loop < 20:
        print("Status: Soldado da Resistência ⚔️")
    elif loop < 30:
        print("Status: O ANJO DE VERDUN 👑")
    else:
        print("Status: MESTRE DO RESET TEMPORAL 🌌")
    print("="*35)

def iniciar_jogo():
    print("--- NO LIMITE DO AMANHÃ: SIMULADOR DE COMBATE ---")
    nome = "Josilerio" 
    
    dados = escolher_classe()
    vida = dados["vida"]
    ataque = dados["ataque"]
    xp = 0
    loop_atual = 1
    
    while vida > 0:
        print(f"\n--- RESET TEMPORAL Nº {loop_atual} ---")
        print(f"Unidade: {dados['classe']} | Integridade: {vida} | Força: {ataque}")
        time.sleep(1)
        
        monstro_vida = 25 + (loop_atual * 7)
        monstro_ataque = 6 + (loop_atual * 2)
        
        print(f"🚨 Alerta! Mimic detectado! (Energia: {monstro_vida})")
        
        while monstro_vida > 0 and vida > 0:
            sorte = random.randint(1, 100)
            if sorte > 80:
                dano_final = ataque * 2
                print(f"🔥 CONTRA-ATAQUE CRÍTICO! Dano: {dano_final}")
            else:
                dano_final = ataque
                print(f"Você disparou seu exotraje! Dano: {dano_final}")
            
            monstro_vida -= dano_final
            
            if monstro_vida > 0:
                vida -= monstro_ataque
                print(f"O Mimic atingiu você! Integridade: {vida}")
            else:
                print("✨ Mimic neutralizado! Coletando dados de memória...")
                xp += 15 * loop_atual
                ataque += 4 
                vida += 20 
                loop_atual += 1
                
        if vida <= 0:
            print(f"\n💀 VOCÊ MORREU! {dados['classe']} {nome} caiu no Loop {loop_atual}.")
            print("Reiniciando dia em 3... 2... 1...")
            mostrar_ranking(loop_atual)

if __name__ == "__main__":
    iniciar_jogo()








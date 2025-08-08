def main():
    material_rad = float(input(f"qual é o valor da massa ? "))
    massa_inicial = material_rad
    tempo = 0 
    while material_rad > 0.05:
        material_rad/=2
        tempo += 50
    hora = tempo // 3600
    minuto = (tempo%3600) // 60
    segundo = tempo% 60
    tempo_total=(f"{hora}h{ minuto}m{segundo}s")
    print(f"essa e a massa inicial: {massa_inicial}")
    print(f"essa e a massa final: {material_rad :.2f}")
    print(f"essa e a tempo total: {tempo_total}")
main()
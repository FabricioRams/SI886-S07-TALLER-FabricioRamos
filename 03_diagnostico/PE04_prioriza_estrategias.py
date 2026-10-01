# -*- coding: utf-8 -*-
"""
PE04_prioriza_estrategias.py - Priorizacion Cuantitativa de Estrategias Cruzadas
Curso: SI-886 Planeamiento Estrategico de TI
Semana 07 - Taller de Laboratorio
Universidad Privada de Tacna - EPIS
Docente: Dr. Oscar Juan Jimenez Flores
Estudiante: Fabricio Ramos
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    foda_path = os.path.join(base_dir, "PE03_foda_cruzado.csv")
    efi_path = os.path.join(base_dir, "PE02_matriz_efi.csv")
    efe_path = os.path.join(base_dir, "PE02_matriz_efe.csv")
    
    e = pd.read_csv(foda_path)
    efi = pd.read_csv(efi_path).set_index("id")
    efe = pd.read_csv(efe_path).set_index("id")
    
    # Combinar serie de pesos de factores
    pesos = pd.concat([efi["peso"], efe["peso"]])
    
    def peso_estrategia(fs):
        factores = [f.strip() for f in fs.replace("+", " ").split()]
        return round(sum(pesos.get(f, 0.0) for f in factores), 3)
    
    e["peso_factores"] = e["Factores cruzados"].apply(peso_estrategia)
    
    # Bonificacion estrategica: supervivencia y defensa primero
    # DA: 1.35 (critico), FA: 1.20, DO: 1.10, FO: 1.00
    BONO = {"DA": 1.35, "FA": 1.20, "DO": 1.10, "FO": 1.00}
    e["bono"] = e["Tipo"].map(BONO)
    e["puntaje"] = (e["peso_factores"] * e["bono"]).round(3)
    
    # Ordenar por puntaje descendente
    e = e.sort_values("puntaje", ascending=False).reset_index(drop=True)
    e["ranking"] = e.index + 1
    
    # Exportar archivo CSV priorizado
    out_csv = os.path.join(base_dir, "PE04_estrategias_priorizadas.csv")
    cols_order = ["ranking", "id", "Tipo", "Factores cruzados", "peso_factores", "bono", "puntaje", "Objetivo al que apunta", "Proyecto candidato"]
    e[cols_order].to_csv(out_csv, index=False)
    
    # Generar salida textual formateada
    out_lines = []
    out_lines.append("=" * 90)
    out_lines.append("TALLER 07 · RESULTADOS DE LA PRIORIZACION CUANTITATIVA DE ESTRATEGIAS (FODA CRUZADO)")
    out_lines.append("=" * 90)
    out_lines.append(f"{'Rnk':<4} | {'ID':<5} | {'Tipo':<5} | {'Factores':<14} | {'Peso Fact':<10} | {'Bono':<5} | {'Puntaje':<8} | {'Proyecto Candidato':<35}")
    out_lines.append("-" * 90)
    for _, r in e.iterrows():
        p_name = (r['Proyecto candidato'][:32] + '...') if len(r['Proyecto candidato']) > 35 else r['Proyecto candidato']
        out_lines.append(f"{r['ranking']:<4} | {r['id']:<5} | {r['Tipo']:<5} | {r['Factores cruzados']:<14} | {r['peso_factores']:<10.3f} | {r['bono']:<5.2f} | {r['puntaje']:<8.3f} | {p_name:<35}")
    out_lines.append("-" * 90)
    
    out_lines.append("\nDISTRIBUCION DE ESTRATEGIAS POR TIPO Y CUADRANTE:")
    dist = e["Tipo"].value_counts()
    for tipo, cnt in dist.items():
        out_lines.append(f"  - {tipo}: {cnt} estrategias ({cnt/len(e)*100:.1f}%)")
        
    out_lines.append("\nINTERPRETACION ESTRATEGICA DEL RANKING:")
    top_tipo = e.head(4)["Tipo"].value_counts().to_dict()
    out_lines.append(f"  En el Top 4 de maxima prioridad predominan las estrategias: {top_tipo}.")
    out_lines.append("  -> Como predominan las estrategias DA y FA en la cima del ranking, la organizacion se encuentra en")
    out_lines.append("    una POSICION ESTRATEGICA DEFENSIVA Y DE SUPERVIVENCIA.")
    out_lines.append("  -> Mandato ineludible para el PETI:")
    out_lines.append("    1. Atender primero la continuidad operativa ante el fin de soporte del ERP (E-05, E-12).")
    out_lines.append("    2. Resolver la contingencia legal por la entrada del Reglamento de Proteccion de Datos (E-11).")
    out_lines.append("    3. Mitigar la personodependencia del unico programador institucional (E-10).")
    out_lines.append("    4. Sanear el costo critico del despacho mediante optimizacion logistica (E-09).")
    out_lines.append("    Solo una vez blindada la estabilidad y continuidad se ejecutaran las estrategias FO de expansion digital.")
    out_lines.append("=" * 90)
    
    report_text = "\n".join(out_lines)
    print(report_text)
    
    # Guardar archivo de salida de texto
    out_dir = os.path.join(base_dir, "..", "docs", "evidencias", "S07", "salidas")
    os.makedirs(out_dir, exist_ok=True)
    out_txt_file = os.path.join(out_dir, "salida_priorizacion.txt")
    with open(out_txt_file, "w", encoding="utf-8") as f:
        f.write(report_text)
    print(f"\n[OK] Salida de priorizacion guardada en: {out_txt_file}")
    print(f"[OK] Archivo CSV priorizado guardado en: {out_csv}")
    
    # Generar grafico de barras de priorizacion
    graficos_dir = os.path.join(base_dir, "..", "graficos")
    os.makedirs(graficos_dir, exist_ok=True)
    fig_path = os.path.join(graficos_dir, "priorizacion_estrategias.png")
    
    plt.figure(figsize=(12, 6))
    colors = {"DA": "#d62728", "FA": "#ff7f0e", "DO": "#1f77b4", "FO": "#2ca02c"}
    bar_colors = [colors[t] for t in e["Tipo"]]
    
    bars = plt.barh(e["id"] + " (" + e["Tipo"] + ")", e["puntaje"], color=bar_colors)
    plt.gca().invert_yaxis()
    plt.title("Ranking de Priorizacion Cuantitativa de Estrategias FODA Cruzado · DISUR S.A.C.", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Puntaje Ponderado Ajustado por Bono de Supervivencia", fontsize=11)
    plt.ylabel("Estrategia y Cuadrante", fontsize=11)
    
    # Anotar valores en las barras
    for bar in bars:
        w = bar.get_width()
        plt.text(w + 0.005, bar.get_y() + bar.get_height()/2, f"{w:.3f}", va='center', fontsize=9, fontweight='bold')
        
    # Leyenda personalizada
    import matplotlib.patches as mpatches
    legend_patches = [
        mpatches.Patch(color='#d62728', label='DA (Supervivencia - Bono 1.35)'),
        mpatches.Patch(color='#ff7f0e', label='FA (Defensiva - Bono 1.20)'),
        mpatches.Patch(color='#1f77b4', label='DO (Reorientacion - Bono 1.10)'),
        mpatches.Patch(color='#2ca02c', label='FO (Crecimiento - Bono 1.00)')
    ]
    plt.legend(handles=legend_patches, loc='lower right', framealpha=0.9)
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(fig_path, dpi=300)
    plt.close()
    print(f"[OK] Grafico de priorizacion guardado en: {fig_path}")

if __name__ == "__main__":
    main()

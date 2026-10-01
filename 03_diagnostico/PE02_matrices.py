# -*- coding: utf-8 -*-
"""
PE02_matrices.py - Calculo y Analisis de las Matrices EFI y EFE
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
    efi_path = os.path.join(base_dir, "PE02_matriz_efi.csv")
    efe_path = os.path.join(base_dir, "PE02_matriz_efe.csv")
    
    # 1. Cargar datos
    efi = pd.read_csv(efi_path)
    efe = pd.read_csv(efe_path)
    
    # 2. Calculo de ponderados
    efi["ponderado"] = (efi["peso"] * efi["calificacion"]).round(3)
    efe["ponderado"] = (efe["peso"] * efe["calificacion"]).round(3)
    
    # 3. Sumatorias
    sum_peso_efi = round(efi["peso"].sum(), 3)
    sum_pond_efi = round(efi["ponderado"].sum(), 3)
    
    sum_peso_efe = round(efe["peso"].sum(), 3)
    sum_pond_efe = round(efe["ponderado"].sum(), 3)
    
    # 4. Generar reporte textual
    output_lines = []
    output_lines.append("=" * 80)
    output_lines.append("TALLER 07 · EVALUACION DE FACTORES INTERNOS Y EXTERNOS (MATRICES EFI Y EFE)")
    output_lines.append("Organizacion: Distribuidora Mayorista del Sur S.A.C. (DISUR S.A.C.)")
    output_lines.append("=" * 80)
    output_lines.append("\n[1] MATRIZ DE EVALUACION DE FACTORES INTERNOS (EFI)")
    output_lines.append("-" * 80)
    output_lines.append(f"{'ID':<5} | {'Factor':<48} | {'Peso':<6} | {'Calif':<5} | {'Pond':<6}")
    output_lines.append("-" * 80)
    for _, r in efi.iterrows():
        f_name = (r['factor'][:45] + '...') if len(r['factor']) > 48 else r['factor']
        output_lines.append(f"{r['id']:<5} | {f_name:<48} | {r['peso']:<6.3f} | {r['calificacion']:<5} | {r['ponderado']:<6.3f}")
    output_lines.append("-" * 80)
    output_lines.append(f"TOTAL PESO: {sum_peso_efi:.3f} (Validacion suma = 1.0: {'OK' if sum_peso_efi == 1.0 else 'ERROR'})")
    output_lines.append(f"TOTAL PONDERADO EFI: {sum_pond_efi:.3f} / 4.000")
    
    # Interpretacion EFI
    if sum_pond_efi < 2.5:
        interp_efi = (
            f"El total ponderado ({sum_pond_efi:.3f}) se situa por DEBAJO del promedio neutral (2.500).\n"
            "Diagnostico: La organizacion presenta una POSICION INTERNA DEBIL / VULNERABLE.\n"
            "Las debilidades operativas (ruteo manual en Excel, dependencia critica de un unico desarrollador,\n"
            "ausencia de capacidades analiticas y falta de politicas de datos) superan el valor de sus fortalezas.\n"
            "El PETI debe priorizar el saneamiento y estabilizacion de procesos de TI antes de emprender iniciativas expansivas."
        )
    else:
        interp_efi = f"El total ponderado ({sum_pond_efi:.3f}) es superior al promedio (2.500), reflejando una posicion interna fuerte."
    output_lines.append(f"\nInterpretacion EFI:\n{interp_efi}\n")
    
    output_lines.append("\n" + "=" * 80)
    output_lines.append("[2] MATRIZ DE EVALUACION DE FACTORES EXTERNOS (EFE)")
    output_lines.append("-" * 80)
    output_lines.append(f"{'ID':<5} | {'Factor':<48} | {'Peso':<6} | {'Calif':<5} | {'Pond':<6}")
    output_lines.append("-" * 80)
    for _, r in efe.iterrows():
        f_name = (r['factor'][:45] + '...') if len(r['factor']) > 48 else r['factor']
        output_lines.append(f"{r['id']:<5} | {f_name:<48} | {r['peso']:<6.3f} | {r['calificacion']:<5} | {r['ponderado']:<6.3f}")
    output_lines.append("-" * 80)
    output_lines.append(f"TOTAL PESO: {sum_peso_efe:.3f} (Validacion suma = 1.0: {'OK' if sum_peso_efe == 1.0 else 'ERROR'})")
    output_lines.append(f"TOTAL PONDERADO EFE: {sum_pond_efe:.3f} / 4.000")
    
    # Interpretacion EFE
    if sum_pond_efe < 2.5:
        interp_efe = (
            f"El total ponderado ({sum_pond_efe:.3f}) se ubica significativamente por DEBAJO del promedio (2.500).\n"
            "Diagnostico: La organizacion demuestra una RESPUESTA DEFICIENTE O INEFICAZ ante el entorno externo.\n"
            "A pesar de que existen oportunidades latentes claras (penetracion de smartphones, soluciones SaaS y talento regional),\n"
            "la empresa no cuenta con canales ni herramientas para capitalizarlas, encontrandose seriamente expuesta ante\n"
            "el fin de soporte de su ERP, las fiscalizaciones punitivas de la ANPD y la fuga de capital humano tecnico."
        )
    else:
        interp_efe = f"El total ponderado ({sum_pond_efe:.3f}) supera el promedio (2.500), evidenciando una respuesta sobresaliente al entorno."
    output_lines.append(f"\nInterpretacion EFE:\n{interp_efe}\n")
    
    output_lines.append("=" * 80)
    output_lines.append("SINTESIS DE POSICIONAMIENTO ESTRATEGICO (MATRIZ INTERNA-EXTERNA / IE)")
    output_lines.append(f"Coordenada Estrategica: (EFI={sum_pond_efi:.3f}, EFE={sum_pond_efe:.3f})")
    output_lines.append("Cuadrante de Destino: Cuadrante VIII / IX (Retener y Mantener / Cosechar o Desinvertir)")
    output_lines.append("Postura Estrategica Obligatoria: DEFENSIVA Y DE SUPERVIVENCIA.")
    output_lines.append("Implicancia para el PETI: Prohibido priorizar proyectos de transformacion o adquisicion agresiva sin antes")
    output_lines.append("resolver la continuidad operativa (migracion ERP, backup), el cumplimiento legal (ANPD) y la personodependencia.")
    output_lines.append("=" * 80)
    
    report_text = "\n".join(output_lines)
    print(report_text)
    
    # Guardar en archivo de salida
    out_dir = os.path.join(base_dir, "..", "docs", "evidencias", "S07", "salidas")
    os.makedirs(out_dir, exist_ok=True)
    out_txt_file = os.path.join(out_dir, "salida_matrices.txt")
    with open(out_txt_file, "w", encoding="utf-8") as f:
        f.write(report_text)
    print(f"\n[OK] Reporte guardado exitosamente en: {out_txt_file}")
    
    # 5. Generar grafico de Posicionamiento Estrategico con matplotlib
    graficos_dir = os.path.join(base_dir, "..", "graficos")
    os.makedirs(graficos_dir, exist_ok=True)
    fig_path = os.path.join(graficos_dir, "posicion_estrategica_efi_efe.png")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Subplot 1: Matriz IE
    ax1.set_xlim(1.0, 4.0)
    ax1.set_ylim(1.0, 4.0)
    ax1.axvline(2.0, color='gray', linestyle='--', alpha=0.6)
    ax1.axvline(3.0, color='gray', linestyle='--', alpha=0.6)
    ax1.axhline(2.0, color='gray', linestyle='--', alpha=0.6)
    ax1.axhline(3.0, color='gray', linestyle='--', alpha=0.6)
    ax1.axvline(2.5, color='red', linestyle=':', alpha=0.5, label='Media neutral (2.5)')
    ax1.axhline(2.5, color='red', linestyle=':', alpha=0.5)
    
    # Marcar regiones
    ax1.text(1.5, 3.5, "Crecer y\nConstruir", ha='center', va='center', fontsize=9, color='green', alpha=0.7)
    ax1.text(3.5, 3.5, "Crecer y\nConstruir", ha='center', va='center', fontsize=9, color='green', alpha=0.7)
    ax1.text(2.5, 2.7, "Retener y\nMantener", ha='center', va='center', fontsize=9, color='orange', alpha=0.7)
    ax1.text(1.5, 1.5, "Cosechar o\nDesinvertir\n(Defensivo)", ha='center', va='center', fontsize=9, color='crimson', alpha=0.7)
    
    ax1.scatter([sum_pond_efi], [sum_pond_efe], color='darkblue', s=200, zorder=5, label=f'DISUR ({sum_pond_efi:.2f}, {sum_pond_efe:.2f})')
    ax1.set_title("Matriz Interna-Externa (IE) · DISUR S.A.C.", fontsize=12, fontweight='bold', pad=12)
    ax1.set_xlabel("Puntaje Ponderado EFI (Fortalezas / Debilidades Internas)", fontsize=10)
    ax1.set_ylabel("Puntaje Ponderado EFE (Capacidad de Respuesta Externa)", fontsize=10)
    ax1.legend(loc='upper left')
    ax1.grid(True, linestyle='--', alpha=0.3)
    
    # Subplot 2: Distribucion de pesos por factor
    all_factors = []
    for _, r in efi.iterrows():
        all_factors.append({'id': r['id'], 'peso': r['peso'], 'tipo': 'Fortaleza' if r['id'].startswith('F') else 'Debilidad'})
    for _, r in efe.iterrows():
        all_factors.append({'id': r['id'], 'peso': r['peso'], 'tipo': 'Oportunidad' if r['id'].startswith('O') else 'Amenaza'})
    df_factors = pd.DataFrame(all_factors)
    
    colors = {'Fortaleza': '#2ca02c', 'Debilidad': '#d62728', 'Oportunidad': '#1f77b4', 'Amenaza': '#ff7f0e'}
    bar_colors = [colors[t] for t in df_factors['tipo']]
    
    ax2.barh(df_factors['id'], df_factors['peso'], color=bar_colors)
    ax2.set_title("Ponderacion Relativa de Factores Estrategicos (EFI & EFE)", fontsize=12, fontweight='bold', pad=12)
    ax2.set_xlabel("Peso Asignado (Suma = 1.0 por matriz)", fontsize=10)
    ax2.invert_yaxis()
    ax2.grid(True, axis='x', linestyle='--', alpha=0.4)
    
    plt.tight_layout()
    plt.savefig(fig_path, dpi=300)
    plt.close()
    print(f"[OK] Grafico de posicionamiento estrategico generado en: {fig_path}")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
genera_anexos.py - Generador automatico de anexos XLSX y graficos para el informe
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    diag_dir = os.path.join(root_dir, "03_diagnostico")
    
    # 1. Anexo A: PESTEL
    df_pestel = pd.read_csv(os.path.join(diag_dir, "PE01_pestel.csv"))
    anexo_a_path = os.path.join(root_dir, "anexo_A_pestel.xlsx")
    df_pestel.to_excel(anexo_a_path, index=False, sheet_name="Analisis_PESTEL")
    print(f"[OK] Generado: {anexo_a_path}")
    
    # 2. Anexo B: Matrices EFI y EFE
    df_efi = pd.read_csv(os.path.join(diag_dir, "PE02_matriz_efi.csv"))
    df_efe = pd.read_csv(os.path.join(diag_dir, "PE02_matriz_efe.csv"))
    df_efi["ponderado"] = (df_efi["peso"] * df_efi["calificacion"]).round(3)
    df_efe["ponderado"] = (df_efe["peso"] * df_efe["calificacion"]).round(3)
    
    anexo_b_path = os.path.join(root_dir, "anexo_B_matrices_efi_efe.xlsx")
    with pd.ExcelWriter(anexo_b_path, engine="openpyxl") as writer:
        df_efi.to_excel(writer, index=False, sheet_name="Matriz_EFI")
        df_efe.to_excel(writer, index=False, sheet_name="Matriz_EFE")
    print(f"[OK] Generado: {anexo_b_path}")
    
    # 3. Anexo C: Grafico FODA Cruzado
    anexo_c_path = os.path.join(root_dir, "anexo_C_foda_cruzado.png")
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.axis("off")
    
    # Titulo
    plt.suptitle("MATRIZ FODA CRUZADO · 12 ESTRATEGIAS DERIVADAS\nDistribuidora Mayorista del Sur S.A.C. (DISUR S.A.C.)", fontsize=14, fontweight="bold", y=0.96)
    
    # Dibujar 4 cuadrantes
    bbox_props_fo = dict(boxstyle="round,pad=0.6", facecolor="#e8f5e9", edgecolor="#2e7d32", lw=2)
    bbox_props_fa = dict(boxstyle="round,pad=0.6", facecolor="#fff3e0", edgecolor="#ef6c00", lw=2)
    bbox_props_do = dict(boxstyle="round,pad=0.6", facecolor="#e3f2fd", edgecolor="#1565c0", lw=2)
    bbox_props_da = dict(boxstyle="round,pad=0.6", facecolor="#ffebee", edgecolor="#c62828", lw=2)
    
    text_fo = (
        "CUADRANTE FO (Crecimiento / Ataque)\n"
        "• E-01 (F2+O1+O2): Canal Digital B2B Movil con Motor de Recomendacion\n"
        "   Puntaje: 0.350 | Proy: App Movil B2B con analitica predictiva SaaS\n\n"
        "• E-02 (F1+O4): Ruteo Dinamico y Despacho Macro-Sur\n"
        "   Puntaje: 0.240 | Proy: Sistema de ruteo inteligente y consolidacion\n\n"
        "• E-03 (F4+O5): Integracion Transaccional de Pagos Digitales\n"
        "   Puntaje: 0.160 | Proy: Pasarela de interoperabilidad y conciliacion bancaria"
    )
    
    text_fa = (
        "CUADRANTE FA (Defensiva / Diferenciacion)\n"
        "• E-04 (F1+A1): Trazabilidad GPS y Entrega Verificada en 24h\n"
        "   Puntaje: 0.312 | Proy: Portal de trazabilidad y Proof of Delivery\n\n"
        "• E-05 (F4+A2): Migracion y Modernizacion de ERP a la Nube [CRITICO]\n"
        "   Puntaje: 0.276 | Proy: Reemplazo de servidor obsoleto por ERP Cloud\n\n"
        "• E-06 (F2+A4): Planificacion de Compras y Cobertura Cambiaria\n"
        "   Puntaje: 0.228 | Proy: Modulo analitico de compras por volumen en soles"
    )
    
    text_do = (
        "CUADRANTE DO (Reorientacion / Adaptacion)\n"
        "• E-07 (D1+O2+O3): Gobierno del Dato y Tableros BI [Alta]\n"
        "   Puntaje: 0.319 | Proy: Plataforma SaaS de BI y semillero tecnico local\n\n"
        "• E-09 (D4+O2): Solucion SaaS de Ruteo Vehicular [CRITICO]\n"
        "   Puntaje: 0.264 | Proy: Software VRP para reducir el 22% del gasto operativo\n\n"
        "• E-08 (D3+O1): Rediseno Mobile PWA y Programa de Fidelizacion\n"
        "   Puntaje: 0.253 | Proy: App PWA minorista y capacitacion al bodeguero"
    )
    
    text_da = (
        "CUADRANTE DA (Supervivencia / Saneamiento)\n"
        "• E-12 (D6+A2): Continuidad Operativa, Backup Cloud y DRP [CRITICO]\n"
        "   Puntaje: 0.270 | Proy: Copias inmutables regla 3-2-1 y pruebas RTO/RPO\n\n"
        "• E-10 (D2+A5): Redundancia de Talento TI y DevOps [CRITICO]\n"
        "   Puntaje: 0.270 | Proy: Repositorios Git, documentacion y 2do ingeniero\n\n"
        "• E-11 (D5+A3): Cumplimiento de Proteccion de Datos (ANPD) [CRITICO]\n"
        "   Puntaje: 0.216 | Proy: Adecuacion a D.S. 016-2024-JUS y seguridad de la info"
    )
    
    # Colocar textos
    ax.text(0.24, 0.70, text_fo, ha="center", va="center", fontsize=10, bbox=bbox_props_fo, wrap=True)
    ax.text(0.76, 0.70, text_fa, ha="center", va="center", fontsize=10, bbox=bbox_props_fa, wrap=True)
    ax.text(0.24, 0.26, text_do, ha="center", va="center", fontsize=10, bbox=bbox_props_do, wrap=True)
    ax.text(0.76, 0.26, text_da, ha="center", va="center", fontsize=10, bbox=bbox_props_da, wrap=True)
    
    plt.tight_layout()
    plt.savefig(anexo_c_path, dpi=300)
    plt.close()
    print(f"[OK] Generado: {anexo_c_path}")
    
    # 4. Anexo D: Estrategias Priorizadas
    df_prio = pd.read_csv(os.path.join(diag_dir, "PE04_estrategias_priorizadas.csv"))
    anexo_d_path = os.path.join(root_dir, "anexo_D_estrategias_priorizadas.xlsx")
    df_prio.to_excel(anexo_d_path, index=False, sheet_name="Priorizacion_Estrategias")
    print(f"[OK] Generado: {anexo_d_path}")
    
    # 5. Anexo E: Trazabilidad
    df_traz = pd.read_csv(os.path.join(diag_dir, "PE05_trazabilidad.csv"))
    anexo_e_path = os.path.join(root_dir, "anexo_E_trazabilidad.xlsx")
    df_traz.to_excel(anexo_e_path, index=False, sheet_name="Matriz_Trazabilidad")
    print(f"[OK] Generado: {anexo_e_path}")

if __name__ == "__main__":
    main()

# 3.3 AnÃ¡lisis PESTEL

## 3.3.1 MetodologÃ­a y fuentes
El anÃ¡lisis PESTEL (PolÃ­tico, EconÃ³mico, Social, TecnolÃ³gico, EcolÃ³gico/Ã‰tico, Legal) examina las fuerzas del macroentorno que inciden directa y materialmente sobre las operaciones, modelo de negocio e infraestructura tecnolÃ³gica de **Distribuidora Mayorista del Sur S.A.C. (DISUR S.A.C.)**.

Para asegurar la rigurosidad analÃ­tica y evitar que el anÃ¡lisis degenere en una recopilaciÃ³n de opiniones genÃ©ricas, se implementÃ³ la **Regla de Oro del PESTEL del curso**:
> *Â«Un factor sin cifra cuantitativa, sin fuente oficial verificable y sin una decisiÃ³n obligatoria para la gerencia, no califica como factor estratÃ©gico y debe ser descartado o reformuladoÂ».*

### Fuentes Institucionales Oficiales Utilizadas:
1. **Presidencia del Consejo de Ministros (PCM) / SecretarÃ­a de Gobierno y TransformaciÃ³n Digital (SGTD):** Decreto Supremo NÂ° 085-2023-PCM (PolÃ­tica Nacional de TransformaciÃ³n Digital al 2030) y normatividad de interoperabilidad PIDE.
2. **Banco Central de Reserva del PerÃº (BCRP):** Series estadÃ­sticas macroeconÃ³micas y tipo de cambio bancario interanual (EstadÃ­sticas Cambiarias 2024-2026).
3. **Instituto Nacional de EstadÃ­stica e InformÃ¡tica (INEI):** Encuesta Nacional de Hogares (ENAHO 2025-2026) sobre tecnologÃ­as de informaciÃ³n y comunicaciÃ³n en hogares y unidades econÃ³micas de la macro-regiÃ³n sur.
4. **DocumentaciÃ³n Oficial de Fabricantes TecnolÃ³gicos (Microsoft / Oracle):** Ciclos de vida de soporte de software de bases de datos y servidores empresariales.
5. **Gartner / International Data Corporation (IDC):** Reportes de tendencias de software de optimizaciÃ³n logÃ­stica en la nube (Vehicle Routing Problem) y Business Intelligence SaaS (2024-2025).
6. **Ministerio del Ambiente (MINAM):** Decreto Supremo NÂ° 009-2019-MINAM, RÃ©gimen Especial para la GestiÃ³n de Residuos de Aparatos ElÃ©ctricos y ElectrÃ³nicos (RAEE).
7. **UNESCO y OrganizaciÃ³n para la CooperaciÃ³n y el Desarrollo EconÃ³micos (OCDE):** RecomendaciÃ³n sobre la Ã‰tica de la Inteligencia Artificial (2021) y Principios sobre IA Confiable (2024).
8. **Autoridad Nacional de ProtecciÃ³n de Datos Personales (ANPD - MINJUSDH):** Ley NÂ° 29733 y Decreto Supremo NÂ° 016-2024-JUS (Nuevo Reglamento de ProtecciÃ³n de Datos Personales).

---

## 3.3.2 Factores por dimensiÃ³n, con evidencia y decisiÃ³n que obliga

| ID | DimensiÃ³n | Factor EstratÃ©gico | Evidencia con Cifra Verificable | Fuente Oficial y AÃ±o | Efecto EspecÃ­fico sobre DISUR S.A.C. | Tipo | Intensidad (1â€“5) | Horizonte | DecisiÃ³n que Obliga |
|:---:|:---:|:---|:---|:---:|:---|:---:|:---:|:---:|:---|
| **PE-01** | **PolÃ­tico** | PolÃ­tica Nacional de TransformaciÃ³n Digital al 2030 | Aprobada por D. S. 085-2023-PCM; mandatos prioritarios de interoperabilidad en compras y servicios pÃºblicos | PCM, 2023 | Al licitar suministros mayoristas con entidades del Estado, la interoperabilidad digital y facturaciÃ³n vÃ­a PIDE es condiciÃ³n contractual excluyente | **O** | 3 | 24â€“36 m | Implementar capa de microservicios y APIs REST conformes a los estÃ¡ndares de interoperabilidad del Estado |
| **PE-02** | **EconÃ³mico** | Volatilidad cambiaria e inflaciÃ³n en insumos TI | VariaciÃ³n acumulada interanual de 4.2% frente al USD en el mercado bancario | BCRP, EstadÃ­sticas Cambiarias 2026 | El 68% de los contratos de software empresarial, cloud y hardware estÃ¡ dolarizado, encareciendo el presupuesto de TI | **A** | 4 | Continuo | Incorporar clÃ¡usulas de cobertura cambiaria y renegociar contratos plurianuales de soporte y nube en moneda nacional |
| **PE-03** | **Social** | PenetraciÃ³n y adopciÃ³n masiva de smartphones | El 86.4% de comerciantes y microempresarios de la macro-regiÃ³n sur accede a internet mediante smartphone | INEI, ENAHO 2025-2026 | Habilita y viabiliza la autogestiÃ³n de pedidos comerciales mÃ³viles para mÃ¡s del 80% de los 8 400 minoristas de la cartera | **O** | 4 | 12â€“24 m | Priorizar el rediseÃ±o mobile-first y desarrollo de una Progressive Web App (PWA) de pedidos B2B con soporte offline |
| **PE-04** | **TecnolÃ³gico** | Fin de ciclo de vida y soporte oficial del ERP | Fabricante anunciÃ³ fin perentorio de parches y soporte de seguridad para el SO y motor de base de datos | Fabricante Oficial, 2025 | El servidor central de facturaciÃ³n y ventas quedarÃ¡ expuesto a vulnerabilidades de seguridad crÃ­ticas sin parches | **A** | 5 | 12â€“18 m | Aprobar e iniciar inmediatamente el proyecto de migraciÃ³n y modernizaciÃ³n del ERP hacia una arquitectura Cloud |
| **PE-05** | **TecnolÃ³gico** | Madurez de plataformas SaaS de analÃ­tica y ruteo | ReducciÃ³n de 35% en costos de suscripciÃ³n de plataformas de analÃ­tica predictiva y algoritmos de ruteo (VRP) | Gartner / IDC, 2025 | Permite implementar analÃ­tica de pedidos y ruteo dinÃ¡mico con bajo costo operativo sin inversiÃ³n en licencias perpetuas | **O** | 4 | 6â€“12 m | Reemplazar el ruteo manual en hojas de cÃ¡lculo por una soluciÃ³n SaaS especializada de optimizaciÃ³n vehicular |
| **PE-06** | **EcolÃ³gico/Ã‰tico** | DisposiciÃ³n y manejo de residuos electrÃ³nicos | Cumplimiento mandatorio del rÃ©gimen RAEE establecido en el D. S. NÂ° 009-2019-MINAM | MINAM, 2024 | La renovaciÃ³n planificada del parque informÃ¡tico y servidores obsoletos obliga a certificaciÃ³n ambiental de disposiciÃ³n | **A** | 2 | Continuo | Formalizar convenio con un operador RAEE autorizado y presupuestar las partidas de baja y disposiciÃ³n ecolÃ³gica |
| **PE-07** | **EcolÃ³gico/Ã‰tico** | Ã‰tica algorÃ­tmica y uso responsable de datos | Recomendaciones de la UNESCO sobre Ã©tica de IA y principios de tratamiento de datos de la OCDE | UNESCO, 2021; OCDE, 2024 | Los algoritmos comerciales de recomendaciÃ³n y evaluaciÃ³n de crÃ©dito a minoristas deben ser transparentes e imparciales | **A** | 3 | Al implementar | Aprobar la PolÃ­tica Institucional de Uso Ã‰tico del Dato antes de poner en producciÃ³n el motor de analÃ­tica |
| **PE-08** | **Legal** | Nuevo Reglamento de ProtecciÃ³n de Datos Personales | D. S. 016-2024-JUS vigente; fiscalizaciÃ³n estricta de la ANPD con sanciones de hasta 100 UIT | ANPD - MINJUSDH, 2024 | Exigencia obligatoria de registro de bancos de datos, consentimiento informado y auditorÃ­a de seguridad en sistemas | **A** | 5 | Inmediato | Ejecutar con carÃ¡cter urgente un Programa de Cumplimiento Normativo de ProtecciÃ³n de Datos Personales y Ciberseguridad |

---

## 3.3.3 SÃ­ntesis Â· Factores de Mayor Intensidad
De la matriz PESTEL se desprenden tres factores de criticidad extrema (Intensidad 5 y 4) que condicionan de forma ineludible la viabilidad estratÃ©gica y tecnolÃ³gica de DISUR S.A.C.:

1. **Fin de Soporte del ERP Central (PE-04 Â· Intensidad 5 Â· Amenaza):**  
   Representa un riesgo inminente de discontinuidad operacional. En una distribuidora con mÃ¡s de 8 400 clientes y alta rotaciÃ³n transaccional, operar un servidor de base de datos sin parches de seguridad expone la continuidad del negocio a incidentes de ransomware y fallos irrecuperables. Requiere acciÃ³n inmediata antes del plazo fatal de 12â€“18 meses.
2. **Entrada en Vigencia del Nuevo Reglamento de ProtecciÃ³n de Datos (PE-08 Â· Intensidad 5 Â· Amenaza):**  
   El D. S. 016-2024-JUS cambia radicalmente las reglas de juego. La carencia de consentimiento explÃ­cito de los minoristas, la ausencia de medidas tÃ©cnicas de seguridad y la omisiÃ³n del registro formal de los bancos de datos exponen a la empresa a multas que podrÃ­an superar los S/ 515,000 (100 UIT), ademÃ¡s del daÃ±o reputacional.
3. **PenetraciÃ³n de Smartphones en Minoristas (PE-03 Â· Intensidad 4 Â· Oportunidad):**  
   El 86.4% de conectividad mÃ³vil en el mercado minorista de Tacna y la macro-regiÃ³n sur convierte al canal mÃ³vil en el vehÃ­culo natural de crecimiento comercial, tornando obsoleto el modelo tradicional basado exclusivamente en visitas de preventistas presenciales.
# 3.4 AnÃ¡lisis FODA y Matrices de EvaluaciÃ³n

## 3.4.1 Factores Internos Â· Fortalezas y Debilidades
Los factores internos se derivan estrictamente del diagnÃ³stico organizacional de **Distribuidora Mayorista del Sur S.A.C. (DISUR S.A.C.)**, consolidando evidencias de la Cadena de Valor (SecciÃ³n 3.1.1), el Inventario de Activos de InformaciÃ³n (SecciÃ³n 3.1.2), el AnÃ¡lisis de Recursos y Capacidades VRIO (SecciÃ³n 3.1.3), la Arquitectura de Aplicaciones e Infraestructura (SecciÃ³n 3.1.4) y la Madurez de Ciberseguridad (SecciÃ³n 3.1.6).

### Fortalezas (F):
- **F1:** Red de distribuciÃ³n logÃ­stica propia con flota vehicular y despacho garantizado en 24 horas en Tacna, Moquegua, Ilo y zonas aledaÃ±as (SecciÃ³n 3.1.1 CV-03).
- **F2:** Base de datos histÃ³rica consolidada de compras, frecuencia de pedidos y comportamiento transaccional de 8 400 clientes minoristas por mÃ¡s de 6 aÃ±os (SecciÃ³n 3.1.2).
- **F3:** Cobertura comercial establecida con red de agentes de ventas zonales y alto reconocimiento de marca en el canal minorista tradicional de la macro-regiÃ³n sur (SecciÃ³n 3.1.1).
- **F4:** Procesos comerciales operativos de despacho y facturaciÃ³n electrÃ³nica estandarizados y sincronizados con el ERP central y SUNAT (SecciÃ³n 3.1.4).

### Debilidades (D):
- **D1:** Ausencia total de capacidades analÃ­ticas estructuradas de datos, inteligencia de negocios (BI) y modelos cuantitativos de previsiÃ³n de la demanda (SecciÃ³n 3.1.5).
- **D2:** Extrema personodependencia tecnolÃ³gica: un Ãºnico desarrollador concentra el conocimiento exclusivo de la arquitectura, cÃ³digo y mantenimiento del portal B2B (SecciÃ³n 3.1.3 VRIO).
- **D3:** Baja tasa de adopciÃ³n del portal web B2B por parte de clientes minoristas (menos del 8% del total de pedidos) debido a un diseÃ±o de escritorio no responsivo (SecciÃ³n 3.1.1).
- **D4:** GestiÃ³n del ruteo y asignaciÃ³n de despachos realizada manualmente en hojas de cÃ¡lculo (Excel), concentrando el 22% del costo operativo total del negocio (SecciÃ³n 3.1.1 CV-03).
- **D5:** Carencia de un programa formal de cumplimiento normativo de seguridad de la informaciÃ³n y protecciÃ³n de datos personales (D. S. 016-2024-JUS) (SecciÃ³n 3.1.6).
- **D6:** Carencia de redundancia en la infraestructura on-premise de servidores y ausencia de pruebas periÃ³dicas de restauraciÃ³n de copias de seguridad (SecciÃ³n 3.1.4).

---

## 3.4.2 Factores Externos Â· Oportunidades y Amenazas
Los factores externos provienen del macroentorno analizado en la matriz PESTEL (SecciÃ³n 3.3) y del anÃ¡lisis de la industria y fuerzas competitivas (SecciÃ³n 3.2):

### Oportunidades (O):
- **O1:** PenetraciÃ³n masiva de smartphones y conectividad mÃ³vil 4G/5G en comerciantes minoristas (86.4% segÃºn INEI ENAHO 2025-2026) (SecciÃ³n 3.3 PE-03).
- **O2:** Disponibilidad de herramientas SaaS y soluciones cloud de analÃ­tica comercial, BI y algoritmos de optimizaciÃ³n de rutas (VRP) a costos escalables (SecciÃ³n 3.3 PE-05).
- **O3:** Ecosistema regional de talento tÃ©cnico egresado de carreras de ingenierÃ­a de sistemas de universidades e institutos de Tacna y la macro-regiÃ³n sur (SecciÃ³n 3.2).
- **O4:** Crecimiento sostenido del consumo y actividad comercial mayorista regional en el sur del paÃ­s (incremento interanual superior a 4.5%) (SecciÃ³n 3.2).
- **O5:** PolÃ­ticas nacionales de interoperabilidad tributaria digital y consolidaciÃ³n del ecosistema de pagos y facturaciÃ³n electrÃ³nica (SecciÃ³n 3.3 PE-01).

### Amenazas (A):
- **A1:** Entrada agresiva de plataformas mayoristas y distribuidores digitales de Lima con canales mÃ³viles y despacho directo sin tiendas fÃ­sicas (SecciÃ³n 3.2).
- **A2:** Fin de soporte oficial anunciado por el fabricante para el sistema operativo y motor de base de datos del servidor ERP central (SecciÃ³n 3.3 PE-04).
- **A3:** RÃ©gimen fiscalizador y sanciones punitivas de hasta 100 UIT por la ANPD ante el nuevo Reglamento de ProtecciÃ³n de Datos Personales (D. S. 016-2024-JUS) (SecciÃ³n 3.3 PE-08).
- **A4:** Volatilidad cambiaria que encarece la adquisiciÃ³n de equipamiento de TI, servicios en la nube y licencias dolarizadas (SecciÃ³n 3.3 PE-02).
- **A5:** Alta rotaciÃ³n laboral en perfiles de TI y captaciÃ³n remota de ingenieros por empresas de tecnologÃ­a internacionales (SecciÃ³n 3.2).

---

## 3.4.3 Matriz EFI (EvaluaciÃ³n de Factores Internos)

### Criterio de CalificaciÃ³n:
* **4 = Fortaleza Mayor:** Factor distintivo, difÃ­cilmente imitable, base de la ventaja competitiva.
* **3 = Fortaleza Menor:** Factor favorable, pero comÃºn o mejorable en el mercado.
* **2 = Debilidad Menor:** Deficiencia subsanable a corto plazo con recursos internos.
* **1 = Debilidad Mayor:** Vulnerabilidad crÃ­tica que compromete la operaciÃ³n o la supervivencia.

| ID | Factor Interno | SecciÃ³n de Origen | Peso | Calif. | Ponderado | JustificaciÃ³n MetodolÃ³gica del Peso |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| **F1** | Red logÃ­stica propia con entrega 24 h en el sur | Sec. 3.1.1 CV-03 | 0.140 | 4 | 0.560 | Principal barrera de entrada frente a mayoristas forÃ¡neos y sustento de los ingresos operativos. |
| **F2** | Base de datos histÃ³rica de 8 400 minoristas (6 aÃ±os) | Sec. 3.1.2 Activos | 0.110 | 4 | 0.440 | Activo de informaciÃ³n insustituible para personalizaciÃ³n de la oferta y anÃ¡lisis predictivo. |
| **F3** | Cobertura zonal y reconocimiento en el canal minorista | Sec. 3.1.1 Ventas | 0.080 | 3 | 0.240 | Mantiene fidelizada la cartera tradicional y asegura rotaciÃ³n continua de inventarios. |
| **F4** | Procesos comerciales estandarizados en el ERP | Sec. 3.1.4 Apps | 0.090 | 3 | 0.270 | Garantiza continuidad operativa y emisiÃ³n de comprobantes de pago sin multas ante SUNAT. |
| **D1** | Ausencia total de capacidades analÃ­ticas y de BI | Sec. 3.1.5 TI | 0.100 | 1 | 0.100 | Causa directa de sobrestock y compras ineficientes basadas en intuiciÃ³n del personal. |
| **D2** | Personodependencia crÃ­tica del Ãºnico desarrollador | Sec. 3.1.3 VRIO | 0.120 | 1 | 0.120 | Riesgo operacional inaceptable; su desvinculaciÃ³n pararÃ­a el soporte y evoluciÃ³n del portal. |
| **D3** | Baja adopciÃ³n del portal web B2B (<8% pedidos) | Sec. 3.1.1 Canales | 0.100 | 2 | 0.200 | Limita el retorno de inversiÃ³n tecnolÃ³gica y sobrecarga de costos al canal de preventa fÃ­sica. |
| **D4** | Ruteo manual en Excel concentra 22% del costo operativo | Sec. 3.1.1 CV-03 | 0.130 | 1 | 0.130 | Mayor rubro individual de sobrecosto evitable por kilometraje ocioso y demoras de despacho. |
| **D5** | Carencia de programa de protecciÃ³n de datos (ANPD) | Sec. 3.1.6 Ciber | 0.070 | 1 | 0.070 | ExposiciÃ³n a contingencias legales inmediatas y multas regulatorias de hasta 100 UIT. |
| **D6** | Ausencia de redundancia y pruebas de restauraciÃ³n | Sec. 3.1.4 Infra | 0.060 | 2 | 0.120 | Falta de resiliencia operativa; un fallo fÃ­sico de discos paraliza la facturaciÃ³n por dÃ­as. |
| **TOTAL** | **Matriz EFI Consolidada** | | **1.000** | â€” | **2.250** | *Suma de pesos = 1.000 validada matemÃ¡ticamente sin desviaciones.* |

---

## 3.4.4 Matriz EFE (EvaluaciÃ³n de Factores Externos)

### Regla Fundamental de la CalificaciÃ³n EFE:
> **La calificaciÃ³n EFE NO evalÃºa quÃ© tan grave o importante es el factor del entorno, sino quÃ© tan bien responde la organizaciÃ³n frente a dicho factor:**  
> * **4 = Respuesta superior:** La empresa aprovecha activamente la oportunidad o neutraliza la amenaza con excelencia.  
> * **3 = Respuesta por encima del promedio:** La organizaciÃ³n responde adecuadamente con acciones estructuradas.  
> * **2 = Respuesta por debajo del promedio:** La empresa tiene respuestas reactivas o incipientes.  
> * **1 = Respuesta deficiente:** La organizaciÃ³n no tiene ninguna capacidad ni acciÃ³n para responder ante el factor.

| ID | Factor Externo | SecciÃ³n de Origen | Peso | Calif. | Ponderado | JustificaciÃ³n del Peso y CalificaciÃ³n de Respuesta |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| **O1** | Smartphones en 86.4% de minoristas (INEI) | Sec. 3.3 PE-03 | 0.130 | 2 | 0.260 | *Peso:* Oportunidad de mayor escala. *Calif 2:* Respuesta rezagada; solo se ofrece un portal web no responsivo con 8% de uso. |
| **O2** | Plataformas SaaS accesibles de BI y ruteo (VRP) | Sec. 3.3 PE-05 | 0.110 | 2 | 0.220 | *Peso:* Permite modernizar TI sin Capex. *Calif 2:* No se han desplegado soluciones cloud ni pilotos analÃ­ticos. |
| **O3** | Ecosistema de talento tÃ©cnico regional macro-sur | Sec. 3.2 Laboral | 0.080 | 2 | 0.160 | *Peso:* Capital humano local accesible. *Calif 2:* No existen alianzas universitarias ni semillero tÃ©cnico formal. |
| **O4** | Crecimiento comercial sostenido en la macro-sur | Sec. 3.2 Mercado | 0.100 | 3 | 0.300 | *Peso:* Demanda en expansiÃ³n. *Calif 3:* La flota y red logÃ­stica propia absorbe eficazmente el aumento de pedidos. |
| **O5** | PolÃ­ticas de digitalizaciÃ³n tributaria e interoperabilidad | Sec. 3.3 PE-01 | 0.070 | 3 | 0.210 | *Peso:* Requisito formal. *Calif 3:* El ERP emite comprobantes electrÃ³nicos a SUNAT de manera integrada y puntual. |
| **A1** | Entrada de plataformas mayoristas digitales forÃ¡neas | Sec. 3.2 Competencia | 0.120 | 2 | 0.240 | *Peso:* Amenaza de desintermediaciÃ³n. *Calif 2:* Se compite solo con presencia fÃ­sica; no hay canal mÃ³vil para competir. |
| **A2** | Fin de soporte anunciado del servidor/DB del ERP | Sec. 3.3 PE-04 | 0.140 | 1 | 0.140 | *Peso:* Riesgo de continuidad mÃ¡xima. *Calif 1:* Respuesta nula; la migraciÃ³n no estÃ¡ iniciada ni presupuestada formalmente. |
| **A3** | Multas de hasta 100 UIT por datos (D. S. 016-2024-JUS) | Sec. 3.3 PE-08 | 0.090 | 1 | 0.090 | *Peso:* Riesgo sancionatorio inminente. *Calif 1:* Respuesta nula; carece de registro de bancos y consentimiento informado. |
| **A4** | Volatilidad cambiaria que encarece licencias en USD | Sec. 3.3 PE-02 | 0.080 | 2 | 0.160 | *Peso:* Encarece Capex y Opex de TI. *Calif 2:* No se han contratado coberturas financieras ni tarifas fijas en moneda local. |
| **A5** | Alta rotaciÃ³n de TI y fuga de talento tÃ©cnico | Sec. 3.2 Mercado TI | 0.080 | 1 | 0.080 | *Peso:* Amenaza directa a la operatividad. *Calif 1:* Respuesta deficiente; carece de planes de retenciÃ³n y documentaciÃ³n. |
| **TOTAL** | **Matriz EFE Consolidada** | | **1.000** | â€” | **1.860** | *Suma de pesos = 1.000 validada matemÃ¡ticamente sin desviaciones.* |

---

## 3.4.5 InterpretaciÃ³n de la PosiciÃ³n EstratÃ©gica
1. **DimensiÃ³n Interna (Puntaje EFI = 2.250 / 4.000):**  
   Al situarse por debajo de la media teÃ³rica de **2.500**, la organizaciÃ³n exhibe una **condiciÃ³n interna dÃ©bil y vulnerable**. A pesar de contar con ventajas operativas fÃ­sicas relevantes (flota de distribuciÃ³n propia y cartera histÃ³rica de clientes), la ineficiencia logÃ­stica manual (22% del gasto en ruteo), la ausencia de analÃ­tica y la personodependencia del cÃ³digo colocan a la empresa en una situaciÃ³n de fragilidad estructural.
2. **DimensiÃ³n Externa (Puntaje EFE = 1.860 / 4.000):**  
   El puntaje de 1.860 evidencia una **respuesta global ineficaz y deficiente frente al entorno**. La organizaciÃ³n no estÃ¡ aprovechando las oportunidades del mercado digital mÃ³vil ni se estÃ¡ defendiendo oportunamente de amenazas crÃ­ticas (obsolescencia del ERP y fiscalizaciÃ³n de protecciÃ³n de datos).
3. **UbicaciÃ³n en la Matriz Interna-Externa (IE):**  
   Coordenada estratÃ©gica: `(EFI = 2.250, EFE = 1.860)`.  
   Esta coordenada posiciona a la empresa en el **Cuadrante VIII / IX (RegiÃ³n Defensiva de Cosechar, Desinvertir o Reestructurar)**.
   * **Mandato EstratÃ©gico para el PETI:**  
     Queda terminantemente prohibido formular estrategias de expansiÃ³n agresiva o transformaciÃ³n digital avanzada que ignoren las vulnerabilidades de base. **La regla de supervivencia impera:** el plan debe concentrarse primero en sanear las debilidades operativas, blindar la continuidad del ERP, cumplir con la legislaciÃ³n de datos y eliminar la dependencia tÃ©cnica unipersonal.
# 3.5 Estrategias Derivadas del DiagnÃ³stico

## 3.5.1 Matriz FODA Cruzado
La matriz FODA cruzado transforma el diagnÃ³stico situacional en decisiones concretas. Cruza metÃ³dicamente las fortalezas y debilidades internas con las oportunidades y amenazas del entorno para derivar un portafolio de **12 estrategias**, distribuidas equitativamente en los cuatro cuadrantes tÃ¡cticos (3 estrategias por cuadrante).

```
                      +---------------------------------------+---------------------------------------+
                      |           OPORTUNIDADES (O)           |             AMENAZAS (A)              |
                      | O1: Smartphone minorista 86.4%        | A1: Mayoristas digitales de Lima      |
                      | O2: Plataformas SaaS BI y VRP         | A2: Fin soporte fabricante ERP        |
                      | O3: Talento tÃ©cnico regional          | A3: Sanciones ANPD D.S. 016-2024      |
                      | O4: Crecimiento consumo macro-sur     | A4: Volatilidad cambiaria USD         |
                      | O5: DigitalizaciÃ³n tributaria SUNAT   | A5: Fuga de talento TI y rotaciÃ³n     |
+---------------------+---------------------------------------+---------------------------------------+
|   FORTALEZAS (F)    |      ESTRATEGIAS FO (Crecimiento)     |      ESTRATEGIAS FA (Defensivas)      |
| F1: LogÃ­stica 24h   | E-01: App B2B con analÃ­tica SaaS      | E-04: Trazabilidad GPS y entrega 24h  |
| F2: 8 400 clientes  |       (F2 + O1 + O2)                  |       (F1 + A1)                       |
| F3: Cobertura zonal | E-02: Ruteo logÃ­stico macro-sur       | E-05: MigraciÃ³n ERP Cloud             |
| F4: ERP integrado   |       (F1 + O4)                       |       (F4 + A2)                       |
|                     | E-03: Pagos digitales y conciliaciÃ³n  | E-06: PlanificaciÃ³n compras en soles  |
|                     |       (F4 + O5)                       |       (F2 + A4)                       |
+---------------------+---------------------------------------+---------------------------------------+
|   DEBILIDADES (D)   |    ESTRATEGIAS DO (ReorientaciÃ³n)     |     ESTRATEGIAS DA (Supervivencia)    |
| D1: Sin analÃ­tica   | E-07: Gobierno del dato y BI local    | E-10: Redundancia talento y DevOps    |
| D2: Programador 1   |       (D1 + O2 + O3)                  |       (D2 + A5)                       |
| D3: Baja adopciÃ³n   | E-08: RediseÃ±o PWA y adopciÃ³n bodega  | E-11: Cumplimiento ANPD y seguridad   |
| D4: Ruteo Excel 22% |       (D3 + O1)                       |       (D5 + A3)                       |
| D5: Sin datos ANPD  | E-09: Software SaaS de ruteo VRP      | E-12: Continuidad, backup cloud y DRP |
| D6: Sin redundancia |       (D4 + O2)                       |       (D6 + A2)                       |
+---------------------+---------------------------------------+---------------------------------------+
```

---

## 3.5.2 Estrategias FO, FA, DO y DA

### Cuadrante FO Â· Estrategias de Crecimiento y Ataque:
1. **E-01 (F2 + O1 + O2): Canal Digital B2B MÃ³vil con Motor de RecomendaciÃ³n.**  
   *Estrategia:* Aprovechar la base histÃ³rica de compras de 8 400 clientes (F2) y la masiva adopciÃ³n de smartphones del segmento minorista (O1) mediante el despliegue de una aplicaciÃ³n mÃ³vil B2B apoyada en algoritmos de analÃ­tica SaaS (O2) para generar recomendaciones automatizadas de pedidos y promociones personalizadas.  
   *Objetivo:* Incrementar la participaciÃ³n de pedidos por canal digital al 35% del total de la cartera.  
   *Proyecto Candidato:* Plataforma MÃ³vil B2B y Motor de RecomendaciÃ³n Comercial.
2. **E-02 (F1 + O4): Sistema de Ruteo DinÃ¡mico y Despacho Inteligente.**  
   *Estrategia:* Aprovechar la flota y red de distribuciÃ³n logÃ­stica propia con entrega garantizada en 24 h (F1) para capturar el crecimiento del consumo comercial de la macro-regiÃ³n sur (O4), optimizando y consolidando las rutas de transporte interdepartamentales.  
   *Objetivo:* Reducir el costo unitario de despacho logÃ­stico e incrementar la cobertura geogrÃ¡fica en un 20%.  
   *Proyecto Candidato:* Sistema de Ruteo DinÃ¡mico y Despacho Inteligente.
3. **E-03 (F4 + O5): IntegraciÃ³n de Pagos Digitales e Interoperabilidad Financiera.**  
   *Estrategia:* Aprovechar la estabilidad e integraciÃ³n transaccional del ERP (F4) conectÃ¡ndolo con pasarelas de interoperabilidad y billeteras digitales (O5) para cobro electrÃ³nico y conciliaciÃ³n bancaria automatizada en tiempo real.  
   *Objetivo:* Reducir el tiempo del ciclo de caja y conciliaciÃ³n diaria a menos de 2 horas.  
   *Proyecto Candidato:* IntegraciÃ³n de Pagos Digitales e Interoperabilidad Financiera.

### Cuadrante FA Â· Estrategias Defensivas y de DiferenciaciÃ³n:
4. **E-04 (F1 + A1): Portal de Trazabilidad de Despachos y Prueba Digital de Entrega.**  
   *Estrategia:* Utilizar la red de distribuciÃ³n fÃ­sica propia con entrega garantizada en 24 h (F1) para neutralizar la entrada de mayoristas digitales forÃ¡neos sin logÃ­stica local (A1), proveyendo trazabilidad GPS en tiempo real y confirmaciÃ³n digital de entrega (Proof of Delivery).  
   *Objetivo:* Blindar y fidelizar al 95% de los clientes clave ante la incursiÃ³n de plataformas forÃ¡neas.  
   *Proyecto Candidato:* Portal de Trazabilidad de Despachos y Prueba Digital de Entrega.
5. **E-05 (F4 + A2): MigraciÃ³n y ModernizaciÃ³n de la Plataforma ERP a la Nube.**  
   *Estrategia:* Utilizar la estandarizaciÃ³n y estabilidad de procesos del ERP actual (F4) como especificaciÃ³n funcional y base de migraciÃ³n hacia una plataforma ERP Cloud moderna antes de la fecha lÃ­mite de fin de soporte del fabricante (A2).  
   *Objetivo:* Asegurar la continuidad operacional del negocio con cero tiempo de inactividad no planificado.  
   *Proyecto Candidato:* MigraciÃ³n y ModernizaciÃ³n de la Plataforma ERP a la Nube.
6. **E-06 (F2 + A4): MÃ³dulo AnalÃ­tico de PlanificaciÃ³n de Compras y Cobertura de Precios.**  
   *Estrategia:* Utilizar el histÃ³rico de compras de 8 400 clientes (F2) para calibrar compras por volumen y coberturas de stock en moneda nacional, mitigando la exposiciÃ³n del margen bruto a la volatilidad cambiaria (A4).  
   *Objetivo:* Proteger el margen bruto operativo en al menos 4 puntos porcentuales frente a devaluaciones.  
   *Proyecto Candidato:* MÃ³dulo AnalÃ­tico de PlanificaciÃ³n de Compras y Cobertura de Precios.

### Cuadrante DO Â· Estrategias de ReorientaciÃ³n y ModernizaciÃ³n:
7. **E-07 (D1 + O2 + O3): Gobierno del Dato y Tablero de Inteligencia de Negocios (BI).**  
   *Estrategia:* Superar la ausencia total de capacidad analÃ­tica interna (D1) aprovechando herramientas SaaS de BI de bajo costo (O2) y reclutando egresados de ingenierÃ­a de sistemas de la macro-regiÃ³n sur (O3) para estructurar el gobierno de datos y cuadros de mando comerciales.  
   *Objetivo:* Habilitar la toma de decisiones basada en datos para compras, inventarios y polÃ­ticas de crÃ©dito.  
   *Proyecto Candidato:* Gobierno del Dato y Tablero de Inteligencia de Negocios (BI).
8. **E-08 (D3 + O1): RediseÃ±o Mobile PWA y Programa de FidelizaciÃ³n Digital B2B.**  
   *Estrategia:* Superar la baja tasa de adopciÃ³n del portal web B2B (D3) capitalizando la masiva tenencia de smartphones en minoristas (O1) mediante un rediseÃ±o bajo estÃ¡ndar Progressive Web App (PWA) mÃ³vil y un programa presencial de alfabetizaciÃ³n digital al comerciante bodeguero.  
   *Objetivo:* Elevar la tasa de adopciÃ³n del canal de pedidos digital del 8% al 40% en 18 meses.  
   *Proyecto Candidato:* RediseÃ±o Mobile PWA y Programa de FidelizaciÃ³n Digital B2B.
9. **E-09 (D4 + O2): ImplementaciÃ³n de SoluciÃ³n SaaS de Ruteo y Despacho Vehicular.**  
   *Estrategia:* Superar la ineficiencia del ruteo manual en Excel que absorbe el 22% del costo operativo (D4) adoptando una soluciÃ³n SaaS de Vehicle Routing Problem (VRP) con algoritmos de optimizaciÃ³n de flotas y geocodificaciÃ³n automÃ¡tica (O2).  
   *Objetivo:* Reducir el gasto logÃ­stico operativo en un 18% y eliminar errores de direccionamiento.  
   *Proyecto Candidato:* ImplementaciÃ³n de SoluciÃ³n SaaS de Ruteo y Despacho Vehicular.

### Cuadrante DA Â· Estrategias de Supervivencia y MitigaciÃ³n de Vulnerabilidades:
10. **E-10 (D2 + A5): GestiÃ³n del Conocimiento, Repositorios DevOps y Redundancia de Personal TI.**  
    *Estrategia:* Reducir la dependencia extrema de un Ãºnico desarrollador (D2) para mitigar el riesgo crÃ­tico de fuga de talento y alta rotaciÃ³n en el sector TI (A5), mediante la documentaciÃ³n integral de arquitectura, estandarizaciÃ³n en Git/DevOps y contrataciÃ³n de un segundo perfil de ingenierÃ­a.  
    *Objetivo:* Eliminar el riesgo operacional por personodependencia tecnolÃ³gica y asegurar transferibilidad tÃ©cnica.  
    *Proyecto Candidato:* GestiÃ³n del Conocimiento, Repositorios DevOps y Redundancia de Personal TI.
11. **E-11 (D5 + A3): Programa de Cumplimiento Normativo de ProtecciÃ³n de Datos y Ciberseguridad.**  
    *Estrategia:* Subsanar la carencia absoluta de un programa de cumplimiento de protecciÃ³n de datos (D5) para neutralizar la exposiciÃ³n a multas coercitivas de hasta 100 UIT ante el nuevo Reglamento de ProtecciÃ³n de Datos Personales (A3) mediante registro formal de bancos y polÃ­ticas ISO 27001.  
    *Objetivo:* Alcanzar 100% de cumplimiento legal ante la normativa de protecciÃ³n de datos personales (D. S. 016-2024-JUS).  
    *Proyecto Candidato:* Programa de Cumplimiento Normativo de ProtecciÃ³n de Datos y Ciberseguridad.
12. **E-12 (D6 + A2): Plan de Continuidad Operativa, Copias Inmutables Cloud y DRP.**  
    *Estrategia:* Resolver la falta de redundancia y copias de seguridad no verificadas (D6) frente a la inminente obsolescencia y fin de soporte del servidor ERP (A2) implementando un esquema de respaldo inmutable en la nube (regla 3-2-1) y pruebas semestrales de restauraciÃ³n.  
    *Objetivo:* Garantizar la resiliencia operativa y recuperaciÃ³n ante desastres con RTO < 4 horas y RPO < 1 hora.  
    *Proyecto Candidato:* Plan de Continuidad Operativa, Copias Inmutables Cloud y DRP.

---

## 3.5.3 PriorizaciÃ³n de Estrategias y su JustificaciÃ³n

### Criterio MetodolÃ³gico de PonderaciÃ³n:
La priorizaciÃ³n cuantitativa aplica la fÃ³rmula formal establecida en el marco metodolÃ³gico del curso:
$$\text{Puntaje} = \text{Peso Total de Factores Cruzados} \times \text{Bono EstratÃ©gico por Cuadrante}$$

Donde los bonos reflejan el principio de **Â«Supervivencia y Continuidad Operativa PrimeroÂ»**:
* **Bono DA = 1.35:** Prioridad mÃ¡xima; si la empresa quiebra o es multada fatalmente, las estrategias de crecimiento pierden sentido.
* **Bono FA = 1.20:** Defensa de la cuota de mercado y activos nucleares ante amenazas activas.
* **Bono DO = 1.10:** ReorganizaciÃ³n interna y capacitaciÃ³n para superar debilidades aprovechando oportunidades.
* **Bono FO = 1.00:** Crecimiento y expansiÃ³n sobre fortalezas consolidadas.

### Tabla Consolidada de PriorizaciÃ³n de Estrategias:

| Ranking | ID | Tipo | Factores Cruzados | Suma Peso Factores | Bono | Puntaje Final | Proyecto Candidato | Prioridad PETI |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **1** | **E-01** | **FO** | F2 + O1 + O2 | 0.350 | 1.00 | **0.350** | Canal Digital B2B MÃ³vil con Motor de RecomendaciÃ³n | Alta |
| **2** | **E-07** | **DO** | D1 + O2 + O3 | 0.290 | 1.10 | **0.319** | Gobierno del Dato y Tablero de Inteligencia de Negocios (BI) | Alta |
| **3** | **E-04** | **FA** | F1 + A1 | 0.260 | 1.20 | **0.312** | Portal de Trazabilidad de Despachos y Prueba Digital de Entrega | Alta |
| **4** | **E-05** | **FA** | F4 + A2 | 0.230 | 1.20 | **0.276** | MigraciÃ³n y ModernizaciÃ³n de la Plataforma ERP a la Nube | **CrÃ­tica** |
| **5** | **E-12** | **DA** | D6 + A2 | 0.200 | 1.35 | **0.270** | Plan de Continuidad Operativa, Copias Inmutables Cloud y DRP | **CrÃ­tica** |
| **6** | **E-10** | **DA** | D2 + A5 | 0.200 | 1.35 | **0.270** | GestiÃ³n del Conocimiento, Repositorios DevOps y Redundancia TI | **CrÃ­tica** |
| **7** | **E-09** | **DO** | D4 + O2 | 0.240 | 1.10 | **0.264** | ImplementaciÃ³n de SoluciÃ³n SaaS de Ruteo y Despacho Vehicular | **CrÃ­tica** |
| **8** | **E-08** | **DO** | D3 + O1 | 0.230 | 1.10 | **0.253** | RediseÃ±o Mobile PWA y Programa de FidelizaciÃ³n Digital B2B | Alta |
| **9** | **E-02** | **FO** | F1 + O4 | 0.240 | 1.00 | **0.240** | Sistema de Ruteo DinÃ¡mico y Despacho Inteligente | Alta |
| **10** | **E-06** | **FA** | F2 + A4 | 0.190 | 1.20 | **0.228** | MÃ³dulo AnalÃ­tico de PlanificaciÃ³n de Compras y Cobertura Precios | Alta |
| **11** | **E-11** | **DA** | D5 + A3 | 0.160 | 1.35 | **0.216** | Programa de Cumplimiento Normativo de ProtecciÃ³n de Datos | **CrÃ­tica** |
| **12** | **E-03** | **FO** | F4 + O5 | 0.160 | 1.00 | **0.160** | IntegraciÃ³n de Pagos Digitales e Interoperabilidad Financiera | Media |

### AnÃ¡lisis EstratÃ©gico de la PriorizaciÃ³n:
El anÃ¡lisis cuantitativo revela que, si bien la estrategia `E-01` alcanza el puntaje individual mÃ¡s alto por concentrar los factores de mayor peso conjunto (0.350), **el bloque de proyectos clasificados como Â«CrÃ­ticosÂ» (E-05, E-12, E-10, E-09 y E-11) pertenece a los cuadrantes defensivos (DA, FA y DO)**.  
Esto demuestra que el PETI de DISUR S.A.C. debe adoptar un **enfoque por olas de implementaciÃ³n (Roadmap EstratÃ©gico)**:
- **Ola 1 (Meses 1â€“6 Â· EstabilizaciÃ³n y Cumplimiento):** EjecuciÃ³n inmediata de E-11 (AdecuaciÃ³n ANPD), E-10 (DocumentaciÃ³n y duplicaciÃ³n del desarrollador Ãºnico), E-12 (Copias inmutables y DRP) e inicio de la migraciÃ³n del ERP (E-05).
- **Ola 2 (Meses 7â€“12 Â· Eficiencia Operacional):** Despliegue de la soluciÃ³n SaaS de ruteo vehicular (E-09 / E-02) para capturar el ahorro del 18% en costos logÃ­sticos y puesta en marcha del gobierno de datos (E-07).
- **Ola 3 (Meses 13â€“24 Â· ExpansiÃ³n Digital):** Lanzamiento de la plataforma mÃ³vil B2B para minoristas (E-01, E-08) y trazabilidad al cliente (E-04).

---

## 3.5.4 Matriz de Trazabilidad Integral
*(Consignada en el Paso D y en el archivo `03_diagnostico/PE05_trazabilidad.csv`)*
Cada proyecto de inversiÃ³n de TI se encuentra sustentado en una cadena ininterrumpida de custodia analÃ­tica:
$$\text{Evidencia del DiagnÃ³stico} \longrightarrow \text{Factor EstratÃ©gico} \longrightarrow \text{Estrategia Cruzada} \longrightarrow \text{Objetivo del PETI} \longrightarrow \text{Proyecto de TI}$$
Cualquier intento de incorporar proyectos tecnolÃ³gicos que no cuenten con esta trazabilidad queda formalmente desestimado.

# BASE DE CONOCIMIENTOS - SISTEMA EXPERTO PARA DIAGNÓSTICO DE FALLAS EN COMPUTADORAS
# 500 REGLAS ÚNICAS

knowledge_base = {
    
    # ============================================================================
    # CATEGORÍA 1: FUENTE DE PODER (50 reglas)
    # ============================================================================
    
    "R001": {
        "condiciones": ["computadora_no_enciende", "led_fuente_apagado", "olor_quemado"],
        "conclusion": "fuente_poder_quemada",
        "certeza": 95,
        "solucion": "Reemplazar fuente de poder inmediatamente",
        "categoria": "Fuente de Poder"
    },
    
    "R002": {
        "condiciones": ["computadora_no_enciende", "led_fuente_encendido", "ventilador_fuente_no_gira"],
        "conclusion": "ventilador_fuente_dañado",
        "certeza": 85,
        "solucion": "Verificar y reemplazar ventilador de fuente",
        "categoria": "Fuente de Poder"
    },
    
    "R003": {
        "condiciones": ["reinicios_aleatorios", "bajo_voltaje_detectado"],
        "conclusion": "fuente_poder_insuficiente",
        "certeza": 80,
        "solucion": "Actualizar a fuente de mayor potencia",
        "categoria": "Fuente de Poder"
    },
    
    "R004": {
        "condiciones": ["computadora_enciende", "apaga_segundos_despues", "led_fuente_parpadea"],
        "conclusion": "cortocircuito_fuente",
        "certeza": 90,
        "solucion": "Revisar conexiones y reemplazar fuente",
        "categoria": "Fuente de Poder"
    },
    
    "R005": {
        "condiciones": ["ruido_electrico_fuente", "zumbido_constante"],
        "conclusion": "condensadores_fuente_deteriorados",
        "certeza": 75,
        "solucion": "Reemplazar condensadores o fuente completa",
        "categoria": "Fuente de Poder"
    },
    
    "R006": {
        "condiciones": ["computadora_no_enciende", "cable_poder_conectado", "tomacorriente_funcional"],
        "conclusion": "cable_poder_interno_dañado",
        "certeza": 70,
        "solucion": "Verificar cable de poder interno",
        "categoria": "Fuente de Poder"
    },
    
    "R007": {
        "condiciones": ["fuente_muy_caliente", "apagados_intermitentes"],
        "conclusion": "sobrecalentamiento_fuente",
        "certeza": 85,
        "solucion": "Limpiar ventilación y verificar carga",
        "categoria": "Fuente de Poder"
    },
    
    "R008": {
        "condiciones": ["chispas_fuente", "ruido_explosion"],
        "conclusion": "capacitor_fuente_explotado",
        "certeza": 98,
        "solucion": "Reemplazo urgente de fuente de poder",
        "categoria": "Fuente de Poder"
    },
    
    "R009": {
        "condiciones": ["voltaje_fluctuante", "parpadeo_luces_sistema"],
        "conclusion": "regulador_voltaje_fuente_fallando",
        "certeza": 80,
        "solucion": "Reemplazar fuente o usar estabilizador externo",
        "categoria": "Fuente de Poder"
    },
    
    "R010": {
        "condiciones": ["fuente_enciende", "no_voltaje_12v_rail"],
        "conclusion": "rail_12v_fuente_dañado",
        "certeza": 88,
        "solucion": "Verificar con multímetro y reemplazar fuente",
        "categoria": "Fuente de Poder"
    },
    
    "R011": {
        "condiciones": ["computadora_no_enciende", "boton_encendido_no_responde", "fuente_probada_ok"],
        "conclusion": "boton_power_desconectado",
        "certeza": 75,
        "solucion": "Revisar conexión del botón de encendido",
        "categoria": "Fuente de Poder"
    },
    
    "R012": {
        "condiciones": ["led_standby_encendido", "no_arranca_al_presionar"],
        "conclusion": "señal_power_on_no_llega",
        "certeza": 70,
        "solucion": "Verificar cable power switch a motherboard",
        "categoria": "Fuente de Poder"
    },
    
    "R013": {
        "condiciones": ["fuente_hace_clic", "no_mantiene_encendido"],
        "conclusion": "proteccion_ocp_activada",
        "certeza": 82,
        "solucion": "Reducir carga o reemplazar fuente",
        "categoria": "Fuente de Poder"
    },
    
    "R014": {
        "condiciones": ["conectores_24pin_quemados", "marcas_derretimiento"],
        "conclusion": "sobrecarga_conector_principal",
        "certeza": 92,
        "solucion": "Reemplazar fuente y verificar motherboard",
        "categoria": "Fuente de Poder"
    },
    
    "R015": {
        "condiciones": ["gpu_no_enciende", "conectores_pcie_sin_voltaje"],
        "conclusion": "rails_pcie_fuente_dañados",
        "certeza": 85,
        "solucion": "Reemplazar fuente con rails PCIe funcionales",
        "categoria": "Fuente de Poder"
    },
    
    "R016": {
        "condiciones": ["fuente_silba", "alta_frecuencia_audible"],
        "conclusion": "coil_whine_fuente",
        "certeza": 65,
        "solucion": "Normal pero molesto, considerar reemplazo",
        "categoria": "Fuente de Poder"
    },
    
    "R017": {
        "condiciones": ["olores_plastico_quemado", "fuente_apagada"],
        "conclusion": "aislamiento_cables_derretido",
        "certeza": 88,
        "solucion": "No encender, reemplazar fuente inmediatamente",
        "categoria": "Fuente de Poder"
    },
    
    "R018": {
        "condiciones": ["tester_fuente_indica_ok", "pc_no_enciende"],
        "conclusion": "fuente_funciona_sin_carga_falla_con_carga",
        "certeza": 77,
        "solucion": "Probar fuente bajo carga real",
        "categoria": "Fuente de Poder"
    },
    
    "R019": {
        "condiciones": ["multimetro_muestra_voltajes_bajos", "bajo_carga"],
        "conclusion": "fuente_envejecida_capacidad_reducida",
        "certeza": 83,
        "solucion": "Reemplazar por fuente de calidad",
        "categoria": "Fuente de Poder"
    },
    
    "R020": {
        "condiciones": ["switch_110_220v_incorrecto"],
        "conclusion": "configuracion_voltaje_incorrecta",
        "certeza": 95,
        "solucion": "Ajustar switch según voltaje local",
        "categoria": "Fuente de Poder"
    },
    
    "R021": {
        "condiciones": ["fuente_modular", "cables_mal_conectados"],
        "conclusion": "conexion_modular_incompleta",
        "certeza": 70,
        "solucion": "Verificar todos los cables modulares",
        "categoria": "Fuente de Poder"
    },
    
    "R022": {
        "condiciones": ["ruido_rattling", "vibracion_fuente"],
        "conclusion": "ventilador_desbalanceado",
        "certeza": 72,
        "solucion": "Lubricar o reemplazar ventilador",
        "categoria": "Fuente de Poder"
    },
    
    "R023": {
        "condiciones": ["fuente_enciende_30_segundos", "luego_apaga"],
        "conclusion": "proteccion_termica_activandose",
        "certeza": 80,
        "solucion": "Verificar ventilación y pasta térmica",
        "categoria": "Fuente de Poder"
    },
    
    "R024": {
        "condiciones": ["certificacion_fuente_generica", "problemas_constantes"],
        "conclusion": "fuente_baja_calidad",
        "certeza": 68,
        "solucion": "Invertir en fuente certificada 80 Plus",
        "categoria": "Fuente de Poder"
    },
    
    "R025": {
        "condiciones": ["picos_voltaje", "componentes_dañandose"],
        "conclusion": "falta_proteccion_ovp",
        "certeza": 75,
        "solucion": "Usar fuente con protecciones OVP/UVP",
        "categoria": "Fuente de Poder"
    },
    
    "R026": {
        "condiciones": ["fuente_sata_chispea", "discos_no_detectan"],
        "conclusion": "conector_sata_cortocircuito",
        "certeza": 87,
        "solucion": "Reemplazar cable SATA y verificar fuente",
        "categoria": "Fuente de Poder"
    },
    
    "R027": {
        "condiciones": ["edad_fuente_mas_5_años", "fallos_intermitentes"],
        "conclusion": "fuente_vida_util_agotada",
        "certeza": 73,
        "solucion": "Mantenimiento preventivo: reemplazar fuente",
        "categoria": "Fuente de Poder"
    },
    
    "R028": {
        "condiciones": ["ruido_clicking_ritmico", "rpm_ventilador_bajo"],
        "conclusion": "rodamiento_ventilador_gastado",
        "certeza": 78,
        "solucion": "Reemplazar ventilador preventivamente",
        "categoria": "Fuente de Poder"
    },
    
    "R029": {
        "condiciones": ["molex_derretidos", "cables_calientes"],
        "conclusion": "amperaje_excesivo_molex",
        "certeza": 90,
        "solucion": "No conectar más de 2 dispositivos por molex",
        "categoria": "Fuente de Poder"
    },
    
    "R030": {
        "condiciones": ["fuente_no_certificada", "consumo_alto"],
        "conclusion": "eficiencia_energetica_baja",
        "certeza": 65,
        "solucion": "Actualizar a fuente 80 Plus Bronze o superior",
        "categoria": "Fuente de Poder"
    },
    
    "R031": {
        "condiciones": ["ripple_voltaje_alto", "reseteos_usb"],
        "conclusion": "filtrado_fuente_deficiente",
        "certeza": 76,
        "solucion": "Usar fuente con mejor filtrado",
        "categoria": "Fuente de Poder"
    },
    
    "R032": {
        "condiciones": ["bateria_cmos_descarga_rapida", "fuente_sin_standby"],
        "conclusion": "circuito_standby_fuente_dañado",
        "certeza": 71,
        "solucion": "Verificar modo standby de fuente",
        "categoria": "Fuente de Poder"
    },
    
    "R033": {
        "condiciones": ["cables_rigidos", "mal_manejo_cables"],
        "conclusion": "cables_fuente_baja_calidad",
        "certeza": 60,
        "solucion": "Considerar fuente con cables mallados",
        "categoria": "Fuente de Poder"
    },
    
    "R034": {
        "condiciones": ["fuente_atx_12v", "conector_p4_falta"],
        "conclusion": "incompatibilidad_conector_cpu",
        "certeza": 85,
        "solucion": "Usar adaptador o fuente compatible",
        "categoria": "Fuente de Poder"
    },
    
    "R035": {
        "condiciones": ["gpu_high_end", "fuente_bajo_wattage"],
        "conclusion": "potencia_insuficiente_gpu",
        "certeza": 88,
        "solucion": "Calcular TDP y actualizar fuente",
        "categoria": "Fuente de Poder"
    },
    
    "R036": {
        "condiciones": ["multiples_rails_12v", "una_rail_sobrecargada"],
        "conclusion": "desbalance_carga_rails",
        "certeza": 74,
        "solucion": "Redistribuir conexiones entre rails",
        "categoria": "Fuente de Poder"
    },
    
    "R037": {
        "condiciones": ["fuente_semi_pasiva", "no_arranca_ventilador"],
        "conclusion": "modo_eco_fuente_activo",
        "certeza": 55,
        "solucion": "Normal bajo carga baja, verificar temperatura",
        "categoria": "Fuente de Poder"
    },
    
    "R038": {
        "condiciones": ["interferencia_radio", "fuente_economica"],
        "conclusion": "falta_blindaje_emi",
        "certeza": 63,
        "solucion": "Usar fuente con certificación FCC",
        "categoria": "Fuente de Poder"
    },
    
    "R039": {
        "condiciones": ["factor_forma_sfx", "incompatibilidad_gabinete"],
        "conclusion": "fuente_tamaño_incorrecto",
        "certeza": 92,
        "solucion": "Verificar compatibilidad ATX/SFX/TFX",
        "categoria": "Fuente de Poder"
    },
    
    "R040": {
        "condiciones": ["gpu_sag_extremo", "cables_pcie_tirando"],
        "conclusion": "cables_gpu_muy_rigidos",
        "certeza": 58,
        "solucion": "Usar extensores o cables más flexibles",
        "categoria": "Fuente de Poder"
    },
    
    "R041": {
        "condiciones": ["psu_tester_luz_verde", "pc_no_post"],
        "conclusion": "tester_basico_no_detecta_fallo_carga",
        "certeza": 69,
        "solucion": "Hacer prueba con carga real o multímetro",
        "categoria": "Fuente de Poder"
    },
    
    "R042": {
        "condiciones": ["corrosion_conectores", "ambiente_humedo"],
        "conclusion": "oxidacion_contactos_fuente",
        "certeza": 81,
        "solucion": "Limpiar con alcohol isopropílico y mejorar ventilación",
        "categoria": "Fuente de Poder"
    },
    
    "R043": {
        "condiciones": ["fuente_enciende_solo_con_paperclip"],
        "conclusion": "señal_ps_on_no_recibida",
        "certeza": 79,
        "solucion": "Verificar conexión a motherboard o reemplazar MB",
        "categoria": "Fuente de Poder"
    },
    
    "R044": {
        "condiciones": ["transientes_voltaje", "apagados_instantaneos"],
        "conclusion": "falta_ups_proteccion",
        "certeza": 67,
        "solucion": "Instalar UPS con regulación de voltaje",
        "categoria": "Fuente de Poder"
    },
    
    "R045": {
        "condiciones": ["consumo_electrico_alto", "factura_elevada"],
        "conclusion": "fuente_baja_eficiencia",
        "certeza": 62,
        "solucion": "Migrar a fuente 80 Plus Gold o superior",
        "categoria": "Fuente de Poder"
    },
    
    "R046": {
        "condiciones": ["fuente_no_arranca", "capacitor_hinchado_visible"],
        "conclusion": "capacitor_filtro_dañado",
        "certeza": 94,
        "solucion": "Reemplazar fuente, riesgo de explosión",
        "categoria": "Fuente de Poder"
    },
    
    "R047": {
        "condiciones": ["multiples_gpus", "fuente_single_rail"],
        "conclusion": "rail_12v_sobrecargada",
        "certeza": 77,
        "solucion": "Usar fuente multi-rail o mayor amperaje",
        "categoria": "Fuente de Poder"
    },
    
    "R048": {
        "condiciones": ["fuente_calienta_mucho", "dust_buildup_severo"],
        "conclusion": "obstruccion_flujo_aire_fuente",
        "certeza": 84,
        "solucion": "Limpieza profunda con aire comprimido",
        "categoria": "Fuente de Poder"
    },
    
    "R049": {
        "condiciones": ["leds_rgb_parpadean", "fuente_voltage_drop"],
        "conclusion": "voltaje_5v_inestable",
        "certeza": 72,
        "solucion": "Verificar rail 5V y considerar reemplazo",
        "categoria": "Fuente de Poder"
    },
    
    "R050": {
        "condiciones": ["arranque_lento", "fuente_power_good_delay"],
        "conclusion": "señal_power_good_retrasada",
        "certeza": 68,
        "solucion": "Normal en algunas fuentes, verificar compatibilidad",
        "categoria": "Fuente de Poder"
    },
    
    # ============================================================================
    # CATEGORÍA 2: MOTHERBOARD / PLACA MADRE (60 reglas)
    # ============================================================================
    
    "R051": {
        "condiciones": ["pitido_1_largo_2_cortos", "pantalla_negra"],
        "conclusion": "falla_tarjeta_video_o_slot_pcie",
        "certeza": 87,
        "solucion": "Verificar GPU, probar en otro slot PCIe",
        "categoria": "Motherboard"
    },
    
    "R052": {
        "condiciones": ["pitidos_continuos", "no_post"],
        "conclusion": "falla_memoria_ram_no_detectada",
        "certeza": 90,
        "solucion": "Reinstalar o reemplazar módulos RAM",
        "categoria": "Motherboard"
    },
    
    "R053": {
        "condiciones": ["sin_pitidos", "sin_video", "ventiladores_giran"],
        "conclusion": "motherboard_no_post",
        "certeza": 78,
        "solucion": "Verificar conexiones, hacer reset CMOS",
        "categoria": "Motherboard"
    },
    
    "R054": {
        "condiciones": ["leds_debug_indican_cpu"],
        "conclusion": "cpu_no_detectada_o_dañada",
        "certeza": 85,
        "solucion": "Reinstalar CPU, verificar pines",
        "categoria": "Motherboard"
    },
    
    "R055": {
        "condiciones": ["leds_debug_indican_dram"],
        "conclusion": "problema_slots_ram",
        "certeza": 82,
        "solucion": "Probar RAM en diferentes slots",
        "categoria": "Motherboard"
    },
    
    "R056": {
        "condiciones": ["leds_debug_indican_vga"],
        "conclusion": "problema_deteccion_gpu",
        "certeza": 80,
        "solucion": "Reposicionar GPU, verificar alimentación PCIe",
        "categoria": "Motherboard"
    },
    
    "R057": {
        "condiciones": ["leds_debug_indican_boot"],
        "conclusion": "problema_dispositivo_almacenamiento",
        "certeza": 83,
        "solucion": "Verificar conexión SSD/HDD, revisar BIOS",
        "categoria": "Motherboard"
    },
    
    "R058": {
        "condiciones": ["capacitores_hinchados_motherboard"],
        "conclusion": "capacitores_motherboard_dañados",
        "certeza": 96,
        "solucion": "Reemplazar motherboard o reparar capacitores",
        "categoria": "Motherboard"
    },
    
    "R059": {
        "condiciones": ["manchas_liquido_motherboard", "corrosion_visible"],
        "conclusion": "daño_por_liquido_derramado",
        "certeza": 93,
        "solucion": "Limpieza profesional con ultrasonido o reemplazo",
        "categoria": "Motherboard"
    },
    
    "R060": {
        "condiciones": ["usb_no_funcionan", "todos_puertos_muertos"],
        "conclusion": "controlador_usb_motherboard_dañado",
        "certeza": 81,
        "solucion": "Actualizar drivers o reemplazar motherboard",
        "categoria": "Motherboard"
    },
    
    "R061": {
        "condiciones": ["puerto_ethernet_no_funciona", "led_nic_apagado"],
        "conclusion": "chip_ethernet_integrado_dañado",
        "certeza": 79,
        "solucion": "Usar tarjeta de red PCIe externa",
        "categoria": "Motherboard"
    },
    
    "R062": {
        "condiciones": ["audio_integrado_no_funciona", "crackling_ruido"],
        "conclusion": "codec_audio_motherboard_fallando",
        "certeza": 76,
        "solucion": "Actualizar drivers o usar tarjeta de sonido",
        "categoria": "Motherboard"
    },
    
    "R063": {
        "condiciones": ["slots_pcie_no_detectan_dispositivos"],
        "conclusion": "lanes_pcie_dañadas",
        "certeza": 84,
        "solucion": "Probar otros slots, verificar BIOS",
        "categoria": "Motherboard"
    },
    
    "R064": {
        "condiciones": ["bateria_cmos_descarga_constantemente"],
        "conclusion": "circuito_rtc_motherboard_dañado",
        "certeza": 77,
        "solucion": "Reemplazar batería, si persiste: reparar motherboard",
        "categoria": "Motherboard"
    },
    
    "R065": {
        "condiciones": ["configuracion_bios_no_guarda", "fecha_hora_resetea"],
        "conclusion": "bateria_cmos_agotada",
        "certeza": 88,
        "solucion": "Reemplazar batería CR2032",
        "categoria": "Motherboard"
    },
    
    "R066": {
        "condiciones": ["sobrecalentamiento_vrm", "throttling_cpu"],
        "conclusion": "vrm_motherboard_insuficiente",
        "certeza": 82,
        "solucion": "Mejorar flujo aire, reducir overclock",
        "categoria": "Motherboard"
    },
    
    "R067": {
        "condiciones": ["socket_cpu_pines_doblados"],
        "conclusion": "pines_socket_dañados",
        "certeza": 95,
        "solucion": "Enderezar con herramienta o reemplazar motherboard",
        "categoria": "Motherboard"
    },
    
    "R068": {
        "condiciones": ["slot_ram_no_detecta", "otros_slots_ok"],
        "conclusion": "slot_ram_individual_dañado",
        "certeza": 86,
        "solucion": "Evitar ese slot, considerar RMA si bajo garantía",
        "categoria": "Motherboard"
    },
    
    "R069": {
        "condiciones": ["sata_ports_no_funcionan", "m2_ok"],
        "conclusion": "controladora_sata_dañada",
        "certeza": 80,
        "solucion": "Usar controladora PCIe SATA o puertos funcionales",
        "categoria": "Motherboard"
    },
    
    "R070": {
        "condiciones": ["chipset_muy_caliente", "errores_sistema"],
        "conclusion": "disipador_chipset_insuficiente",
        "certeza": 75,
        "solucion": "Agregar disipador o ventilador adicional",
        "categoria": "Motherboard"
    },
    
    "R071": {
        "condiciones": ["boot_loop_infinito", "no_llega_bios"],
        "conclusion": "bios_corrupto",
        "certeza": 83,
        "solucion": "Flashback BIOS o usar dual BIOS",
        "categoria": "Motherboard"
    },
    
    "R072": {
        "condiciones": ["incompatibilidad_cpu_motherboard"],
        "conclusion": "bios_version_antigua_sin_soporte_cpu",
        "certeza": 91,
        "solucion": "Actualizar BIOS con CPU compatible o flashback",
        "categoria": "Motherboard"
    },
    
    "R073": {
        "condiciones": ["rgb_headers_no_funcionan"],
        "conclusion": "controlador_rgb_motherboard_dañado",
        "certeza": 68,
        "solucion": "Usar controlador RGB externo",
        "categoria": "Motherboard"
    },
    
    "R074": {
        "condiciones": ["ventiladores_no_controlan_velocidad"],
        "conclusion": "headers_fan_sin_pwm",
        "certeza": 64,
        "solucion": "Verificar modo PWM/DC en BIOS o usar hub",
        "categoria": "Motherboard"
    },
    
    "R075": {
        "condiciones": ["m2_nvme_no_detecta", "slot_vacio_funcional"],
        "conclusion": "incompatibilidad_nvme_generacion",
        "certeza": 72,
        "solucion": "Verificar soporte Gen3/Gen4 en manual",
        "categoria": "Motherboard"
    },
    
    "R076": {
        "condiciones": ["post_codes_aa_ff_ciclo"],
        "conclusion": "fallo_inicializacion_hardware",
        "certeza": 78,
        "solucion": "Consultar manual códigos POST específicos",
        "categoria": "Motherboard"
    },
    
    "R077": {
        "condiciones": ["pantalla_artifacts_arranque", "logo_bios_corrupto"],
        "conclusion": "chip_bios_parcialmente_dañado",
        "certeza": 74,
        "solucion": "Reflash BIOS completo",
        "categoria": "Motherboard"
    },
    
    "R078": {
        "condiciones": ["thunderbolt_no_funciona", "otros_usb_ok"],
        "conclusion": "controlador_thunderbolt_problema",
        "certeza": 71,
        "solucion": "Actualizar firmware Thunderbolt",
        "categoria": "Motherboard"
    },
    
    "R079": {
        "condiciones": ["wifi_integrado_no_detecta", "bluetooth_ok"],
        "conclusion": "modulo_wifi_desconectado",
        "certeza": 79,
        "solucion": "Verificar conexión M.2 WIFI o antenas",
        "categoria": "Motherboard"
    },
    
    "R080": {
        "condiciones": ["sensors_motherboard_lecturas_erraticas"],
        "conclusion": "sensores_temperatura_calibracion_perdida",
        "certeza": 62,
        "solucion": "Reset BIOS o ignorar si sistema estable",
        "categoria": "Motherboard"
    },
    
    "R081": {
        "condiciones": ["dual_bios_switch", "no_arranca_bios_principal"],
        "conclusion": "bios_primario_corrupto",
        "certeza": 87,
        "solucion": "Cambiar a BIOS secundario y copiar",
        "categoria": "Motherboard"
    },
    
    "R082": {
        "condiciones": ["overclock_inestable", "crashes_bajo_carga"],
        "conclusion": "vrm_no_soporta_overclock",
        "certeza": 73,
        "solucion": "Reducir voltajes/frecuencias o mejorar cooling VRM",
        "categoria": "Motherboard"
    },
    
    "R083": {
        "condiciones": ["ram_velocidad_limitada", "xmp_no_aplica"],
        "conclusion": "imc_motherboard_limitacion",
        "certeza": 69,
        "solucion": "Ajustar timings manualmente o cambiar motherboard",
        "categoria": "Motherboard"
    },
    
    "R084": {
        "condiciones": ["pcie_lanes_deshabilitadas", "configuracion_bios_incorrecta"],
        "conclusion": "bifurcation_pcie_mal_configurado",
        "certeza": 76,
        "solucion": "Ajustar PCIe bifurcation en BIOS",
        "categoria": "Motherboard"
    },
    
    "R085": {
        "condiciones": ["headers_argb_5v_3pin", "dispositivo_12v_conectado"],
        "conclusion": "incompatibilidad_voltaje_rgb",
        "certeza": 89,
        "solucion": "No mezclar 5V y 12V RGB, riesgo de daño",
        "categoria": "Motherboard"
    },
    
    "R086": {
        "condiciones": ["tpm_no_detecta", "windows_11_incompatible"],
        "conclusion": "tpm_deshabilitado_bios",
        "certeza": 82,
        "solucion": "Habilitar fTPM/PTT en BIOS",
        "categoria": "Motherboard"
    },
    
    "R087": {
        "condiciones": ["secure_boot_error", "no_bootea_os"],
        "conclusion": "configuracion_secure_boot_incorrecta",
        "certeza": 78,
        "solucion": "Deshabilitar Secure Boot o configurar keys",
        "categoria": "Motherboard"
    },
    
    "R088": {
        "condiciones": ["csm_legacy_problemas", "arranque_lento"],
        "conclusion": "modo_arranque_mixto_conflicto",
        "certeza": 70,
        "solucion": "Usar solo UEFI o solo Legacy",
        "categoria": "Motherboard"
    },
    
    "R089": {
        "condiciones": ["multi_gpu_no_detecta_segunda"],
        "conclusion": "sli_crossfire_no_habilitado",
        "certeza": 75,
        "solucion": "Habilitar multi-GPU en BIOS",
        "categoria": "Motherboard"
    },
    
    "R090": {
        "condiciones": ["resizable_bar_no_funciona", "gpu_compatible"],
        "conclusion": "resizable_bar_deshabilitado",
        "certeza": 73,
        "solucion": "Habilitar Above 4G y Re-BAR en BIOS",
        "categoria": "Motherboard"
    },
    
    "R091": {
        "condiciones": ["smart_access_memory_no_activa"],
        "conclusion": "configuracion_sam_incompleta",
        "certeza": 71,
        "solucion": "Verificar CPU/GPU AMD y habilitar en BIOS",
        "categoria": "Motherboard"
    },
    
    "R092": {
        "condiciones": ["virtualizacion_no_funciona", "vt_x_vt_d_necesaria"],
        "conclusion": "virtualizacion_deshabilitada_bios",
        "certeza": 85,
        "solucion": "Habilitar VT-x/AMD-V en BIOS",
        "categoria": "Motherboard"
    },
    
    "R093": {
        "condiciones": ["motherboard_forma_atx", "gabinete_micro_atx"],
        "conclusion": "incompatibilidad_form_factor",
        "certeza": 98,
        "solucion": "Verificar compatibilidad gabinete antes comprar",
        "categoria": "Motherboard"
    },
    
    "R094": {
        "condiciones": ["quemadura_visible_pcb", "circuito_expuesto"],
        "conclusion": "corto_circuito_motherboard",
        "certeza": 97,
        "solucion": "Reemplazo obligatorio de motherboard",
        "categoria": "Motherboard"
    },
    
    "R095": {
        "condiciones": ["standoffs_mal_ubicados", "short_circuito"],
        "conclusion": "tornillo_instalacion_cortocircuito",
        "certeza": 88,
        "solucion": "Verificar posición standoffs según form factor",
        "categoria": "Motherboard"
    },
    
    "R096": {
        "condiciones": ["io_shield_falta", "interferencia_electrica"],
        "conclusion": "emi_sin_io_shield",
        "certeza": 59,
        "solucion": "Instalar IO shield para blindaje adecuado",
        "categoria": "Motherboard"
    },
    
    "R097": {
        "condiciones": ["post_speaker_no_pitidos", "funcionamiento_normal"],
        "conclusion": "motherboard_sin_speaker_integrado",
        "certeza": 66,
        "solucion": "Instalar speaker externo para diagnósticos",
        "categoria": "Motherboard"
    },
    
    "R098": {
        "condiciones": ["headers_usb_20_conectados_30"],
        "conclusion": "incompatibilidad_headers_usb",
        "certeza": 81,
        "solucion": "Conectar según versión correcta USB",
        "categoria": "Motherboard"
    },
    
    "R099": {
        "condiciones": ["front_panel_mal_conectado", "leds_no_funcionan"],
        "conclusion": "conexion_front_panel_incorrecta",
        "certeza": 77,
        "solucion": "Consultar manual y reconectar según diagrama",
        "categoria": "Motherboard"
    },
    
    "R100": {
        "condiciones": ["hd_audio_ac97_confusion", "audio_frontal_no_funciona"],
        "conclusion": "header_audio_incorrecto",
        "certeza": 74,
        "solucion": "Usar HD Audio en motherboards modernas",
        "categoria": "Motherboard"
    },
    
    "R101": {
        "condiciones": ["oc_profile_corrupto", "no_arranca_tras_oc"],
        "conclusion": "perfil_overclock_inestable",
        "certeza": 80,
        "solucion": "Clear CMOS y reconfigurar overclock gradualmente",
        "categoria": "Motherboard"
    },
    
    "R102": {
        "condiciones": ["bios_actualizacion_interrumpida", "brick_motherboard"],
        "conclusion": "bios_flash_fallido",
        "certeza": 94,
        "solucion": "Usar BIOS flashback o servicio técnico",
        "categoria": "Motherboard"
    },
    
    "R103": {
        "condiciones": ["debug_led_permanente_amarillo"],
        "conclusion": "hardware_especifico_fallando",
        "certeza": 79,
        "solucion": "Consultar manual debug LED específico modelo",
        "categoria": "Motherboard"
    },
    
    "R104": {
        "condiciones": ["ventilador_cpu_rpm_0", "cable_conectado"],
        "conclusion": "header_cpu_fan_dañado",
        "certeza": 76,
        "solucion": "Conectar a otro header y configurar en BIOS",
        "categoria": "Motherboard"
    },
    
    "R105": {
        "condiciones": ["esd_damage_visible", "componente_quemado_puntual"],
        "conclusion": "descarga_estatica_componente",
        "certeza": 86,
        "solucion": "Prevención: usar pulsera antiestática",
        "categoria": "Motherboard"
    },
    
    "R106": {
        "condiciones": ["northbridge_extremadamente_caliente"],
        "conclusion": "pasta_termica_chipset_seca",
        "certeza": 72,
        "solucion": "Reaplicar pasta térmica en chipset",
        "categoria": "Motherboard"
    },
    
    "R107": {
        "condiciones": ["compatibility_list_cpu_no_incluida"],
        "conclusion": "cpu_no_soportada_oficialmente",
        "certeza": 83,
        "solucion": "Verificar QVL antes de comprar componentes",
        "categoria": "Motherboard"
    },
    
    "R108": {
        "condiciones": ["bios_f_keys_no_responden"],
        "conclusion": "teclado_no_inicializa_bios",
        "certeza": 69,
        "solucion": "Usar puerto USB 2.0 o teclado PS/2",
        "categoria": "Motherboard"
    },
    
    "R109": {
        "condiciones": ["optane_memory_no_detecta"],
        "conclusion": "configuracion_rst_incorrecta",
        "certeza": 75,
        "solucion": "Habilitar Intel RST en BIOS",
        "categoria": "Motherboard"
    },
    
    "R110": {
        "condiciones": ["zen_architecture", "ram_no_dual_channel"],
        "conclusion": "configuracion_ram_sub_optima",
        "certeza": 71,
        "solucion": "Instalar RAM en slots A2/B2 para dual channel",
        "categoria": "Motherboard"
    },
    
    # ============================================================================
    # CATEGORÍA 3: PROCESADOR / CPU (40 reglas)
    # ============================================================================
    
    "R111": {
        "condiciones": ["sobrecalentamiento_cpu", "thermal_throttling"],
        "conclusion": "disipador_insuficiente_o_mal_instalado",
        "certeza": 88,
        "solucion": "Verificar montaje, aplicar pasta térmica",
        "categoria": "CPU"
    },
    
    "R112": {
        "condiciones": ["temperaturas_cpu_95_grados", "stock_cooler"],
        "conclusion": "cooler_stock_insuficiente",
        "certeza": 82,
        "solucion": "Actualizar a cooler tower o AIO",
        "categoria": "CPU"
    },
    
    "R113": {
        "condiciones": ["pines_cpu_doblados", "no_post"],
        "conclusion": "cpu_amd_pines_dañados",
        "certeza": 91,
        "solucion": "Enderezar con cuidado o reemplazar CPU",
        "categoria": "CPU"
    },
    
    "R114": {
        "condiciones": ["contactos_cpu_quemados", "marca_arco_electrico"],
        "conclusion": "short_circuit_cpu",
        "certeza": 96,
        "solucion": "Reemplazar CPU y verificar motherboard",
        "categoria": "CPU"
    },
    
    "R115": {
        "condiciones": ["crashes_bajo_carga", "stress_test_falla"],
        "conclusion": "cpu_inestable_o_degradada",
        "certeza": 79,
        "solucion": "Reducir overclock o RMA si bajo garantía",
        "categoria": "CPU"
    },
    
    "R116": {
        "condiciones": ["frecuencia_cpu_bloqueada_baja"],
        "conclusion": "power_limit_throttling",
        "certeza": 76,
        "solucion": "Ajustar power limits en BIOS",
        "categoria": "CPU"
    },
    
    "R117": {
        "condiciones": ["vcore_muy_alto", "degradacion_rapida"],
        "conclusion": "voltaje_cpu_excesivo",
        "certeza": 84,
        "solucion": "Reducir voltaje inmediatamente",
        "categoria": "CPU"
    },
    
    "R118": {
        "condiciones": ["single_core_bajo_rendimiento"],
        "conclusion": "nucleo_cpu_defectuoso",
        "certeza": 73,
        "solucion": "Deshabilitar núcleo problema o RMA",
        "categoria": "CPU"
    },
    
    "R119": {
        "condiciones": ["ihs_despegado", "temperaturas_erraticas"],
        "conclusion": "delid_cpu_problema_tim",
        "certeza": 81,
        "solucion": "Relid con adhesivo o metal líquido",
        "categoria": "CPU"
    },
    
    "R120": {
        "condiciones": ["thermal_paste_seca", "5_años_uso"],
        "conclusion": "pasta_termica_envejecida",
        "certeza": 86,
        "solucion": "Limpiar y reaplicar pasta térmica",
        "categoria": "CPU"
    },
    
    "R121": {
        "condiciones": ["mounting_pressure_desigual", "hotspot_extremo"],
        "conclusion": "cooler_mal_montado_presion",
        "certeza": 78,
        "solucion": "Remontar cooler con presión uniforme",
        "categoria": "CPU"
    },
    
    "R122": {
        "condiciones": ["plastic_peel_no_removido", "100_grados"],
        "conclusion": "proteccion_plastica_cooler_instalada",
        "certeza": 99,
        "solucion": "Remover film protector de base cooler",
        "categoria": "CPU"
    },
    
    "R123": {
        "condiciones": ["backplate_falta", "cooler_flojo"],
        "conclusion": "backplate_instalacion_incompleta",
        "certeza": 87,
        "solucion": "Instalar backplate según manual",
        "categoria": "CPU"
    },
    
    "R124": {
        "condiciones": ["retention_bracket_roto"],
        "conclusion": "bracket_cpu_dañado",
        "certeza": 84,
        "solucion": "Reemplazar bracket o usar cooler diferente",
        "categoria": "CPU"
    },
    
    "R125": {
        "condiciones": ["avx_workloads_crash", "normal_workloads_ok"],
        "conclusion": "inestabilidad_avx_offset_necesario",
        "certeza": 77,
        "solucion": "Aumentar AVX offset o voltaje",
        "categoria": "CPU"
    },
    
    "R126": {
        "condiciones": ["cinebench_score_50_percent_esperado"],
        "conclusion": "throttling_severo_cpu",
        "certeza": 83,
        "solucion": "Revisar temperaturas y power limits",
        "categoria": "CPU"
    },
    
    "R127": {
        "condiciones": ["cpu_usage_100_percent_idle"],
        "conclusion": "proceso_malware_cpu",
        "certeza": 71,
        "solucion": "Escanear malware, revisar task manager",
        "categoria": "CPU"
    },
    
    "R128": {
        "condiciones": ["cpu_downclocking_constante", "power_plan_balanced"],
        "conclusion": "power_plan_limitando_rendimiento",
        "certeza": 74,
        "solucion": "Cambiar a plan alto rendimiento",
        "categoria": "CPU"
    },
    
    "R129": {
        "condiciones": ["vdroop_excesivo", "crashes_boost"],
        "conclusion": "llc_load_line_calibration_bajo",
        "certeza": 72,
        "solucion": "Aumentar LLC en BIOS gradualmente",
        "categoria": "CPU"
    },
    
    "R130": {
        "condiciones": ["whea_errors_cache", "event_viewer"],
        "conclusion": "cache_cpu_errores",
        "certeza": 80,
        "solucion": "Reducir overclock o RMA CPU",
        "categoria": "CPU"
    },
    
    "R131": {
        "condiciones": ["bsod_clock_watchdog_timeout"],
        "conclusion": "overclock_cpu_inestable",
        "certeza": 82,
        "solucion": "Aumentar voltaje o reducir frecuencia",
        "categoria": "CPU"
    },
    
    "R132": {
        "condiciones": ["microcode_update_falta", "vulnerabilidades"],
        "conclusion": "bios_microcode_desactualizado",
        "certeza": 69,
        "solucion": "Actualizar BIOS para parches seguridad",
        "categoria": "CPU"
    },
    
    "R133": {
        "condiciones": ["spectre_meltdown_mitigations", "perdida_rendimiento"],
        "conclusion": "parches_seguridad_impacto",
        "certeza": 68,
        "solucion": "Trade-off seguridad vs rendimiento",
        "categoria": "CPU"
    },
    
    "R134": {
        "condiciones": ["hyperthreading_deshabilitado_bios"],
        "conclusion": "smt_ht_desactivado",
        "certeza": 79,
        "solucion": "Habilitar HT/SMT para mejor multitarea",
        "categoria": "CPU"
    },
    
    "R135": {
        "condiciones": ["cores_parked_windows"],
        "conclusion": "cpu_core_parking_activo",
        "certeza": 73,
        "solucion": "Deshabilitar core parking para latencia",
        "categoria": "CPU"
    },
    
    "R136": {
        "condiciones": ["turbo_boost_no_activa"],
        "conclusion": "turbo_deshabilitado_bios",
        "certeza": 81,
        "solucion": "Habilitar Intel Turbo Boost o AMD PBO",
        "categoria": "CPU"
    },
    
    "R137": {
        "condiciones": ["precision_boost_overdrive_inestable"],
        "conclusion": "pbo_limites_agresivos",
        "certeza": 75,
        "solucion": "Ajustar límites PBO conservadoramente",
        "categoria": "CPU"
    },
    
    "R138": {
        "condiciones": ["curve_optimizer_crashes"],
        "conclusion": "undervolting_agresivo",
        "certeza": 78,
        "solucion": "Reducir curve optimizer offset",
        "categoria": "CPU"
    },
    
    "R139": {
        "condiciones": ["fclk_uclk_desync"],
        "conclusion": "infinity_fabric_ratio_incorrecto",
        "certeza": 70,
        "solucion": "Sincronizar FCLK con MCLK 1:1",
        "categoria": "CPU"
    },
    
    "R140": {
        "condiciones": ["ring_ratio_muy_alto", "cache_errors"],
        "conclusion": "uncore_overclock_inestable",
        "certeza": 74,
        "solucion": "Reducir cache/ring ratio",
        "categoria": "CPU"
    },
    
    "R141": {
        "condiciones": ["sa_vccio_muy_bajo", "memory_training_falla"],
        "conclusion": "voltajes_auxiliares_insuficientes",
        "certeza": 76,
        "solucion": "Aumentar SA y VCCIO ligeramente",
        "categoria": "CPU"
    },
    
    "R142": {
        "condiciones": ["degradacion_silicon", "requiere_mas_voltaje"],
        "conclusion": "cpu_envejecimiento_normal",
        "certeza": 67,
        "solucion": "Aceptar o reducir overclock permanentemente",
        "categoria": "CPU"
    },
    
    "R143": {
        "condiciones": ["golden_sample_lottery_perdido"],
        "conclusion": "silicon_lottery_chip_mediocre",
        "certeza": 58,
        "solucion": "Normal, no todos chips overclock igual",
        "categoria": "CPU"
    },
    
    "R144": {
        "condiciones": ["socket_lga_contacto_pobre"],
        "conclusion": "ihs_no_contacta_uniformemente",
        "certeza": 72,
        "solucion": "Verificar flatness IHS y coldplate",
        "categoria": "CPU"
    },
    
    "R145": {
        "condiciones": ["liquid_metal_derrame", "short_capacitors"],
        "conclusion": "metal_liquido_conductivo_derramado",
        "certeza": 93,
        "solucion": "Limpiar inmediatamente, aplicar barniz protector",
        "categoria": "CPU"
    },
    
    "R146": {
        "condiciones": ["capacitor_decoupling_cpu_dañado"],
        "conclusion": "caps_cerca_socket_problema",
        "certeza": 85,
        "solucion": "Reparación nivel motherboard o reemplazo",
        "categoria": "CPU"
    },
    
    "R147": {
        "condiciones": ["socket_am4_palanca_rota"],
        "conclusion": "mecanismo_retention_dañado",
        "certeza": 89,
        "solucion": "Reemplazar motherboard, crítico para contacto",
        "categoria": "CPU"
    },
    
    "R148": {
        "condiciones": ["bending_lga1700", "hotspot_cpu"],
        "conclusion": "socket_curvatura_lga1700",
        "certeza": 77,
        "solucion": "Usar contact frame o washer mod",
        "categoria": "CPU"
    },
    
    "R149": {
        "condiciones": ["tjmax_alcanzado", "thermal_shutdown"],
        "conclusion": "temperatura_maxima_junction",
        "certeza": 94,
        "solucion": "Apagar inmediatamente, revisar cooling",
        "categoria": "CPU"
    },
    
    "R150": {
        "condiciones": ["dts_sensor_reading_negativa"],
        "conclusion": "sensor_temperatura_malfuncion",
        "certeza": 66,
        "solucion": "Ignorar lectura o actualizar BIOS",
        "categoria": "CPU"
    },
    
    # ============================================================================
    # CATEGORÍA 4: MEMORIA RAM (50 reglas)
    # ============================================================================
    
    "R151": {
        "condiciones": ["pantalla_azul_memory_management"],
        "conclusion": "falla_memoria_ram",
        "certeza": 83,
        "solucion": "Ejecutar memtest86, reemplazar módulo defectuoso",
        "categoria": "RAM"
    },
    
    "R152": {
        "condiciones": ["computadora_pitidos_intermitentes", "no_video"],
        "conclusion": "ram_mal_instalada_o_sucia",
        "certeza": 81,
        "solucion": "Limpiar contactos con goma, reinstalar firmemente",
        "categoria": "RAM"
    },
    
    "R153": {
        "condiciones": ["memtest_errores_miles"],
        "conclusion": "modulo_ram_defectuoso",
        "certeza": 95,
        "solucion": "Identificar y reemplazar módulo con errores",
        "categoria": "RAM"
    },
    
    "R154": {
        "condiciones": ["sistema_detecta_menos_ram_instalada"],
        "conclusion": "modulo_no_reconocido_o_slot_dañado",
        "certeza": 79,
        "solucion": "Probar módulo en otro slot, verificar compatibilidad",
        "categoria": "RAM"
    },
    
    "R155": {
        "condiciones": ["xmp_profile_no_estable", "crashes_aleatorios"],
        "conclusion": "xmp_requiere_ajuste_manual",
        "certeza": 76,
        "solucion": "Aumentar voltaje DRAM o aflojar timings",
        "categoria": "RAM"
    },
    
    "R156": {
        "condiciones": ["ram_3600mhz", "solo_corre_2133mhz"],
        "conclusion": "xmp_docp_no_habilitado",
        "certeza": 88,
        "solucion": "Activar XMP/DOCP en BIOS",
        "categoria": "RAM"
    },
    
    "R157": {
        "condiciones": ["dual_channel_no_activo", "ram_slots_incorrectos"],
        "conclusion": "configuracion_dual_channel_incorrecta",
        "certeza": 84,
        "solucion": "Instalar en slots A2/B2 o según manual",
        "categoria": "RAM"
    },
    
    "R158": {
        "condiciones": ["quad_channel_no_detecta"],
        "conclusion": "poblacion_canales_incompleta",
        "certeza": 78,
        "solucion": "Instalar 4 módulos para quad channel",
        "categoria": "RAM"
    },
    
    "R159": {
        "condiciones": ["mixing_ram_different_speeds"],
        "conclusion": "ram_mixta_corre_velocidad_menor",
        "certeza": 72,
        "solucion": "Normal, sistema usa velocidad más baja",
        "categoria": "RAM"
    },
    
    "R160": {
        "condiciones": ["mixing_ram_different_brands", "inestabilidad"],
        "conclusion": "incompatibilidad_ram_mixta",
        "certeza": 74,
        "solucion": "Usar kits matched para mejor estabilidad",
        "categoria": "RAM"
    },
    
    "R161": {
        "condiciones": ["ecc_ram_non_ecc_motherboard"],
        "conclusion": "incompatibilidad_ecc",
        "certeza": 91,
        "solucion": "Verificar soporte ECC en motherboard",
        "categoria": "RAM"
    },
    
    "R162": {
        "condiciones": ["single_rank_vs_dual_rank", "rendimiento_diferente"],
        "conclusion": "configuracion_rank_impacta_rendimiento",
        "certeza": 69,
        "solucion": "Preferir dual rank para Ryzen",
        "categoria": "RAM"
    },
    
    "R163": {
        "condiciones": ["ram_sobrecalentamiento", "crashes_gaming"],
        "conclusion": "temperatura_ram_excesiva",
        "certeza": 71,
        "solucion": "Agregar ventilación o reducir voltaje",
        "categoria": "RAM"
    },
    
    "R164": {
        "condiciones": ["heatsink_ram_contacto_cooler"],
        "conclusion": "disipador_ram_choca_cooler_cpu",
        "certeza": 82,
        "solucion": "Usar RAM low profile o cambiar cooler",
        "categoria": "RAM"
    },
    
    "R165": {
        "condiciones": ["rgb_ram_luces_muertas", "funciona_normal"],
        "conclusion": "leds_ram_dañados",
        "certeza": 68,
        "solucion": "Cosmético, funcional no afectado",
        "categoria": "RAM"
    },
    
    "R166": {
        "condiciones": ["ram_4_sticks_no_estable", "2_sticks_ok"],
        "conclusion": "imc_estres_4_dimms",
        "certeza": 77,
        "solucion": "Aumentar voltaje SOC/SA o reducir frecuencia",
        "categoria": "RAM"
    },
    
    "R167": {
        "condiciones": ["samsung_b_die", "mejor_overclock"],
        "conclusion": "ic_ram_calidad_superior",
        "certeza": 73,
        "solucion": "B-die permite timings ajustados",
        "categoria": "RAM"
    },
    
    "R168": {
        "condiciones": ["hynix_cjr_djr", "sweet_spot_3600"],
        "conclusion": "ic_especifico_caracteristicas",
        "certeza": 65,
        "solucion": "Investigar IC para optimizar OC",
        "categoria": "RAM"
    },
    
    "R169": {
        "condiciones": ["gear_1_vs_gear_2", "intel_12gen"],
        "conclusion": "memory_gear_ratio_latencia",
        "certeza": 70,
        "solucion": "Gear 1 mejor latencia, Gear 2 más frecuencia",
        "categoria": "RAM"
    },
    
    "R170": {
        "condiciones": ["trfc_muy_bajo", "errores_memoria"],
        "conclusion": "timing_refresh_agresivo",
        "certeza": 75,
        "solucion": "Aumentar tRFC para estabilidad",
        "categoria": "RAM"
    },
    
    "R171": {
        "condiciones": ["primary_timings_sueltos", "bajo_rendimiento"],
        "conclusion": "timings_no_optimizados",
        "certeza": 68,
        "solucion": "Ajustar CL, tRCD, tRP manualmente",
        "categoria": "RAM"
    },
    
    "R172": {
        "condiciones": ["command_rate_2t", "latencia_alta"],
        "conclusion": "cr_no_optimizado",
        "certeza": 66,
        "solucion": "Intentar command rate 1T con más voltaje",
        "categoria": "RAM"
    },
    
    "R173": {
        "condiciones": ["vdimm_1_5v", "degradacion_ram"],
        "conclusion": "voltaje_ram_muy_alto",
        "certeza": 79,
        "solucion": "Mantenerbajo 1.45V para longevidad DDR4",
        "categoria": "RAM"
    },
    
    "R174": {
        "condiciones": ["capacidad_32gb_reconoce_16gb"],
        "conclusion": "limite_capacidad_motherboard_cpu",
        "certeza": 81,
        "solucion": "Verificar máx capacidad soportada",
        "categoria": "RAM"
    },
    
    "R175": {
        "condiciones": ["windows_32bit", "ram_mas_4gb_no_usable"],
        "conclusion": "limitacion_so_32bits",
        "certeza": 96,
        "solucion": "Migrar a Windows 64-bit",
        "categoria": "RAM"
    },
    
    "R176": {
        "condiciones": ["page_file_disabled", "ram_insuficiente_errors"],
        "conclusion": "memoria_virtual_deshabilitada",
        "certeza": 74,
        "solucion": "Habilitar page file o agregar RAM",
        "categoria": "RAM"
    },
    
    "R177": {
        "condiciones": ["memory_leak_aplicacion"],
        "conclusion": "software_mal_programado",
        "certeza": 72,
        "solucion": "Actualizar aplicación o reportar bug",
        "categoria": "RAM"
    },
    
    "R178": {
        "condiciones": ["ram_usage_95_percent", "sistema_lento"],
        "conclusion": "ram_insuficiente_workload",
        "certeza": 86,
        "solucion": "Agregar más RAM",
        "categoria": "RAM"
    },
    
    "R179": {
        "condiciones": ["ddr3_slot_ddr4_ram"],
        "conclusion": "incompatibilidad_generacion_ram",
        "certeza": 99,
        "solucion": "Usar generación correcta (físicamente incompatible)",
        "categoria": "RAM"
    },
    
    "R180": {
        "condiciones": ["sodimm_laptop_dimm_desktop"],
        "conclusion": "factor_forma_ram_incorrecto",
        "certeza": 98,
        "solucion": "SO-DIMM para laptop, DIMM para desktop",
        "categoria": "RAM"
    },
    
    "R181": {
        "condiciones": ["parity_error_ecc_ram"],
        "conclusion": "bit_flip_detectado_corregido",
        "certeza": 77,
        "solucion": "ECC funcionando, monitorear frecuencia",
        "categoria": "RAM"
    },
    
    "R182": {
        "condiciones": ["uncorrectable_ecc_error"],
        "conclusion": "error_multi_bit_ram",
        "certeza": 89,
        "solucion": "Reemplazar módulo urgentemente",
        "categoria": "RAM"
    },
    
    "R183": {
        "condiciones": ["registered_rdimm_unbuffered_udimm"],
        "conclusion": "tipo_ram_servidor_incompatible",
        "certeza": 92,
        "solucion": "Verificar requerimiento registered vs unbuffered",
        "categoria": "RAM"
    },
    
    "R184": {
        "condiciones": ["oxidacion_contactos_ram", "no_detecta"],
        "conclusion": "corrosion_pines_ram",
        "certeza": 80,
        "solucion": "Limpiar con goma blanca suavemente",
        "categoria": "RAM"
    },
    
    "R185": {
        "condiciones": ["ram_suelta_slot", "conexion_intermitente"],
        "conclusion": "clips_retencion_debiles",
        "certeza": 75,
        "solucion": "Asegurar clips totalmente cerrados",
        "categoria": "RAM"
    },
    
    "R186": {
        "condiciones": ["qvl_lista_ram_no_incluida"],
        "conclusion": "ram_no_validada_fabricante",
        "certeza": 64,
        "solucion": "No garantiza incompatibilidad, pero puede ayudar",
        "categoria": "RAM"
    },
    
    "R187": {
        "condiciones": ["blue_screen_irql_not_less_or_equal"],
        "conclusion": "driver_o_ram_problema",
        "certeza": 70,
        "solucion": "Actualizar drivers y testear RAM",
        "categoria": "RAM"
    },
    
    "R188": {
        "condiciones": ["ram_fake_counterfeit", "problemas_multiples"],
        "conclusion": "ram_falsificada",
        "certeza": 73,
        "solucion": "Comprar de fuentes confiables solamente",
        "categoria": "RAM"
    },
    
    "R189": {
        "condiciones": ["advertised_latency_real_diferente"],
        "conclusion": "spd_vs_xmp_timings",
        "certeza": 67,
        "solucion": "Habilitar XMP para timings anunciados",
        "categoria": "RAM"
    },
    
    "R190": {
        "condiciones": ["ram_subtimings_auto", "rendimiento_suboptimo"],
        "conclusion": "secondary_tertiary_timings_flojos",
        "certeza": 62,
        "solucion": "Ajustar manualmente con presets conocidos",
        "categoria": "RAM"
    },
    
    "R191": {
        "condiciones": ["thaiphoon_burner_lectura", "ic_identificacion"],
        "conclusion": "identificar_chips_ram_overclock",
        "certeza": 71,
        "solucion": "Usar Thaiphoon para saber IC específico",
        "categoria": "RAM"
    },
    
    "R192": {
        "condiciones": ["testmem5_anta_extreme", "errores_sutiles"],
        "conclusion": "test_stress_exhaustivo_necesario",
        "certeza": 74,
        "solucion": "TM5 más exigente que memtest86",
        "categoria": "RAM"
    },
    
    "R193": {
        "condiciones": ["karhu_ramtest_errors"],
        "conclusion": "inestabilidad_ram_detectada",
        "certeza": 78,
        "solucion": "Relajar timings o aumentar voltaje",
        "categoria": "RAM"
    },
    
    "R194": {
        "condiciones": ["prime95_blend_errors", "ram_overclock"],
        "conclusion": "stress_cpu_ram_conjunto_inestable",
        "certeza": 76,
        "solucion": "Ajustar OC RAM o CPU individualmente",
        "categoria": "RAM"
    },
    
    "R195": {
        "condiciones": ["gaming_stutters", "ram_baja_velocidad"],
        "conclusion": "ram_cuello_botella_ryzen",
        "certeza": 69,
        "solucion": "Ryzen se beneficia de RAM rápida 3600+",
        "categoria": "RAM"
    },
    
    "R196": {
        "condiciones": ["intel_alder_lake", "ddr4_ddr5_eleccion"],
        "conclusion": "plataforma_dual_ram_soporte",
        "certeza": 73,
        "solucion": "Elegir motherboard según tipo RAM",
        "categoria": "RAM"
    },
    
    "R197": {
        "condiciones": ["ddr5_early_adoption", "precios_altos"],
        "conclusion": "nueva_generacion_prima_precio",
        "certeza": 66,
        "solucion": "Esperar madurez mercado o usar DDR4",
        "categoria": "RAM"
    },
    
    "R198": {
        "condiciones": ["ddr5_voltage_1_1v", "no_mucho_overclock"],
        "conclusion": "ddr5_margen_oc_inicial_limitado",
        "certeza": 63,
        "solucion": "Generación temprana, mejorará con tiempo",
        "categoria": "RAM"
    },
    
    "R199": {
        "condiciones": ["on_die_ecc_ddr5"],
        "conclusion": "ddr5_correccion_errores_integrada",
        "certeza": 68,
        "solucion": "Mayor confiabilidad vs DDR4",
        "categoria": "RAM"
    },
    
    "R200": {
        "condiciones": ["capacity_128gb_kit", "precio_prohibitivo"],
        "conclusion": "alta_capacidad_workstation",
        "certeza": 71,
        "solucion": "Evaluar necesidad real vs costo",
        "categoria": "RAM"
    },
    
    # ============================================================================
    # CATEGORÍA 5: ALMACENAMIENTO - HDD/SSD (60 reglas)
    # ============================================================================
    
    "R201": {
        "condiciones": ["hdd_clicking_sound", "no_detecta"],
        "conclusion": "fallo_mecanico_hdd_click_muerte",
        "certeza": 94,
        "solucion": "Recuperación datos profesional, reemplazar HDD",
        "categoria": "Almacenamiento"
    },
    
    "R202": {
        "condiciones": ["hdd_grinding_noise", "acceso_lento"],
        "conclusion": "cabezal_lectura_dañado",
        "certeza": 91,
        "solucion": "Backup inmediato, reemplazo urgente",
        "categoria": "Almacenamiento"
    },
    
    "R203": {
        "condiciones": ["smart_reallocated_sectors_alto"],
        "conclusion": "sectores_defectuosos_hdd",
        "certeza": 88,
        "solucion": "Backup y monitoreo, considerar reemplazo",
        "categoria": "Almacenamiento"
    },
    
    "R204": {
        "condiciones": ["smart_pending_sectors", "warnings"],
        "conclusion": "sectores_pendientes_remapeo",
        "certeza": 82,
        "solucion": "Escribir en disco para forzar remapeo",
        "categoria": "Almacenamiento"
    },
    
    "R205": {
        "condiciones": ["crystaldiskinfo_caution_warning"],
        "conclusion": "salud_disco_deteriorada",
        "certeza": 84,
        "solucion": "Backup urgente, planificar reemplazo",
        "categoria": "Almacenamiento"
    },
    
    "R206": {
        "condiciones": ["ssd_nvme_no_detecta", "m2_instalado"],
        "conclusion": "incompatibilidad_m2_key",
        "certeza": 79,
        "solucion": "Verificar M.2 M-key vs B-key",
        "categoria": "Almacenamiento"
    },
    
    "R207": {
        "condiciones": ["ssd_sata_no_aparece_bios"],
        "conclusion": "cable_sata_dañado_o_puerto_malo",
        "certeza": 77,
        "solucion": "Cambiar cable y probar otro puerto SATA",
        "categoria": "Almacenamiento"
    },
    
    "R208": {
        "condiciones": ["ssd_rendimiento_degradado", "80_percent_lleno"],
        "conclusion": "ssd_sin_espacio_overprovisioning",
        "certeza": 76,
        "solucion": "Mantener 10-20% espacio libre",
        "categoria": "Almacenamiento"
    },
    
    "R209": {
        "condiciones": ["ssd_escrituras_lentas", "cache_slc_lleno"],
        "conclusion": "cache_dinamico_agotado",
        "certeza": 74,
        "solucion": "Normal en SSDs económicos bajo carga",
        "categoria": "Almacenamiento"
    },
    
    "R210": {
        "condiciones": ["trim_no_habilitado", "ssd_lento"],
        "conclusion": "trim_deshabilitado",
        "certeza": 81,
        "solucion": "Habilitar TRIM en sistema operativo",
        "categoria": "Almacenamiento"
    },
    
    "R211": {
        "condiciones": ["ssd_temperatura_80_grados"],
        "conclusion": "thermal_throttling_ssd",
        "certeza": 85,
        "solucion": "Agregar disipador M.2 o mejorar flujo",
        "categoria": "Almacenamiento"
    },
    
    "R212": {
        "condiciones": ["nvme_pcie_gen4", "motherboard_gen3"],
        "conclusion": "bottleneck_generacion_pcie",
        "certeza": 73,
        "solucion": "Funciona pero a velocidad Gen3",
        "categoria": "Almacenamiento"
    },
    
    "R213": {
        "condiciones": ["qlc_nand_ssd", "escrituras_pesadas"],
        "conclusion": "qlc_no_apropiado_uso_intensivo",
        "certeza": 70,
        "solucion": "Preferir TLC o MLC para workloads pesados",
        "categoria": "Almacenamiento"
    },
    
    "R214": {
        "condiciones": ["dram_cache_ssd_no_tiene"],
        "conclusion": "ssd_dram_less_menor_rendimiento",
        "certeza": 67,
        "solucion": "Suficiente para uso casual, no profesional",
        "categoria": "Almacenamiento"
    },
    
    "R215": {
        "condiciones": ["hmb_host_memory_buffer_activo"],
        "conclusion": "ssd_usa_ram_sistema",
        "certeza": 66,
        "solucion": "Alternativa a DRAM onboard en SSD",
        "categoria": "Almacenamiento"
    },
    
    "R216": {
        "condiciones": ["write_amplification_muy_alto"],
        "conclusion": "garbage_collection_ineficiente",
        "certeza": 72,
        "solucion": "Mantener espacio libre, habilitar TRIM",
        "categoria": "Almacenamiento"
    },
    
    "R217": {
        "condiciones": ["tbw_terabytes_written_excedido"],
        "conclusion": "vida_util_ssd_agotada",
        "certeza": 83,
        "solucion": "Funciona pero fuera de garantía, reemplazar",
        "categoria": "Almacenamiento"
    },
    
    "R218": {
        "condiciones": ["raid_array_degraded", "disco_fallando"],
        "conclusion": "miembro_raid_fallo",
        "certeza": 87,
        "solucion": "Reemplazar disco y reconstruir array",
        "categoria": "Almacenamiento"
    },
    
    "R219": {
        "condiciones": ["raid_0_disco_fallo", "datos_perdidos"],
        "conclusion": "raid_0_sin_redundancia",
        "certeza": 96,
        "solucion": "Restaurar desde backup, RAID 0 = sin protección",
        "categoria": "Almacenamiento"
    },
    
    "R220": {
        "condiciones": ["raid_5_dos_discos_fallan"],
        "conclusion": "raid_5_solo_tolera_un_fallo",
        "certeza": 94,
        "solucion": "Datos irrecuperables, restaurar backup",
        "categoria": "Almacenamiento"
    },
    
    "R221": {
        "condiciones": ["inicializacion_lenta_hdd", "5400rpm"],
        "conclusion": "hdd_baja_velocidad_rotacion",
        "certeza": 69,
        "solucion": "Normal para 5400RPM, considerar 7200RPM o SSD",
        "categoria": "Almacenamiento"
    },
    
    "R222": {
        "condiciones": ["fragmentacion_disco_alta"],
        "conclusion": "hdd_necesita_desfragmentacion",
        "certeza": 75,
        "solucion": "Desfragmentar HDD (NO hacer en SSD)",
        "categoria": "Almacenamiento"
    },
    
    "R223": {
        "condiciones": ["ssd_desfragmentado_accidentalmente"],
        "conclusion": "ciclos_escritura_ssd_desperdiciados",
        "certeza": 78,
        "solucion": "No crítico una vez, evitar en futuro",
        "categoria": "Almacenamiento"
    },
    
    "R224": {
        "condiciones": ["particion_sistema_100_llena"],
        "conclusion": "disco_c_sin_espacio",
        "certeza": 91,
        "solucion": "Limpiar archivos temporales, mover datos",
        "categoria": "Almacenamiento"
    },
    
    "R225": {
        "condiciones": ["disco_clonar_mayor_menor"],
        "conclusion": "destino_insuficiente_clonacion",
        "certeza": 86,
        "solucion": "Reducir partición o usar disco mayor",
        "categoria": "Almacenamiento"
    },
    
    "R226": {
        "condiciones": ["mbr_disco_mayor_2tb"],
        "conclusion": "mbr_limita_2tb_usar_gpt",
        "certeza": 93,
        "solucion": "Convertir a GPT para discos >2TB",
        "categoria": "Almacenamiento"
    },
    
    "R227": {
        "condiciones": ["gpt_bios_legacy", "no_bootea"],
        "conclusion": "gpt_requiere_uefi",
        "certeza": 89,
        "solucion": "Usar MBR con Legacy o GPT con UEFI",
        "categoria": "Almacenamiento"
    },
    
    "R228": {
        "condiciones": ["bootmgr_missing"],
        "conclusion": "gestor_arranque_dañado",
        "certeza": 84,
        "solucion": "Reparar boot con medios instalación Windows",
        "categoria": "Almacenamiento"
    },
    
    "R229": {
        "condiciones": ["no_bootable_device"],
        "conclusion": "orden_boot_incorrecto_o_disco_muerto",
        "certeza": 82,
        "solucion": "Verificar orden boot BIOS y estado disco",
        "categoria": "Almacenamiento"
    },
    
    "R230": {
        "condiciones": ["operating_system_not_found"],
        "conclusion": "particion_boot_no_activa",
        "certeza": 79,
        "solucion": "Marcar partición como activa o reparar",
        "categoria": "Almacenamiento"
    },
    
    "R231": {
        "condiciones": ["disk_read_error"],
        "conclusion": "error_lectura_disco_hardware",
        "certeza": 88,
        "solucion": "Verificar cables, SMART, considerar fallo",
        "categoria": "Almacenamiento"
    },
    
    "R232": {
        "condiciones": ["scandisk_errores_filesystem"],
        "conclusion": "sistema_archivos_corrupto",
        "certeza": 81,
        "solucion": "Ejecutar chkdsk /f /r desde recovery",
        "categoria": "Almacenamiento"
    },
    
    "R233": {
        "condiciones": ["bad_pool_header_bsod"],
        "conclusion": "driver_disco_o_ram_problema",
        "certeza": 72,
        "solucion": "Actualizar driver almacenamiento y testear RAM",
        "categoria": "Almacenamiento"
    },
    
    "R234": {
        "condiciones": ["external_hdd_no_reconoce", "luz_encendida"],
        "conclusion": "problema_driver_o_letra_unidad",
        "certeza": 74,
        "solucion": "Disk Management asignar letra manualmente",
        "categoria": "Almacenamiento"
    },
    
    "R235": {
        "condiciones": ["external_hdd_clicks", "no_enciende_luz"],
        "conclusion": "fuente_poder_externa_insuficiente",
        "certeza": 80,
        "solucion": "Usar adaptador correcto amperaje",
        "categoria": "Almacenamiento"
    },
    
    "R236": {
        "condiciones": ["usb_hdd_desconecta_solo"],
        "conclusion": "ahorro_energia_usb_suspendiendo",
        "certeza": 76,
        "solucion": "Deshabilitar suspensión selectiva USB",
        "categoria": "Almacenamiento"
    },
    
    "R237": {
        "condiciones": ["nas_drive_desktop_pc"],
        "conclusion": "firmware_nas_optimizado_diferente",
        "certeza": 68,
        "solucion": "Funcionará pero no óptimo, preferir uso indicado",
        "categoria": "Almacenamiento"
    },
    
    "R238": {
        "condiciones": ["smr_drive_raid", "rendimiento_pesimo"],
        "conclusion": "smr_no_apropiado_raid",
        "certeza": 84,
        "solucion": "Usar CMR drives para RAID/NAS",
        "categoria": "Almacenamiento"
    },
    
    "R239": {
        "condiciones": ["helium_hdd_alta_capacidad"],
        "conclusion": "tecnologia_helium_mayor_densidad",
        "certeza": 71,
        "solucion": "Discos 10TB+ generalmente helium",
        "categoria": "Almacenamiento"
    },
    
    "R240": {
        "condiciones": ["ssd_trim_raid"],
        "conclusion": "trim_no_soportado_algunos_raids",
        "certeza": 73,
        "solucion": "Verificar compatibilidad TRIM con RAID",
        "categoria": "Almacenamiento"
    },
    
    "R241": {
        "condiciones": ["optane_memory_acceleracion"],
        "conclusion": "cache_hdd_con_optane",
        "certeza": 76,
        "solucion": "Mejora HDD pero no igual que SSD puro",
        "categoria": "Almacenamiento"
    },
    
    "R242": {
        "condiciones": ["storemi_amd", "ssd_hdd_tier"],
        "conclusion": "fusion_almacenamiento_amd",
        "certeza": 69,
        "solucion": "StoreMI combina SSD+HDD inteligentemente",
        "categoria": "Almacenamiento"
    },
    
    "R243": {
        "condiciones": ["secure_erase_ssd_falla"],
        "conclusion": "frozen_state_ssd",
        "certeza": 77,
        "solucion": "Sleep PC y reintentar secure erase",
        "categoria": "Almacenamiento"
    },
    
    "R244": {
        "condiciones": ["ssd_firmware_outdated"],
        "conclusion": "actualizacion_firmware_ssd_disponible",
        "certeza": 70,
        "solucion": "Actualizar firmware para correcciones/mejoras",
        "categoria": "Almacenamiento"
    },
    
    "R245": {
        "condiciones": ["nvme_pcie_adapter", "no_booteable"],
        "conclusion": "bios_no_soporta_boot_nvme_adapter",
        "certeza": 74,
        "solucion": "Verificar soporte boot o usar como secundario",
        "categoria": "Almacenamiento"
    },
    
    "R246": {
        "condiciones": ["usb_3_0_velocidad_usb_2"],
        "conclusion": "puerto_o_cable_usb_2_limitando",
        "certeza": 81,
        "solucion": "Verificar puerto azul USB 3.0 y cable compatible",
        "categoria": "Almacenamiento"
    },
    
    "R247": {
        "condiciones": ["type_c_usb_ssd_no_funciona"],
        "conclusion": "cable_type_c_solo_carga",
        "certeza": 72,
        "solucion": "Usar cable USB-C con soporte datos",
        "categoria": "Almacenamiento"
    },
    
    "R248": {
        "condiciones": ["thunderbolt_ssd_no_detecta"],
        "conclusion": "certificacion_thunderbolt_falta",
        "certeza": 70,
        "solucion": "Verificar dispositivo certificado Thunderbolt",
        "categoria": "Almacenamiento"
    },
    
    "R249": {
        "condiciones": ["wear_leveling_count_bajo"],
        "conclusion": "desgaste_ssd_avanzado",
        "certeza": 80,
        "solucion": "Monitorear y preparar reemplazo",
        "categoria": "Almacenamiento"
    },
    
    "R250": {
        "condiciones": ["power_on_hours_50000"],
        "conclusion": "disco_antiguo_alto_uso",
        "certeza": 75,
        "solucion": "5+ años, considerar reemplazo preventivo",
        "categoria": "Almacenamiento"
    },
    
    "R251": {
        "condiciones": ["uncorrectable_sector_count_incrementa"],
        "conclusion": "sectores_irrecuperables_apareciendo",
        "certeza": 91,
        "solucion": "Fallo inminente, backup inmediato",
        "categoria": "Almacenamiento"
    },
    
    "R252": {
        "condiciones": ["ssd_brick_firmware_bug"],
        "conclusion": "bug_firmware_modelo_especifico",
        "certeza": 78,
        "solucion": "Investigar modelo, RMA si es issue conocido",
        "categoria": "Almacenamiento"
    },
    
    "R253": {
        "condiciones": ["sata_3_port_sata_2_ssd"],
        "conclusion": "retrocompatibilidad_sata",
        "certeza": 68,
        "solucion": "Funciona pero limitado a velocidad SATA 2",
        "categoria": "Almacenamiento"
    },
    
    "R254": {
        "condiciones": ["ahci_mode_vs_ide"],
        "conclusion": "modo_sata_bios_suboptimo",
        "certeza": 79,
        "solucion": "Usar AHCI para SSDs, no IDE mode",
        "categoria": "Almacenamiento"
    },
    
    "R255": {
        "condiciones": ["hot_swap_sata_sin_preparar"],
        "conclusion": "extraccion_disco_sin_safe_remove",
        "certeza": 73,
        "solucion": "Siempre expulsar antes de remover",
        "categoria": "Almacenamiento"
    },
    
    "R256": {
        "condiciones": ["m2_sata_vs_m2_nvme_confusion"],
        "conclusion": "m2_dos_protocolos_diferentes",
        "certeza": 83,
        "solucion": "Verificar slot soporta SATA y/o NVMe",
        "categoria": "Almacenamiento"
    },
    
    "R257": {
        "condiciones": ["pcie_lanes_compartidas", "nvme_reduce_gpu"],
        "conclusion": "bifurcacion_lanes_conflicto",
        "certeza": 75,
        "solucion": "Consultar manual lanes compartidas",
        "categoria": "Almacenamiento"
    },
    
    "R258": {
        "condiciones": ["ssd_cache_vs_ssd_principal"],
        "conclusion": "diferencia_uso_cache_storage",
        "certeza": 64,
        "solucion": "Cache acelera, storage es destino final",
        "categoria": "Almacenamiento"
    },
    
    "R259": {
        "condiciones": ["directstorage_windows_11", "nvme_necesario"],
        "conclusion": "tecnologia_carga_rapida_gaming",
        "certeza": 69,
        "solucion": "NVMe Gen4 recomendado para DirectStorage",
        "categoria": "Almacenamiento"
    },
    
    "R260": {
        "condiciones": ["bitlocker_ssd_rendimiento"],
        "conclusion": "encriptacion_impacto_minimo_hardware",
        "certeza": 67,
        "solucion": "CPUs modernos: encriptación sin impacto notable",
        "categoria": "Almacenamiento"
    },
    
    # ============================================================================
    # CATEGORÍA 6: TARJETA GRÁFICA / GPU (60 reglas)
    # ============================================================================
    
    "R261": {
        "condiciones": ["gpu_no_video", "ventiladores_giran"],
        "conclusion": "gpu_no_detectada_o_dañada",
        "certeza": 82,
        "solucion": "Verificar conexión PCIe, probar en otro slot",
        "categoria": "GPU"
    },
    
    "R262": {
        "condiciones": ["gpu_artifacts_pantalla", "lineas_colores"],
        "conclusion": "vram_gpu_defectuosa",
        "certeza": 87,
        "solucion": "RMA GPU, VRAM dañada no reparable",
        "categoria": "GPU"
    },
    
    "R263": {
        "condiciones": ["gpu_sobrecalentamiento_95_grados"],
        "conclusion": "pasta_termica_gpu_seca",
        "certeza": 84,
        "solucion": "Repaste GPU y limpieza ventiladores",
        "categoria": "GPU"
    },
    
    "R264": {
        "condiciones": ["gpu_crashes_gaming", "driver_timeout"],
        "conclusion": "driver_gpu_inestable",
        "certeza": 76,
        "solucion": "DDU clean install drivers",
        "categoria": "GPU"
    },
    
    "R265": {
        "condiciones": ["gpu_fans_100_percent", "ruido_excesivo"],
        "conclusion": "curva_ventiladores_agresiva",
        "certeza": 71,
        "solucion": "Ajustar curva con MSI Afterburner",
        "categoria": "GPU"
    },
    
    "R266": {
        "condiciones": ["gpu_fans_no_giran", "idle_ok"],
        "conclusion": "zero_rpm_mode_activo",
        "certeza": 69,
        "solucion": "Normal, fans se activan bajo carga",
        "categoria": "GPU"
    },
    
    "R267": {
        "condiciones": ["gpu_sag_severo", "slot_stress"],
        "conclusion": "gpu_pesada_sin_soporte",
        "certeza": 80,
        "solucion": "Usar anti-sag bracket o soporte",
        "categoria": "GPU"
    },
    
    "R268": {
        "condiciones": ["pcie_power_no_conectado", "error_boot"],
        "conclusion": "alimentacion_pcie_faltante",
        "certeza": 93,
        "solucion": "Conectar todos cables PCIe 6/8 pines",
        "categoria": "GPU"
    },
    
    "R269": {
        "condiciones": ["gpu_throttling", "power_limit_alcanzado"],
        "conclusion": "tdp_gpu_limitando_rendimiento",
        "certeza": 78,
        "solucion": "Aumentar power limit si cooling permite",
        "categoria": "GPU"
    },
    
    "R270": {
        "condiciones": ["gpu_under_clocking", "temp_limit_alcanzado"],
        "conclusion": "thermal_throttling_gpu",
        "certeza": 86,
        "solucion": "Mejorar cooling, repaste, airflow",
        "categoria": "GPU"
    },
    
    "R271": {
        "condiciones": ["black_screen_gaming", "fans_gpu_max"],
        "conclusion": "crash_gpu_o_driver",
        "certeza": 79,
        "solucion": "Verificar temperaturas, reinstalar drivers",
        "categoria": "GPU"
    },
    
    "R272": {
        "condiciones": ["gpu_coil_whine", "carga_alta"],
        "conclusion": "inductores_gpu_vibrando",
        "certeza": 74,
        "solucion": "Normal pero molesto, limitar FPS ayuda",
        "categoria": "GPU"
    },
    
    "R273": {
        "condiciones": ["dual_gpu_sli_no_scale"],
        "conclusion": "juego_sin_soporte_sli",
        "certeza": 72,
        "solucion": "SLI muerto, usar single GPU potente",
        "categoria": "GPU"
    },
    
    "R274": {
        "condiciones": ["raytracing_on_fps_bajo"],
        "conclusion": "rt_cores_demandante",
        "certeza": 70,
        "solucion": "Normal, RT costoso, usar DLSS si disponible",
        "categoria": "GPU"
    },
    
    "R275": {
        "condiciones": ["dlss_borroso", "calidad_performance"],
        "conclusion": "dlss_modo_agresivo",
        "certeza": 66,
        "solucion": "Cambiar a DLSS Quality para más nitidez",
        "categoria": "GPU"
    },
    
    "R276": {
        "condiciones": ["fsr_amd_nvidia_gpu"],
        "conclusion": "fsr_agnóstico_funciona_ambas",
        "certeza": 73,
        "solucion": "FSR funciona en cualquier GPU",
        "categoria": "GPU"
    },
    
    "R277": {
        "condiciones": ["hdmi_2_1_no_4k_120hz"],
        "conclusion": "cable_hdmi_version_antigua",
        "certeza": 81,
        "solucion": "Usar cable HDMI 2.1 certificado ultra high speed",
        "categoria": "GPU"
    },
    
    "R278": {
        "condiciones": ["displayport_no_señal"],
        "conclusion": "cable_dp_defectuoso",
        "certeza": 75,
        "solucion": "Probar otro cable DisplayPort",
        "categoria": "GPU"
    },
    
    "R279": {
        "condiciones": ["multiple_monitors_uno_no_detecta"],
        "conclusion": "puerto_gpu_especifico_dañado",
        "certeza": 77,
        "solucion": "Usar otro puerto GPU",
        "categoria": "GPU"
    },
    
    "R280": {
        "condiciones": ["igpu_dgpu_conflicto"],
        "conclusion": "grafica_integrada_discreta_confusion",
        "certeza": 74,
        "solucion": "Deshabilitar iGPU en BIOS si no se usa",
        "categoria": "GPU"
    },
    
    "R281": {
        "condiciones": ["monitor_conectado_motherboard", "gpu_instalada"],
        "conclusion": "video_sale_igpu_no_gpu",
        "certeza": 89,
        "solucion": "Conectar monitor a puertos GPU",
        "categoria": "GPU"
    },
    
    "R282": {
        "condiciones": ["gpu_bios_switch_posicion_incorrecta"],
        "conclusion": "bios_secundario_modo_silencioso",
        "certeza": 68,
        "solucion": "Verificar switch BIOS en OC position",
        "categoria": "GPU"
    },
    
    "R283": {
        "condiciones": ["vram_insuficiente_juego"],
        "conclusion": "texturas_altas_exceden_vram",
        "certeza": 83,
        "solucion": "Reducir calidad texturas o upgrade GPU",
        "categoria": "GPU"
    },
    
    "R284": {
        "condiciones": ["mining_gpu_segunda_mano"],
        "conclusion": "gpu_minado_desgaste_alto",
        "certeza": 72,
        "solucion": "Revisar exhaustivamente antes de comprar",
        "categoria": "GPU"
    },
    
    "R285": {
        "condiciones": ["gpu_repaste_mejora_20_grados"],
        "conclusion": "pasta_original_muy_mala",
        "certeza": 80,
        "solucion": "Repaste recommended para GPUs usadas",
        "categoria": "GPU"
    },
    
    "R286": {
        "condiciones": ["thermal_pads_deteriorados"],
        "conclusion": "vram_sin_contacto_termico",
        "certeza": 78,
        "solucion": "Reemplazar thermal pads con grosor correcto",
        "categoria": "GPU"
    },
    
    "R287": {
        "condiciones": ["gpu_backplate_caliente"],
        "conclusion": "vram_trasera_sin_cooling",
        "certeza": 71,
        "solucion": "Agregar thermal pads a backplate",
        "categoria": "GPU"
    },
    
    "R288": {
        "condiciones": ["rtx_3080_crashes", "capacitor_issue"],
        "conclusion": "poscaps_vs_mlcc_problema_lanzamiento",
        "certeza": 69,
        "solucion": "Actualizar VBIOS o RMA modelo afectado",
        "categoria": "GPU"
    },
    
    "R289": {
        "condiciones": ["radeon_driver_timeout", "polaris_gpu"],
        "conclusion": "driver_amd_issue_conocido",
        "certeza": 67,
        "solucion": "Ajustar TDR delay registro Windows",
        "categoria": "GPU"
    },
    
    "R290": {
        "condiciones": ["nvidia_driver_clean_install_ddu"],
        "conclusion": "restos_driver_anterior_conflictos",
        "certeza": 82,
        "solucion": "Siempre usar DDU en safe mode",
        "categoria": "GPU"
    },
    
    "R291": {
        "condiciones": ["cuda_no_disponible"],
        "conclusion": "cuda_toolkit_no_instalado",
        "certeza": 76,
        "solucion": "Instalar CUDA toolkit de NVIDIA",
        "categoria": "GPU"
    },
    
    "R292": {
        "condiciones": ["opencl_benchmark_bajo"],
        "conclusion": "opencl_drivers_optimizacion",
        "certeza": 64,
        "solucion": "Actualizar drivers para mejor OpenCL",
        "categoria": "GPU"
    },
    
    "R293": {
        "condiciones": ["vulkan_no_funciona"],
        "conclusion": "vulkan_runtime_falta",
        "certeza": 73,
        "solucion": "Instalar Vulkan runtime library",
        "categoria": "GPU"
    },
    
    "R294": {
        "condiciones": ["directx_12_not_supported"],
        "conclusion": "gpu_muy_antigua_dx12",
        "certeza": 81,
        "solucion": "GPU pre-2015 generalmente sin DX12",
        "categoria": "GPU"
    },
    
    "R295": {
        "condiciones": ["gpu_encoding_nvenc_no_detecta"],
        "conclusion": "nvenc_deshabilitado_o_driver",
        "certeza": 70,
        "solucion": "Verificar GPU tiene NVENC y drivers actualizados",
        "categoria": "GPU"
    },
    
    "R296": {
        "condiciones": ["obs_encoding_overload"],
        "conclusion": "preset_encoding_muy_alto",
        "certeza": 72,
        "solucion": "Usar NVENC/VCE en vez CPU encoding",
        "categoria": "GPU"
    },
    
    "R297": {
        "condiciones": ["freesync_nvidia_gpu"],
        "conclusion": "gsync_compatible_freesync",
        "certeza": 74,
        "solucion": "Muchos monitores FreeSync funcionan con NVIDIA",
        "categoria": "GPU"
    },
    
    "R298": {
        "condiciones": ["gsync_module_vs_compatible"],
        "conclusion": "gsync_nativo_vs_adaptative_sync",
        "certeza": 67,
        "solucion": "Ambos funcionan, G-Sync nativo más caro",
        "categoria": "GPU"
    },
    
    "R299": {
        "condiciones": ["screen_tearing_vsync_off"],
        "conclusion": "sincronizacion_vertical_desactivada",
        "certeza": 79,
        "solucion": "Activar VSync, G-Sync o FreeSync",
        "categoria": "GPU"
    },
    
    "R300": {
        "condiciones": ["input_lag_vsync_on"],
        "conclusion": "vsync_introduce_latencia",
        "certeza": 75,
        "solucion": "Usar G-Sync/FreeSync para menos lag",
        "categoria": "GPU"
    },
    
    "R301": {
        "condiciones": ["gpu_bios_flash_falla"],
        "conclusion": "brick_gpu_bios_corrupto",
        "certeza": 88,
        "solucion": "Dual BIOS switch o programador hardware",
        "categoria": "GPU"
    },
    
    "R302": {
        "condiciones": ["pcie_riser_cable_problemas"],
        "conclusion": "riser_calidad_baja_señal",
        "certeza": 77,
        "solucion": "Usar riser blindado Gen3/Gen4 calidad",
        "categoria": "GPU"
    },
    
    "R303": {
        "condiciones": ["crypto_mining_damage_gpu"],
        "conclusion": "overclock_24_7_desgaste",
        "certeza": 71,
        "solucion": "Inspeccionar VRM, capacitors, fans",
        "categoria": "GPU"
    },
    
    "R304": {
        "condiciones": ["lhr_lite_hash_rate"],
        "conclusion": "nvidia_limiter_mining",
        "certeza": 73,
        "solucion": "Limitación intencional Ethereum mining",
        "categoria": "GPU"
    },
    
    "R305": {
        "condiciones": ["watercooled_gpu_leak"],
        "conclusion": "aio_gpu_fuga_liquido",
        "certeza": 92,
        "solucion": "Apagar inmediatamente, secar, RMA",
        "categoria": "GPU"
    },
    
    "R306": {
        "condiciones": ["vrm_gpu_sobrecalentamiento"],
        "conclusion": "mosfets_gpu_sin_cooling_adecuado",
        "certeza": 79,
        "solucion": "Agregar heatsinks pequeños a VRM",
        "categoria": "GPU"
    },
    
    "R307": {
        "condiciones": ["pcie_4_0_x8_vs_x16"],
        "conclusion": "ancho_banda_reducido_mitad",
        "certeza": 69,
        "solucion": "Impacto mínimo GPUs actuales en x8",
        "categoria": "GPU"
    },
    
    "R308": {
        "condiciones": ["resizable_bar_mejora_fps"],
        "conclusion": "rebar_sam_beneficio_juegos",
        "certeza": 68,
        "solucion": "Habilitar en BIOS para 5-10% mejora",
        "categoria": "GPU"
    },
    
    "R309": {
        "condiciones": ["gpu_benchmark_scores_bajos"],
        "conclusion": "bottleneck_cpu_ram_otros",
        "certeza": 72,
        "solucion": "Identificar cuello botella sistema",
        "categoria": "GPU"
    },
    
    "R310": {
        "condiciones": ["furmark_crash_gpu"],
        "conclusion": "power_virus_stress_extremo",
        "certeza": 70,
        "solucion": "FurMark extremo, usar tests realistas",
        "categoria": "GPU"
    },
    
    # ============================================================================
    # CATEGORÍA 7: REFRIGERACIÓN / COOLING (40 reglas)
    # ============================================================================
    
    "R311": {
        "condiciones": ["temperaturas_altas_todas", "ventiladores_lentos"],
        "conclusion": "flujo_aire_inadecuado",
        "certeza": 84,
        "solucion": "Configurar fans: frente intake, atrás exhaust",
        "categoria": "Refrigeración"
    },
    
    "R312": {
        "condiciones": ["dust_buildup_severo", "temps_altas"],
        "conclusion": "polvo_obstruyendo_cooling",
        "certeza": 89,
        "solucion": "Limpieza profunda con aire comprimido",
        "categoria": "Refrigeración"
    },
    
    "R313": {
        "condiciones": ["aio_pump_ruido_gorgoteo"],
        "conclusion": "aire_atrapado_sistema_liquido",
        "certeza": 81,
        "solucion": "Reposicionar radiador pump arriba",
        "categoria": "Refrigeración"
    },
    
    "R314": {
        "condiciones": ["aio_pump_no_funciona"],
        "conclusion": "bomba_aio_muerta",
        "certeza": 87,
        "solucion": "Reemplazar AIO urgente, usar stock temporalmente",
        "categoria": "Refrigeración"
    },
    
    "R315": {
        "condiciones": ["custom_loop_leak_test_falla"],
        "conclusion": "conexion_fitting_floja",
        "certeza": 86,
        "solucion": "Apretar fittings, leak test 24h",
        "categoria": "Refrigeración"
    },
    
    "R316": {
        "condiciones": ["aio_radiator_top_mount", "caso_positivo"],
        "conclusion": "configuracion_radiador_optima",
        "certeza": 72,
        "solucion": "Top exhaust común, tubing abajo mejor",
        "categoria": "Refrigeración"
    },
    
    "R317": {
        "condiciones": ["fan_hub_no_detecta"],
        "conclusion": "hub_ventiladores_sin_power",
        "certeza": 78,
        "solucion": "Conectar SATA power a fan hub",
        "categoria": "Refrigeración"
    },
    
    "R318": {
        "condiciones": ["pwm_fans_dc_header"],
        "conclusion": "incompatibilidad_control_ventilador",
        "certeza": 74,
        "solucion": "PWM 4-pin, DC 3-pin, verificar header",
        "categoria": "Refrigeración"
    },
    
    "R319": {
        "condiciones": ["noctua_fans_ruido_minimo"],
        "conclusion": "ventiladores_premium_silenciosos",
        "certeza": 71,
        "solucion": "Noctua referencia calidad/silencio",
        "categoria": "Refrigeración"
    },
    
    "R320": {
        "condiciones": ["static_pressure_vs_airflow"],
        "conclusion": "tipo_fan_segun_uso",
        "certeza": 69,
        "solucion": "Static para radiadores, airflow para case",
        "categoria": "Refrigeración"
    },
    
    "R321": {
        "condiciones": ["positive_pressure_vs_negative"],
        "conclusion": "presion_case_balance",
        "certeza": 67,
        "solucion": "Positive reduce polvo, negative mejor temps",
        "categoria": "Refrigeración"
    },
    
    "R322": {
        "condiciones": ["cable_management_malo", "flujo_bloqueado"],
        "conclusion": "cables_obstruyendo_airflow",
        "certeza": 76,
        "solucion": "Organizar cables detras motherboard tray",
        "categoria": "Refrigeración"
    },
    
    "R323": {
        "condiciones": ["mesh_front_panel_vs_solid"],
        "conclusion": "mesh_mejor_airflow",
        "certeza": 73,
        "solucion": "Frente mesh mejora intake significativamente",
        "categoria": "Refrigeración"
    },
    
    "R324": {
        "condiciones": ["small_form_factor_temps_altas"],
        "conclusion": "itx_case_cooling_limitado",
        "certeza": 78,
        "solucion": "SFF requiere planning cooling cuidadoso",
        "categoria": "Refrigeración"
    },
    
    "R325": {
        "condiciones": ["open_bench_table"],
        "conclusion": "sin_case_mejor_cooling",
        "certeza": 70,
        "solucion": "Excelente cooling pero sin protección polvo",
        "categoria": "Refrigeración"
    },
    
    "R326": {
        "condiciones": ["thermal_paste_application_demasiado"],
        "conclusion": "exceso_pasta_termica",
        "certeza": 68,
        "solucion": "Grano arroz suficiente, no bañar",
        "categoria": "Refrigeración"
    },
    
    "R327": {
        "condiciones": ["thermal_paste_application_insuficiente"],
        "conclusion": "cobertura_incompleta",
        "certeza": 72,
        "solucion": "Debe cubrir toda IHS al montar",
        "categoria": "Refrigeración"
    },
    
    "R328": {
        "condiciones": ["thermal_grizzly_kryonaut", "rendimiento_top"],
        "conclusion": "pasta_premium_alto_rendimiento",
        "certeza": 66,
        "solucion": "1-3°C mejor que pastas comunes",
        "categoria": "Refrigeración"
    },
    
    "R329": {
        "condiciones": ["liquid_metal_aplicacion"],
        "conclusion": "metal_liquido_mejor_conductividad",
        "certeza": 74,
        "solucion": "5-10°C mejor pero riesgoso aplicar",
        "categoria": "Refrigeración"
    },
    
    "R330": {
        "condiciones": ["liquid_metal_aluminum_heatsink"],
        "conclusion": "aluminio_metal_liquido_reaccion",
        "certeza": 94,
        "solucion": "NUNCA usar con aluminio, solo cobre/níquel",
        "categoria": "Refrigeración"
    },
    
    "R331": {
        "condiciones": ["tower_cooler_vs_aio_240mm"],
        "conclusion": "rendimiento_comparable_precio",
        "certeza": 69,
        "solucion": "Tower high-end compite con AIO 240mm",
        "categoria": "Refrigeración"
    },
    
    "R332": {
        "condiciones": ["aio_360mm_overkill"],
        "conclusion": "diminishing_returns_cooling",
        "certeza": 64,
        "solucion": "280mm suficiente mayoría casos",
        "categoria": "Refrigeración"
    },
    
    "R333": {
        "condiciones": ["fans_140mm_vs_120mm"],
        "conclusion": "140mm_mas_aire_menos_ruido",
        "certeza": 71,
        "solucion": "140mm mejor si case soporta",
        "categoria": "Refrigeración"
    },
    
    "R334": {
        "condiciones": ["fan_rpm_very_high", "ruido_excesivo"],
        "conclusion": "curva_ventiladores_agresiva",
        "certeza": 77,
        "solucion": "Ajustar curva menos pendiente",
        "categoria": "Refrigeración"
    },
    
    "R335": {
        "condiciones": ["fan_bearing_ruido"],
        "conclusion": "rodamiento_ventilador_desgaste",
        "certeza": 79,
        "solucion": "Reemplazar ventilador preventivamente",
        "categoria": "Refrigeración"
    },
    
    "R336": {
        "condiciones": ["magnetic_levitation_fans"],
        "conclusion": "maglev_fans_durabilidad",
        "certeza": 68,
        "solucion": "Maglev más caros pero duran más",
        "categoria": "Refrigeración"
    },
    
    "R337": {
        "condiciones": ["rgb_fans_vs_performance"],
        "conclusion": "rgb_añade_peso_costo",
        "certeza": 62,
        "solucion": "Priorizar performance sobre estética",
        "categoria": "Refrigeración"
    },
    
    "R338": {
        "condiciones": ["ambient_temperature_35_grados"],
        "conclusion": "temperatura_ambiente_alta",
        "certeza": 83,
        "solucion": "AC o cooling mejorado, límites físicos",
        "categoria": "Refrigeración"
    },
    
    "R339": {
        "condiciones": ["case_ventilation_holes_bloqueados"],
        "conclusion": "ventilacion_obstruida_ubicacion",
        "certeza": 80,
        "solucion": "Dejar espacio alrededor del case",
        "categoria": "Refrigeración"
    },
    
    "R340": {
        "condiciones": ["dust_filters_sucios"],
        "conclusion": "filtros_necesitan_limpieza",
        "certeza": 85,
        "solucion": "Limpiar filtros mensualmente",
        "categoria": "Refrigeración"
    },
    
    "R341": {
        "condiciones": ["passive_cooling_case"],
        "conclusion": "fanless_design_limitado",
        "certeza": 73,
        "solucion": "Solo viable low power systems",
        "categoria": "Refrigeración"
    },
    
    "R342": {
        "condiciones": ["watercooling_maintenance_never"],
        "conclusion": "liquido_refrigerante_envejecido",
        "certeza": 76,
        "solucion": "Custom loops: cambiar coolant anualmente",
        "categoria": "Refrigeración"
    },
    
    "R343": {
        "condiciones": ["radiator_thickness_slim_vs_thick"],
        "conclusion": "radiadores_gruesos_mejor_disipacion",
        "certeza": 70,
        "solucion": "Si case permite, thick radiator mejor",
        "categoria": "Refrigeración"
    },
    
    "R344": {
        "condiciones": ["push_vs_pull_configuration"],
        "conclusion": "push_pull_maximo_rendimiento",
        "certeza": 68,
        "solucion": "Push-pull 2-5°C mejor pero costoso",
        "categoria": "Refrigeración"
    },
    
    "R345": {
        "condiciones": ["vrm_heatsink_ausente"],
        "conclusion": "motherboard_budget_sin_disipadores",
        "certeza": 75,
        "solucion": "Agregar cooling VRM si overclock",
        "categoria": "Refrigeración"
    },
    
    "R346": {
        "condiciones": ["chipset_fan_failure"],
        "conclusion": "ventilador_chipset_pequeno_murio",
        "certeza": 78,
        "solucion": "Reemplazar o usar passive cooling mod",
        "categoria": "Refrigeración"
    },
    
    "R347": {
        "condiciones": ["m2_heatsink_nvme_throttling"],
        "conclusion": "nvme_sin_disipacion_termica",
        "certeza": 81,
        "solucion": "Instalar heatsink M.2",
        "categoria": "Refrigeración"
    },
    
    "R348": {
        "condiciones": ["gpu_backplate_thermal_pads"],
        "conclusion": "backplate_mejora_cooling_vram",
        "certeza": 72,
        "solucion": "Pads entre backplate y PCB ayudan",
        "categoria": "Refrigeración"
    },
    
    "R349": {
        "condiciones": ["thermal_throttling_multiple_components"],
        "conclusion": "cooling_sistema_completo_inadecuado",
        "certeza": 86,
        "solucion": "Rediseñar estrategia cooling completa",
        "categoria": "Refrigeración"
    },
    
    "R350": {
        "condiciones": ["silent_pc_build_objetivo"],
        "conclusion": "trade_off_silencio_temperatura",
        "certeza": 69,
        "solucion": "Be Quiet, Noctua, fans low RPM",
        "categoria": "Refrigeración"
    },
    
    # ============================================================================
    # CATEGORÍA 8: SISTEMA OPERATIVO Y SOFTWARE (50 reglas)
    # ============================================================================
    
    "R351": {
        "condiciones": ["windows_no_bootea", "boot_loop"],
        "conclusion": "archivos_sistema_corruptos",
        "certeza": 82,
        "solucion": "Reparar con SFC /scannow o DISM",
        "categoria": "Sistema Operativo"
    },
    
    "R352": {
        "condiciones": ["pantalla_azul_system_service_exception"],
        "conclusion": "driver_incompatible_o_corrupto",
        "certeza": 80,
        "solucion": "Boot safe mode, desinstalar driver reciente",
        "categoria": "Sistema Operativo"
    },
    
    "R353": {
        "condiciones": ["windows_update_loop_infinito"],
        "conclusion": "actualizacion_fallando_repetidamente",
        "certeza": 78,
        "solucion": "Windows Update Troubleshooter o reset",
        "categoria": "Sistema Operativo"
    },
    
    "R354": {
        "condiciones": ["windows_activation_error"],
        "conclusion": "licencia_no_activada",
        "certeza": 85,
        "solucion": "Verificar key, vincular cuenta Microsoft",
        "categoria": "Sistema Operativo"
    },
    
    "R355": {
        "condiciones": ["slow_boot_windows"],
        "conclusion": "programas_inicio_excesivos",
        "certeza": 76,
        "solucion": "Deshabilitar startup programs innecesarios",
        "categoria": "Sistema Operativo"
    },
    
    "R356": {
        "condiciones": ["100_disk_usage_windows"],
        "conclusion": "windows_search_indexing_superfetch",
        "certeza": 79,
        "solucion": "Deshabilitar servicios problemáticos",
        "categoria": "Sistema Operativo"
    },
    
    "R357": {
        "condiciones": ["windows_10_vs_11_tpm"],
        "conclusion": "win11_requisitos_hardware_estrictos",
        "certeza": 87,
        "solucion": "TPM 2.0 y Secure Boot necesarios Win11",
        "categoria": "Sistema Operativo"
    },
    
    "R358": {
        "condiciones": ["driver_firma_digital_error"],
        "conclusion": "driver_no_firmado_bloqueado",
        "certeza": 81,
        "solucion": "Deshabilitar firma digital temporalmente",
        "categoria": "Sistema Operativo"
    },
    
    "R359": {
        "condiciones": ["dll_missing_error"],
        "conclusion": "libreria_sistema_faltante",
        "certeza": 77,
        "solucion": "Reinstalar Visual C++ Redistributables",
        "categoria": "Sistema Operativo"
    },
    
    "R360": {
        "condiciones": ["registry_error_windows"],
        "conclusion": "registro_windows_corrupto",
        "certeza": 74,
        "solucion": "CCleaner registry repair o system restore",
        "categoria": "Sistema Operativo"
    },
    
    "R361": {
        "condiciones": ["windows_slow_after_update"],
        "conclusion": "actualizacion_problematica",
        "certeza": 73,
        "solucion": "Desinstalar update reciente",
        "categoria": "Sistema Operativo"
    },
    
    "R362": {
        "condiciones": ["antivirus_false_positive"],
        "conclusion": "deteccion_falsa_software_legitimo",
        "certeza": 70,
        "solucion": "Agregar excepción en antivirus",
        "categoria": "Sistema Operativo"
    },
    
    "R363": {
        "condiciones": ["malware_detected_multiple"],
        "conclusion": "infeccion_sistema",
        "certeza": 89,
        "solucion": "Malwarebytes full scan, reinstalar OS si severo",
        "categoria": "Sistema Operativo"
    },
    
    "R364": {
        "condiciones": ["ransomware_files_encrypted"],
        "conclusion": "ataque_ransomware",
        "certeza": 96,
        "solucion": "NO pagar, restaurar desde backup",
        "categoria": "Sistema Operativo"
    },
    
    "R365": {
        "condiciones": ["browser_redirects_ads"],
        "conclusion": "adware_browser_hijacker",
        "certeza": 84,
        "solucion": "AdwCleaner, reset browser settings",
        "categoria": "Sistema Operativo"
    },
    
    "R366": {
        "condiciones": ["system_restore_point_falta"],
        "conclusion": "proteccion_sistema_deshabilitada",
        "certeza": 76,
        "solucion": "Habilitar System Restore preventivamente",
        "categoria": "Sistema Operativo"
    },
    
    "R367": {
        "condiciones": ["partition_lost_not_visible"],
        "conclusion": "tabla_particiones_corrupta",
        "certeza": 80,
        "solucion": "TestDisk para recuperar particiones",
        "categoria": "Sistema Operativo"
    },
    
    "R368": {
        "condiciones": ["windows_installation_media_corrupt"],
        "conclusion": "usb_instalacion_dañado",
        "certeza": 78,
        "solucion": "Recrear USB con Media Creation Tool",
        "categoria": "Sistema Operativo"
    },
    
    "R369": {
        "condiciones": ["dual_boot_linux_windows"],
        "conclusion": "grub_gestiona_arranque_dual",
        "certeza": 75,
        "solucion": "Instalar Windows primero, luego Linux",
        "categoria": "Sistema Operativo"
    },
    
    "R370": {
        "condiciones": ["grub_rescue_prompt"],
        "conclusion": "grub_bootloader_corrupto",
        "certeza": 82,
        "solucion": "Boot desde Live USB, reinstalar grub",
        "categoria": "Sistema Operativo"
    },
    
    "R371": {
        "condiciones": ["linux_kernel_panic"],
        "conclusion": "kernel_error_critico",
        "certeza": 81,
        "solucion": "Boot kernel anterior desde grub",
        "categoria": "Sistema Operativo"
    },
    
    "R372": {
        "condiciones": ["nvidia_driver_linux_problemas"],
        "conclusion": "nouveau_vs_proprietary_driver",
        "certeza": 77,
        "solucion": "Instalar driver propietario NVIDIA",
        "categoria": "Sistema Operativo"
    },
    
    "R373": {
        "condiciones": ["wifi_not_working_linux"],
        "conclusion": "driver_wireless_falta",
        "certeza": 74,
        "solucion": "Instalar linux-firmware paquete",
        "categoria": "Sistema Operativo"
    },
    
    "R374": {
        "condiciones": ["permission_denied_linux"],
        "conclusion": "permisos_usuario_insuficientes",
        "certeza": 73,
        "solucion": "Usar sudo o cambiar permisos chmod",
        "categoria": "Sistema Operativo"
    },
    
    "R375": {
        "condiciones": ["package_dependency_error_linux"],
        "conclusion": "dependencias_rotas",
        "certeza": 76,
        "solucion": "apt --fix-broken install o equivalent",
        "categoria": "Sistema Operativo"
    },
    
    "R376": {
        "condiciones": ["x_server_crash_linux"],
        "conclusion": "servidor_grafico_fallo",
        "certeza": 79,
        "solucion": "Reinstalar xorg o cambiar a wayland",
        "categoria": "Sistema Operativo"
    },
    
    "R377": {
        "condiciones": ["steam_proton_game_no_inicia"],
        "conclusion": "compatibilidad_proton_juego",
        "certeza": 71,
        "solucion": "Probar versiones Proton diferentes",
        "categoria": "Sistema Operativo"
    },
    
    "R378": {
        "condiciones": ["lutris_wine_configuration"],
        "conclusion": "runner_wine_necesita_configuracion",
        "certeza": 68,
        "solucion": "Instalar dependencias wine correctas",
        "categoria": "Sistema Operativo"
    },
    
    "R379": {
        "condiciones": ["virtual_machine_slow_performance"],
        "conclusion": "virtualizacion_hardware_no_habilitada",
        "certeza": 82,
        "solucion": "Habilitar VT-x/AMD-V en BIOS",
        "categoria": "Sistema Operativo"
    },
    
    "R380": {
        "condiciones": ["vmware_vs_virtualbox"],
        "conclusion": "vmware_mejor_rendimiento",
        "certeza": 69,
        "solucion": "VirtualBox gratis, VMware más rápido",
        "categoria": "Sistema Operativo"
    },
    
    "R381": {
        "condiciones": ["docker_container_not_starting"],
        "conclusion": "docker_daemon_problema",
        "certeza": 72,
        "solucion": "Restart docker service, verificar logs",
        "categoria": "Sistema Operativo"
    },
    
    "R382": {
        "condiciones": ["wsl2_windows_integration"],
        "conclusion": "linux_subsystem_windows",
        "certeza": 74,
        "solucion": "WSL2 mejor que WSL1, requiere Hyper-V",
        "categoria": "Sistema Operativo"
    },
    
    "R383": {
        "condiciones": ["hackintosh_incompatible_hardware"],
        "conclusion": "componentes_no_soportados_macos",
        "certeza": 76,
        "solucion": "Verificar Hackintosh compatibility list",
        "categoria": "Sistema Operativo"
    },
    
    "R384": {
        "condiciones": ["opencore_bootloader_config"],
        "conclusion": "configuracion_hackintosh_compleja",
        "certeza": 70,
        "solucion": "Seguir guía Dortania exhaustivamente",
        "categoria": "Sistema Operativo"
    },
    
    "R385": {
        "condiciones": ["bios_settings_optimal_gaming"],
        "conclusion": "configuracion_bios_rendimiento",
        "certeza": 67,
        "solucion": "XMP, MCE, C-States off, max performance",
        "categoria": "Sistema Operativo"
    },
    
    "R386": {
        "condiciones": ["game_mode_windows_10"],
        "conclusion": "modo_juego_optimiza_recursos",
        "certeza": 66,
        "solucion": "Habilitar Game Mode para gaming",
        "categoria": "Sistema Operativo"
    },
    
    "R387": {
        "condiciones": ["hardware_acceleration_browser"],
        "conclusion": "aceleracion_gpu_navegador",
        "certeza": 71,
        "solucion": "Habilitar en settings para videos suaves",
        "categoria": "Sistema Operativo"
    },
    
    "R388": {
        "condiciones": ["nvidia_control_panel_settings_gaming"],
        "conclusion": "optimizacion_gpu_por_aplicacion",
        "certeza": 69,
        "solucion": "Prefer maximum performance, low latency",
        "categoria": "Sistema Operativo"
    },
    
    "R389": {
        "condiciones": ["power_plan_high_performance"],
        "conclusion": "plan_energia_impacta_rendimiento",
        "certeza": 77,
        "solucion": "Ultimate Performance plan para gaming PC",
        "categoria": "Sistema Operativo"
    },
    
    "R390": {
        "condiciones": ["background_processes_consuming_resources"],
        "conclusion": "procesos_segundo_plano_excesivos",
        "certeza": 75,
        "solucion": "Desactivar apps innecesarias task manager",
        "categoria": "Sistema Operativo"
    },
    
    "R391": {
        "condiciones": ["discord_hardware_acceleration_lag"],
        "conclusion": "aceleracion_discord_conflicto",
        "certeza": 68,
        "solucion": "Toggle hardware acceleration Discord",
        "categoria": "Sistema Operativo"
    },
    
    "R392": {
        "condiciones": ["rgb_software_conflicts"],
        "conclusion": "multiples_programas_rgb_conflicto",
        "certeza": 73,
        "solucion": "Usar solo un software RGB control",
        "categoria": "Sistema Operativo"
    },
    
    "R393": {
        "condiciones": ["motherboard_software_bloatware"],
        "conclusion": "software_fabricante_innecesario",
        "certeza": 70,
        "solucion": "Desinstalar excepto monitoring tools",
        "categoria": "Sistema Operativo"
    },
    
    "R394": {
        "condiciones": ["windows_defender_vs_third_party"],
        "conclusion": "defender_suficiente_mayoria",
        "certeza": 72,
        "solucion": "Windows Defender adecuado, terceros opcional",
        "categoria": "Sistema Operativo"
    },
    
    "R395": {
        "condiciones": ["ccleaner_registry_cleaning"],
        "conclusion": "limpieza_registro_controversial",
        "certeza": 64,
        "solucion": "Usar con precaución, backup registry",
        "categoria": "Sistema Operativo"
    },
    
    "R396": {
        "condiciones": ["windows_debloater_scripts"],
        "conclusion": "remover_bloatware_windows",
        "certeza": 68,
        "solucion": "Scripts community para limpiar Win10/11",
        "categoria": "Sistema Operativo"
    },
    
    "R397": {
        "condiciones": ["telemetry_windows_privacy"],
        "conclusion": "telemetria_envio_datos_microsoft",
        "certeza": 71,
        "solucion": "Deshabilitar para mejor privacidad",
        "categoria": "Sistema Operativo"
    },
    
    "R398": {
        "condiciones": ["cortana_disabled"],
        "conclusion": "asistente_voz_recursos_consume",
        "certeza": 66,
        "solucion": "Deshabilitar si no se usa",
        "categoria": "Sistema Operativo"
    },
    
    "R399": {
        "condiciones": ["windows_search_indexing_high_cpu"],
        "conclusion": "indexacion_busqueda_consume_recursos",
        "certeza": 74,
        "solucion": "Limitar folders indexados o deshabilitar",
        "categoria": "Sistema Operativo"
    },
    
    "R400": {
        "condiciones": ["superfetch_ssd_innecesario"],
        "conclusion": "superfetch_optimizado_hdd",
        "certeza": 72,
        "solucion": "Deshabilitar con SSD instalado",
        "categoria": "Sistema Operativo"
    },
    
    # ============================================================================
    # CATEGORÍA 9: RED Y CONECTIVIDAD (40 reglas)
    # ============================================================================
    
    "R401": {
        "condiciones": ["no_internet_connection", "wifi_conectado"],
        "conclusion": "dns_problema_o_gateway",
        "certeza": 79,
        "solucion": "Cambiar DNS a 8.8.8.8 o flush DNS",
        "categoria": "Red y Conectividad"
    },
    
    "R402": {
        "condiciones": ["ethernet_no_detecta"],
        "conclusion": "cable_ethernet_dañado_o_nic_problema",
        "certeza": 81,
        "solucion": "Probar otro cable, verificar luces NIC",
        "categoria": "Red y Conectividad"
    },
    
    "R403": {
        "condiciones": ["wifi_signal_weak", "router_cerca"],
        "conclusion": "interferencia_o_antena_problema",
        "certeza": 74,
        "solucion": "Cambiar canal WiFi, verificar antenas",
        "categoria": "Red y Conectividad"
    },
    
    "R404": {
        "condiciones": ["network_adapter_not_found"],
        "conclusion": "driver_red_falta_o_hardware_dañado",
        "certeza": 82,
        "solucion": "Reinstalar driver chipset y LAN",
        "categoria": "Red y Conectividad"
    },
    
    "R405": {
        "condiciones": ["limited_connectivity"],
        "conclusion": "dhcp_no_asignando_ip",
        "certeza": 77,
        "solucion": "Renew IP: ipconfig /release /renew",
        "categoria": "Red y Conectividad"
    },
    
    "R406": {
        "condiciones": ["dns_not_responding"],
        "conclusion": "servidor_dns_caido",
        "certeza": 80,
        "solucion": "Cambiar a DNS públicos Google o Cloudflare",
        "categoria": "Red y Conectividad"
    },
    
    "R407": {
        "condiciones": ["high_ping_gaming"],
        "conclusion": "latencia_alta_conexion",
        "certeza": 76,
        "solucion": "Ethernet en vez WiFi, QoS router",
        "categoria": "Red y Conectividad"
    },
    
    "R408": {
        "condiciones": ["packet_loss_online_gaming"],
        "conclusion": "perdida_paquetes_red",
        "certeza": 78,
        "solucion": "Verificar calidad ISP, cambiar router",
        "categoria": "Red y Conectividad"
    },
    
    "R409": {
        "condiciones": ["wifi_6_not_faster", "router_ax"],
        "conclusion": "dispositivo_cliente_no_wifi6",
        "certeza": 85,
        "solucion": "Ambos (router y PC) deben ser compatibles con AX",
        "categoria": "Red y Conectividad"
    },
    
    "R410": {
        "condiciones": ["5ghz_wifi_range_bad", "2_4ghz_ok"],
        "conclusion": "5ghz_menor_penetracione_paredes",
        "certeza": 92,
        "solucion": "Usar 2.4GHz para distancia, 5GHz para velocidad cerca",
        "categoria": "Red y Conectividad"
    },
    
    "R411": {
        "condiciones": ["bluetooth_interference_wifi"],
        "conclusion": "frecuencia_2_4ghz_saturada",
        "certeza": 78,
        "solucion": "Mover WiFi a 5GHz o cambiar canal del router",
        "categoria": "Red y Conectividad"
    },
    
    "R412": {
        "condiciones": ["vpn_connected_no_internet"],
        "conclusion": "vpn_gateway_problema_o_killswitch",
        "certeza": 81,
        "solucion": "Desactivar killswitch o cambiar servidor VPN",
        "categoria": "Red y Conectividad"
    },
    
    "R413": {
        "condiciones": ["firewall_blocking_app"],
        "conclusion": "reglas_firewall_restrictivas",
        "certeza": 84,
        "solucion": "Crear regla de excepción en Firewall de Windows",
        "categoria": "Red y Conectividad"
    },
    
    "R414": {
        "condiciones": ["network_discovery_off", "no_ve_otros_pc"],
        "conclusion": "perfil_red_publica_activado",
        "certeza": 88,
        "solucion": "Cambiar perfil de red a 'Privada'",
        "categoria": "Red y Conectividad"
    },
    
    "R415": {
        "condiciones": ["mac_filtering_router_active"],
        "conclusion": "dispositivo_nuevo_bloqueado_mac",
        "certeza": 79,
        "solucion": "Agregar dirección MAC a lista blanca del router",
        "categoria": "Red y Conectividad"
    },
    
    "R416": {
        "condiciones": ["ip_address_conflict_error"],
        "conclusion": "dos_dispositivos_misma_ip_estatica",
        "certeza": 93,
        "solucion": "Cambiar a DHCP o asignar IP manual única",
        "categoria": "Red y Conectividad"
    },
    
    "R417": {
        "condiciones": ["gigabit_internet_slow_100mbps"],
        "conclusion": "cable_cat5_o_puerto_fast_ethernet",
        "certeza": 86,
        "solucion": "Usar cable Cat5e/Cat6 y puerto Gigabit",
        "categoria": "Red y Conectividad"
    },
    
    "R418": {
        "condiciones": ["powerline_adapter_slow_disconnects"],
        "conclusion": "ruido_electrico_linea_hogar",
        "certeza": 75,
        "solucion": "No conectar en regletas, directo a pared",
        "categoria": "Red y Conectividad"
    },
    
    "R419": {
        "condiciones": ["router_overheating_restarts"],
        "conclusion": "router_ventilacion_insuficiente",
        "certeza": 80,
        "solucion": "Colocar router en lugar abierto y ventilado",
        "categoria": "Red y Conectividad"
    },
    
    "R420": {
        "condiciones": ["isp_throttling_detected"],
        "conclusion": "proveedor_limita_ancho_banda",
        "certeza": 70,
        "solucion": "Usar VPN para evitar traffic shaping",
        "categoria": "Red y Conectividad"
    },
    
    # ============================================================================
    # CATEGORÍA 10: PERIFÉRICOS (TECLADO, MOUSE, MONITOR) (40 reglas)
    # ============================================================================
    
    "R421": {
        "condiciones": ["keyboard_ghosting_gaming"],
        "conclusion": "teclado_membrana_limite_teclas",
        "certeza": 90,
        "solucion": "Usar teclado mecánico con NKRO",
        "categoria": "Periféricos"
    },
    
    "R422": {
        "condiciones": ["mechanical_switch_chatter_double_type"],
        "conclusion": "interruptor_mecanico_sucio_o_dañado",
        "certeza": 85,
        "solucion": "Limpiar con aire/alcohol o reemplazar switch",
        "categoria": "Periféricos"
    },
    
    "R423": {
        "condiciones": ["wireless_mouse_lag_stutter"],
        "conclusion": "interferencia_usb_3_0_o_bateria",
        "certeza": 78,
        "solucion": "Usar extensor USB para receptor o cambiar batería",
        "categoria": "Periféricos"
    },
    
    "R424": {
        "condiciones": ["mouse_dpi_too_fast"],
        "conclusion": "configuracion_dpi_alta",
        "certeza": 95,
        "solucion": "Bajar DPI en software del mouse o botón físico",
        "categoria": "Periféricos"
    },
    
    "R425": {
        "condiciones": ["usb_hub_disconnects_devices"],
        "conclusion": "hub_usb_sin_alimentacion_suficiente",
        "certeza": 82,
        "solucion": "Usar Hub USB con adaptador de corriente externo",
        "categoria": "Periféricos"
    },
    
    "R426": {
        "condiciones": ["webcam_flicker_lights"],
        "conclusion": "frecuencia_hz_camara_incorrecta",
        "certeza": 88,
        "solucion": "Cambiar entre 50Hz/60Hz en settings cámara",
        "categoria": "Periféricos"
    },
    
    "R427": {
        "condiciones": ["microphone_static_noise"],
        "conclusion": "ground_loop_o_interferencia_electrica",
        "certeza": 76,
        "solucion": "Usar puerto trasero o tarjeta de sonido USB",
        "categoria": "Periféricos"
    },
    
    "R428": {
        "condiciones": ["monitor_dead_pixel_black"],
        "conclusion": "pixel_muerto_panel_lcd",
        "certeza": 99,
        "solucion": "Generalmente irreparable, revisar garantía (ISO 13406-2)",
        "categoria": "Periféricos"
    },
    
    "R429": {
        "condiciones": ["monitor_stuck_pixel_color"],
        "conclusion": "pixel_atascado",
        "certeza": 80,
        "solucion": "Intentar software de flash colores rápidos",
        "categoria": "Periféricos"
    },
    
    "R430": {
        "condiciones": ["monitor_backlight_bleed"],
        "conclusion": "fuga_luz_panel_ips",
        "certeza": 85,
        "solucion": "Defecto de fabricación común, bajar brillo ayuda",
        "categoria": "Periféricos"
    },
    
    "R431": {
        "condiciones": ["hdmi_no_signal_handshake"],
        "conclusion": "fallo_negociacion_hdmi",
        "certeza": 72,
        "solucion": "Desconectar y reconectar cables en ambos extremos",
        "categoria": "Periféricos"
    },
    
    "R432": {
        "condiciones": ["printer_spooler_stuck"],
        "conclusion": "cola_impresion_bloqueada",
        "certeza": 89,
        "solucion": "Reiniciar servicio 'Print Spooler' en Windows",
        "categoria": "Periféricos"
    },
    
    "R433": {
        "condiciones": ["vr_headset_usb_bandwidth"],
        "conclusion": "ancho_banda_usb_saturado",
        "certeza": 77,
        "solucion": "Desconectar otros dispositivos USB o usar tarjeta PCIe USB",
        "categoria": "Periféricos"
    },
    
    "R434": {
        "condiciones": ["gamepad_stick_drift"],
        "conclusion": "potenciometro_analogico_desgaste",
        "certeza": 92,
        "solucion": "Limpiar con contact cleaner o reemplazar joystick",
        "categoria": "Periféricos"
    },
    
    "R435": {
        "condiciones": ["audio_jack_loose_static"],
        "conclusion": "puerto_jack_3_5mm_dañado",
        "certeza": 84,
        "solucion": "Usar audio panel trasero o DAC USB",
        "categoria": "Periféricos"
    },
    
    "R436": {
        "condiciones": ["bluetooth_audio_delay"],
        "conclusion": "latencia_bluetooth_codec_basico",
        "certeza": 90,
        "solucion": "Usar dispositivos aptX LL o conexión cableada",
        "categoria": "Periféricos"
    },
    
    "R437": {
        "condiciones": ["monitor_flickering_freesync"],
        "conclusion": "rango_freesync_inestable_brillo",
        "certeza": 71,
        "solucion": "Desactivar FreeSync o actualizar firmware monitor",
        "categoria": "Periféricos"
    },
    
    "R438": {
        "condiciones": ["mechanical_keyboard_key_chatter"],
        "conclusion": "rebote_switch_defectuoso",
        "certeza": 80,
        "solucion": "Ajustar 'debounce time' en software teclado",
        "categoria": "Periféricos"
    },
    
    "R439": {
        "condiciones": ["mouse_sensor_spinout"],
        "conclusion": "sensor_mouse_sucio_o_superficie_mala",
        "certeza": 76,
        "solucion": "Limpiar lente sensor y usar mousepad color sólido",
        "categoria": "Periféricos"
    },
    
    "R440": {
        "condiciones": ["headset_usb_not_recognized"],
        "conclusion": "firmware_audifonos_corrupto",
        "certeza": 73,
        "solucion": "Reinstalar software propietario (iCUE, Synapse, etc)",
        "categoria": "Periféricos"
    },
    
    "R441": {
        "condiciones": ["monitor_color_accuracy_bad"],
        "conclusion": "perfil_color_incorrecto_o_tn_panel",
        "certeza": 82,
        "solucion": "Calibrar color o instalar perfil ICC del fabricante",
        "categoria": "Periféricos"
    },
    
    "R442": {
        "condiciones": ["kvm_switch_lag"],
        "conclusion": "kvm_baja_calidad_emulacion",
        "certeza": 69,
        "solucion": "Usar KVM con soporte EDID passthrough",
        "categoria": "Periféricos"
    },
    
    "R443": {
        "condiciones": ["stream_deck_buttons_blank"],
        "conclusion": "plugin_stream_deck_crasheado",
        "certeza": 75,
        "solucion": "Reiniciar software Stream Deck",
        "categoria": "Periféricos"
    },
    
    "R444": {
        "condiciones": ["wacom_tablet_driver_not_found"],
        "conclusion": "servicio_wacom_detenido",
        "certeza": 88,
        "solucion": "Reiniciar servicio Wacom Professional Service",
        "categoria": "Periféricos"
    },
    
    "R445": {
        "condiciones": ["external_dac_popping_sound"],
        "conclusion": "latencia_dpc_usb",
        "certeza": 65,
        "solucion": "Analizar con LatencyMon, actualizar drivers chipset",
        "categoria": "Periféricos"
    },
    
    "R446": {
        "condiciones": ["ups_beep_continuo"],
        "conclusion": "bateria_ups_agotada_o_sobrecarga",
        "certeza": 90,
        "solucion": "Reemplazar batería interna del UPS",
        "categoria": "Periféricos"
    },
    
    "R447": {
        "condiciones": ["surge_protector_light_off"],
        "conclusion": "proteccion_picos_agotada",
        "certeza": 95,
        "solucion": "Reemplazar regleta, ya no protege",
        "categoria": "Periféricos"
    },
    
    "R448": {
        "condiciones": ["monitor_out_of_range"],
        "conclusion": "resolucion_o_hz_no_soportados",
        "certeza": 98,
        "solucion": "Entrar modo seguro y bajar resolución",
        "categoria": "Periféricos"
    },
    
    "R449": {
        "condiciones": ["display_scaling_blurry_text"],
        "conclusion": "escalado_windows_no_nativo",
        "certeza": 85,
        "solucion": "Ajustar escala DPI (100%, 125%) o fix apps borrosas",
        "categoria": "Periféricos"
    },
    
    "R450": {
        "condiciones": ["multiple_audio_outputs_simultaneous"],
        "conclusion": "windows_limita_salida_unica",
        "certeza": 90,
        "solucion": "Usar software como Voicemeeter Banana",
        "categoria": "Periféricos"
    },
    
    # ============================================================================
    # CATEGORÍA 11: PORTÁTILES / LAPTOPS (30 reglas)
    # ============================================================================
    
    "R451": {
        "condiciones": ["laptop_bateria_hinchada", "touchpad_levantado"],
        "conclusion": "bateria_litio_expandida_peligro",
        "certeza": 99,
        "solucion": "Remover batería inmediatamente, riesgo incendio",
        "categoria": "Portátiles"
    },
    
    "R452": {
        "condiciones": ["plugged_in_not_charging"],
        "conclusion": "bateria_dañada_o_adaptador_falla",
        "certeza": 82,
        "solucion": "Verificar salud batería en BIOS o cambiar cargador",
        "categoria": "Portátiles"
    },
    
    "R453": {
        "condiciones": ["laptop_hinge_broken", "ruido_crack_al_abrir"],
        "conclusion": "bisagra_o_montura_plastico_rota",
        "certeza": 95,
        "solucion": "No forzar, requiere cambio de carcasa/bisagra",
        "categoria": "Portátiles"
    },
    
    "R454": {
        "condiciones": ["touchpad_not_working", "mouse_externo_ok"],
        "conclusion": "touchpad_deshabilitado_fn_key",
        "certeza": 85,
        "solucion": "Presionar tecla Fn + icono touchpad",
        "categoria": "Portátiles"
    },
    
    "R455": {
        "condiciones": ["laptop_overheating_shutdown", "base_muy_caliente"],
        "conclusion": "disipador_laptop_obstruido_pelusa",
        "certeza": 90,
        "solucion": "Abrir y limpiar ventilador/radiador",
        "categoria": "Portátiles"
    },
    
    "R456": {
        "condiciones": ["keyboard_liquid_spill_laptop"],
        "conclusion": "daño_liquido_teclado_motherboard",
        "certeza": 95,
        "solucion": "Apagar, desconectar batería, secar días, no encender",
        "categoria": "Portátiles"
    },
    
    "R457": {
        "condiciones": ["screen_flicker_move_lid"],
        "conclusion": "cable_flex_video_dañado",
        "certeza": 88,
        "solucion": "Reemplazar cable LVDS/eDP de la pantalla",
        "categoria": "Portátiles"
    },
    
    "R458": {
        "condiciones": ["ac_adapter_wattage_warning"],
        "conclusion": "cargador_potencia_insuficiente",
        "certeza": 92,
        "solucion": "Usar cargador original con Watts correctos",
        "categoria": "Portátiles"
    },
    
    "R459": {
        "condiciones": ["optimus_graphics_stuck_intel"],
        "conclusion": "no_cambia_a_gpu_dedicada",
        "certeza": 78,
        "solucion": "Forzar GPU alto rendimiento en panel NVIDIA/Windows",
        "categoria": "Portátiles"
    },
    
    "R460": {
        "condiciones": ["battery_drain_sleep_mode"],
        "conclusion": "modern_standby_s0_issues",
        "certeza": 75,
        "solucion": "Desactivar fast startup o usar Hibernación",
        "categoria": "Portátiles"
    },
    
    "R461": {
        "condiciones": ["lid_sensor_not_sleeping"],
        "conclusion": "sensor_magnetico_tapa_fallando",
        "certeza": 70,
        "solucion": "Configurar botón power para dormir como alternativa",
        "categoria": "Portátiles"
    },
    
    "R462": {
        "condiciones": ["wifi_antenna_loose_laptop"],
        "conclusion": "cable_antena_interno_desconectado",
        "certeza": 81,
        "solucion": "Reconectar cables IPEX en tarjeta WiFi",
        "categoria": "Portátiles"
    },
    
    "R463": {
        "condiciones": ["laptop_fan_grinding_noise"],
        "conclusion": "ventilador_laptop_descentrado",
        "certeza": 89,
        "solucion": "Reemplazar ventilador específico del modelo",
        "categoria": "Portátiles"
    },
    
    "R464": {
        "condiciones": ["battery_wear_level_high"],
        "conclusion": "bateria_fin_vida_util",
        "certeza": 90,
        "solucion": "Reemplazar batería (consumible)",
        "categoria": "Portátiles"
    },
    
    "R465": {
        "condiciones": ["throttling_on_battery"],
        "conclusion": "modo_ahorro_energia_agresivo",
        "certeza": 85,
        "solucion": "Normal, rendimiento limitado por batería",
        "categoria": "Portátiles"
    },
    
    "R466": {
        "condiciones": ["num_lock_typing_numbers_letters"],
        "conclusion": "teclado_numerico_integrado_activo",
        "certeza": 90,
        "solucion": "Desactivar NumLock (Fn + NumLk)",
        "categoria": "Portátiles"
    },
    
    "R467": {
        "condiciones": ["webcam_privacy_shutter_closed"],
        "conclusion": "tapa_privacidad_bloquea_imagen",
        "certeza": 98,
        "solucion": "Abrir obturador físico de la cámara",
        "categoria": "Portátiles"
    },
    
    "R468": {
        "condiciones": ["bloatware_mcafee_norton_slow"],
        "conclusion": "antivirus_preinstalado_consume_recursos",
        "certeza": 85,
        "solucion": "Desinstalar versiones prueba antivirus",
        "categoria": "Portátiles"
    },
    
    "R469": {
        "condiciones": ["rubber_feet_missing_overheating"],
        "conclusion": "falta_elevacion_flujo_aire",
        "certeza": 70,
        "solucion": "Reemplazar gomas base para intake aire",
        "categoria": "Portátiles"
    },
    
    "R470": {
        "condiciones": ["keyboard_backlight_off"],
        "conclusion": "iluminacion_teclado_desactivada",
        "certeza": 80,
        "solucion": "Activar con atajo teclado (ej. Fn + Space)",
        "categoria": "Portátiles"
    },
    
    "R471": {
        "condiciones": ["usb_c_charging_not_working"],
        "conclusion": "puerto_usb_c_no_soporta_pd",
        "certeza": 88,
        "solucion": "Verificar si puerto soporta Power Delivery",
        "categoria": "Portátiles"
    },
    
    "R472": {
        "condiciones": ["thunderbolt_dock_no_video"],
        "conclusion": "driver_thunderbolt_o_cable_malo",
        "certeza": 79,
        "solucion": "Aprobar dispositivo en Centro Thunderbolt",
        "categoria": "Portátiles"
    },
    
    "R473": {
        "condiciones": ["laptop_screen_brightness_stuck"],
        "conclusion": "driver_graficos_bug",
        "certeza": 76,
        "solucion": "Actualizar driver iGPU/dGPU",
        "categoria": "Portátiles"
    },
    
    "R474": {
        "condiciones": ["fingerprint_reader_not_working"],
        "conclusion": "sensor_huella_sucio_o_driver",
        "certeza": 82,
        "solucion": "Limpiar sensor o reinstalar driver biométrico",
        "categoria": "Portátiles"
    },
    
    "R475": {
        "condiciones": ["coil_whine_laptop_silent_room"],
        "conclusion": "vibracion_inductor_electrico",
        "certeza": 70,
        "solucion": "Normal en ultrabooks, no hay fix fácil",
        "categoria": "Portátiles"
    },
    
    "R476": {
        "condiciones": ["hdd_shock_protection_active"],
        "conclusion": "sensor_caida_detiene_disco",
        "certeza": 85,
        "solucion": "Normal si se mueve laptop bruscamente",
        "categoria": "Portátiles"
    },
    
    "R477": {
        "condiciones": ["soldered_ram_upgrade"],
        "conclusion": "ram_soldada_no_actualizable",
        "certeza": 99,
        "solucion": "Imposible upgrade físico en estos modelos",
        "categoria": "Portátiles"
    },
    
    "R478": {
        "condiciones": ["mxm_gpu_upgrade_possible"],
        "conclusion": "gpu_formato_mxm_reemplazable",
        "certeza": 60,
        "solucion": "Posible en laptops gaming antiguas/workstations",
        "categoria": "Portátiles"
    },
    
    "R479": {
        "condiciones": ["stylus_pen_not_writing"],
        "conclusion": "bateria_lapiz_agotada_aaaa",
        "certeza": 88,
        "solucion": "Reemplazar batería AAAA del stylus",
        "categoria": "Portátiles"
    },
    
    "R480": {
        "condiciones": ["airplane_mode_stuck"],
        "conclusion": "interruptor_fisico_modo_avion",
        "certeza": 85,
        "solucion": "Verificar switch físico lateral si existe",
        "categoria": "Portátiles"
    },
    
    # ============================================================================
    # CATEGORÍA 12: MANTENIMIENTO, PREVENCIÓN Y VARIOS (20 reglas)
    # ============================================================================
    
    "R481": {
        "condiciones": ["dust_filter_clogged_airflow_0"],
        "conclusion": "filtro_polvo_totalmente_tapado",
        "certeza": 95,
        "solucion": "Lavar y secar filtros de aire",
        "categoria": "Mantenimiento"
    },
    
    "R482": {
        "condiciones": ["smoke_residue_pc_components"],
        "conclusion": "daño_por_humo_tabaco_pegajoso",
        "certeza": 88,
        "solucion": "Limpieza profunda alcohol isopropílico (difícil)",
        "categoria": "Mantenimiento"
    },
    
    "R483": {
        "condiciones": ["cable_management_messy_hot"],
        "conclusion": "cables_bloquean_flujo_aire",
        "certeza": 75,
        "solucion": "Usar precintos y organizar cables",
        "categoria": "Mantenimiento"
    },
    
    "R484": {
        "condiciones": ["bios_password_forgotten"],
        "conclusion": "acceso_bios_bloqueado",
        "certeza": 90,
        "solucion": "Remover batería CMOS/Jumper reset (si no es laptop enterprise)",
        "categoria": "Mantenimiento"
    },
    
    "R485": {
        "condiciones": ["cmos_jumper_position_wrong"],
        "conclusion": "pc_en_modo_reset_permanente",
        "certeza": 92,
        "solucion": "Mover jumper a posición default",
        "categoria": "Mantenimiento"
    },
    
    "R486": {
        "condiciones": ["static_shock_during_build"],
        "conclusion": "riesgo_esd_componentes",
        "certeza": 60,
        "solucion": "Siempre tocar metal o usar pulsera antes",
        "categoria": "Mantenimiento"
    },
    
    "R487": {
        "condiciones": ["screw_stripped_motherboard"],
        "conclusion": "tornillo_rodado_atascado",
        "certeza": 85,
        "solucion": "Usar banda elástica o alicates presión",
        "categoria": "Mantenimiento"
    },
    
    "R488": {
        "condiciones": ["thermal_pad_missing_thickness"],
        "conclusion": "contacto_termico_incompleto",
        "certeza": 90,
        "solucion": "Usar grosor exacto (1mm, 1.5mm) requerido",
        "categoria": "Mantenimiento"
    },
    
    "R489": {
        "condiciones": ["fan_orientation_wrong"],
        "conclusion": "ventiladores_compitiendo_flujo",
        "certeza": 82,
        "solucion": "Verificar flechas flujo aire en marco ventilador",
        "categoria": "Mantenimiento"
    },
    
    "R490": {
        "condiciones": ["water_cooling_algae_growth"],
        "conclusion": "crecimiento_biologico_loop",
        "certeza": 95,
        "solucion": "Desarmar, limpiar y usar biocida en liquido",
        "categoria": "Mantenimiento"
    },
    
    "R491": {
        "condiciones": ["acrylic_tubing_cracked"],
        "conclusion": "tubo_rigido_apretado_exceso",
        "certeza": 90,
        "solucion": "Reemplazar tubo, no apretar fittings exceso",
        "categoria": "Mantenimiento"
    },
    
    "R492": {
        "condiciones": ["gpu_sag_pcie_damage"],
        "conclusion": "peso_gpu_daña_puerto",
        "certeza": 85,
        "solucion": "Instalar soporte GPU inmediatamente",
        "categoria": "Mantenimiento"
    },
    
    "R493": {
        "condiciones": ["tempered_glass_shattered_tile"],
        "conclusion": "vidrio_templado_toco_ceramica",
        "certeza": 98,
        "solucion": "Cerámica rompe vidrio templado instantáneamente",
        "categoria": "Mantenimiento"
    },
    
    "R494": {
        "condiciones": ["motherboard_box_test_bench"],
        "conclusion": "prueba_fuera_gabinete_segura",
        "certeza": 80,
        "solucion": "Recomendado probar componentes sobre caja antes de armar",
        "categoria": "Mantenimiento"
    },
    
    "R495": {
        "condiciones": ["molex_to_sata_fire_hazard"],
        "conclusion": "adaptador_molex_sata_baja_calidad",
        "certeza": 85,
        "solucion": "Molex to SATA, lose all your data (Evitar)",
        "categoria": "Mantenimiento"
    },
    
    "R496": {
        "condiciones": ["cheap_psu_cables_mix"],
        "conclusion": "pinout_cables_modulares_diferente",
        "certeza": 99,
        "solucion": "NUNCA mezclar cables de fuentes diferentes",
        "categoria": "Mantenimiento"
    },
    
    "R497": {
        "condiciones": ["compressed_air_liquid_spray"],
        "conclusion": "aire_comprimido_invertido",
        "certeza": 90,
        "solucion": "Mantener lata vertical para no congelar componentes",
        "categoria": "Mantenimiento"
    },
    
    "R498": {
        "condiciones": ["vacuum_cleaner_static"],
        "conclusion": "aspiradora_genera_estatica",
        "certeza": 85,
        "solucion": "No usar aspiradora doméstica dentro del PC",
        "categoria": "Mantenimiento"
    },
    
    "R499": {
        "condiciones": ["alcohol_not_dried_boot"],
        "conclusion": "corto_por_liquido_limpieza",
        "certeza": 80,
        "solucion": "Esperar evaporación total alcohol antes de encender",
        "categoria": "Mantenimiento"
    },
    
    "R500": {
        "condiciones": ["unknown_error_system_instability"],
        "conclusion": "diagnostico_no_concluyente",
        "certeza": 0,
        "solucion": "Consultar servicio técnico profesional avanzado",
        "categoria": "Varios"
    }
}

# Función para obtener todas las categorías únicas
def get_categorias():
    categorias = set()
    for regla in knowledge_base.values():
        categorias.add(regla.get("categoria", "Sin categoría"))
    return sorted(list(categorias))

# Función para buscar reglas por condiciones
def buscar_por_condiciones(condiciones_busqueda):
    """
    Busca reglas que coincidan con las condiciones proporcionadas.
    condiciones_busqueda: lista de strings con condiciones a buscar
    """
    resultados = []
    for id_regla, regla in knowledge_base.items():
        coincidencias = 0
        condiciones_regla = regla.get("condiciones", [])
        
        # Contar cuántas condiciones de búsqueda coinciden
        for condicion_busqueda in condiciones_busqueda:
            for condicion_regla in condiciones_regla:
                if condicion_busqueda.lower() in condicion_regla.lower():
                    coincidencias += 1
                    break
        
        if coincidencias > 0 and len(condiciones_busqueda) > 0:
            porcentaje_coincidencia = (coincidencias / len(condiciones_busqueda)) * 100
            resultados.append({
                "id": id_regla,
                "regla": regla,
                "coincidencias": coincidencias,
                "porcentaje": porcentaje_coincidencia
            })
    
    # Ordenar por porcentaje de coincidencia y certeza
    resultados.sort(key=lambda x: (x["porcentaje"], x["regla"]["certeza"]), reverse=True)
    return resultados

# Función para filtrar por categoría
def filtrar_por_categoria(categoria):
    """Filtra reglas por categoría"""
    return {k: v for k, v in knowledge_base.items() if v.get("categoria") == categoria}

# Función para obtener reglas por rango de certeza
def filtrar_por_certeza(min_certeza=0, max_certeza=100):
    """Filtra reglas por rango de certeza"""
    return {k: v for k, v in knowledge_base.items() 
            if min_certeza <= v.get("certeza", 0) <= max_certeza}


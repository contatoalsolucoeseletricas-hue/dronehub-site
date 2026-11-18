# -*- coding: utf-8 -*-
import os, sys

def main():
    src_path = r"C:\DRONE\marketplace_app.html"
    with open(src_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Header text
    old_header = """          <div class="flex items-center gap-1.5">
            <span class="font-extrabold text-base tracking-tight text-white">DRONE<span class="text-cyan-400">HUB</span></span>
            <span class="text-[9px] font-mono font-bold bg-cyan-950 text-cyan-300 border border-cyan-800 px-1.5 py-0.5 rounded uppercase">LATAM V4</span>
          </div>
          <p class="text-[10px] text-slate-400 font-medium">América do Sul • Live & Cockpit</p>"""

    new_header = """          <div class="flex items-center gap-1.5">
            <span class="font-extrabold text-base tracking-tight text-white">DRONE<span class="text-cyan-400">HUB</span></span>
            <span class="text-[9px] font-mono font-bold bg-cyan-950 text-cyan-300 border border-cyan-800 px-1.5 py-0.5 rounded uppercase">PAN-AM V6</span>
          </div>
          <p class="text-[10px] text-slate-400 font-medium">Américas Total • Live, Cockpit & IA</p>"""

    if old_header in html:
        html = html.replace(old_header, new_header, 1)
        print("Updated header text successfully")
    else:
        print("Warning: old header text not matched exactly")

    # 2. Add Copiloto IA button in top header
    old_buttons = """      <div class="flex items-center gap-1.5">
        <button onclick="openRetaModal()" """

    new_buttons = """      <div class="flex items-center gap-1.5">
        <button onclick="openAeroAIModal()" class="flex items-center gap-1 text-[11px] font-bold bg-gradient-to-r from-cyan-950 to-blue-950 border border-cyan-400/60 text-cyan-300 px-2 py-1.5 rounded-lg active:scale-95 transition shadow-sm animate-pulse">
          <span>🤖 Copiloto IA</span>
        </button>
        <button onclick="openRetaModal()" """

    if old_buttons in html:
        html = html.replace(old_buttons, new_buttons, 1)
        print("Added Copiloto IA button to top header")
    else:
        print("Warning: old buttons row not matched exactly")

    # 3. Add Digital Compass into Live HUD
    target_ladder = """          <!-- Centro: Mira & Pitch Ladder -->
          <div class="hud-ladder"></div>"""

    new_hud_compass = """          <!-- BÚSSOLA DIGITAL & HEADING TÁTICO HUD (Fita de Rumo Giroscópica) -->
          <div class="absolute top-2.5 left-1/2 -translate-x-1/2 bg-black/75 backdrop-blur-md px-3 py-1 rounded-xl border border-cyan-500/40 font-mono shadow-xl flex items-center gap-2.5 z-20">
            <!-- Mini Bússola Giroscópica -->
            <div class="relative w-7 h-7 rounded-full border border-cyan-400/60 bg-slate-950/80 flex items-center justify-center">
              <div id="hudCompassRose" class="w-full h-full flex items-center justify-center transition-transform duration-200" style="transform: rotate(42deg);">
                <span class="text-[8px] font-bold text-rose-500 absolute -top-0.5">N</span>
                <span class="text-[7px] font-bold text-slate-400 absolute -bottom-0.5">S</span>
                <span class="text-[7px] font-bold text-slate-400 absolute -right-0.5">E</span>
                <span class="text-[7px] font-bold text-slate-400 absolute -left-0.5">W</span>
                <div class="w-0.5 h-3.5 bg-gradient-to-t from-cyan-500 to-white rounded-full shadow-sm shadow-cyan-400"></div>
              </div>
            </div>
            <div>
              <div class="flex items-center gap-1 text-[10px]">
                <span class="text-slate-400">PROA:</span>
                <span id="hudHeadingVal" class="text-white font-bold font-mono">042° NE</span>
                <span class="text-cyan-400 text-[9px] font-semibold">(MAG)</span>
              </div>
              <div class="text-[8px] text-emerald-400 font-mono flex items-center gap-1">
                <span>🏠 HOME: 228° SW (410m)</span>
              </div>
            </div>
          </div>

          <!-- Centro: Mira & Pitch Ladder -->
          <div class="hud-ladder"></div>"""

    if target_ladder in html:
        html = html.replace(target_ladder, new_hud_compass, 1)
        print("Added HUD Digital Compass successfully")
    else:
        print("Warning: target_ladder not matched")

    # 4. Enhance Cockpit (Despacho): Tactical Compass 360, IA shortcut, KP/PDOP educational cards and Simulator
    old_cockpit_top = """      <!-- Topo do Cockpit -->
      <div class="card p-3 flex items-center justify-between border-cyan-500/20">
        <div>
          <span class="text-xs font-bold text-white flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
            DRONENINJA DISPATCH COCKPIT
          </span>
          <p class="text-[10px] text-slate-400 font-mono">SARPAS DECEA: AUTORIZADO • VOO VLOS</p>
        </div>
        <div class="text-right">
          <span class="text-[11px] font-mono text-emerald-400 font-bold bg-emerald-950/70 border border-emerald-800 px-2 py-0.5 rounded">
            GO / SCORE 94%
          </span>
        </div>
      </div>"""

    new_cockpit_top = """      <!-- Topo do Cockpit -->
      <div class="card p-3 flex items-center justify-between border-cyan-500/20" id="cockpitHeaderCard">
        <div>
          <span class="text-xs font-bold text-white flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse" id="cockpitPulseDot"></span>
            DRONENINJA DISPATCH COCKPIT
          </span>
          <p class="text-[10px] text-slate-400 font-mono" id="cockpitSarpasText">SARPAS DECEA: AUTORIZADO (BR-94812) • VOO VLOS</p>
        </div>
        <div class="text-right">
          <span class="text-[11px] font-mono text-emerald-400 font-bold bg-emerald-950/70 border border-emerald-800 px-2 py-0.5 rounded transition" id="cockpitScoreBadge">
            GO / SCORE 94%
          </span>
        </div>
      </div>

      <!-- CARD ATALHO PARA COPILOTO IA AEROESPACIAL -->
      <div class="bg-gradient-to-r from-blue-950/80 via-slate-900 to-cyan-950/80 border border-cyan-500/30 rounded-2xl p-3 flex items-center justify-between shadow-lg">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-xl bg-cyan-500/20 border border-cyan-400/50 flex items-center justify-center text-cyan-400 font-bold text-sm">
            🤖
          </div>
          <div>
            <div class="flex items-center gap-1.5">
              <h4 class="text-xs font-bold text-white">Copiloto IA de Espaço Aéreo</h4>
              <span class="text-[8px] font-mono font-bold bg-cyan-950 text-cyan-300 border border-cyan-700 px-1 rounded">PAN-AM</span>
            </div>
            <p class="text-[10px] text-slate-300">Dúvidas sobre regras por país (DECEA, FAA, Transport Canada) ou clima solar?</p>
          </div>
        </div>
        <button onclick="openAeroAIModal()" class="text-[10px] font-bold bg-cyan-500 hover:bg-cyan-400 text-slate-950 px-2.5 py-1.5 rounded-lg whitespace-nowrap active:scale-95 shadow-sm transition">
          Consultar IA
        </button>
      </div>

      <!-- BÚSSOLA TÁTICA 360° & ORIENTAÇÃO AEROESPACIAL -->
      <div class="card p-3 space-y-2.5 border-cyan-500/30">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-1.5">
            <span class="text-sm">🧭</span>
            <span class="text-xs font-bold text-slate-200 uppercase tracking-wider">Bússola Tática 360° & Vetores de Orientação</span>
          </div>
          <span class="text-[10px] font-mono text-cyan-400 font-bold bg-cyan-950 px-2 py-0.5 rounded border border-cyan-800">
            SISTEMA GIROSCÓPICO ATIVO
          </span>
        </div>

        <div class="grid grid-cols-12 gap-3 items-center">
          <!-- Dial Visual da Bússola -->
          <div class="col-span-5 flex justify-center">
            <div class="relative w-28 h-28 rounded-full border-2 border-cyan-500/40 bg-slate-950 shadow-inner flex items-center justify-center p-1">
              <!-- Rosa dos Ventos Giratória -->
              <div id="cockpitCompassDial" class="w-full h-full rounded-full relative flex items-center justify-center transition-transform duration-300" style="transform: rotate(42deg);">
                <span class="text-[10px] font-black text-rose-500 absolute top-0.5">N</span>
                <span class="text-[9px] font-bold text-cyan-400 absolute right-1">E</span>
                <span class="text-[9px] font-bold text-slate-400 absolute bottom-0.5">S</span>
                <span class="text-[9px] font-bold text-slate-400 absolute left-1">W</span>
                
                <div class="w-full h-px bg-slate-800/80 absolute"></div>
                <div class="h-full w-px bg-slate-800/80 absolute"></div>

                <!-- Silhueta Tática do Drone no Centro -->
                <div class="w-6 h-6 flex items-center justify-center z-10">
                  <svg width="22" height="22" fill="#22d3ee" viewBox="0 0 24 24">
                    <path d="M12 2L4 20l8-3 8 3z"/>
                  </svg>
                </div>
              </div>

              <!-- Anel de Graduação Externa -->
              <div class="absolute inset-0 rounded-full border border-dashed border-cyan-400/20 pointer-events-none"></div>
            </div>
          </div>

          <!-- Informações de Orientação & Vetores -->
          <div class="col-span-7 space-y-2 text-xs font-mono">
            <div class="bg-slate-900/80 p-2 rounded-xl border border-slate-800 flex justify-between items-center">
              <span class="text-slate-400 text-[10px]">RUMO / HEADING:</span>
              <span class="text-white font-bold" id="cockpitHeadingText">042° (Nordeste)</span>
            </div>
            <div class="bg-slate-900/80 p-2 rounded-xl border border-slate-800 flex justify-between items-center">
              <span class="text-slate-400 text-[10px]">VETOR HOME (RTH):</span>
              <span class="text-emerald-400 font-bold" id="cockpitHomeVector">228° SW (Dist: 410m)</span>
            </div>
            <div class="bg-slate-900/80 p-2 rounded-xl border border-slate-800 flex justify-between items-center">
              <span class="text-slate-400 text-[10px]">VENTO RELATIVO:</span>
              <span class="text-cyan-300 font-bold" id="cockpitWindRelative">Vento de Proa (12 km/h)</span>
            </div>

            <!-- Botões de Giro Rápido para o Piloto Testar Orientação -->
            <div class="flex gap-1 pt-0.5">
              <button onclick="rotateDroneHeading(0)" class="flex-1 py-1 rounded-lg bg-slate-950 border border-slate-800 text-[10px] text-slate-300 hover:border-cyan-500 transition active:scale-95">Norte 0°</button>
              <button onclick="rotateDroneHeading(90)" class="flex-1 py-1 rounded-lg bg-slate-950 border border-slate-800 text-[10px] text-slate-300 hover:border-cyan-500 transition active:scale-95">Leste 90°</button>
              <button onclick="rotateDroneHeading(180)" class="flex-1 py-1 rounded-lg bg-slate-950 border border-slate-800 text-[10px] text-slate-300 hover:border-cyan-500 transition active:scale-95">Sul 180°</button>
              <button onclick="rotateDroneHeading(270)" class="flex-1 py-1 rounded-lg bg-slate-950 border border-slate-800 text-[10px] text-slate-300 hover:border-cyan-500 transition active:scale-95">Oeste 270°</button>
            </div>
          </div>
        </div>
      </div>"""

    if old_cockpit_top in html:
        html = html.replace(old_cockpit_top, new_cockpit_top, 1)
        print("Updated Cockpit top and added 360 Compass successfully")
    else:
        print("Warning: old_cockpit_top not matched")

    # 5. Replace Clima Espacial (KP Index) & Satélites section with educational cards & risk simulation
    old_kp_section = """        <!-- Clima Espacial (KP Index) & Satélites -->
        <div class="grid grid-cols-2 gap-2 text-xs">
          <div class="bg-slate-900/60 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between">
            <div>
              <span class="text-[10px] text-slate-400 block">Índice Solar (KP)</span>
              <span class="text-sm font-bold text-emerald-400 font-mono">KP 1.8 (Calmo)</span>
            </div>
            <span class="text-[10px] bg-emerald-950 text-emerald-300 px-1.5 py-0.5 rounded font-mono font-semibold">GPS SEGURO</span>
          </div>
          <div class="bg-slate-900/60 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between">
            <div>
              <span class="text-[10px] text-slate-400 block">Satélites Visíveis</span>
              <span class="text-sm font-bold text-cyan-400 font-mono">29 Sats (RTK)</span>
            </div>
            <span class="text-[10px] bg-cyan-950 text-cyan-300 px-1.5 py-0.5 rounded font-mono font-semibold">PDOP 1.1</span>
          </div>
        </div>"""

    new_kp_section = """        <!-- Clima Espacial (KP Index) & Satélites com Cards Educativos -->
        <div class="grid grid-cols-2 gap-2 text-xs">
          <!-- Card KP -->
          <div onclick="openKpPdopModal('kp')" class="bg-slate-900/70 hover:bg-slate-800/80 p-2.5 rounded-xl border border-slate-800 hover:border-cyan-500/50 cursor-pointer transition flex flex-col justify-between group">
            <div class="flex items-center justify-between mb-1">
              <span class="text-[10px] text-slate-400 flex items-center gap-1 font-semibold">
                Índice Solar (KP)
                <span class="w-3.5 h-3.5 rounded-full bg-cyan-950 text-cyan-400 border border-cyan-800 flex items-center justify-center text-[8px] font-bold group-hover:bg-cyan-500 group-hover:text-slate-950 transition">ⓘ</span>
              </span>
              <span class="text-[9px] font-mono px-1.5 py-0.2 rounded font-bold transition" id="badgeKpStatus">GPS SEGURO</span>
            </div>
            <div class="flex items-baseline justify-between">
              <span class="text-sm font-bold font-mono transition" id="valKpStatus">KP 1.8 (Calmo)</span>
              <span class="text-[9px] text-cyan-400 underline font-medium">Ver Risco</span>
            </div>
          </div>

          <!-- Card PDOP -->
          <div onclick="openKpPdopModal('pdop')" class="bg-slate-900/70 hover:bg-slate-800/80 p-2.5 rounded-xl border border-slate-800 hover:border-cyan-500/50 cursor-pointer transition flex flex-col justify-between group">
            <div class="flex items-center justify-between mb-1">
              <span class="text-[10px] text-slate-400 flex items-center gap-1 font-semibold">
                Satélites & PDOP
                <span class="w-3.5 h-3.5 rounded-full bg-cyan-950 text-cyan-400 border border-cyan-800 flex items-center justify-center text-[8px] font-bold group-hover:bg-cyan-500 group-hover:text-slate-950 transition">ⓘ</span>
              </span>
              <span class="text-[9px] font-mono bg-cyan-950 text-cyan-300 px-1.5 py-0.2 rounded font-bold" id="badgePdopStatus">PDOP 1.1</span>
            </div>
            <div class="flex items-baseline justify-between">
              <span class="text-sm font-bold text-cyan-400 font-mono" id="valSatsStatus">29 Sats (RTK)</span>
              <span class="text-[9px] text-cyan-400 underline font-medium">Ver Risco</span>
            </div>
          </div>
        </div>

        <!-- Seletor de Simulação Meteorológica & Solar para o Piloto -->
        <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex items-center justify-between text-xs">
          <span class="text-[10px] text-slate-400">Simulador de Condições:</span>
          <div class="flex gap-1.5">
            <button onclick="setFlightCondition('safe')" id="btnCondSafe" class="px-2 py-1 rounded-lg text-[10px] font-bold bg-emerald-500 text-slate-950 transition active:scale-95 shadow-sm">
              ☀️ Clima Seguro (KP 1.8)
            </button>
            <button onclick="setFlightCondition('danger')" id="btnCondDanger" class="px-2 py-1 rounded-lg text-[10px] font-bold bg-slate-900 text-rose-400 border border-rose-900 hover:border-rose-500 transition active:scale-95">
              ⚠️ Tempestade Solar (KP 6.2)
            </button>
          </div>
        </div>

        <!-- ALERTA CRÍTICO DE RISCO (EXIBIDO SE SIMULAR TEMPESTADE / NO-GO) -->
        <div id="riskWarningBox" class="hidden bg-rose-950/80 border-2 border-rose-500/80 rounded-2xl p-3.5 space-y-2.5 animate-pulse">
          <div class="flex items-start gap-2.5">
            <span class="text-xl">⚠️</span>
            <div>
              <h4 class="text-xs font-black text-rose-200 uppercase tracking-wider">OPERAÇÃO EM ESTADO NO-GO / RISCO CRÍTICO</h4>
              <p class="text-[11px] text-rose-300 mt-0.5 leading-relaxed">
                Índice Solar <b>KP 6.2 (Tempestade Geomagnética G2)</b> e Rajadas de <b>42 km/h</b> detectados. Há perigo real de perda de sinal GPS, deriva incontrolável (Flyaway) e queda.
              </p>
            </div>
          </div>

          <div class="bg-black/60 p-2 rounded-xl border border-rose-800/60 text-[10px] text-slate-300 font-mono">
            <span>DECISÃO: DECOLAGEM AUTOMÁTICA REPROVADA PELO DESPACHO</span>
          </div>

          <!-- Botão para abrir o Termo de Assunção de Risco -->
          <button onclick="openRiskWaiverModal()" class="w-full py-2.5 rounded-xl bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-extrabold text-xs shadow-lg shadow-rose-950/80 active:scale-95 transition flex items-center justify-center gap-2">
            <span>📋 Abrir Termo de Assunção de Risco (Safe Harbor)</span>
          </button>
        </div>"""

    if old_kp_section in html:
        html = html.replace(old_kp_section, new_kp_section, 1)
        print("Updated KP section with educational and risk simulator")
    else:
        print("Warning: old_kp_section not matched")

    # 6. Add the 3 new modals: KpPdopModal, RiskWaiverModal, AeroAIModal
    target_modals_end = "  <!-- ================= MODAL SEGURO RETA AERONÁUTICO OBRIGATÓRIO ================= -->"
    
    new_three_modals = """  <!-- ================= MODAL EDUCATIVO: ÍNDICE KP & PDOP ================= -->
  <div id="kpPdopModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-end sm:items-center justify-center p-3 animate-fade-in">
    <div class="bg-slate-900 border border-cyan-500/50 rounded-2xl w-full max-w-md p-4 space-y-3.5 shadow-2xl max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between border-b border-slate-800 pb-2.5">
        <div class="flex items-center gap-2">
          <span class="text-xl">🛰️</span>
          <div>
            <h3 class="text-xs font-bold text-white uppercase tracking-wider">Clima Espacial & Geometria GNSS</h3>
            <p class="text-[9px] text-slate-400">Guia Técnico de Segurança de Voo para Pilotos</p>
          </div>
        </div>
        <button onclick="closeKpPdopModal()" class="text-slate-400 hover:text-white font-bold text-sm">✕</button>
      </div>

      <!-- Abas Internas: KP vs PDOP -->
      <div class="flex gap-2">
        <button onclick="switchKpTab('kp')" id="btnTabModalKp" class="flex-1 py-1.5 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition active:scale-95">
          ☀️ Índice Solar (KP)
        </button>
        <button onclick="switchKpTab('pdop')" id="btnTabModalPdop" class="flex-1 py-1.5 rounded-xl text-xs font-bold bg-slate-950 border border-slate-800 text-slate-400 transition active:scale-95">
          🛰️ PDOP & Satélites
        </button>
      </div>

      <!-- Conteúdo da Aba KP -->
      <div id="contentModalKp" class="space-y-3 text-xs">
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
          <span class="text-cyan-400 font-bold block text-xs">O que é o Índice KP (0 a 9) da NOAA?</span>
          <p class="text-slate-300 leading-relaxed text-[11px]">
            O <b>Índice Planetário Kp</b> é a métrica oficial da <b>NOAA</b> (Agência Espacial e Oceânica dos EUA) que quantifica distúrbios geomagnéticos causados pelo vento solar e ejeções de massa coronal que atingem o campo magnético da Terra.
          </p>
        </div>

        <div class="space-y-1.5 text-[11px]">
          <span class="text-white font-bold block">Por que o KP alto é perigoso para o drone?</span>
          <div class="bg-slate-950/80 p-2.5 rounded-lg border border-slate-800 space-y-1 text-slate-300">
            <div class="flex items-start gap-1.5">
              <span class="text-rose-400 font-bold">1.</span>
              <span><b>Distorção do Sinal GPS:</b> Partículas solares ionizam a camada F2 da atmosfera, alterando a velocidade de propagação do sinal dos satélites e gerando erros de metros na posição calculada.</span>
            </div>
            <div class="flex items-start gap-1.5">
              <span class="text-rose-400 font-bold">2.</span>
              <span><b>Perda de Fix no RTK:</b> Em mapeamentos com RTK, o receptor não consegue fixar ambiguidades (perda da precisão centimétrica).</span>
            </div>
            <div class="flex items-start gap-1.5">
              <span class="text-rose-400 font-bold">3.</span>
              <span><b>Risco de Flyaway:</b> A bússola magnética interna entra em conflito com o vetor de GPS distorcido. A controladora pode desarmar o modo de posição e o drone sair voando com o vento.</span>
            </div>
          </div>
        </div>

        <!-- Tabela de Decisão KP -->
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1.5 text-[10px] font-mono">
          <div class="flex justify-between items-center text-emerald-400 font-bold">
            <span>KP 0 a 3: Calmo (Seguro)</span>
            <span class="bg-emerald-950 px-1.5 py-0.5 rounded border border-emerald-800">VOO AUTORIZADO</span>
          </div>
          <div class="flex justify-between items-center text-amber-400 font-bold">
            <span>KP 4: Moderado</span>
            <span class="bg-amber-950 px-1.5 py-0.5 rounded border border-amber-800">ATENÇÃO REDOBRADA</span>
          </div>
          <div class="flex justify-between items-center text-rose-400 font-bold">
            <span>KP 5 a 9: Tempestade Solar G1-G5</span>
            <span class="bg-rose-950 px-1.5 py-0.5 rounded border border-rose-800">NO-GO / CRÍTICO</span>
          </div>
        </div>
      </div>

      <!-- Conteúdo da Aba PDOP -->
      <div id="contentModalPdop" class="space-y-3 text-xs hidden">
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
          <span class="text-cyan-400 font-bold block text-xs">O que é PDOP (Positional Dilution of Precision)?</span>
          <p class="text-slate-300 leading-relaxed text-[11px]">
            O <b>PDOP</b> é o valor matemático que expressa a qualidade da <b>geometria tridimensional dos satélites</b> visíveis no céu. Quanto mais espalhados em diferentes ângulos da abóbada celeste os satélites estiverem, menor será o valor de PDOP e maior a precisão do drone.
          </p>
        </div>

        <div class="space-y-1.5 text-[11px]">
          <span class="text-white font-bold block">Critérios Operacionais de PDOP:</span>
          <div class="bg-slate-950/80 p-2.5 rounded-lg border border-slate-800 space-y-1.5 text-slate-300 text-[10px] font-mono">
            <div class="flex justify-between items-center text-emerald-400">
              <span>PDOP &lt; 2.0 (Excelente):</span>
              <span class="font-bold">Precisão Centimétrica RTK Ideal</span>
            </div>
            <div class="flex justify-between items-center text-cyan-400">
              <span>PDOP 2.0 a 3.0 (Bom):</span>
              <span class="font-bold">Apropriado para Inspeções Visuais</span>
            </div>
            <div class="flex justify-between items-center text-amber-400">
              <span>PDOP 3.0 a 5.0 (Pobre):</span>
              <span class="font-bold">Erro Métrico, Não recomendado RTK</span>
            </div>
            <div class="flex justify-between items-center text-rose-400">
              <span>PDOP &gt; 5.0 (Inaceitável):</span>
              <span class="font-bold">Satélites alinhados ou bloqueados</span>
            </div>
          </div>
        </div>
      </div>

      <button onclick="closeKpPdopModal()" class="w-full py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded-xl transition">
        Entendido, Fechar Guia
      </button>
    </div>
  </div>

  <!-- ================= MODAL TERMO DE ASSUNÇÃO DE RISCO (WAIVER / SAFE HARBOR) ================= -->
  <div id="riskWaiverModal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden flex items-end sm:items-center justify-center p-3 animate-fade-in">
    <div class="bg-slate-900 border-2 border-rose-500/80 rounded-2xl w-full max-w-md p-4 space-y-3.5 shadow-2xl max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between border-b border-slate-800 pb-2.5">
        <div class="flex items-center gap-2">
          <span class="text-xl">⚠️</span>
          <div>
            <h3 class="text-xs font-black text-rose-300 uppercase tracking-wider">Termo de Assunção de Responsabilidade</h3>
            <p class="text-[9px] text-slate-400">Operação em Condições Meteorológicas/Solares NO-GO</p>
          </div>
        </div>
        <button onclick="closeRiskWaiverModal()" class="text-slate-400 hover:text-white font-bold text-sm">✕</button>
      </div>

      <!-- Texto Jurídico Oficial de Safe Harbor -->
      <div class="bg-slate-950 p-3 rounded-xl border border-rose-900/50 space-y-2 text-xs">
        <span class="text-[10px] font-mono text-rose-400 font-bold block uppercase">Declaração Operacional & Isenção de Responsabilidade:</span>
        <div class="text-slate-300 text-[11px] leading-relaxed space-y-1.5 max-h-36 overflow-y-auto pr-1">
          <p>
            <b>1. CIÊNCIA DOS RISCOS:</b> O piloto abaixo qualificado declara ter sido expressamente notificado pelo sistema DroneHub sobre a existência de parâmetros meteorológicos e/ou espaciais adversos (vento acima dos limites recomendados e/ou tempestade solar com índice KP ≥ 5), os quais desaconselham a decolagem.
          </p>
          <p>
            <b>2. ASSUNÇÃO INTEGRAL DE CULPA E RISCO:</b> Ao optar conscientemente por executar a decolagem, o piloto declara possuir capacidade técnica para pilotagem em modo manual (ATTI), assumindo de forma pessoal, integral e irrevogável toda a responsabilidade civil, criminal e administrativa por eventuais acidentes, colisões, danos materiais a terceiros, lesões corporais, flyaways ou perda do equipamento (fundamentado nos Arts. 186 e 927 do Código Civil Brasileiro e RBAC-E 94 ANAC).
          </p>
          <p>
            <b>3. ISENÇÃO TOTAL DA PLATAFORMA:</b> O operador isenta a plataforma DroneHub de qualquer corresponsabilidade solidária ou subsidiária decorrente da decisão autônoma e unilateral de voo.
          </p>
        </div>
      </div>

      <!-- Formulário de Aceite Digital do Piloto -->
      <form onsubmit="handleRiskWaiverSubmit(e); return false;" class="space-y-2.5 text-xs">
        <div>
          <label class="text-[10px] text-slate-400 block mb-0.5">Nome Completo do Piloto em Comando:</label>
          <input type="text" id="waiverPilotName" required value="Lucas Andrade" class="w-full bg-slate-950 border border-slate-800 text-slate-200 text-xs rounded-xl p-2 focus:border-rose-500">
        </div>
        <div>
          <label class="text-[10px] text-slate-400 block mb-0.5">Registro do Piloto (ANAC / FAA / DGAC):</label>
          <input type="text" id="waiverPilotReg" required value="PP-892144702" class="w-full bg-slate-950 border border-slate-800 text-slate-200 text-xs rounded-xl p-2 focus:border-rose-500">
        </div>
        
        <label class="flex items-start gap-2 p-2 rounded-xl bg-rose-950/40 border border-rose-800/60 cursor-pointer">
          <input type="checkbox" id="waiverCheckbox" required class="accent-rose-500 mt-0.5">
          <span class="text-[10px] text-rose-200 leading-tight">
            Li, compreendi os riscos de flyaway/queda e assumo 100% da responsabilidade pela operação em modo de risco, isentando a DroneHub.
          </span>
        </label>

        <button type="submit" class="w-full py-2.5 rounded-xl bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-extrabold text-xs shadow-lg shadow-rose-950/80 active:scale-95 transition">
          ✍️ Assinar Termo Digitalmente & Liberar Voo
        </button>
      </form>
    </div>
  </div>

  <!-- ================= MODAL CENTRAL: COPILOTO IA DE ESPAÇO AÉREO PAN-AMERICANO ================= -->
  <div id="aeroAIModal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden flex items-end sm:items-center justify-center p-3 animate-fade-in">
    <div class="bg-slate-900 border border-cyan-500/50 rounded-2xl w-full max-w-lg p-4 space-y-3 shadow-2xl flex flex-col h-[85vh]">
      <!-- Cabeçalho da IA -->
      <div class="flex items-center justify-between border-b border-slate-800 pb-2.5">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-xl bg-cyan-500/20 border border-cyan-400/50 flex items-center justify-center text-base">
            🤖
          </div>
          <div>
            <div class="flex items-center gap-1.5">
              <h3 class="text-xs font-bold text-white uppercase tracking-wider">AeroAI • Copiloto Pan-Americano</h3>
              <span class="text-[8px] font-mono bg-emerald-950 text-emerald-300 border border-emerald-700 px-1 rounded font-bold">SISTEMA ATIVO</span>
            </div>
            <p class="text-[9px] text-cyan-400">Autorizações, Legislações das Américas, KP e Segurança</p>
          </div>
        </div>
        <button onclick="closeAeroAIModal()" class="text-slate-400 hover:text-white font-bold text-sm">✕</button>
      </div>

      <!-- Barra de Atalhos Rápidos por País / Assunto -->
      <div class="flex gap-1.5 overflow-x-auto pb-1 text-[10px] font-semibold">
        <button onclick="askAeroAI('Quais as regras do Brasil (DECEA, SARPAS, ANAC, Seguro RETA)?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-slate-300 rounded-lg whitespace-nowrap active:scale-95">🇧🇷 Brasil (SARPAS)</button>
        <button onclick="askAeroAI('Sou do Brasil e vou voar no Canadá. Quais as regras da Transport Canada?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-slate-300 rounded-lg whitespace-nowrap active:scale-95">🇨🇦 Canadá (Regras)</button>
        <button onclick="askAeroAI('Quais as regras da FAA para voar comercialmente nos EUA (Part 107 e LAANC)?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-slate-300 rounded-lg whitespace-nowrap active:scale-95">🇺🇸 EUA (FAA LAANC)</button>
        <button onclick="askAeroAI('Quais são as regras para operar drone no Equador (DGAC RDAC 101)?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-slate-300 rounded-lg whitespace-nowrap active:scale-95">🇪🇨 Equador (DGAC)</button>
        <button onclick="askAeroAI('Quais as regras no México (AFAC NOM-107)?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-slate-300 rounded-lg whitespace-nowrap active:scale-95">🇲🇽 México (AFAC)</button>
        <button onclick="askAeroAI('Quais as regras na Colômbia (Aerocivil RAC 100)?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-slate-300 rounded-lg whitespace-nowrap active:scale-95">🇨🇴 Colômbia (RAC 100)</button>
        <button onclick="askAeroAI('Quais as regras na Argentina (ANAC Res. 880)?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-slate-300 rounded-lg whitespace-nowrap active:scale-95">🇦🇷 Argentina (ANAC)</button>
        <button onclick="askAeroAI('Quais as regras no Chile (DGAC DAN 151)?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-slate-300 rounded-lg whitespace-nowrap active:scale-95">🇨🇱 Chile (DGAC)</button>
        <button onclick="askAeroAI('Quais as regras no Peru (DGAC NTC 001)?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-slate-300 rounded-lg whitespace-nowrap active:scale-95">🇵🇪 Peru (DGAC)</button>
        <button onclick="askAeroAI('O que é o Índice KP e por que voar com KP acima de 5 causa flyaway?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-amber-300 rounded-lg whitespace-nowrap active:scale-95">☀️ O que é KP Solar?</button>
        <button onclick="askAeroAI('O que é PDOP e qual o valor ideal para topografia com RTK?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-cyan-300 rounded-lg whitespace-nowrap active:scale-95">🛰️ O que é PDOP?</button>
        <button onclick="askAeroAI('Como funciona a bússola giroscópica e a orientação magnética no drone?')" class="px-2.5 py-1 bg-slate-950 border border-slate-800 hover:border-cyan-500 text-emerald-300 rounded-lg whitespace-nowrap active:scale-95">🧭 Bússola & Orientação</button>
      </div>

      <!-- Feed de Chat da IA -->
      <div id="aeroAIChatFeed" class="flex-1 overflow-y-auto space-y-3 p-2 bg-slate-950 rounded-xl border border-slate-800 text-xs">
        <div class="bg-cyan-950/40 border border-cyan-800/40 p-2.5 rounded-xl space-y-1">
          <div class="flex items-center gap-1.5 font-bold text-cyan-400 font-mono text-[11px]">
            <span>🤖 AeroAI Copilot:</span>
          </div>
          <p class="text-slate-200 text-[11px] leading-relaxed">
            Olá comandante! Sou o seu <b>Copiloto de Espaço Aéreo e Conformidade Regulatória Pan-Americana</b>.
          </p>
          <p class="text-slate-400 text-[10px]">
            Posso tirar dúvidas sobre autorizações de voo (SARPAS no Brasil, FAA nos EUA, Transport Canada, DGAC Equador/Chile/Peru), exigência de Seguro RETA, limites de teto AGL, distâncias de aeroportos e riscos de clima solar (KP Index e PDOP).
          </p>
        </div>
      </div>

      <!-- Caixa de Pergunta -->
      <form onsubmit="handleAeroAISubmit(event)" class="flex gap-2 pt-1">
        <input type="text" id="aeroAIInput" placeholder="Ex: Sou do Brasil e vou voar no Canadá, quais as regras?" 
               class="flex-1 bg-slate-950 border border-slate-800 text-slate-200 text-xs rounded-xl px-3 py-2.5 focus:outline-none focus:border-cyan-500">
        <button type="submit" class="bg-gradient-to-r from-cyan-500 to-teal-500 hover:from-cyan-400 hover:to-teal-400 text-slate-950 font-bold px-4 py-2.5 rounded-xl text-xs transition active:scale-95">
          Perguntar
        </button>
      </form>
    </div>
  </div>

  <!-- ================= MODAL SEGURO RETA AERONÁUTICO OBRIGATÓRIO ================= -->"""

    if target_modals_end in html:
        html = html.replace(target_modals_end, new_three_modals, 1)
        print("Inserted the 3 new modals successfully")
    else:
        print("Warning: target_modals_end not matched")

    # 7. Add JavaScript for Bússola, Modais, KP/PDOP Simulator, Waiver and AeroAI with strict guardrails
    target_js_end = "// 10. CALCULADORA DE MISSÃO & DESPACHO"

    new_js_logic = """// ——————————————————————————————————————————————————————————
// 9.5 BÚSSOLA TÁTICA 360°, SIMULADOR METEOROLÓGICO & COPILOTO IA
// ——————————————————————————————————————————————————————————
let currentDroneHeading = 42; // Rumo inicial 042° NE
let currentFlightCondition = 'safe'; // 'safe' | 'danger'

// Controle da Bússola Tática
function rotateDroneHeading(degrees) {
  currentDroneHeading = degrees % 360;
  
  // Atualiza Bússola do Cockpit
  const dial = document.getElementById('cockpitCompassDial');
  if (dial) dial.style.transform = `rotate(${currentDroneHeading}deg)`;
  
  // Atualiza Bússola do HUD
  const hudRose = document.getElementById('hudCompassRose');
  if (hudRose) hudRose.style.transform = `rotate(${currentDroneHeading}deg)`;

  // Cardinal point
  let cardinal = 'N';
  if (currentDroneHeading >= 23 && currentDroneHeading < 68) cardinal = 'NE';
  else if (currentDroneHeading >= 68 && currentDroneHeading < 113) cardinal = 'Leste (E)';
  else if (currentDroneHeading >= 113 && currentDroneHeading < 158) cardinal = 'SE';
  else if (currentDroneHeading >= 158 && currentDroneHeading < 203) cardinal = 'Sul (S)';
  else if (currentDroneHeading >= 203 && currentDroneHeading < 248) cardinal = 'SW';
  else if (currentDroneHeading >= 248 && currentDroneHeading < 293) cardinal = 'Oeste (W)';
  else if (currentDroneHeading >= 293 && currentDroneHeading < 338) cardinal = 'NW';

  const headingStr = String(currentDroneHeading).padStart(3, '0') + '°';
  const headingText = document.getElementById('cockpitHeadingText');
  if (headingText) headingText.innerText = `${headingStr} (${cardinal})`;

  const hudHeadingVal = document.getElementById('hudHeadingVal');
  if (hudHeadingVal) hudHeadingVal.innerText = `${headingStr} ${cardinal}`;
}

// Alternar Condições de Voo (Normal vs Tempestade Solar KP)
function setFlightCondition(condition) {
  currentFlightCondition = condition;
  const btnSafe = document.getElementById('btnCondSafe');
  const btnDanger = document.getElementById('btnCondDanger');
  const badgeKp = document.getElementById('badgeKpStatus');
  const valKp = document.getElementById('valKpStatus');
  const scoreBadge = document.getElementById('cockpitScoreBadge');
  const pulseDot = document.getElementById('cockpitPulseDot');
  const riskBox = document.getElementById('riskWarningBox');
  const sarpasText = document.getElementById('cockpitSarpasText');

  if (condition === 'safe') {
    btnSafe.className = 'px-2 py-1 rounded-lg text-[10px] font-bold bg-emerald-500 text-slate-950 transition active:scale-95 shadow-sm';
    btnDanger.className = 'px-2 py-1 rounded-lg text-[10px] font-bold bg-slate-900 text-rose-400 border border-rose-900 hover:border-rose-500 transition active:scale-95';
    
    badgeKp.className = 'text-[9px] font-mono bg-emerald-950 text-emerald-300 px-1.5 py-0.2 rounded font-bold';
    badgeKp.innerText = 'GPS SEGURO';
    valKp.className = 'text-sm font-bold font-mono text-emerald-400';
    valKp.innerText = 'KP 1.8 (Calmo)';
    
    scoreBadge.className = 'text-[11px] font-mono text-emerald-400 font-bold bg-emerald-950/70 border border-emerald-800 px-2 py-0.5 rounded';
    scoreBadge.innerText = 'GO / SCORE 94%';
    pulseDot.className = 'w-2 h-2 rounded-full bg-cyan-400 animate-pulse';
    sarpasText.innerText = 'SARPAS DECEA: AUTORIZADO (BR-94812) • VOO VLOS';

    riskBox.classList.add('hidden');
  } else {
    btnSafe.className = 'px-2 py-1 rounded-lg text-[10px] font-bold bg-slate-900 text-slate-400 border border-slate-800 transition active:scale-95';
    btnDanger.className = 'px-2 py-1 rounded-lg text-[10px] font-bold bg-rose-600 text-white transition active:scale-95 shadow-md shadow-rose-900';
    
    badgeKp.className = 'text-[9px] font-mono bg-rose-950 text-rose-300 px-1.5 py-0.2 rounded font-bold animate-pulse';
    badgeKp.innerText = 'TEMPESTADE G2';
    valKp.className = 'text-sm font-bold font-mono text-rose-400';
    valKp.innerText = 'KP 6.2 (Crítico)';
    
    scoreBadge.className = 'text-[11px] font-mono text-rose-400 font-bold bg-rose-950/90 border border-rose-700 px-2 py-0.5 rounded animate-pulse';
    scoreBadge.innerText = 'NO-GO / SCORE 35%';
    pulseDot.className = 'w-2 h-2 rounded-full bg-rose-500 animate-ping';
    sarpasText.innerText = 'SARPAS DECEA: SUSPENSO DEVIDO A ALERTA METEOROLÓGICO/SOLAR';

    riskBox.classList.remove('hidden');
  }
}

// Modais de KP / PDOP
function openKpPdopModal(tab) {
  document.getElementById('kpPdopModal').classList.remove('hidden');
  switchKpTab(tab || 'kp');
}
function closeKpPdopModal() {
  document.getElementById('kpPdopModal').classList.add('hidden');
}
function switchKpTab(tab) {
  const btnKp = document.getElementById('btnTabModalKp');
  const btnPdop = document.getElementById('btnTabModalPdop');
  const contentKp = document.getElementById('contentModalKp');
  const contentPdop = document.getElementById('contentModalPdop');

  if (tab === 'kp') {
    btnKp.className = 'flex-1 py-1.5 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition active:scale-95';
    btnPdop.className = 'flex-1 py-1.5 rounded-xl text-xs font-bold bg-slate-950 border border-slate-800 text-slate-400 transition active:scale-95';
    contentKp.classList.remove('hidden');
    contentPdop.classList.add('hidden');
  } else {
    btnPdop.className = 'flex-1 py-1.5 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition active:scale-95';
    btnKp.className = 'flex-1 py-1.5 rounded-xl text-xs font-bold bg-slate-950 border border-slate-800 text-slate-400 transition active:scale-95';
    contentPdop.classList.remove('hidden');
    contentKp.classList.add('hidden');
  }
}

// Modal de Termo de Assunção de Risco (Waiver)
function openRiskWaiverModal() {
  document.getElementById('riskWaiverModal').classList.remove('hidden');
}
function closeRiskWaiverModal() {
  document.getElementById('riskWaiverModal').classList.add('hidden');
}
function handleRiskWaiverSubmit(e) {
  if (e) e.preventDefault();
  const pilotName = document.getElementById('waiverPilotName').value;
  const pilotReg = document.getElementById('waiverPilotReg').value;
  const isChecked = document.getElementById('waiverCheckbox').checked;

  if (!isChecked) {
    alert('⚠️ Você deve marcar a caixa concordando em assumir os riscos operacionais.');
    return;
  }

  const logTimestamp = new Date().toISOString();
  console.log(`[SAFE HARBOR WAIVER LOG] Piloto: ${pilotName} | Registro: ${pilotReg} | Data: ${logTimestamp} | Condição: KP 6.2 Assumido`);
  
  closeRiskWaiverModal();
  alert(`✅ TERMO DE RESPONSABILIDADE ASSINADO DIGITALMENTE!\\n\\nPiloto: ${pilotName}\\nRegistro: ${pilotReg}\\nData/Hora: ${new Date().toLocaleString('pt-BR')}\\n\\nO despacho liberou o modo manual de emergência. A DroneHub fica isenta de qualquer solidariedade por sinistros decorrentes desta operação.`);
}

// ——————————————————————————————————————————————————————————
// BASE DE CONHECIMENTO AEROESPACIAL PAN-AMERICANA (AEROAI)
// ——————————————————————————————————————————————————————————
const AERO_KNOWLEDGE_BASE = {
  brasil: {
    orgaos: "DECEA (Força Aérea Brasileira), ANAC e ANATEL.",
    sistema: "SARPAS NG (Sistema de Solicitação de Acesso ao Espaço Aéreo por RPA).",
    leis: "ICA 100-40 (DECEA) e RBAC-E 94 (ANAC).",
    seguro: "Seguro RETA obrigatório (Lei 7.565/86 - Código Brasileiro de Aeronáutica).",
    teto: "120 metros (400 pés) AGL para voos normais VLOS.",
    aeroportos: "Distância mínima de 5,4 km (3 NM) a 9 km dependendo da zona de aproximação.",
    estrangeiro: "Pilotos estrangeiros no Brasil precisam homologar o rádio na Anatel, cadastrar a aeronave no SISANT da ANAC com CPF/Passaporte e submeter voo no SARPAS com antecedência mínima de 48h a 18 dias úteis se for área urbana."
  },
  canada: {
    orgaos: "Transport Canada (Aviation Civile).",
    sistema: "Drone Management Portal & NAV CANADA NAV Drone App.",
    leis: "Canadian Aviation Regulations (CARs) Part IX.",
    categorias: "Micro-drones (&lt;250g como DJI Mini) não precisam de registro nem licença, mas exigem voo seguro. Drones de 250g a 25kg exigem registro de $5 CAD e exame de piloto (Basic ou Advanced).",
    teto: "122 metros (400 pés) AGL.",
    aeroportos: "5,6 km (3 milhas náuticas) de aeroportos certificados e 1,9 km de heliportos.",
    estrangeiro: "ATENÇÃO PILOTO BRASILEIRO NO CANADÁ: Você NÃO pode operar comercialmente no Canadá sem um SFOC (Special Flight Operations Certificate for Foreign Operators). Você precisa solicitar com pelo menos 30 dias de antecedência no Transport Canada comprovando certificação e seguro de responsabilidade civil!"
  },
  eua: {
    orgaos: "FAA (Federal Aviation Administration).",
    sistema: "LAANC (Low Altitude Authorization and Notification Capability) e FAADroneZone.",
    leis: "14 CFR Part 107 (Operações Comerciais) e 49 U.S.C. 44809 (Recreativo TRUST).",
    requisitos: "Remote ID obrigatório para todos os drones com mais de 250g. Certificado de Piloto Remoto Part 107 para qualquer atividade comercial.",
    teto: "400 pés (122 metros) AGL.",
    aeroportos: "Autorização automática em tempo real via LAANC perto de centenas de aeroportos classe B, C, D e E.",
    estrangeiro: "Piloto estrangeiro nos EUA precisa registrar o drone no FAADroneZone ($5 USD) e passar no exame Part 107 (presencial nos EUA em centro PSI) se for receber por qualquer trabalho, ou TRUST se for lazer."
  },
  mexico: {
    orgaos: "AFAC (Agencia Federal de Aviación Civil).",
    sistema: "Portal de Registro de RPAS AFAC.",
    leis: "Norma Oficial Mexicana NOM-107-SCT3-2019.",
    requisitos: "Registro obrigatório de qualquer drone acima de 250g. Seguro de responsabilidade civil para danos a terceiros obrigatório para uso comercial.",
    teto: "122 metros (400 pés) AGL.",
    aeroportos: "9,2 km de aeroportos controlados e 900 metros de heliportos.",
    estrangeiro: "Pilotos estrangeiros no México só podem operar drones com autorização temporária prévia da AFAC e não podem realizar trabalhos comerciais sem visto de trabalho mexicano e seguro emitido no país."
  },
  colombia: {
    orgaos: "Aerocivil (Unidad Administrativa Especial de Aeronáutica Civil - UAEAC).",
    sistema: "SISANDRONES (Sistema de Aeronaves No Tripuladas).",
    leis: "Regulamento Aeronáutico da Colômbia - RAC 100.",
    requisitos: "Registro do drone, certificado de idoneidade de piloto emitido por centro de instrução certificado (CIAC) e apólice de seguro contra terceiros.",
    teto: "123 metros (400 pés) AGL.",
    aeroportos: "Distância mínima de 5 km de aeródromos e 1 km de heliportos.",
    estrangeiro: "Turistas podem operar drones recreativos sub-250g. Para drones maiores ou uso comercial, deve homologar a licença estrangeira na Aerocivil."
  },
  argentina: {
    orgaos: "ANAC (Administración Nacional de Aviación Civil).",
    sistema: "Casillero Aeronáutico Digital (CAD).",
    leis: "Resolução ANAC 880/2019.",
    requisitos: "Registro de VANT, seguro obrigatório e certificado de competência de piloto.",
    teto: "120 metros AGL.",
    estrangeiro: "Necessário registro temporário no CAD da ANAC Argentina antes de cruzar a alfândega com o drone."
  },
  chile: {
    orgaos: "DGAC (Dirección General de Aeronáutica Civil de Chile).",
    sistema: "Sistema de Registro de RPA da DGAC.",
    leis: "DAN 151 (Áreas povoadas) e DAN 91 (Geral).",
    requisitos: "Credencial de operador RPA, drone empadronado com placa metálica e apólice de seguro de responsabilidade civil aeronáutica.",
    teto: "130 metros AGL."
  },
  peru: {
    orgaos: "DGAC Perú (Ministerio de Transportes y Comunicaciones - MTC).",
    sistema: "Registro Nacional de RPAS do MTC.",
    leis: "Norma Técnica Complementar NTC 001-2015.",
    requisitos: "Cartão de registro de aeronave, licença de operador e autorização de sobrevoo para áreas urbanas.",
    teto: "152 metros (500 pés) AGL."
  },
  equador: {
    orgaos: "DGAC Ecuador (Dirección General de Aviación Civil).",
    sistema: "Registro de RPAS DGAC.",
    leis: "Regulamento RDAC Parte 101.",
    requisitos: "Drones acima de 250g devem ser registrados. É obrigatório seguro contra terceiros para uso comercial. É proibido sobrevoar parques nacionais como Galápagos sem licença ambiental especial do Ministério do Ambiente.",
    teto: "122 metros (400 pés) AGL.",
    aeroportos: "9 km de aeroportos internacionais e 3 km de pistas secundárias."
  }
};

// Funções do Modal Copiloto IA
function openAeroAIModal() {
  document.getElementById('aeroAIModal').classList.remove('hidden');
  const chatFeed = document.getElementById('aeroAIChatFeed');
  chatFeed.scrollTop = chatFeed.scrollHeight;
}
function closeAeroAIModal() {
  document.getElementById('aeroAIModal').classList.add('hidden');
}

function handleAeroAISubmit(e) {
  if (e) e.preventDefault();
  const input = document.getElementById('aeroAIInput');
  const question = input.value.trim();
  if (!question) return;
  input.value = '';
  askAeroAI(question);
}

function askAeroAI(question) {
  openAeroAIModal();
  const chatFeed = document.getElementById('aeroAIChatFeed');

  // Adiciona a pergunta do usuário no chat
  chatFeed.innerHTML += `
    <div class="bg-slate-900 border border-slate-800 p-2.5 rounded-xl ml-4 space-y-1 animate-slide-up">
      <span class="text-[10px] text-cyan-400 font-bold block font-mono">PILOTO COMANDANTE:</span>
      <span class="text-slate-200 text-xs">${escapeHtml(question)}</span>
    </div>
  `;
  chatFeed.scrollTop = chatFeed.scrollHeight;

  // Resposta com Inteligência Semântica e Filtro de Segurança
  setTimeout(() => {
    const responseHtml = processAeroAIQuery(question);
    chatFeed.innerHTML += `
      <div class="bg-cyan-950/40 border border-cyan-800/40 p-2.5 rounded-xl mr-4 space-y-1.5 animate-slide-up">
        <div class="flex items-center justify-between">
          <span class="text-[10px] text-emerald-400 font-bold font-mono">🤖 AEROAI COPILOT:</span>
          <span class="text-[8px] text-slate-400 font-mono">CONFORMIDADE VERIFICADA</span>
        </div>
        <div class="text-slate-200 text-[11px] leading-relaxed">
          ${responseHtml}
        </div>
      </div>
    `;
    chatFeed.scrollTop = chatFeed.scrollHeight;
  }, 400);
}

function escapeHtml(text) {
  const div = document.createElement('div');
  div.innerText = text;
  return div.innerHTML;
}

// Mecanismo de Inteligência Artificial Aeronáutica com Guardrails
function processAeroAIQuery(q) {
  const query = q.toLowerCase();

  // GUARDRAIL RIGOROSO: Bloqueio de assuntos estranhos ao universo de drones e espaço aéreo
  const forbiddenKeywords = [
    'futebol', 'jogo', 'receita', 'fazer bolo', 'piada', 'presidente', 'eleição', 
    'fofoca', 'bitcoin', 'namoro', 'signo', 'horóscopo', 'filme', 'série', 'musica', 'canção'
  ];
  for (const word of forbiddenKeywords) {
    if (query.includes(word)) {
      return `
        <div class="p-2 rounded-lg bg-rose-950/60 border border-rose-800/60 text-rose-200 text-[11px]">
          🔒 <b>ASSUNTO FORA DO ESCOPO AERONÁUTICO:</b><br>
          Como Copiloto Oficial de Espaço Aéreo da DroneHub, meu sistema de inteligência opera exclusivamente com base em normas de aviação civil (DECEA, ANAC, FAA, Transport Canada, DGAC), autorizações de voo, clima espacial (KP/PDOP) e segurança operacional de drones nas Américas. Por favor, envie uma dúvida relacionada a regulamentações ou voo de aeronaves não tripuladas!
        </div>
      `;
    }
  }

  // 1. CANADÁ / PILOTO BRASILEIRO NO CANADÁ
  if (query.includes('canadá') || query.includes('canada') || (query.includes('brasil') && query.includes('canada'))) {
    const c = AERO_KNOWLEDGE_BASE.canada;
    return `
      <div class="space-y-1.5">
        <span class="font-bold text-cyan-300 block">🇨🇦 REGRAS DE VOO NO CANADÁ (TRANSPORT CANADA):</span>
        <p><b>1. Drones &lt; 250g (ex: DJI Mini):</b> Não requerem licença nem registro obrigatório, mas devem ser voados em VLOS com segurança e longe de aeroportos.</p>
        <p><b>2. Drones de 250g a 25kg:</b> Exigem cadastro no Drone Management Portal ($5 CAD) e certificado de piloto (Basic ou Advanced).</p>
        <p><b>3. Teto Máximo:</b> 122 metros (400 pés) AGL. Distância de aeroportos: 5,6 km (3 NM).</p>
        <div class="p-2 rounded-lg bg-amber-950/50 border border-amber-800/60 text-amber-200 mt-1">
          ⚠️ <b>SE VOCÊ FOR PILOTO BRASILEIRO INDO AO CANADÁ:</b><br>
          Cidadãos estrangeiros NÃO podem operar drones comercialmente no Canadá sem solicitar previamente o <b>SFOC (Special Flight Operations Certificate for Foreign Operators)</b> junto à Transport Canada com pelo menos 30 dias de antecedência!
        </div>
      </div>
    `;
  }

  // 2. EQUADOR (DGAC RDAC 101)
  if (query.includes('equador') || query.includes('ecuador')) {
    const e = AERO_KNOWLEDGE_BASE.equador;
    return `
      <div class="space-y-1.5">
        <span class="font-bold text-cyan-300 block">🇪🇨 REGRAS PARA DRONES NO EQUADOR (DGAC):</span>
        <p><b>1. Órgão Regulador:</b> Dirección General de Aviación Civil (DGAC) - Regulamento <b>RDAC Parte 101</b>.</p>
        <p><b>2. Registro Obrigatório:</b> Todos os drones acima de 250g devem ser cadastrados no portal da DGAC antes da operação.</p>
        <p><b>3. Seguro:</b> Apólice de responsabilidade civil contra danos a terceiros obrigatória para operações comerciais.</p>
        <p><b>4. Limites de Voo:</b> Altura máxima de 122 metros (400 pés) AGL e pelo menos 9 km de distância de aeroportos internacionais.</p>
        <div class="p-2 rounded-lg bg-cyan-950/60 border border-cyan-800/60 text-cyan-200 mt-1">
          📌 <b>Dica Galápagos:</b> Se for visitar o Parque Nacional Galápagos, é terminantemente proibido voar sem autorização expressa conjunta da DGAC e do Ministério do Ambiente.
        </div>
      </div>
    `;
  }

  // 3. BRASIL (DECEA / SARPAS / ANAC / SEGURO RETA)
  if (query.includes('brasil') || query.includes('sarpas') || query.includes('decea') || query.includes('anac') || query.includes('reta')) {
    const b = AERO_KNOWLEDGE_BASE.brasil;
    return `
      <div class="space-y-1.5">
        <span class="font-bold text-cyan-300 block">🇧🇷 REGULAMENTAÇÃO BRASILEIRA (DECEA / ANAC / ANATEL):</span>
        <p><b>1. Controle do Espaço Aéreo:</b> O espaço aéreo pertence ao DECEA (FAB). Qualquer voo comercial deve ser submetido via sistema <b>SARPAS NG</b>.</p>
        <p><b>2. Cadastro ANAC:</b> Drones com mais de 250g devem possuir registro no SISANT e identificação visível (PP-XXXXXXXXX).</p>
        <p><b>3. Seguro RETA Obrigatório:</b> Exigido pelo Código Brasileiro de Aeronáutica (Art. 178 da Lei 7.565/86) para garantir danos a terceiros no solo.</p>
        <p><b>4. Parâmetros de Voo:</b> Altura máxima de 120m AGL, operação sempre em linha de visada visual (VLOS) a menos de 30m de pessoas não anuentes.</p>
      </div>
    `;
  }

  // 4. ESTADOS UNIDOS (FAA PART 107 / LAANC)
  if (query.includes('eua') || query.includes('estados unidos') || query.includes('usa') || query.includes('faa') || query.includes('laanc')) {
    const u = AERO_KNOWLEDGE_BASE.eua;
    return `
      <div class="space-y-1.5">
        <span class="font-bold text-cyan-300 block">🇺🇸 REGRAS NOS ESTADOS UNIDOS (FAA):</span>
        <p><b>1. Operação Comercial (Part 107):</b> Exige obter a licença Remote Pilot Certificate da FAA (exame presencial de conhecimentos aeronáuticos).</p>
        <p><b>2. Autorização em Espaço Controlado (LAANC):</b> Use aplicativos autorizados da FAA (como Aloft/Airspace Link) para receber autorização quase instantânea em espaços classe B, C, D e E.</p>
        <p><b>3. Remote ID:</b> Obrigatório para qualquer drone comercial ou com mais de 250g transmitindo sinal de localização em tempo real.</p>
        <p><b>4. Teto de Voo:</b> 400 pés (122m) AGL. Velocidade máx: 100 mph (160 km/h).</p>
      </div>
    `;
  }

  // 5. MÉXICO
  if (query.includes('méxico') || query.includes('mexico') || query.includes('afac')) {
    return `
      <div class="space-y-1.5">
        <span class="font-bold text-cyan-300 block">🇲🇽 REGRAS NO MÉXICO (AFAC):</span>
        <p><b>1. Norma Oficial:</b> NOM-107-SCT3-2019 da Agencia Federal de Aviación Civil.</p>
        <p><b>2. Registro:</b> Obrigatório no portal da AFAC para drones com mais de 250g.</p>
        <p><b>3. Seguro:</b> Seguro de responsabilidade civil contra danos a terceiros obrigatório para qualquer voo comercial.</p>
        <p><b>4. Limites:</b> 122m AGL e distância de 9,2 km de aeroportos controlados.</p>
      </div>
    `;
  }

  // 6. COLÔMBIA
  if (query.includes('colômbia') || query.includes('colombia') || query.includes('aerocivil')) {
    return `
      <div class="space-y-1.5">
        <span class="font-bold text-cyan-300 block">🇨🇴 REGRAS NA COLÔMBIA (AEROCIVIL - RAC 100):</span>
        <p><b>1. Sistema SISANDRONES:</b> Registro obrigatório da aeronave e autorização prévia da Aerocivil.</p>
        <p><b>2. Certificado de Piloto:</b> Emitido por Centro de Instrução Aeronáutico certificado.</p>
        <p><b>3. Seguro:</b> Apólice de danos a terceiros exigida para todas as classes comerciais.</p>
        <p><b>4. Teto:</b> 123 metros (400 pés) AGL.</p>
      </div>
    `;
  }

  // 7. ARGENTINA / CHILE / PERU
  if (query.includes('argentina') || query.includes('chile') || query.includes('peru') || query.includes('perú')) {
    return `
      <div class="space-y-1.5">
        <span class="font-bold text-cyan-300 block">🌎 REGRAS NA AMÉRICA DO SUL (DGAC / ANAC):</span>
        <p><b>• Argentina (ANAC Res. 880):</b> Cadastro obrigatório no Casillero Aeronáutico Digital (CAD), seguro contra terceiros e teto de 120m.</p>
        <p><b>• Chile (DGAC DAN 151):</b> Credencial de operador RPA da DGAC, drone empadronado com placa identificadora e seguro aeronáutico.</p>
        <p><b>• Peru (DGAC NTC 001):</b> Registro da aeronave no MTC, licença de operador e teto de até 152m (500 pés) AGL fora de áreas restritas.</p>
      </div>
    `;
  }

  // 8. CLIMA ESPACIAL / ÍNDICE KP / TEMPESTADE SOLAR
  if (query.includes('kp') || query.includes('solar') || query.includes('tempestade') || query.includes('geomagnética') || query.includes('flyaway')) {
    return `
      <div class="space-y-1.5">
        <span class="font-bold text-amber-300 block">☀️ IMPACTO DO ÍNDICE KP & TEMPESTADES SOLARES:</span>
        <p><b>• O que é o KP (0 a 9)?</b> Escala da NOAA que mede perturbações geomagnéticas causadas por ejeções do Sol.</p>
        <p><b>• Por que afeta o drone?</b> O vento solar ioniza a atmosfera e desvia as ondas de rádio L1/L2 dos satélites GNSS, causando erros de cálculo posicional de vários metros e descalibrando a bússola magnética.</p>
        <p><b>• O perigo de Flyaway:</b> Quando a controladora de voo detecta conflito entre a bússola e o GPS em KP ≥ 5, ela pode entrar em falha de navegação e sair derivando descontroladamente.</p>
        <p><b>• Regra de Ouro:</b> KP 0 a 3 é voo seguro; KP 4 exige atenção; <b>KP ≥ 5 é estado NO-GO</b> (aborte missões autônomas ou voe apenas em modo manual com termo assinado).</p>
      </div>
    `;
  }

  // 9. PDOP & GEOMETRIA DE SATÉLITES RTK
  if (query.includes('pdop') || query.includes('satélite') || query.includes('rtk') || query.includes('precisão')) {
    return `
      <div class="space-y-1.5">
        <span class="font-bold text-cyan-300 block">🛰️ PDOP & QUALIDADE GEOMÉTRICA DE SATÉLITES:</span>
        <p><b>• Significado:</b> Positional Dilution of Precision (Diluição de Precisão Posicional em 3D).</p>
        <p><b>• PDOP Ideal (&lt; 2.0):</b> Satélites bem espalhados por todo o céu. Proporciona solução FIX no RTK com precisão centimétrica de 1 a 2 cm.</p>
        <p><b>• PDOP Elevado (&gt; 3.0):</b> Satélites concentrados no mesmo quadrante (ou bloqueados por prédios/árvores). A precisão cai drasticamente e o RTK pode degradar para FLOAT.</p>
      </div>
    `;
  }

  // 10. BÚSSOLA & ORIENTAÇÃO
  if (query.includes('bússola') || query.includes('bussola') || query.includes('orientação') || query.includes('heading') || query.includes('vento')) {
    return `
      <div class="space-y-1.5">
        <span class="font-bold text-emerald-300 block">🧭 BÚSSOLA GIROSCÓPICA & ORIENTAÇÃO TÁTICA:</span>
        <p><b>• Heading (Proa):</b> Indica o ângulo magnético (0° a 360°) para onde o nariz da aeronave está apontando em relação ao Norte magnético.</p>
        <p><b>• Vetor Home (RTH):</b> Direção calculada em tempo real para o ponto exato onde o drone decolou. Crucial em caso de perda de link de rádio.</p>
        <p><b>• Dica Aeronáutica:</b> Sempre decole e pouse com vento de proa (contra o vento), pois isso aumenta a sustentação nas hélices e economiza bateria!</p>
      </div>
    `;
  }

  // RESPOSTA PADRÃO AEROESPACIAL
  return `
    <div class="space-y-1.5">
      <span class="font-bold text-cyan-300 block">📡 RESUMO DE CONFORMIDADE AERONÁUTICA:</span>
      <p>Entendi sua consulta sobre operações de aeronaves não tripuladas. Nas Américas, todo voo comercial exige três pilares fundamentais:</p>
      <p>1. <b>Autorização de Espaço Aéreo:</b> Submissão de plano de voo no órgão militar/civil do país (ex: SARPAS no Brasil, LAANC nos EUA, Transport Canada).</p>
      <p>2. <b>Seguro Aeronáutico Obrigatório:</b> Apólice contra danos a terceiros (Seguro RETA no Brasil e apólices similares nos demais países).</p>
      <p>3. <b>Envoltória Meteorológica e Solar:</b> Ventos dentro do limite da aeronave e índice solar KP &lt; 5 para evitar perda de sinal GNSS.</p>
      <p class="text-slate-400 text-[10px] mt-1">Quer saber as regras específicas de algum país (Brasil, Canadá, EUA, Equador, etc.) ou sobre tempestades solares KP? Basta perguntar!</p>
    </div>
  `;
}

"""

    if target_js_end in html:
        html = html.replace(target_js_end, new_js_logic + target_js_end, 1)
        print("Inserted JavaScript logic for Compass, Modals and AeroAI successfully")
    else:
        print("Warning: target_js_end not matched")

    # Write out upgraded file
    with open(src_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Upgraded marketplace_app.html written successfully! New size:", len(html))

if __name__ == '__main__':
    main()

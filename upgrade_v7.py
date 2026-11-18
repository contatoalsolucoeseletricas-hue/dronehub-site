# -*- coding: utf-8 -*-
import os, sys, re, json

def main():
    path = r"C:\DRONE\marketplace_app.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    print("Original size:", len(html))

    # 1. Update Chips de Categoria
    old_chips = """        <!-- Carrossel de Categorias — Scroll Horizontal com Touch Nativo -->
        <div class="chips-scroll" id="categoryChips">
          <button class="category-chip active" onclick="selectCategory('TODAS', this)">⚡ Todas</button>
          <button class="category-chip" onclick="selectCategory('Topografia & LiDAR', this)">📐 Topo & LiDAR</button>
          <button class="category-chip" onclick="selectCategory('Inspeção Eólica & Solar', this)">⚡ Eólica & Solar</button>"""

    new_chips = """        <!-- Carrossel de Categorias — Scroll Horizontal com Touch Nativo -->
        <div class="chips-scroll" id="categoryChips">
          <button class="category-chip active" onclick="selectCategory('TODAS', this)">⚡ Todas</button>
          <button class="category-chip" onclick="selectCategory('Câmera 360° & Tour Virtual', this)">🔄 Câmera 360°</button>
          <button class="category-chip" onclick="selectCategory('Timelapse de Obras', this)">⏱️ Timelapse</button>
          <button class="category-chip" onclick="selectCategory('Topografia & LiDAR', this)">📐 Topo & LiDAR</button>
          <button class="category-chip" onclick="selectCategory('Inspeção Eólica & Solar', this)">⚡ Eólica & Solar</button>"""

    if old_chips in html:
        html = html.replace(old_chips, new_chips, 1)
        print("[OK] Updated Category Chips")
    else:
        print("[WARN] old_chips not found")

    # 2. Update Pilot Registration Form (tabCadastro)
    old_specs_form = """            <div class="grid grid-cols-2 gap-1.5 text-[11px] text-slate-300">
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Topografia & LiDAR" checked class="accent-cyan-500"> Topografia & LiDAR</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Inspeção Eólica & Solar" checked class="accent-cyan-500"> Eólica & Solar</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Termografia Industrial" class="accent-cyan-500"> Termografia</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Construção & BIM" class="accent-cyan-500"> Construção & BIM</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Transmissão ao Vivo" class="accent-cyan-500"> Transmissão Live</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Pulverização Agrícola" class="accent-cyan-500"> Agro & Pulverização</label>
            </div>
          </div>

          <div>
            <label class="text-[10px] text-slate-400 block mb-1">Diária Média Estimada (R$)</label>"""

    new_specs_form = """            <div class="grid grid-cols-2 gap-1.5 text-[11px] text-slate-300">
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Topografia & LiDAR" checked class="accent-cyan-500"> Topografia & LiDAR</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Câmera 360° & Tour Virtual" checked class="accent-cyan-500"> 🔄 Câmera 360° & Tour</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Timelapse de Obras" checked class="accent-cyan-500"> ⏱️ Timelapse Obras</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Inspeção Eólica & Solar" class="accent-cyan-500"> Eólica & Solar</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Termografia Industrial" class="accent-cyan-500"> Termografia</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Construção & BIM" class="accent-cyan-500"> Construção & BIM</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Transmissão ao Vivo" class="accent-cyan-500"> Transmissão Live</label>
              <label class="flex items-center gap-1.5"><input type="checkbox" name="pSpec" value="Pulverização Agrícola" class="accent-cyan-500"> Agro & Pulverização</label>
            </div>
          </div>

          <!-- Redes Sociais do Piloto (Instagram, Threads, LinkedIn, Facebook) -->
          <div class="space-y-2 pt-2 border-t border-slate-800/80">
            <span class="text-[10px] font-bold text-cyan-400 uppercase tracking-wider block">Redes Sociais & Portfólio</span>
            <div class="grid grid-cols-2 gap-2">
              <div>
                <label class="text-[10px] text-slate-400 block mb-0.5">📸 Instagram (@usuario)</label>
                <input type="text" id="pInstagram" placeholder="ex: seu.perfil" class="w-full bg-slate-900 border border-slate-800 rounded-xl p-2 text-slate-100 text-xs">
              </div>
              <div>
                <label class="text-[10px] text-slate-400 block mb-0.5">🧵 Threads (@usuario - Meta)</label>
                <input type="text" id="pThreads" placeholder="ex: seu.perfil" class="w-full bg-slate-900 border border-slate-800 rounded-xl p-2 text-slate-100 text-xs">
              </div>
              <div>
                <label class="text-[10px] text-slate-400 block mb-0.5">💼 LinkedIn (perfil)</label>
                <input type="text" id="pLinkedin" placeholder="ex: seu-nome-piloto" class="w-full bg-slate-900 border border-slate-800 rounded-xl p-2 text-slate-100 text-xs">
              </div>
              <div>
                <label class="text-[10px] text-slate-400 block mb-0.5">📘 Facebook (página/perfil)</label>
                <input type="text" id="pFacebook" placeholder="ex: suapagina" class="w-full bg-slate-900 border border-slate-800 rounded-xl p-2 text-slate-100 text-xs">
              </div>
            </div>
            <div>
              <label class="text-[10px] text-slate-400 block mb-0.5">🖼️ Link da Foto de Perfil / Fotos de Amostra (URL)</label>
              <input type="url" id="pFoto" placeholder="https://exemplo.com/sua-foto.jpg" class="w-full bg-slate-900 border border-slate-800 rounded-xl p-2 text-slate-100 text-xs">
            </div>
          </div>

          <div>
            <label class="text-[10px] text-slate-400 block mb-1">Diária Média Estimada (R$)</label>"""

    if old_specs_form in html:
        html = html.replace(old_specs_form, new_specs_form, 1)
        print("[OK] Updated tabCadastro form with 360, Timelapse and Social Media")
    else:
        print("[WARN] old_specs_form not found")

    # 3. Add Modal de Portfólio (Fotos 360°, Timelapse e Galerias)
    target_modal_anchor = "  <!-- ================= MODAL SEGURO RETA AERONÁUTICO OBRIGATÓRIO ================= -->"
    portfolio_modal_html = """  <!-- ================= MODAL GALERIA DE FOTOS, CÂMERA 360° & TIMELAPSE ================= -->
  <div id="portfolioModal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden flex items-end sm:items-center justify-center p-3 animate-fade-in">
    <div class="bg-slate-900 border border-cyan-500/50 rounded-2xl w-full max-w-lg p-4 space-y-3.5 shadow-2xl max-h-[90vh] overflow-y-auto">
      <!-- Cabeçalho do Modal -->
      <div class="flex items-center justify-between border-b border-slate-800 pb-2.5">
        <div class="flex items-center gap-2.5">
          <img id="portPilotImg" src="" class="w-10 h-10 rounded-xl object-cover border border-cyan-400/50">
          <div>
            <h3 class="text-xs font-bold text-white uppercase tracking-wider" id="portPilotName">Portfólio do Piloto</h3>
            <p class="text-[10px] text-cyan-400 font-mono" id="portPilotLocation">📍 Cidade - UF</p>
          </div>
        </div>
        <button onclick="closePortfolioModal()" class="text-slate-400 hover:text-white font-bold text-sm">✕</button>
      </div>

      <!-- Abas de Tipo de Trabalho -->
      <div class="flex gap-1.5 text-[11px] font-semibold">
        <button onclick="switchPortTab('360')" id="btnPortTab360" class="flex-1 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold transition active:scale-95 shadow-sm">
          🔄 Câmera 360°
        </button>
        <button onclick="switchPortTab('timelapse')" id="btnPortTabTimelapse" class="flex-1 py-1.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-400 font-bold transition active:scale-95">
          ⏱️ Timelapse Obras
        </button>
        <button onclick="switchPortTab('fotos')" id="btnPortTabFotos" class="flex-1 py-1.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-400 font-bold transition active:scale-95">
          📸 Fotos Aéreas 4K
        </button>
      </div>

      <!-- Conteúdo da Aba 360° (Simulador Panorâmico Interativo) -->
      <div id="portContent360" class="space-y-2.5">
        <div class="relative w-full aspect-video rounded-xl overflow-hidden border border-cyan-500/40 bg-slate-950 shadow-inner group">
          <img id="port360Image" src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1000&auto=format&fit=crop" 
               class="w-full h-full object-cover transition-transform duration-700 ease-out" style="transform: scale(1.15) translateX(0px);">
          
          <!-- Badge e Overlay 360° -->
          <div class="absolute top-2.5 left-2.5 bg-black/75 backdrop-blur-md px-2.5 py-1 rounded-lg border border-cyan-500/50 flex items-center gap-1.5 font-mono text-[10px] text-cyan-300 font-bold">
            <span class="animate-spin text-xs">🔄</span>
            <span>PANORAMA ESFÉRICO 360°</span>
          </div>

          <!-- Controles de Giro Panorâmico -->
          <div class="absolute bottom-2.5 inset-x-2.5 flex items-center justify-between bg-black/80 backdrop-blur-md px-3 py-1.5 rounded-xl border border-white/10 text-xs">
            <button onclick="pan360(-30)" class="px-2 py-1 rounded bg-slate-800 hover:bg-cyan-500 hover:text-slate-950 text-white font-bold transition active:scale-95">◀ Girar Esquerda</button>
            <span class="text-[10px] text-slate-400 font-mono">Arraste ou Gire</span>
            <button onclick="pan360(30)" class="px-2 py-1 rounded bg-slate-800 hover:bg-cyan-500 hover:text-slate-950 text-white font-bold transition active:scale-95">Girar Direita ▶</button>
          </div>
        </div>
        <p class="text-[11px] text-slate-300 leading-relaxed">
          <b>Tour Virtual 360° Imobiliário & Inspeção:</b> Imagens aéreas esféricas em 8K com giroscópio integrado para incorporadoras, construtoras e mapeamento de patrimônio.
        </p>
      </div>

      <!-- Conteúdo da Aba Timelapse (Evolução Temporal de Obras) -->
      <div id="portContentTimelapse" class="space-y-2.5 hidden">
        <div class="relative w-full aspect-video rounded-xl overflow-hidden border border-amber-500/40 bg-slate-950 shadow-inner">
          <img id="portTimelapseImg" src="https://images.unsplash.com/photo-1541888946425-d0fbb186156f?w=1000&auto=format&fit=crop" 
               class="w-full h-full object-cover transition-opacity duration-300">

          <div class="absolute top-2.5 left-2.5 bg-black/75 backdrop-blur-md px-2.5 py-1 rounded-lg border border-amber-500/50 flex items-center gap-1.5 font-mono text-[10px] text-amber-300 font-bold">
            <span>⏱️ TIMELAPSE DE CONSTRUÇÃO</span>
          </div>

          <!-- Linha do Tempo / Seletor de Fases da Obra -->
          <div class="absolute bottom-2.5 inset-x-2.5 bg-black/85 backdrop-blur-md px-2.5 py-1.5 rounded-xl border border-white/10 flex items-center justify-between text-[10px] font-mono">
            <button onclick="setTimelapsePhase(1)" id="btnTlPhase1" class="px-2 py-0.5 rounded bg-amber-500 text-slate-950 font-bold">Fase 1: Terraplenagem</button>
            <button onclick="setTimelapsePhase(2)" id="btnTlPhase2" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-bold hover:text-white">Fase 2: Estrutura</button>
            <button onclick="setTimelapsePhase(3)" id="btnTlPhase3" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-bold hover:text-white">Fase 3: Acabamento</button>
          </div>
        </div>
        <p class="text-[11px] text-slate-300 leading-relaxed">
          <b>Acompanhamento Periódico de Obras (Timelapse):</b> Voos programados com waypoints milimétricos repetíveis para registrar a evolução cronológica completa da construção.
        </p>
      </div>

      <!-- Conteúdo da Aba Fotos Aéreas -->
      <div id="portContentFotos" class="space-y-2.5 hidden">
        <div class="grid grid-cols-2 gap-2">
          <img src="https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=500&auto=format&fit=crop" class="w-full h-24 object-cover rounded-xl border border-slate-800">
          <img src="https://images.unsplash.com/photo-1473968512647-3e447244af8f?w=500&auto=format&fit=crop" class="w-full h-24 object-cover rounded-xl border border-slate-800">
          <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=500&auto=format&fit=crop" class="w-full h-24 object-cover rounded-xl border border-slate-800">
          <img src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=500&auto=format&fit=crop" class="w-full h-24 object-cover rounded-xl border border-slate-800">
        </div>
        <p class="text-[11px] text-slate-300 leading-relaxed">
          Fotografias ortorretificadas, inspeções termográficas e imagens publicitárias em alta resolução captadas com sensores full-frame e lentes prime.
        </p>
      </div>

      <!-- Redes Sociais do Piloto em Destaque -->
      <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
        <span class="text-[10px] text-slate-400 font-bold uppercase tracking-wider block">Redes Sociais & Contato Oficial do Piloto:</span>
        <div class="flex flex-wrap gap-2 text-xs" id="portSocialLinks">
          <!-- Inserido dinamicamente via JS -->
        </div>
      </div>

      <!-- Botão de Ação -->
      <div class="flex gap-2">
        <button onclick="closePortfolioModal()" class="flex-1 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition">
          Fechar
        </button>
        <a id="portWhatsappBtn" href="#" target="_blank" class="flex-1 py-2 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-extrabold text-center transition shadow-lg shadow-emerald-950/40">
          Chamar no WhatsApp
        </a>
      </div>
    </div>
  </div>\n\n""" + target_modal_anchor

    if target_modal_anchor in html:
        html = html.replace(target_modal_anchor, portfolio_modal_html, 1)
        print("[OK] Inserted Portfolio & 360 Modal")
    else:
        print("[WARN] target_modal_anchor not found")

    # 4. Now let's update DEFAULT_PILOTS with social links, 360, timelapse specialties
    # Let's inspect where DEFAULT_PILOTS starts and ends
    old_pilots_decl = "let pilots = JSON.parse(localStorage.getItem('dh_pilots_v5')) || DEFAULT_PILOTS;"
    new_pilots_decl = "let pilots = JSON.parse(localStorage.getItem('dh_pilots_v7')) || DEFAULT_PILOTS;"
    if old_pilots_decl in html:
        html = html.replace(old_pilots_decl, new_pilots_decl, 1)
        print("[OK] Updated pilots storage key to dh_pilots_v7")

    # Replace renderPilots function to add social icons and portfolio button
    old_render_start = "function renderPilots(data) {"
    
    # Let's see how renderPilots maps pilots
    old_card_template = """      <!-- Tags de Equipamento & Especialidade -->
      <div class="flex flex-wrap gap-1">
        ${p.especialidades.map(e => `
          <span class="text-[10px] px-2 py-0.5 rounded-md bg-slate-900 border border-slate-800 text-slate-300">${e}</span>
        `).join('')}
      </div>

      <div class="text-[11px] text-slate-400 border-t border-slate-800/80 pt-2 flex items-center justify-between gap-2">
        <span class="truncate text-[10px] text-slate-500">🛸 ${p.drones[0]}</span>
        <div class="flex items-center gap-1.5">
          <button onclick="openEscrowForPilot('${p.nome}', ${p.preco})" class="bg-cyan-500/20 hover:bg-cyan-500/30 border border-cyan-400/40 text-cyan-300 font-semibold text-[11px] px-2.5 py-1 rounded-xl transition active:scale-95">
            🛡️ Contratar Seguro
          </button>
          <a href="https://wa.me/55${p.zap}?text=Ol%C3%A1%20${encodeURIComponent(p.nome)},%20vi%20seu%20perfil%20no%20DroneHub%20e%20gostaria%20de%20um%20or%C3%A7amento!" 
             target="_blank" 
             class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs px-2.5 py-1 rounded-xl transition active:scale-95">
            WhatsApp
          </a>
        </div>
      </div>"""

    new_card_template = """      <!-- Tags de Equipamento & Especialidade -->
      <div class="flex flex-wrap gap-1">
        ${p.especialidades.map(e => `
          <span class="text-[10px] px-2 py-0.5 rounded-md ${e.includes('360') ? 'bg-cyan-950 border-cyan-700/60 text-cyan-300 font-bold' : e.includes('Timelapse') ? 'bg-amber-950 border-amber-700/60 text-amber-300 font-bold' : 'bg-slate-900 border-slate-800 text-slate-300'}">${e}</span>
        `).join('')}
      </div>

      <!-- Linha de Redes Sociais do Piloto (Instagram, Threads, LinkedIn, Facebook) -->
      <div class="flex items-center gap-1.5 pt-1 border-t border-slate-800/80 text-[10px] flex-wrap">
        <span class="text-slate-500 font-semibold text-[9px] uppercase font-mono">Redes:</span>
        ${p.social && p.social.instagram ? `
          <a href="https://instagram.com/${p.social.instagram}" target="_blank" class="flex items-center gap-1 px-2 py-0.5 rounded-lg bg-pink-950/60 border border-pink-700/60 text-pink-300 font-bold hover:bg-pink-900 transition" title="Instagram @${p.social.instagram}">
            <span>📸 Insta</span>
          </a>
        ` : ''}
        ${p.social && p.social.threads ? `
          <a href="https://threads.net/@${p.social.threads}" target="_blank" class="flex items-center gap-1 px-2 py-0.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 font-bold hover:border-cyan-500 transition" title="Threads (App da Meta/Instagram) @${p.social.threads}">
            <span>🧵 Threads</span>
          </a>
        ` : ''}
        ${p.social && p.social.linkedin ? `
          <a href="https://linkedin.com/in/${p.social.linkedin}" target="_blank" class="flex items-center gap-1 px-2 py-0.5 rounded-lg bg-blue-950/60 border border-blue-700/60 text-blue-300 font-bold hover:bg-blue-900 transition" title="LinkedIn">
            <span>💼 LinkedIn</span>
          </a>
        ` : ''}
        ${p.social && p.social.facebook ? `
          <a href="https://facebook.com/${p.social.facebook}" target="_blank" class="flex items-center gap-1 px-2 py-0.5 rounded-lg bg-indigo-950/60 border border-indigo-700/60 text-indigo-300 font-bold hover:bg-indigo-900 transition" title="Facebook">
            <span>📘 Face</span>
          </a>
        ` : ''}
        <button onclick="openPortfolioModal('${p.id}')" class="ml-auto text-[10px] text-cyan-400 hover:text-cyan-300 font-bold flex items-center gap-1 underline active:scale-95 transition">
          <span>🖼️ Fotos 360° & Portfólio</span>
        </button>
      </div>

      <div class="text-[11px] text-slate-400 border-t border-slate-800/80 pt-2 flex items-center justify-between gap-2">
        <span class="truncate text-[10px] text-slate-500">🛸 ${p.drones[0]}</span>
        <div class="flex items-center gap-1.5">
          <button onclick="openEscrowForPilot('${p.nome}', ${p.preco})" class="bg-cyan-500/20 hover:bg-cyan-500/30 border border-cyan-400/40 text-cyan-300 font-semibold text-[11px] px-2.5 py-1 rounded-xl transition active:scale-95">
            🛡️ Contratar Seguro
          </button>
          <a href="https://wa.me/55${p.zap}?text=Ol%C3%A1%20${encodeURIComponent(p.nome)},%20vi%20seu%20perfil%20no%20DroneHub%20e%20gostaria%20de%20um%20or%C3%A7amento%20para%20C%C3%A2mera%20360%C2%B0%20/%20Timelapse!" 
             target="_blank" 
             class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs px-2.5 py-1 rounded-xl transition active:scale-95">
            WhatsApp
          </a>
        </div>
      </div>"""

    if old_card_template in html:
        html = html.replace(old_card_template, new_card_template, 1)
        print("[OK] Updated Pilot Card template with social links and 360 portfolio button")
    else:
        print("[WARN] old_card_template not found")

    # 5. Add JavaScript functions for Portfolio, Pan 360°, Timelapse Phases, and updated handlePilotSubmit
    target_js_anchor = "function handlePilotSubmit(e) {"
    portfolio_js = """// ——————————————————————————————————————————————————————————
// PORTFÓLIO DE FOTOS, CÂMERA 360° & TIMELAPSE
// ——————————————————————————————————————————————————————————
let pan360Offset = 0;
let currentViewingPilot = null;

function openPortfolioModal(pilotId) {
  const p = pilots.find(x => x.id === pilotId) || pilots[0];
  currentViewingPilot = p;
  
  document.getElementById('portPilotName').innerText = p.nome;
  document.getElementById('portPilotLocation').innerText = `📍 ${p.cidade}, ${p.uf} • ${p.drones[0]}`;
  document.getElementById('portPilotImg').src = p.foto;
  document.getElementById('portWhatsappBtn').href = `https://wa.me/55${p.zap}?text=Ol%C3%A1%20${encodeURIComponent(p.nome)},%20vi%20suas%20fotos%20360%C2%B0%20e%20timelapse%20no%20DroneHub!`;

  // Renderiza Redes Sociais no Modal
  const sContainer = document.getElementById('portSocialLinks');
  sContainer.innerHTML = '';
  if (p.social) {
    if (p.social.instagram) {
      sContainer.innerHTML += `
        <a href="https://instagram.com/${p.social.instagram}" target="_blank" class="px-2.5 py-1 rounded-lg bg-pink-950/70 border border-pink-700/60 text-pink-300 font-bold flex items-center gap-1.5">
          <span>📸 Instagram: @${p.social.instagram}</span>
        </a>
      `;
    }
    if (p.social.threads) {
      sContainer.innerHTML += `
        <a href="https://threads.net/@${p.social.threads}" target="_blank" class="px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 font-bold flex items-center gap-1.5">
          <span>🧵 Threads (Meta/Insta): @${p.social.threads}</span>
        </a>
      `;
    }
    if (p.social.linkedin) {
      sContainer.innerHTML += `
        <a href="https://linkedin.com/in/${p.social.linkedin}" target="_blank" class="px-2.5 py-1 rounded-lg bg-blue-950/70 border border-blue-700/60 text-blue-300 font-bold flex items-center gap-1.5">
          <span>💼 LinkedIn: ${p.social.linkedin}</span>
        </a>
      `;
    }
    if (p.social.facebook) {
      sContainer.innerHTML += `
        <a href="https://facebook.com/${p.social.facebook}" target="_blank" class="px-2.5 py-1 rounded-lg bg-indigo-950/70 border border-indigo-700/60 text-indigo-300 font-bold flex items-center gap-1.5">
          <span>📘 Facebook: /${p.social.facebook}</span>
        </a>
      `;
    }
  }

  pan360Offset = 0;
  pan360(0);
  switchPortTab('360');
  document.getElementById('portfolioModal').classList.remove('hidden');
}

function closePortfolioModal() {
  document.getElementById('portfolioModal').classList.add('hidden');
}

function switchPortTab(tab) {
  const btn360 = document.getElementById('btnPortTab360');
  const btnTl = document.getElementById('btnPortTabTimelapse');
  const btnFotos = document.getElementById('btnPortTabFotos');
  const c360 = document.getElementById('portContent360');
  const cTl = document.getElementById('portContentTimelapse');
  const cFotos = document.getElementById('portContentFotos');

  btn360.className = 'flex-1 py-1.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-400 font-bold transition active:scale-95';
  btnTl.className = 'flex-1 py-1.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-400 font-bold transition active:scale-95';
  btnFotos.className = 'flex-1 py-1.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-400 font-bold transition active:scale-95';

  c360.classList.add('hidden');
  cTl.classList.add('hidden');
  cFotos.classList.add('hidden');

  if (tab === '360') {
    btn360.className = 'flex-1 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold transition active:scale-95 shadow-sm';
    c360.classList.remove('hidden');
  } else if (tab === 'timelapse') {
    btnTl.className = 'flex-1 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold transition active:scale-95 shadow-sm';
    cTl.classList.remove('hidden');
  } else {
    btnFotos.className = 'flex-1 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold transition active:scale-95 shadow-sm';
    cFotos.classList.remove('hidden');
  }
}

function pan360(step) {
  pan360Offset = (pan360Offset + step);
  if (pan360Offset > 120) pan360Offset = 120;
  if (pan360Offset < -120) pan360Offset = -120;
  const img = document.getElementById('port360Image');
  if (img) img.style.transform = `scale(1.15) translateX(${pan360Offset}px)`;
}

function setTimelapsePhase(phase) {
  const img = document.getElementById('portTimelapseImg');
  const b1 = document.getElementById('btnTlPhase1');
  const b2 = document.getElementById('btnTlPhase2');
  const b3 = document.getElementById('btnTlPhase3');

  b1.className = 'px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-bold hover:text-white';
  b2.className = 'px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-bold hover:text-white';
  b3.className = 'px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-bold hover:text-white';

  if (phase === 1) {
    b1.className = 'px-2 py-0.5 rounded bg-amber-500 text-slate-950 font-bold';
    img.src = 'https://images.unsplash.com/photo-1541888946425-d0fbb186156f?w=1000&auto=format&fit=crop';
  } else if (phase === 2) {
    b2.className = 'px-2 py-0.5 rounded bg-amber-500 text-slate-950 font-bold';
    img.src = 'https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1000&auto=format&fit=crop';
  } else {
    b3.className = 'px-2 py-0.5 rounded bg-amber-500 text-slate-950 font-bold';
    img.src = 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1000&auto=format&fit=crop';
  }
}

"""
    if target_js_anchor in html:
        html = html.replace(target_js_anchor, portfolio_js + target_js_anchor, 1)
        print("[OK] Inserted Portfolio JavaScript logic")
    else:
        print("[WARN] target_js_anchor not found")

    # Update handlePilotSubmit to capture social links and photos
    old_handle_pilot = """function handlePilotSubmit(e) {
  e.preventDefault();
  const specs = Array.from(document.querySelectorAll('input[name="pSpec"]:checked')).map(i => i.value);
  
  const novo = {
    id: 'p_' + Date.now(),
    nome: document.getElementById('pNome').value,
    zap: document.getElementById('pZap').value,
    uf: document.getElementById('pUF').value,
    cidade: document.getElementById('pCidade').value,
    anac: document.getElementById('pAnac').value || 'PP-' + Math.floor(100000000 + Math.random() * 900000000),
    drones: document.getElementById('pDrones').value.split(',').map(s => s.trim()),
    especialidades: specs.length ? specs : ['Topografia & LiDAR'],
    preco: parseFloat(document.getElementById('pPreco').value) || 1800,
    avaliacao: 5.0,
    avaliacoesTotal: 1,
    lat: -23.5505,
    lng: -46.6333,
    foto: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=faces'
  };

  pilots.unshift(novo);
  localStorage.setItem('dh_pilots_v3', JSON.stringify(pilots));
  renderPilots(pilots);
  
  alert('🎉 Parabéns! Seu perfil de piloto foi publicado com sucesso no DroneHub Brasil!');
  switchNavTab('tabExplorar', document.getElementById('btnTabExplorar'));
}"""

    new_handle_pilot = """function handlePilotSubmit(e) {
  e.preventDefault();
  const specs = Array.from(document.querySelectorAll('input[name="pSpec"]:checked')).map(i => i.value);
  const pFotoVal = document.getElementById('pFoto').value.trim();
  
  const novo = {
    id: 'p_' + Date.now(),
    nome: document.getElementById('pNome').value,
    zap: document.getElementById('pZap').value,
    uf: document.getElementById('pUF').value,
    cidade: document.getElementById('pCidade').value,
    anac: document.getElementById('pAnac').value || 'PP-' + Math.floor(100000000 + Math.random() * 900000000),
    drones: document.getElementById('pDrones').value.split(',').map(s => s.trim()),
    especialidades: specs.length ? specs : ['Câmera 360° & Tour Virtual', 'Topografia & LiDAR'],
    preco: parseFloat(document.getElementById('pPreco').value) || 1800,
    avaliacao: 5.0,
    avaliacoesTotal: 1,
    lat: -23.5505,
    lng: -46.6333,
    foto: pFotoVal || 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=faces',
    social: {
      instagram: document.getElementById('pInstagram').value.replace('@','').trim(),
      threads: document.getElementById('pThreads').value.replace('@','').trim(),
      linkedin: document.getElementById('pLinkedin').value.trim(),
      facebook: document.getElementById('pFacebook').value.trim()
    }
  };

  pilots.unshift(novo);
  localStorage.setItem('dh_pilots_v7', JSON.stringify(pilots));
  renderPilots(pilots);
  
  alert('🎉 Parabéns! Seu perfil com redes sociais e fotos 360°/timelapse foi publicado no DroneHub!');
  switchNavTab('tabExplorar', document.getElementById('btnTabExplorar'));
}"""

    if old_handle_pilot in html:
        html = html.replace(old_handle_pilot, new_handle_pilot, 1)
        print("[OK] Updated handlePilotSubmit with social media handling")
    else:
        print("[WARN] old_handle_pilot not found")

    # Update backdrop click listener to close portfolioModal
    old_backdrop = "  if (e.target === aeroAIModal) closeAeroAIModal();"
    new_backdrop = "  if (e.target === aeroAIModal) closeAeroAIModal();\n  const portfolioModal = document.getElementById('portfolioModal');\n  if (e.target === portfolioModal) closePortfolioModal();"
    if old_backdrop in html:
        html = html.replace(old_backdrop, new_backdrop, 1)
        print("[OK] Updated backdrop listener with portfolioModal")

    # Now let's enrich DEFAULT_PILOTS with social media and 360/timelapse specialties
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Base upgrade written. Now updating pilots data...")

if __name__ == "__main__":
    main()

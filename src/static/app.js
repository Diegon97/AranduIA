// AranduIA — Frontend Client Logic & Offline-First State
document.addEventListener('DOMContentLoaded', () => {
  // Estado local
  let modoTEA = false;
  let currentFontSize = 16;
  let chatHistorial = [];
  let ultimoTextoTutor = "";

  // Elementos DOM
  const btnTea = document.getElementById('toggle-tea');
  const btnDyslexia = document.getElementById('toggle-dyslexia');
  const btnFontInc = document.getElementById('font-increase');
  const btnFontDec = document.getElementById('font-decrease');
  const connStatus = document.getElementById('conn-status');

  const tabButtons = document.querySelectorAll('.tab-btn');
  const tabPanes = document.querySelectorAll('.tab-pane');

  const chatBox = document.getElementById('chat-box');
  const studentInput = document.getElementById('student-input');
  const btnSendStudent = document.getElementById('btn-send-student');
  const btnSpeech = document.getElementById('btn-speech');

  const btnGenPlan = document.getElementById('btn-gen-plan');
  const btnGenRubrica = document.getElementById('btn-gen-rubrica');
  const planOutput = document.getElementById('plan-output');
  const planDetails = document.getElementById('plan-details');

  const glossaryContainer = document.getElementById('glossary-container');

  // 1. Registro de Service Worker para Offline-First
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').catch(err => {
      console.log('Service Worker no registrado:', err);
    });
  }

  // 2. Monitoreo de Conectividad
  function updateOnlineStatus() {
    if (navigator.onLine) {
      connStatus.textContent = '🟢 En Línea';
      connStatus.style.background = '#dcfce7';
      connStatus.style.color = '#166534';
    } else {
      connStatus.textContent = '🟡 Modo Offline';
      connStatus.style.background = '#fef3c7';
      connStatus.style.color = '#92400e';
    }
  }
  window.addEventListener('online', updateOnlineStatus);
  window.addEventListener('offline', updateOnlineStatus);
  updateOnlineStatus();

  // 3. Accesibilidad: Modo TEA y Dislexia
  btnTea.addEventListener('click', () => {
    modoTEA = !modoTEA;
    document.body.classList.toggle('tea-calm', modoTEA);
    btnTea.classList.toggle('active', modoTEA);
    if (modoTEA) {
      alert('Modo TEA activado: interfaz con calma visual, pictogramas y lenguaje directo sin metáforas ambiguas.');
    }
  });

  btnDyslexia.addEventListener('click', () => {
    document.body.classList.toggle('dyslexia-font');
    btnDyslexia.classList.toggle('active');
  });

  btnFontInc.addEventListener('click', () => {
    if (currentFontSize < 24) {
      currentFontSize += 2;
      document.documentElement.style.setProperty('--font-size', `${currentFontSize}px`);
    }
  });

  btnFontDec.addEventListener('click', () => {
    if (currentFontSize > 14) {
      currentFontSize -= 2;
      document.documentElement.style.setProperty('--font-size', `${currentFontSize}px`);
    }
  });

  // 4. Navegación por pestañas
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      tabButtons.forEach(b => b.classList.remove('active'));
      tabPanes.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const target = document.getElementById(`pane-${btn.dataset.tab}`);
      if (target) target.classList.add('active');
    });
  });

  // 5. Módulo Estudiante: Chat Socrático
  async function enviarPreguntaEstudiante() {
    const texto = studentInput.value.trim();
    if (!texto) return;

    // Agregar mensaje del estudiante a la UI
    agregarMensajeUI('student', texto);
    studentInput.value = '';

    // Guardar en historial
    chatHistorial.push({ rol: 'usuario', texto });

    // Indicador de carga
    const loaderId = 'loading-' + Date.now();
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'chat-msg tutor';
    loadingDiv.id = loaderId;
    loadingDiv.innerHTML = '<em>AranduIA está pensando una pista socrática...</em>';
    chatBox.appendChild(loadingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
      const res = await fetch('/api/tutor/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          mensaje: texto,
          modo_tea: modoTEA,
          modo_pictogramas: modoTEA,
          historial: chatHistorial
        })
      });

      const loadingElem = document.getElementById(loaderId);
      if (loadingElem) loadingElem.remove();

      if (!res.ok) throw new Error('Error al conectar con el servidor.');
      const data = await res.json();

      let respuestaHTML = `<strong>AranduIA:</strong> ${data.respuesta}`;

      if (data.aliento_jopara) {
        respuestaHTML += `<br><span class="jopara-badge">🇵🇾 ${data.aliento_jopara}</span>`;
      }

      if (data.pictogramas && data.pictogramas.length > 0) {
        const pictoHTML = data.pictogramas.map(p => `<span>${p.emoji} ${p.etiqueta}</span>`).join(' · ');
        respuestaHTML += `<div style="margin-top:0.4rem; font-size:0.85rem; color:var(--text-muted);">${pictoHTML}</div>`;
      }

      agregarMensajeUI('tutor', respuestaHTML);
      ultimoTextoTutor = data.respuesta;
      chatHistorial.push({ rol: 'asistente', texto: data.respuesta });

    } catch (err) {
      const loadingElem = document.getElementById(loaderId);
      if (loadingElem) loadingElem.remove();

      // Fallback offline en navegador si la red falló
      const fallbackMsg = "Paso 1: ¿Qué pensás que te pide resolver este ejercicio? Descompongámoslo en partes más pequeñas.";
      agregarMensajeUI('tutor', `<strong>AranduIA (Offline):</strong> ${fallbackMsg}`);
      ultimoTextoTutor = fallbackMsg;
    }
  }

  function agregarMensajeUI(remitente, htmlContent) {
    const msg = document.createElement('div');
    msg.className = `chat-msg ${remitente}`;
    msg.innerHTML = htmlContent;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  btnSendStudent.addEventListener('click', enviarPreguntaEstudiante);
  studentInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') enviarPreguntaEstudiante();
  });

  // Lectura por voz accesible
  btnSpeech.addEventListener('click', () => {
    if ('speechSynthesis' in window && ultimoTextoTutor) {
      const utter = new SpeechSynthesisUtterance(ultimoTextoTutor);
      utter.lang = 'es-ES';
      window.speechSynthesis.speak(utter);
    } else {
      alert('Síntesis de voz no disponible o no hay mensajes nuevos.');
    }
  });

  // Helper para pictogramas rápidos
  window.insertPrompt = function(texto) {
    studentInput.value = texto;
    studentInput.focus();
  };

  // 6. Módulo Docente: Planificador MEC
  btnGenPlan.addEventListener('click', async () => {
    const tema = document.getElementById('doc-tema').value.trim();
    const materia = document.getElementById('doc-materia').value;
    const grado = document.getElementById('doc-grado').value;
    const tea = document.getElementById('doc-tea').checked;

    if (!tema) {
      alert('Por favor, ingresá el tema de la lección.');
      return;
    }

    btnGenPlan.disabled = true;
    btnGenPlan.textContent = 'Generando Plan MEC...';

    try {
      const res = await fetch('/api/docente/planificar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          tema,
          materia,
          grado_o_curso: grado,
          incluir_adaptacion_tea: tea
        })
      });

      if (!res.ok) throw new Error('Error al generar plan.');
      const data = await res.json();

      let html = `
        <div class="plan-section">
          <h4>🎯 Capacidad Oficial MEC:</h4>
          <p>${data.capacidad_mec}</p>
        </div>
        <div class="plan-section">
          <h4>▶️ Momento de Inicio (15 min):</h4>
          <pre style="white-space:pre-wrap; font-family:inherit;">${data.inicio}</pre>
        </div>
        <div class="plan-section">
          <h4>⚙️ Momento de Desarrollo (50 min):</h4>
          <pre style="white-space:pre-wrap; font-family:inherit;">${data.desarrollo}</pre>
        </div>
        <div class="plan-section">
          <h4>🏁 Momento de Cierre (15 min):</h4>
          <pre style="white-space:pre-wrap; font-family:inherit;">${data.cierre}</pre>
        </div>
        <div class="plan-section">
          <h4>📦 Recursos Didácticos:</h4>
          <ul>${data.recursos.map(r => `<li>${r}</li>`).join('')}</ul>
        </div>
        <div class="plan-section">
          <h4>📊 Evaluación e Indicadores:</h4>
          <ul>${data.evaluacion.indicadores.map(i => `<li>${i}</li>`).join('')}</ul>
        </div>
      `;

      if (data.adaptacion_tea) {
        html += `
          <div class="plan-section" style="background:#f0fdfa; padding:1rem; border-left:4px solid var(--accent-tea);">
            <h4>🧩 Ajustes Curriculares Individualizados (TEA / Ley 5136):</h4>
            <p><strong>Apoyos visuales:</strong> ${data.adaptacion_tea.apoyos_visuales}</p>
            <p><strong>Instrucciones:</strong> ${data.adaptacion_tea.instrucciones}</p>
            <p><strong>Pausas sensoriales:</strong> ${data.adaptacion_tea.pausas_sensoriales}</p>
          </div>
        `;
      }

      planDetails.innerHTML = html;
      document.getElementById('plan-title').textContent = `Plan de Lección: ${data.tema} (${data.grado})`;
      planOutput.style.display = 'block';

    } catch (err) {
      alert('Error al generar el plan de clase. Verificá que el servidor esté activo.');
    } finally {
      btnGenPlan.disabled = false;
      btnGenPlan.textContent = '📄 Generar Plan de Lección MEC';
    }
  });

  // Generar Rúbrica
  btnGenRubrica.addEventListener('click', async () => {
    const tema = document.getElementById('doc-tema').value.trim();
    const materia = document.getElementById('doc-materia').value;
    const grado = document.getElementById('doc-grado').value;

    if (!tema) {
      alert('Por favor, ingresá el tema para la rúbrica.');
      return;
    }

    try {
      const res = await fetch('/api/docente/rubrica', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tema, materia, grado })
      });
      const data = await res.json();

      let tableHTML = `
        <h4>📊 Rúbrica Analítica de Desempeño: ${data.tema}</h4>
        <table style="width:100%; border-collapse:collapse; margin-top:1rem;" border="1">
          <thead>
            <tr style="background:#f1f5f9;">
              <th style="padding:8px;">Criterio</th>
              <th style="padding:8px;">Logrado (L)</th>
              <th style="padding:8px;">En Proceso (EP)</th>
              <th style="padding:8px;">No Logrado (NL)</th>
            </tr>
          </thead>
          <tbody>
            ${data.indicadores.map(ind => `
              <tr>
                <td style="padding:8px; font-weight:bold;">${ind.criterio}</td>
                <td style="padding:8px; background:#f0fdf4;">${ind.logrado}</td>
                <td style="padding:8px; background:#fffbeb;">${ind.en_proceso}</td>
                <td style="padding:8px; background:#fef2f2;">${ind.no_logrado}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      `;

      planDetails.innerHTML = tableHTML;
      document.getElementById('plan-title').textContent = `Rúbrica: ${data.tema}`;
      planOutput.style.display = 'block';
    } catch (err) {
      alert('Error al generar la rúbrica.');
    }
  });

  // 7. Cargar Glosario Jopara
  async function cargarGlosario() {
    try {
      const res = await fetch('/api/tutor/glosario');
      if (res.ok) {
        const data = await res.json();
        let cards = '';
        for (const [termino, info] of Object.entries(data.glosario)) {
          cards += `
            <div class="glossary-card">
              <h4>${termino.toUpperCase()}</h4>
              <p class="guarani-term">🇵🇾 ${info.guarani}</p>
              <p style="font-size:0.85rem; color:var(--text-muted);">${info.significado}</p>
            </div>
          `;
        }
        glossaryContainer.innerHTML = cards;
      }
    } catch (e) {
      console.log('Error cargando glosario');
    }
  }
  cargarGlosario();
});

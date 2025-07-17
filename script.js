// Datos de síntomas
        const symptoms = [
            { key: "Fiebre", label: "Fiebre", icon: "🌡️" },
            { key: "Tos", label: "Tos", icon: "😷" },
            { key: "Dolor_de_garganta", label: "Dolor de garganta", icon: "🗣️" },
            { key: "Dificultad_respiratoria", label: "Dificultad respiratoria", icon: "🫁" },
            { key: "Dolor_en_el_pecho", label: "Dolor en el pecho", icon: "💔" },
            { key: "Fatiga", label: "Fatiga", icon: "😴" },
            { key: "Sudores_nocturnos", label: "Sudores nocturnos", icon: "💦" },
            { key: "Perdida_de_peso", label: "Pérdida de peso", icon: "⚖️" },
            { key: "Hemoptisis", label: "Hemoptisis (sangre en esputo)", icon: "🩸" },
        ];

        // Datos de enfermedades
        const diseases = [
            { key: "COVID_19", label: "COVID-19", color: "bg-red-500" },
            { key: "Bronquitis", label: "Bronquitis", color: "bg-orange-500" },
            { key: "Faringitis", label: "Faringitis", color: "bg-yellow-500" },
            { key: "Neumonia", label: "Neumonía", color: "bg-blue-500" },
            { key: "Tuberculosis", label: "Tuberculosis", color: "bg-purple-500" },
        ];

        // Estado de la aplicación
        let evidence = {};
        let loading = false;

        // Elementos del DOM
        const symptomsList = document.getElementById('symptomsList');
        const symptomsCount = document.getElementById('symptomsCount');
        const diagnoseBtn = document.getElementById('diagnoseBtn');
        const resultsContainer = document.getElementById('resultsContainer');
        const emptyState = document.getElementById('emptyState');

        // Inicializar la aplicación
        function init() {
            renderSymptoms();
            updateSymptomsCount();
        }

        // Renderizar lista de síntomas
        function renderSymptoms() {
            symptomsList.innerHTML = '';
            
            symptoms.forEach(symptom => {
                const symptomItem = document.createElement('div');
                symptomItem.className = 'symptom-item';
                symptomItem.onclick = () => toggleSymptom(symptom.key);
                
                symptomItem.innerHTML = `
                    <div class="checkbox" id="checkbox-${symptom.key}"></div>
                    <label class="symptom-label">
                        <span class="symptom-icon">${symptom.icon}</span>
                        <span>${symptom.label}</span>
                    </label>
                `;
                
                symptomsList.appendChild(symptomItem);
            });
        }

        // Alternar síntoma
        function toggleSymptom(symptomKey) {
            const checkbox = document.getElementById(`checkbox-${symptomKey}`);
            const symptomItem = checkbox.closest('.symptom-item');
            const isChecked = evidence[symptomKey] === 1;
            
            if (isChecked) {
                evidence[symptomKey] = 0;
                checkbox.classList.remove('checked');
                symptomItem.classList.remove('selected');
            } else {
                evidence[symptomKey] = 1;
                checkbox.classList.add('checked');
                symptomItem.classList.add('selected');
            }
            
            updateSymptomsCount();
        }

        // Actualizar contador de síntomas
        function updateSymptomsCount() {
            const count = Object.values(evidence).filter(v => v === 1).length;
            symptomsCount.textContent = count;
            diagnoseBtn.disabled = count === 0 || loading;
        }

        // Realizar diagnóstico
        async function performDiagnosis() {
            if (loading) return;
            
            loading = true;
            updateSymptomsCount();
            
            // Mostrar estado de carga
            showLoading();
            
            // Preparar evidencia completa
            const completeEvidence = {};
            symptoms.forEach(symptom => {
                completeEvidence[symptom.key] = evidence[symptom.key] || 0;
            });
            
            try {
                const response = await fetch('http://localhost:8000/infer', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ evidence: completeEvidence }),
                });
                
                if (!response.ok) {
                    throw new Error(`Error ${response.status}: ${response.statusText}`);
                }
                
                const data = await response.json();
                console.log('Respuesta del backend:', data); // <-- Agregado para depuración
                showResults(data.resultados);
                
            } catch (error) {
                showError(error.message);
            } finally {
                loading = false;
                updateSymptomsCount();
            }
        }

        // Mostrar estado de carga
        function showLoading() {
            resultsContainer.innerHTML = `
                <div class="loading">
                    <svg class="loading-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
                    </svg>
                    <p class="loading-text">Analizando síntomas...</p>
                </div>
            `;
        }

        // Mostrar error
        function showError(errorMessage) {
            resultsContainer.innerHTML = `
                <div class="alert">
                    <div class="alert-content">
                        <svg class="alert-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16c-.77.833.192 2.5 1.732 2.5z"/>
                        </svg>
                        <div class="alert-text">
                            <strong>Error:</strong> ${errorMessage}
                            <small>Asegúrate de que la API esté ejecutándose en http://localhost:8000</small>
                        </div>
                    </div>
                </div>
            `;
        }

        // Mostrar resultados
        function showResults(results) {
            let resultsHTML = `
                <div class="results-header">
                    <h3 class="results-title">Probabilidades de Diagnóstico</h3>
                    <p class="results-subtitle">Ordenadas de mayor a menor probabilidad</p>
                </div>
            `;
            
            diseases.forEach(disease => {
                const probability = results[disease.key] || 0;
                const percentage = Math.round(probability * 100);
                
                resultsHTML += `
                    <div class="disease-item">
                        <div class="disease-header">
                            <span class="disease-name">${disease.label}</span>
                            <span class="disease-percentage">${percentage}%</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 0%" data-target="${percentage}"></div>
                        </div>
                    </div>
                `;
            });
            
            resultsHTML += `
                <div class="note">
                    <p class="note-text">
                        <strong>Nota:</strong> Este sistema es una herramienta de apoyo. Los resultados no sustituyen el criterio médico profesional.
                    </p>
                </div>
            `;
            
            resultsContainer.innerHTML = resultsHTML;
            
            // Animar las barras de progreso
            setTimeout(() => {
                document.querySelectorAll('.progress-fill').forEach(bar => {
                    const targetWidth = bar.getAttribute('data-target');
                    bar.style.width = `${targetWidth}%`;
                });
            }, 100);
        }

        diagnoseBtn.addEventListener('click', performDiagnosis);

        // Actualizar texto del botón durante la carga
        function updateButtonText() {
            if (loading) {
                diagnoseBtn.innerHTML = `
                    <svg class="icon loading-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
                    </svg>
                    Analizando...
                `;
            } else {
                diagnoseBtn.innerHTML = `
                    <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                    </svg>
                    Realizar Diagnóstico
                `;
            }
        }

        Object.defineProperty(window, 'loading', {
            get() { return loading; },
            set(value) {
                loading = value;
                updateButtonText();
            }
        });

        // Inicializar la aplicación
        init();

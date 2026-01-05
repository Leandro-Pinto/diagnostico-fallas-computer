// Estado global de la aplicación
let allRules = [];
let filteredRules = [];
let selectedConditions = [];

// Inicialización cuando el DOM está listo
document.addEventListener('DOMContentLoaded', function() {
    loadRules();
    setupEventListeners();
    setupFilters();
});

// Cargar reglas desde el servidor
async function loadRules() {
    try {
        const response = await fetch('/api/rules');
        const data = await response.json();
        allRules = data.rules;
        filteredRules = allRules;
        renderRules(allRules);
        updateResultsCount(allRules.length);
        populateCategories(data.categories);
    } catch (error) {
        console.error('Error cargando reglas:', error);
        showError('Error al cargar las reglas. Por favor, recarga la página.');
    }
}

// Configurar event listeners
function setupEventListeners() {
    // Búsqueda
    const searchBtn = document.getElementById('searchBtn');
    const searchInput = document.getElementById('searchInput');
    
    searchBtn.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });

    // Filtros
    document.getElementById('categoriaFilter').addEventListener('change', applyFilters);
    document.getElementById('certezaFilter').addEventListener('input', function(e) {
        document.getElementById('certezaValue').textContent = e.target.value + '%';
        applyFilters();
    });

    // Limpiar filtros
    document.getElementById('clearFilters').addEventListener('click', clearFilters);

    // Modal
    const modal = document.getElementById('ruleModal');
    const closeBtn = modal.querySelector('.close');
    
    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
}

// Configurar filtros
function setupFilters() {
    const certezaFilter = document.getElementById('certezaFilter');
    certezaFilter.addEventListener('input', function(e) {
        document.getElementById('certezaValue').textContent = e.target.value + '%';
    });
}

// Realizar búsqueda
function performSearch() {
    const searchInput = document.getElementById('searchInput');
    const searchTerm = searchInput.value.trim().toLowerCase();

    if (searchTerm === '') {
        // Si no hay término de búsqueda, mostrar todas las reglas
        filteredRules = allRules;
        selectedConditions = [];
        updateSelectedConditions();
        applyFilters();
        return;
    }

    // Extraer condiciones de la búsqueda (separadas por comas o espacios)
    const conditions = searchTerm.split(/[,\s]+/).filter(c => c.length > 0);
    selectedConditions = conditions;
    updateSelectedConditions();

    // Buscar reglas que coincidan
    searchRules(conditions);
}

// Buscar reglas por condiciones
async function searchRules(conditions) {
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ condiciones: conditions })
        });
        
        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.resultados && Array.isArray(data.resultados)) {
            filteredRules = data.resultados.map(r => ({
                id: r.id,
                ...r.regla
            }));
        } else {
            filteredRules = [];
        }
        
        applyFilters();
    } catch (error) {
        console.error('Error en búsqueda:', error);
        showError('Error al realizar la búsqueda: ' + error.message);
        filteredRules = [];
        applyFilters();
    }
}

// Aplicar filtros
function applyFilters() {
    let rules = [...filteredRules];

    // Filtro por categoría
    const categoria = document.getElementById('categoriaFilter').value;
    if (categoria) {
        rules = rules.filter(rule => rule.categoria === categoria);
    }

    // Filtro por certeza mínima
    const certezaMin = parseInt(document.getElementById('certezaFilter').value);
    rules = rules.filter(rule => rule.certeza >= certezaMin);

    renderRules(rules);
    updateResultsCount(rules.length);
}

// Limpiar filtros
function clearFilters() {
    document.getElementById('searchInput').value = '';
    document.getElementById('categoriaFilter').value = '';
    document.getElementById('certezaFilter').value = 0;
    document.getElementById('certezaValue').textContent = '0%';
    selectedConditions = [];
    updateSelectedConditions();
    filteredRules = allRules;
    applyFilters();
}

// Actualizar condiciones seleccionadas
function updateSelectedConditions() {
    const container = document.getElementById('selectedConditions');
    const list = document.getElementById('conditionsList');

    if (selectedConditions.length === 0) {
        container.style.display = 'none';
        return;
    }

    container.style.display = 'block';
    list.innerHTML = '';

    selectedConditions.forEach((condition, index) => {
        const tag = document.createElement('div');
        tag.className = 'condition-tag';
        tag.innerHTML = `
            <span>${condition}</span>
            <span class="remove" onclick="removeCondition(${index})">&times;</span>
        `;
        list.appendChild(tag);
    });
}

// Remover condición
function removeCondition(index) {
    selectedConditions.splice(index, 1);
    updateSelectedConditions();
    
    if (selectedConditions.length === 0) {
        filteredRules = allRules;
    } else {
        searchRules(selectedConditions);
    }
    applyFilters();
}

// Renderizar reglas
function renderRules(rules) {
    const container = document.getElementById('resultsContainer');
    
    if (rules.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-search"></i>
                <h3>No se encontraron reglas</h3>
                <p>Intenta ajustar tus filtros de búsqueda</p>
            </div>
        `;
        return;
    }

    container.innerHTML = rules.map(rule => createRuleCard(rule)).join('');
    
    // Agregar event listeners a las tarjetas
    container.querySelectorAll('.rule-card').forEach((card, index) => {
        card.addEventListener('click', () => showRuleDetails(rules[index]));
    });
}

// Crear tarjeta de regla
function createRuleCard(rule) {
    const certezaClass = getCertezaClass(rule.certeza);
    const condicionesHTML = rule.condiciones.map(c => 
        `<span class="condicion-tag-small">${c}</span>`
    ).join('');

    return `
        <div class="rule-card">
            <div class="rule-header">
                <span class="rule-id">${rule.id || 'N/A'}</span>
                <span class="certeza-badge ${certezaClass}">${rule.certeza}%</span>
            </div>
            <div class="rule-conclusion">
                <i class="fas fa-lightbulb"></i> ${rule.conclusion || 'Sin conclusión'}
            </div>
            <div class="rule-solucion">
                <strong>Solución:</strong> ${rule.solucion || 'No especificada'}
            </div>
            <div class="rule-condiciones">
                <h4><i class="fas fa-list"></i> Condiciones:</h4>
                <div class="condiciones-tags">
                    ${condicionesHTML}
                </div>
            </div>
            <div class="rule-categoria">
                <i class="fas fa-tag"></i> ${rule.categoria || 'Sin categoría'}
            </div>
        </div>
    `;
}

// Obtener clase CSS según certeza
function getCertezaClass(certeza) {
    if (certeza >= 80) return 'certeza-alta';
    if (certeza >= 50) return 'certeza-media';
    return 'certeza-baja';
}

// Mostrar detalles de regla en modal
function showRuleDetails(rule) {
    const modal = document.getElementById('ruleModal');
    const modalBody = document.getElementById('modalBody');
    
    const condicionesHTML = rule.condiciones.map(c => 
        `<span class="condicion-tag-small">${c}</span>`
    ).join('');

    modalBody.innerHTML = `
        <h2 style="margin-bottom: 20px; color: var(--primary-color);">
            <i class="fas fa-info-circle"></i> Detalles de la Regla ${rule.id || 'N/A'}
        </h2>
        
        <div style="margin-bottom: 25px;">
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">
                <i class="fas fa-lightbulb"></i> Conclusión
            </h3>
            <p style="font-size: 1.2rem; font-weight: 600; color: var(--text-primary);">
                ${rule.conclusion || 'Sin conclusión'}
            </p>
        </div>

        <div style="margin-bottom: 25px;">
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">
                <i class="fas fa-wrench"></i> Solución Recomendada
            </h3>
            <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-secondary);">
                ${rule.solucion || 'No especificada'}
            </p>
        </div>

        <div style="margin-bottom: 25px;">
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">
                <i class="fas fa-chart-line"></i> Nivel de Certeza
            </h3>
            <div style="display: flex; align-items: center; gap: 15px;">
                <span class="certeza-badge ${getCertezaClass(rule.certeza)}" style="font-size: 1.2rem; padding: 10px 20px;">
                    ${rule.certeza}%
                </span>
                <span style="color: var(--text-secondary);">
                    ${getCertezaDescription(rule.certeza)}
                </span>
            </div>
        </div>

        <div style="margin-bottom: 25px;">
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">
                <i class="fas fa-list"></i> Condiciones (${rule.condiciones.length})
            </h3>
            <div class="condiciones-tags" style="margin-top: 10px;">
                ${condicionesHTML}
            </div>
        </div>

        <div>
            <h3 style="color: var(--text-primary); margin-bottom: 10px;">
                <i class="fas fa-tag"></i> Categoría
            </h3>
            <span style="background: var(--primary-color); color: white; padding: 8px 15px; border-radius: 6px; font-weight: 600;">
                ${rule.categoria || 'Sin categoría'}
            </span>
        </div>
    `;

    modal.style.display = 'block';
}

// Obtener descripción de certeza
function getCertezaDescription(certeza) {
    if (certeza >= 80) return 'Alta confiabilidad';
    if (certeza >= 50) return 'Confiabilidad media';
    return 'Baja confiabilidad - verificar manualmente';
}

// Actualizar contador de resultados
function updateResultsCount(count) {
    document.getElementById('resultsCount').textContent = `${count} resultado${count !== 1 ? 's' : ''}`;
    document.getElementById('resultsTitle').textContent = count > 0 ? 'Resultados encontrados' : 'No hay resultados';
}

// Poblar categorías en el filtro
function populateCategories(categories) {
    const select = document.getElementById('categoriaFilter');
    categories.forEach(categoria => {
        const option = document.createElement('option');
        option.value = categoria;
        option.textContent = categoria;
        select.appendChild(option);
    });
}

// Mostrar error
function showError(message) {
    alert(message); // En producción, usar un sistema de notificaciones mejor
}


from flask import Flask, render_template, jsonify, request
from knowledge_base import (
    knowledge_base, 
    get_categorias, 
    buscar_por_condiciones,
    filtrar_por_categoria,
    filtrar_por_certeza
)

app = Flask(__name__)

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/rules')
def get_rules():
    """Obtener todas las reglas y categorías"""
    # Convertir el diccionario de reglas a lista
    rules_list = []
    for id_regla, regla in knowledge_base.items():
        rule_data = {
            'id': id_regla,
            **regla
        }
        rules_list.append(rule_data)
    
    categorias = get_categorias()
    
    return jsonify({
        'rules': rules_list,
        'total': len(rules_list),
        'categories': categorias
    })

@app.route('/api/search', methods=['POST'])
def search_rules():
    """Buscar reglas por condiciones"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'resultados': [],
                'mensaje': 'No se recibieron datos'
            }), 400
        
        condiciones = data.get('condiciones', [])
        
        if not condiciones or len(condiciones) == 0:
            return jsonify({
                'resultados': [],
                'mensaje': 'No se proporcionaron condiciones de búsqueda'
            })
        
        # Buscar reglas que coincidan
        resultados = buscar_por_condiciones(condiciones)
        
        return jsonify({
            'resultados': resultados,
            'total': len(resultados)
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'resultados': []
        }), 500

@app.route('/api/rules/<rule_id>')
def get_rule(rule_id):
    """Obtener una regla específica por ID"""
    if rule_id in knowledge_base:
        return jsonify({
            'id': rule_id,
            **knowledge_base[rule_id]
        })
    return jsonify({'error': 'Regla no encontrada'}), 404

@app.route('/api/categories')
def get_categories():
    """Obtener todas las categorías"""
    categorias = get_categorias()
    return jsonify({
        'categories': categorias
    })

@app.route('/api/filter')
def filter_rules():
    """Filtrar reglas por categoría y/o certeza"""
    categoria = request.args.get('categoria', None)
    min_certeza = request.args.get('min_certeza', 0, type=int)
    max_certeza = request.args.get('max_certeza', 100, type=int)
    
    rules = knowledge_base
    
    # Filtrar por categoría
    if categoria:
        rules = filtrar_por_categoria(categoria)
    
    # Filtrar por certeza
    rules = filtrar_por_certeza(min_certeza, max_certeza)
    
    # Convertir a lista
    rules_list = []
    for id_regla, regla in rules.items():
        rule_data = {
            'id': id_regla,
            **regla
        }
        rules_list.append(rule_data)
    
    return jsonify({
        'rules': rules_list,
        'total': len(rules_list)
    })

if __name__ == '__main__':
    print("=" * 60)
    print("Sistema Experto - Diagnóstico de Fallas en Computadoras")
    print("=" * 60)
    print(f"Total de reglas cargadas: {len(knowledge_base)}")
    print(f"Categorías disponibles: {len(get_categorias())}")
    print("=" * 60)
    print("\nIniciando servidor en http://127.0.0.1:5000")
    print("Presiona Ctrl+C para detener el servidor\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)


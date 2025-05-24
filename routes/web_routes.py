from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from ..services.municipio_service import get_municipios, add_municipio, delete_municipio
from ..services.organograma_service import (
    get_organograma, add_organograma, edit_organograma, delete_organograma
)

web = Blueprint('web', __name__)

@web.route('/')
def index():
    page = int(request.args.get('page', 1))
    per_page = 10
    offset = (page - 1) * per_page
    municipios, total = get_municipios(per_page, offset)
    return render_template('index.html', municipios=municipios, page=page, total=total, per_page=per_page)

@web.route('/add_municipio', methods=['GET', 'POST'])
def add_municipio_route():
    if request.method == 'POST':
        nome = request.form['nome']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        add_municipio(nome, float(latitude), float(longitude))
        flash('Município adicionado com sucesso!', 'success')
        return redirect(url_for('web.index'))
    return render_template('add_municipio.html')

@web.route('/delete_municipio/<int:id>', methods=['POST'])
def delete_municipio_route(id):
    delete_municipio(id)
    flash('Município excluído com sucesso!', 'success')
    return redirect(url_for('web.index'))

@web.route('/organograma/<int:id>')
def organograma_view(id):
    organograma = get_organograma(id)
    if not organograma:
        abort(404)
    return render_template('organograma_tree.html', organograma=organograma)

@web.route('/add_organograma', methods=['GET', 'POST'])
def add_organograma_route():
    if request.method == 'POST':
        add_organograma(
            municipio_id=int(request.form['municipio_id']),
            nome=request.form['nome'],
            tipo_incidente=request.form['tipo_incidente'],
            estrutura_json=request.form['estrutura_json']
        )
        flash('Organograma adicionado com sucesso!', 'success')
        return redirect(url_for('web.index'))
    return render_template('add_organograma.html')

@web.route('/edit_organograma/<int:id>', methods=['GET', 'POST'])
def edit_organograma_route(id):
    org = get_organograma(id)
    if request.method == 'POST':
        edit_organograma(
            id=id,
            nome=request.form['nome'],
            tipo_incidente=request.form['tipo_incidente'],
            estrutura_json=request.form['estrutura_json']
        )
        flash('Organograma atualizado com sucesso!', 'success')
        return redirect(url_for('web.index'))
    return render_template('edit_organograma.html', organograma=org)

@web.route('/delete_organograma/<int:id>', methods=['POST'])
def delete_organograma_route(id):
    delete_organograma(id)
    flash('Organograma excluído com sucesso!', 'success')
    return redirect(url_for('web.index'))

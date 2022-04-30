from sqlalchemy import false, null
from api_visie.database import db
from api_visie.schema import Pessoa
from flask import redirect, render_template, request, url_for
from datetime import datetime


def person():
    page = 1
    if request.args.get('page'):
        page = int(request.args.get('page'))
    per_page = 5
    persons = Pessoa.query.order_by(
        Pessoa.id_pessoa.desc()).paginate(page, per_page, error_out=False)

    next_url = url_for('person_bp.person', page=persons.next_num) \
        if persons.has_next else None
    prev_url = url_for('person_bp.person', page=persons.prev_num) \
        if persons.has_prev else None

    return render_template('index.html', persons=persons.items, next_url=next_url,
                           prev_url=prev_url)


def person_edit(id):
    person = Pessoa.query.filter_by(id_pessoa=id).first()
    return render_template('person/edit.html', person=person)


def person_delete(id):
    person = Pessoa.query.filter_by(id_pessoa=id).first()
    db.session.delete(person)
    db.session.commit()
    return redirect('/person')


def person_update():

    person = Pessoa.query.filter_by(
        id_pessoa=request.form['id_pessoa']).first()
    person.nome = request.form['nome']
    person.rg = request.form['rg']
    person.cpf = request.form['cpf']
    person.data_nascimento = datetime.strptime(
        request.form['data_nascimento'], "%Y-%m-%d").date()
    person.data_admissao = datetime.strptime(
        request.form['data_admissao'], "%Y-%m-%d").date()
    person.funcao = request.form['funcao']

    db.session.commit()
    return redirect('/person')


def person_create():
    person = Pessoa(
        nome=request.form['nome'], rg=request.form['rg'], cpf=request.form['cpf'],
        data_nascimento=datetime.strptime(
            request.form['data_nascimento'], "%Y-%m-%d").date(),
        data_admissao=datetime.strptime(request.form['data_admissao'], "%Y-%m-%d").date(), funcao=request.form['funcao'])
    db.session.add(person)
    db.session.commit()

    return redirect('/person')

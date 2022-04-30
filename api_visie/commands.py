import imp
from api_visie.database import db
from api_visie.schema import Pessoa
from datetime import datetime


def init_app(app):

    @app.cli.command('create_db')
    def create_db():
        """Creates database"""
        db.create_all()

    @app.cli.command('drop_db')
    def drop_db():
        """Drop database"""
        db.drop_all()

    @app.cli.command('populate_db')
    def populate_db():
        """Populate db with sample data"""

        data = [
            Pessoa(nome='Alberto Vieira', rg='25.507.105-2', cpf='168.637.122-53',
                   data_nascimento=datetime.strptime('1997-07-01', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2020-09-28', "%Y-%m-%d").date()),
            Pessoa(nome='Alexandre Teixeira', rg='79.474.888-8', cpf='877.733.889-89', data_nascimento=datetime.strptime(
                '1982-08-16', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2020-05-15', "%Y-%m-%d").date()),
            Pessoa(nome='Ana Carolina Souza', rg='52.565.667-8', cpf='766.370.920-96', data_nascimento=datetime.strptime(
                '1982-03-19', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2016-08-19', "%Y-%m-%d").date()),
            Pessoa(nome='Ana Paula Soares', rg='54.744.331-9', cpf='746.917.734-52', data_nascimento=datetime.strptime(
                '1984-09-01', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2019-08-25', "%Y-%m-%d").date()),
            Pessoa(nome='Antônio Siqueira', rg='81.669.888-5', cpf='695.991.412-45', data_nascimento=datetime.strptime(
                '1990-07-26', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2016-05-18', "%Y-%m-%d").date()),
            Pessoa(nome='Arthur Silva', rg='43.204.402-9', cpf='345.898.157-88', data_nascimento=datetime.strptime(
                '1996-12-30', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2016-04-28', "%Y-%m-%d").date()),
            Pessoa(nome='Bárbara Santos', rg='57.106.623-3', cpf='587.914.225-66', data_nascimento=datetime.strptime(
                '2000-09-04', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2018-11-17', "%Y-%m-%d").date()),
            Pessoa(nome='Beatriz Santana', rg='70.855.305-2', cpf='093.084.203-04', data_nascimento=datetime.strptime(
                '1994-05-17', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2018-03-05', "%Y-%m-%d").date()),
            Pessoa(nome='Caio Sampaio', rg='14.475.327-9', cpf='483.764.953-05', data_nascimento=datetime.strptime(
                '1995-11-18', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2020-06-03', "%Y-%m-%d").date()),
            Pessoa(nome='Carla Rodrigues', rg='62.692.082-5', cpf='566.412.961-13', data_nascimento=datetime.strptime(
                '1996-08-04', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2015-03-31', "%Y-%m-%d").date()),
            Pessoa(nome='Carlos Rocha', rg='23.782.125-5', cpf='053.166.034-60', data_nascimento=datetime.strptime(
                '1983-07-07', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2017-03-08', "%Y-%m-%d").date()),
            Pessoa(nome='Cauê Ribeiro', rg='33.548.790-1', cpf='491.145.149-15', data_nascimento=datetime.strptime(
                '1981-01-27', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2020-12-31', "%Y-%m-%d").date()),
            Pessoa(nome='Cláudia Reis', rg='54.435.082-9', cpf='511.020.782-80', data_nascimento=datetime.strptime(
                '1986-08-04', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2020-09-25', "%Y-%m-%d").date()),
            Pessoa(nome='Cláudio Ramos', rg='41.432.308-6', cpf='673.452.026-90', data_nascimento=datetime.strptime(
                '1982-08-12', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2019-11-01', "%Y-%m-%d").date()),
            Pessoa(nome='Daiane Pereira', rg='90.815.741-8', cpf='704.352.424-58', data_nascimento=datetime.strptime(
                '2002-11-22', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2017-06-15', "%Y-%m-%d").date()),
            Pessoa(nome='Diego Penha', rg='43.099.953-1', cpf='329.630.074-00', data_nascimento=datetime.strptime(
                '1983-02-23', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2017-12-01', "%Y-%m-%d").date()),
            Pessoa(nome='Eduardo Oliveira', rg='46.249.609-1', cpf='772.220.114-80', data_nascimento=datetime.strptime(
                '2001-02-12', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2020-05-10', "%Y-%m-%d").date()),
            Pessoa(nome='Eliana Nunes', rg='84.269.396-7', cpf='130.491.959-59', data_nascimento=datetime.strptime(
                '1994-07-03', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2018-01-16', "%Y-%m-%d").date()),
            Pessoa(nome='Enzo Nascimento', rg='68.986.227-4', cpf='356.759.355-25', data_nascimento=datetime.strptime(
                '1989-05-05', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2016-08-23', "%Y-%m-%d").date()),
            Pessoa(nome='Fabiana Moura', rg='69.437.526-9', cpf='149.992.262-00', data_nascimento=datetime.strptime(
                '1995-08-21', "%Y-%m-%d").date(), data_admissao=datetime.strptime('2019-03-26', "%Y-%m-%d").date()),
        ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        return Pessoa.query.all()

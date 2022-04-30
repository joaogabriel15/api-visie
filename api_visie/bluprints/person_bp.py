from crypt import methods
from flask import Blueprint
from api_visie.controllers.person_controller import person, person_create, person_delete, person_edit, person_update

person_bp = Blueprint('person_bp', __name__, template_folder='/templates')

person_bp.route('/', methods=['GET'])(person)
person_bp.route('/edit/<int:id>', methods=['GET'])(person_edit)
person_bp.route('/delete/<int:id>', methods=['GET'])(person_delete)
person_bp.route('/create', methods=['POST'])(person_create)
person_bp.route('/update', methods=['POST'])(person_update)

from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Tarefa

lista_bp = Blueprint("lista", __name__)

@lista_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        descricao = request.form.get("descricao")
        if descricao:
            nova_tarefa = Tarefa(descricao=descricao)
            db.session.add(nova_tarefa)
            db.session.commit()
            return redirect(url_for("lista.index"))

    tarefas = Tarefa.query.all()
    return render_template("index.html", tarefas=tarefas)

@lista_bp.route("/deletar/<int:id>", methods=["POST"])
def deletar(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for("lista.index"))

@lista_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    tarefa = Tarefa.query.get_or_404(id)
    if request.method == "POST":
        nova_descricao = request.form.get("descricao")
        if nova_descricao:
            tarefa.descricao = nova_descricao
            db.session.commit()
            return redirect(url_for("lista.index"))

    return render_template("editar.html", tarefa=tarefa)

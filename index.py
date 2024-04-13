from flask import Flask, render_template

app = Flask(__name__)


@app.route("/login")
def getLogin():
    return render_template("login.html")


@app.route("/")
def getIndex():
    return render_template("index.html")


# @app.route("/trabajadores/<campo>/<pagina>")
# def getPlantilla(campo, pagina):

#     if (campo == "personal"):

#         if (pagina == "fichaPersonal"):
#             return "fichaPersonal"
#         elif (pagina == "controlAsistencia"):
#             return "controlAsistencia"
#         elif (pagina == "adelantoAsistencia"):
#             return "adelantoAsistencia"
#         else:
#             return "esta pagina no existe"

#     elif (campo == "asignacionConceptos"):

#         if (pagina == "conceptosTrabajador"):
#             return "conceptosTrabajador"
#         else:
#             return "esta pagina no existe"

#     elif (campo == "tablas"):

#         if (pagina == "cargo"):
#             return "cargo"
#         elif (pagina == "centroCostos"):
#             return "centroCostos"
#         elif (pagina == "comisionAFPs"):
#             return "comisionAFPs"
#         elif (pagina == "conceptos"):
#             return "conceptos"
#         elif (pagina == "declarantes"):
#             return "declarantes"
#         elif (pagina == "departamento"):
#             return "departamento"
#         elif (pagina == "regimenPensionario"):
#             return "regimenPensionario"
#         elif (pagina == "sede"):
#             return "sede"
#         else:
#             return "esta pagina no existe"
#     else:
#         return "esta pagina no existe"


@app.route("/trabajadores/personal/<pagina>")
def getPersonal(pagina):

    if (pagina == "fichaPersonal"):
        return render_template("trabajadores/personal/fichaPersonal.html", pagina=pagina)
    elif (pagina == "controlAsistencia"):
        return render_template("trabajadores/personal/controlAsistencia.html", pagina=pagina)
    elif (pagina == "adelantoAsistencia"):
        return render_template("trabajadores/personal/adelantoAsistencia.html", pagina=pagina)
    else:
        return "esta pagina no existe"


@app.route("/trabajadores/asignacionConceptos/<pagina>")
def getAsignacionConceptos(pagina):

    if (pagina == "conceptosTrabajador"):
        return render_template("trabajadores/asignacionConceptos/conceptosTrabajador.html", pagina=pagina)
    else:
        return "esta pagina no existe"


@app.route("/trabajadores/tablas/<pagina>")
def getTablas(pagina):

    if (pagina == "cargo"):
        return render_template("trabajadores/tablas/cargo.html", pagina=pagina)
    elif (pagina == "centroCostos"):
        return render_template("trabajadores/tablas/centroCostos.html", pagina=pagina)
    elif (pagina == "comisionAFPs"):
        return render_template("trabajadores/tablas/comisionAFPs.html", pagina=pagina)
    elif (pagina == "conceptos"):
        return render_template("trabajadores/tablas/conceptos.html", pagina=pagina)
    elif (pagina == "declarantes"):
        return render_template("trabajadores/tablas/declarantes.html", pagina=pagina)
    elif (pagina == "departamento"):
        return render_template("trabajadores/tablas/departamento.html", pagina=pagina)
    elif (pagina == "regimenPensionario"):
        return render_template("trabajadores/tablas/regimenPensionario.html", pagina=pagina)
    elif (pagina == "sede"):
        return render_template("trabajadores/tablas/sede.html", pagina=pagina)
    else:
        return "esta pagina no existe"


if __name__ == '__main__':
    app.run(debug=True)

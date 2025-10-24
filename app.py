from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"  # necessário para flash messages e sessões

# Usuários de exemplo (em um projeto real, use banco de dados)
usuarios = {
    "admin": "12345",
    "usuario": "senha"
}

@app.route("/")
def home():
    if "usuario" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in usuarios and usuarios[username] == password:
            session["usuario"] = username
            flash(f"Bem-vindo, {username}!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Usuário ou senha incorretos!", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        flash("Você precisa fazer login primeiro!", "warning")
        return redirect(url_for("login"))
    return render_template("dashboard.html", usuario=session["usuario"])

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    flash("Logout realizado com sucesso!", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

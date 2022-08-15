from website import crear_app

if __name__ == "__main__":
    app = crear_app()
    app.run(debug=True) ##Esto hace que al debugear o modificar el programa automaticamente vuelva a correr el servidor con los cambios y adiciones incorporados


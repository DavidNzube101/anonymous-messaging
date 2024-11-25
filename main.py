from website import initialize_app

app = initialize_app()

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8000)
    # app.run(port=8000, debug=True)
    app.run()
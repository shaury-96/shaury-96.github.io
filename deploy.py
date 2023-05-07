from start import app,freezer

if __name__ == '__main__':
    freezer.freeze()
    freezer.run(debug=True)
from flask import Flask 

#factory
def create_app(): 
    app = Flask(__name__)

    # index route
    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'

    #register the pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    #register the fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)
    
    #factory app return
    return app

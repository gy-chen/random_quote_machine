# coding: utf-8
import random
from flask import Flask
from flask import jsonify
from flask import abort
from random_quote_machine import model
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)


@app.route('/quote/random')
def quote_random():
    session = model.Session()
    quote = random.choice(session.query(model.Quote).all())
    result = dict(quote=model.model_to_dict(quote),
                  video=model.model_to_dict(quote.video))
    session.close()
    return jsonify(result)


@app.route('/quote/<int:quote_id>')
def quote(quote_id):
    session = model.Session()
    try:
        quote = session.query(model.Quote).filter(model.Quote.id == quote_id).one()
        result = dict(quote=model.model_to_dict(quote),
                      video=model.model_to_dict(quote.video))
    except NoResultFound:
        abort(404)
    finally:
        session.close()
    return jsonify(result)

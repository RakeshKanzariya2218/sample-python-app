from flask import Blueprint, jsonify

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/')
def list_posts():
    return jsonify({'posts': []})


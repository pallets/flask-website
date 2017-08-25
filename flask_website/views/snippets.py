# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
    render_template, request, url_for

from flask_website.utils import format_creole, request_wants_json, \
    requires_admin, requires_login
from flask_website.database import Category, Comment, Snippet, db_session

mod = Blueprint('snippets', __name__, url_prefix='/snippets')


@mod.route('/')
def index():
    return render_template('snippets/index.html',
        categories=Category.query.order_by(Category.name).all())


@mod.route('/<int:id>/', methods=['GET', 'POST'])
def show(id):
    snippet = Snippet.query.get(id)
    if snippet is None:
        abort(404)
    if request_wants_json():
        return jsonify(snippet=snippet.to_json())
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        if text:
            db_session.add(Comment(snippet, g.user, title, text))
            db_session.commit()
            flash(u'Your comment was added')
            return redirect(snippet.url)
    return render_template('snippets/show.html', snippet=snippet)


@mod.route('/comments/<int:id>/', methods=['GET', 'POST'])
@requires_admin
def edit_comment(id):
    comment = Comment.query.get(id)
    if comment is None:
        abort(404)
    snippet = comment.snippet
    form = dict(title=comment.title, text=comment.text)
    if request.method == 'POST':
        if 'delete' in request.form:
            db_session.delete(comment)
            db_session.commit()
            flash(u'Comment was deleted.')
            return redirect(snippet.url)
        elif 'cancel' in request.form:
            return redirect(snippet.url)
        form['title'] = request.form['title']
        form['text'] = request.form['text']
        if not form['text']:
            flash(u'Error: comment text is required.')
        else:
            comment.title = form['title']
            comment.text = form['text']
            db_session.commit()
            flash(u'Comment was updated.')
            return redirect(snippet.url)
    return render_template('snippets/edit_comment.html', form=form,
                           comment=comment)


@mod.route('/edit/<int:id>/', methods=['GET', 'POST'])
@requires_login
def edit(id):
    snippet = Snippet.query.get(id)
    if snippet is None:
        abort(404)
    if g.user is None or (not g.user.is_admin and snippet.author != g.user):
        abort(401)
    preview = None
    form = dict(title=snippet.title, body=snippet.body,
                category=snippet.category.id)
    if request.method == 'POST':
        form['title'] = request.form['title']
        form['body'] = request.form['body']
        form['category'] = request.form.get('category', type=int)
        if 'preview' in request.form:
            preview = format_creole(request.form['body'])
        elif 'delete' in request.form:
            for comment in snippet.comments:
                db_session.delete(comment)
            db_session.delete(snippet)
            db_session.commit()
            flash(u'Your snippet was deleted')
            return redirect(url_for('snippets.index'))
        else:
            category_id = request.form.get('category', type=int)
            if not form['body']:
                flash(u'Error: you have to enter a snippet')
            else:
                category = Category.query.get(category_id)
                if category is not None:
                    snippet.title = form['title']
                    snippet.body = form['body']
                    snippet.category = category
                    db_session.commit()
                    flash(u'Your snippet was modified')
                    return redirect(snippet.url)
    return render_template('snippets/edit.html',
        snippet=snippet, preview=preview, form=form,
        categories=Category.query.order_by(Category.name).all())


@mod.route('/category/<slug>/')
def category(slug):
    category = Category.query.filter_by(slug=slug).first()
    if category is None:
        abort(404)
    snippets = category.snippets.order_by(Snippet.title).all()
    if request_wants_json():
        return jsonify(category=category.to_json(),
                       snippets=[s.id for s in snippets])
    return render_template('snippets/category.html', category=category,
                           snippets=snippets)

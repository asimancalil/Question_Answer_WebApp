from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Comment, Post
from flaskblog.comments.forms import CommentForm

comments = Blueprint('comments', __name__)


@comments.route("/comments/<int:post_id>", methods=['GET', 'POST'])
@login_required
def post_comments(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, author=current_user, post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been created!', 'success')
        return redirect(url_for('comments.post_comments', post_id=post.id))
    comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.date_posted.desc()).all()
    return render_template('comment.html', title='Comments',
                           form=form, legend='Comment', post=post, comments=comments)


@comments.route("/comments/<int:comment_id>/delete", methods=['POST', 'GET'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user:
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash("Your comment has been deleted!", 'success')
    post_id = comment.post_id
    return redirect(url_for('comments.post_comments', post_id=post_id))
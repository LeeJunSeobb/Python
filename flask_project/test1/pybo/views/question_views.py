from flask import Blueprint, render_template
from pybo.models import Question

bp = Blueprint("question", __name__, url_prefix = "/question")

@bp.route("/list/")
def _list() :
    # 아래 ~~order_py() = 조회결과 정렬 > ~~create_date.desc : 작성일시 기준 역순 // 작성일시기준 : Question.create_date
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template("question/question_list.html", question_list = question_list)

@bp.route("/detail/<int:question_id>/")
def detail(question_id) :
    question = Question.query.get_or_404(question_id)
    return render_template("question/question_detail.html", question = question)
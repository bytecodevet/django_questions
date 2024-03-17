from typing import Any
from urllib import request

from django.views.generic import DetailView, ListView

from .models import Question


class QuestionDetailView(DetailView):
  model = Question
  context_object_name = 'question'
  template_name = 'quiz/quiz.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    if self.request.GET:
      try:
        user_answer_id = int(self.request.GET.get('answer'))
        question = context.get('question')

        user_answer = question.answers.get(pk = user_answer_id)
      except Exception:
        return context

      context['user_answer'] = user_answer
      context['show_answer'] = True
    return context

class QuestionListView(ListView):
  model = Question
  context_object_name = 'questions'
  template_name = 'quiz/index.html'

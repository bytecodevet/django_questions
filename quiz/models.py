from django.db import models


class BaseModel(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text

    class Meta:
        abstract = True

class Question(BaseModel):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = 'answers')
    is_correct = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

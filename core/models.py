from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
# Create your models here.
class User(models.Model):

    first_name = models.CharField(_("Nombre"), max_length=50)
    last_name = models.CharField(_("Apellido"), max_length=50)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})


class Student(User):
    """
    Modelo que almacena los detos de perfil así como los cursos y lecciones tomadas.
    """

    courses = models.ManyToManyField("core.Course", verbose_name=_(
        "Cursos tomados"), related_name='students', help_text="Cursos tomados", through='StudentCourse')
    lessons = models.ManyToManyField("core.Lesson", verbose_name=_(
        "Lecciones tomadas"), related_name='students', help_text="Lecciones tomadas", through='StudentLesson')
    questions = models.ManyToManyField("core.Question", verbose_name=_(
        "Preguntas respondidas"), related_name='students', help_text="Muestra todas las preguntas contestadas por el estudiante")

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})

class StudentCourse(models.Model):

    student = models.ForeignKey("core.Student", verbose_name=_("Estudiante"), on_delete=models.CASCADE)
    course = models.ForeignKey("core.Course", verbose_name=_("Curso"), on_delete=models.CASCADE)
    approved = models.BooleanField(_("Aprobado"), help_text="Indica si el curso fue aprobado")
    current_date = models.DateTimeField(_("Fecha tomada"), auto_now=False, auto_now_add=True, help_text="Fecha que se tomó el curso")
    last_current = models.DateTimeField(_("Actualización"), auto_now=False, auto_now_add=False, help_text="Última vez que entró al curso")


    class Meta:
        verbose_name = _("studentcourse")
        verbose_name_plural = _("studentcourses")

    def __str__(self):
        return "%s - %s" % (student, course)

    def get_absolute_url(self):
        return reverse("studentcourse_detail", kwargs={"pk": self.pk})

class StudentLesson(models.Model):
    """
    Modelo relacional que sirve para tener un rápido acceso a las lecciones.
    """
    student = models.ForeignKey("core.Student", verbose_name=_("Estudiante"), on_delete=models.CASCADE)
    lesson = models.ForeignKey("core.Lesson", verbose_name=_("Lección"), on_delete=models.CASCADE, help_text="Lección tomada")
    approved = models.BooleanField(_("Aprobado"), default=False)
    current_date = models.DateTimeField(_("Fecha tomada"), auto_now=False, auto_now_add=True, help_text="Fecha que se tomó")

    class Meta:
        verbose_name = _("studentlesson")
        verbose_name_plural = _("studentlessons")

    def __str__(self):
        return "%s - %s" % (self.student, self.lesson)

    def get_absolute_url(self):
        return reverse("studentlesson_detail", kwargs={"pk": self.pk})

class StudentQuestion(models.Model):
    """
    Relación que sirve para mostrar todas las preguntas contestadas por los estudiantes
    e indica si contestó correctamente.
    correct_question: Es para tener un acceso rápido que indica si la pregunta fue contestado correctamente.
    """
    student = models.ForeignKey("core.Student", verbose_name=_("Estudiante"), on_delete=models.CASCADE)
    question = models.ForeignKey("core.Question", verbose_name=_("Pregunta"), on_delete=models.CASCADE)
    correct_question = models.BooleanField(_("Pregunta correcta"), help_text="Indica si la pregunta fue contestada correctamente")
    answers = models.ManyToManyField("core.Answer", verbose_name=_("Respuestas"), help_text="Respuestas que seleccionó")
    
    

    class Meta:
        verbose_name = _("StudentQuestion")
        verbose_name_plural = _("StudentQuestions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("StudentQuestion_detail", kwargs={"pk": self.pk})



class Teacher(User):
    

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Course(models.Model):
    name = models.CharField(_("Nombre"), max_length=50)
    teacher = models.ForeignKey("core.Teacher", verbose_name=_("Profesor"), on_delete=models.CASCADE)
    depends_on = models.ForeignKey("core.Course", verbose_name=_(
        "Depende de"), on_delete=models.CASCADE, help_text="El curso depende de otro curso para ser cursado ")
    created_at = models.DateTimeField(
        _("Fecha de creación"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("Fecha de actualización"), auto_now=False, auto_now_add=True)
    

    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"pk": self.pk})



class Lesson(models.Model):

    name = models.CharField(_("Nombre"), max_length=50)
    score_total = models.PositiveSmallIntegerField(_("Puntuación"), help_text="Puntuación a mínima a calificar")
    depends_on = models.ForeignKey("core.Lesson", verbose_name=_(
        "Depende de"), on_delete=models.CASCADE, help_text="La lección depende de otra lección")
    course = models.ForeignKey("core.Course", verbose_name=_("Curso"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("lesson")
        verbose_name_plural = _("lessons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lesson_detail", kwargs={"pk": self.pk})


class Question(models.Model):

    TYPE = (
        ('1', 'Si/No - Verdadero/Falso'),
        ('2', 'Opción múltiple. Una respuesta correcta'),
        ('3', 'Opción múltiple. Varias respuestas correctas'),
        ('4', 'Opción múltiple. Todas las respuestas son correctas')
    )

    name = models.CharField(_("Pregunta"), max_length=50)
    score = models.PositiveSmallIntegerField(_("Score"))
    tipo = models.CharField(_("Tipo"), max_length=50, choices=TYPE)
    answers = models.ManyToManyField("core.Answer", verbose_name=_(
        "Respuestas"), related_name='questions', help_text="Conjunto de respuestas")

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk": self.pk})



class Answer(models.Model):

    name = models.CharField(_("Respuesta"), max_length=50)
    correct = models.BooleanField(_("Respuesta correcta"), default=False)


    class Meta:
        verbose_name = _("answer")
        verbose_name_plural = _("answers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("answer_detail", kwargs={"pk": self.pk})

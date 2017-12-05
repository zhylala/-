from django.db import models

# Create your models here.
class UserInfo(models.Model):
    '''员工表'''
    username = models.CharField(max_length=64,verbose_name="用户名")
    password = models.CharField(max_length=32,verbose_name="用户密码")
    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural="员工表"

class ClassList(models.Model):
    '''班级表'''
    title = models.CharField(max_length=32,verbose_name="班级名")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "班级表"

class Student(models.Model):
    '''学生表'''
    name = models.CharField(max_length=32,verbose_name="学生姓名")
    password = models.CharField(max_length=32,verbose_name="学生密码")
    cls = models.ForeignKey(to="ClassList",verbose_name="所属班级")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "学生表"
class Questionnaire(models.Model):
    '''问卷表'''
    title = models.CharField(max_length=32,verbose_name="问卷名")
    cls = models.ForeignKey(to="ClassList",verbose_name="问卷班级")
    create_user = models.ForeignKey(to="UserInfo",verbose_name="创建问卷的用户")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "问卷表"
class Questions(models.Model):
    '''问卷问题表'''
    caption = models.CharField(max_length=32,verbose_name="问题题目")
    type_choices = (
        (1,"打分"),
        (2,"单选"),
        (3,"评价")
    )
    question_type = models.IntegerField(choices=type_choices,verbose_name="问题类型")
    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "问卷问题表"
class Answer(models.Model):
    '''问卷回答表'''   #谁什么时候对那个问题作答了
    student = models.ForeignKey(to="Student",verbose_name="所属学生")
    queston = models.ForeignKey(to="Questions",verbose_name="所属问题")
    val = models.IntegerField(null=True,blank=True,verbose_name="数字答案")
    content = models.CharField(max_length=255,null=True,blank=True,verbose_name="文本答案")
    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "问卷回答表"

class Option(models.Model):
    '''问卷单选题的选项表'''
    score = models.IntegerField(verbose_name="选项对应的分值")
    question_id = models.ForeignKey(to="Questions",verbose_name="所属问题")
    def __str__(self):
        return str(self.score)

    class Meta:
        verbose_name_plural = "问卷单选题的选项表"
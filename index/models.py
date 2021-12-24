from django.db import models
from django.core.validators import validate_image_file_extension
from PIL import Image
from django.contrib.auth.models import User

subject_choices={
    ("Maths","Maths"),
    ("Physics","Physics"),
    ("Chemistry","Chemistry")
}

class QuizPost(models.Model):
    title=models.CharField(max_length=100,unique=True)
    desc=models.TextField(blank=True,null=False,default='No desc provided')
    subject=models.CharField(choices=subject_choices,max_length=15)
    thumbnail=models.ImageField(upload_to='Quiz-Thumbnail',default='default_quiz.jpeg',validators=[validate_image_file_extension])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.thumbnail.path)

        if img.height > 300 or img.width > 300:
            output_size = (190, 163)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)

    class Meta:
        verbose_name_plural='QuizPost'

        
class Question(models.Model):
    ques_post=models.OneToOneField(QuizPost,on_delete=models.CASCADE)
    ques=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q_op1 = models.CharField(max_length=1,default='a',null=True)
    q_op2 = models.CharField(max_length=1,default='b',null=True)
    q_op3 = models.CharField(max_length=1,default='c',null=True)
    q_op4 = models.CharField(max_length=1,default='d',null=True)
    answer=models.CharField(max_length=1,blank=False)

    ques2=models.ImageField(upload_to='Quiz-Questions',default='default.jpeg',validators=[validate_image_file_extension])
    q2_op1 = models.CharField(max_length=1,default='a',null=True)
    q2_op2 = models.CharField(max_length=1,default='b',null=True)
    q2_op3 = models.CharField(max_length=1,default='c',null=True)
    q2_op4 = models.CharField(max_length=1,default='d',null=True)
    answer2=models.CharField(max_length=1,blank=False)

    ques3=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q3_op1 = models.CharField(max_length=1,default='a',null=True)
    q3_op2 = models.CharField(max_length=1,default='b',null=True)
    q3_op3 = models.CharField(max_length=1,default='c',null=True)
    q3_op4 = models.CharField(max_length=1,default='d',null=True)
    answer3=models.CharField(max_length=1,blank=False)

    ques4=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q4_op1 = models.CharField(max_length=1,default='a',null=True)
    q4_op2 = models.CharField(max_length=1,default='b',null=True)
    q4_op3 = models.CharField(max_length=1,default='c',null=True)
    q4_op4 = models.CharField(max_length=1,default='d',null=True)
    answer4=models.CharField(max_length=1,blank=False)

    ques5=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q5_op1 = models.CharField(max_length=1,default='a',null=True)
    q5_op2 = models.CharField(max_length=1,default='b',null=True)
    q5_op3 = models.CharField(max_length=1,default='c',null=True)
    q5_op4 = models.CharField(max_length=1,default='d',null=True)
    answer5=models.CharField(max_length=1,blank=False)

    ques6=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q6_op1 = models.CharField(max_length=1,default='a',null=True)
    q6_op2 = models.CharField(max_length=1,default='b',null=True)
    q6_op3 = models.CharField(max_length=1,default='c',null=True)
    q6_op4 = models.CharField(max_length=1,default='d',null=True)
    answer6=models.CharField(max_length=1,blank=False)

    ques7=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q7_op1 = models.CharField(max_length=1,default='a',null=True)
    q7_op2 = models.CharField(max_length=1,default='b',null=True)
    q7_op3 = models.CharField(max_length=1,default='c',null=True)
    q7_op4 = models.CharField(max_length=1,default='d',null=True)
    answer7=models.CharField(max_length=1,blank=False)

    ques8=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q8_op1 = models.CharField(max_length=1,default='a',null=True)
    q8_op2 = models.CharField(max_length=1,default='b',null=True)
    q8_op3 = models.CharField(max_length=1,default='c',null=True)
    q8_op4 = models.CharField(max_length=1,default='d',null=True)
    answer8=models.CharField(max_length=1,blank=False)

    ques9=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q9_op1 = models.CharField(max_length=1,default='a',null=True)
    q9_op2 = models.CharField(max_length=1,default='b',null=True)
    q9_op3 = models.CharField(max_length=1,default='c',null=True)
    q9_op4 = models.CharField(max_length=1,default='d',null=True)
    answer9=models.CharField(max_length=1,blank=False)

    ques10=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q10_op1 = models.CharField(max_length=1,default='a',null=True)
    q10_op2 = models.CharField(max_length=1,default='b',null=True)
    q10_op3 = models.CharField(max_length=1,default='c',null=True)
    q10_op4 = models.CharField(max_length=1,default='d',null=True)
    answer10=models.CharField(max_length=1,blank=False)

    ques11=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q11_op1 = models.CharField(max_length=1,default='a',null=True)
    q11_op2 = models.CharField(max_length=1,default='b',null=True)
    q11_op3 = models.CharField(max_length=1,default='c',null=True)
    q11_op4 = models.CharField(max_length=1,default='d',null=True)
    answer11=models.CharField(max_length=1,blank=False)

    ques12=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q12_op1 = models.CharField(max_length=1,default='a',null=True)
    q12_op2 = models.CharField(max_length=1,default='b',null=True)
    q12_op3 = models.CharField(max_length=1,default='c',null=True)
    q12_op4 = models.CharField(max_length=1,default='d',null=True)
    answer12=models.CharField(max_length=1,blank=False)

    ques13=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q13_op1 = models.CharField(max_length=1,default='a',null=True)
    q13_op2 = models.CharField(max_length=1,default='b',null=True)
    q13_op3 = models.CharField(max_length=1,default='c',null=True)
    q13_op4 = models.CharField(max_length=1,default='d',null=True)
    answer13=models.CharField(max_length=1,blank=False)

    ques14=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q14_op1 = models.CharField(max_length=1,default='a',null=True)
    q14_op2 = models.CharField(max_length=1,default='b',null=True)
    q14_op3 = models.CharField(max_length=1,default='c',null=True)
    q14_op4 = models.CharField(max_length=1,default='d',null=True)
    answer14=models.CharField(max_length=1,blank=False)

    ques15=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q15_op1 = models.CharField(max_length=1,default='a',null=True)
    q15_op2 = models.CharField(max_length=1,default='b',null=True)
    q15_op3 = models.CharField(max_length=1,default='c',null=True)
    q15_op4 = models.CharField(max_length=1,default='d',null=True)
    answer15=models.CharField(max_length=1,blank=False)

    ques16=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q16_op1 = models.CharField(max_length=1,default='a',null=True)
    q16_op2 = models.CharField(max_length=1,default='b',null=True)
    q16_op3 = models.CharField(max_length=1,default='c',null=True)
    q16_op4 = models.CharField(max_length=1,default='d',null=True)
    answer16=models.CharField(max_length=1,blank=False)

    ques17=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q17_op1 = models.CharField(max_length=1,default='a',null=True)
    q17_op2 = models.CharField(max_length=1,default='b',null=True)
    q17_op3 = models.CharField(max_length=1,default='c',null=True)
    q17_op4 = models.CharField(max_length=1,default='d',null=True)
    answer17=models.CharField(max_length=1,blank=False)

    ques18=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q18_op1 = models.CharField(max_length=1,default='a',null=True)
    q18_op2 = models.CharField(max_length=1,default='b',null=True)
    q18_op3 = models.CharField(max_length=1,default='c',null=True)
    q18_op4 = models.CharField(max_length=1,default='d',null=True)
    answer18=models.CharField(max_length=1,blank=False)

    ques19=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q19_op1 = models.CharField(max_length=1,default='a',null=True)
    q19_op2 = models.CharField(max_length=1,default='b',null=True)
    q19_op3 = models.CharField(max_length=1,default='c',null=True)
    q19_op4 = models.CharField(max_length=1,default='d',null=True)
    answer19=models.CharField(max_length=1,blank=False)

    ques20=models.ImageField(upload_to='Quiz-Questions',validators=[validate_image_file_extension])
    q20_op1 = models.CharField(max_length=1,default='a',null=True)
    q20_op2 = models.CharField(max_length=1,default='b',null=True)
    q20_op3 = models.CharField(max_length=1,default='c',null=True)
    q20_op4 = models.CharField(max_length=1,default='d',null=True)
    answer20=models.CharField(max_length=1,blank=False)

    def __str__(self):
        return str(self.ques_post)

class Result(models.Model):
    post=models.ForeignKey(Question,on_delete=models.CASCADE)
    score=models.CharField(max_length=5)
    correct=models.CharField(max_length=5)
    wrong=models.CharField(max_length=5)
    not_attempted=models.CharField(max_length=5)
    result_of=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post)
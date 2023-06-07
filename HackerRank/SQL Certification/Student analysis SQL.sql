select si.roll_number, si.name
from student_information si inner join examination_marks em on si.roll_number = em.roll_number
group by em.roll_number
Having Sum(em.subject_one + em.subject_two + em.subject_three) < 100

-- Write your query below
SELECT student_id, exam_id, score
FROM (SELECT student_id, exam_id, score, 
        RANK() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id ASC) as rn
        FROM exam_results) sub
WHERE rn = 1
ORDER BY student_id
-- Selecting score, score count as number and group by score desc
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;

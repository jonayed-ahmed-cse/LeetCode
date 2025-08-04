# Write your MySQL query statement below
SELECT author_id  AS id
FROM Views
WHERE viewer_id = author_id 
GROUP BY viewer_id 
ORDER BY viewer_id ASC;
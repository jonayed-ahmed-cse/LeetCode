Select p.project_id ,
Round(avg(e.experience_years),2) as  average_years
From Project p
Left Join Employee e
On e.employee_id  = p.employee_id 
Group By p.project_id;

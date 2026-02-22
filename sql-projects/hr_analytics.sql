-- HR Analytics Queries
-- Tables assumed: employees, departments, salaries, job_history

-- 1. Headcount by department
SELECT
    d.department_name,
    COUNT(e.employee_id) AS headcount
FROM employees e
JOIN departments d ON d.department_id = e.department_id
WHERE e.status = 'active'
GROUP BY d.department_name
ORDER BY headcount DESC;

-- 2. Average salary by department and job title
SELECT
    d.department_name,
    e.job_title,
    ROUND(AVG(s.salary), 2) AS avg_salary,
    MIN(s.salary)           AS min_salary,
    MAX(s.salary)           AS max_salary
FROM employees e
JOIN departments d ON d.department_id = e.department_id
JOIN salaries s ON s.employee_id = e.employee_id AND s.is_current = TRUE
GROUP BY d.department_name, e.job_title
ORDER BY avg_salary DESC;

-- 3. Employee tenure (years at company)
SELECT
    employee_id,
    first_name || ' ' || last_name                              AS full_name,
    hire_date,
    ROUND(EXTRACT(EPOCH FROM NOW() - hire_date) / 86400 / 365, 1) AS tenure_years
FROM employees
WHERE status = 'active'
ORDER BY tenure_years DESC;

-- 4. Turnover rate by year
SELECT
    EXTRACT(YEAR FROM termination_date) AS year,
    COUNT(*)                            AS employees_left
FROM employees
WHERE status = 'terminated'
GROUP BY 1
ORDER BY 1;

-- 5. Salary bands distribution
SELECT
    CASE
        WHEN salary < 40000              THEN 'Under $40K'
        WHEN salary BETWEEN 40000 AND 60000 THEN '$40K–$60K'
        WHEN salary BETWEEN 60001 AND 80000 THEN '$60K–$80K'
        WHEN salary BETWEEN 80001 AND 100000 THEN '$80K–$100K'
        ELSE 'Over $100K'
    END       AS salary_band,
    COUNT(*)  AS employee_count
FROM salaries
WHERE is_current = TRUE
GROUP BY 1
ORDER BY MIN(salary);

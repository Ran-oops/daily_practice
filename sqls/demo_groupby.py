
sql = """
select a.department_name, b.proj_num from department a left join
(SELECT dept_id, count(*) as proj_num from project groupby(dept_id)) b on a.id == b.dept_id
"""

"""
select a, b, count(c) FROM t groupby a
"""
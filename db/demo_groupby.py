
sql = """
select a.department_name, COALESCE(b.proj_num, 0) from department a left join
(SELECT dept_id, count(*) as proj_num from project GROUP BY dept_id)b on a.id = b.dept_id
"""
"""
ps:
当部门没有项目时，proj_num 将显示为 NULL
如需显示为 0，可改用：COALESCE(b.proj_num, 0)
"""

"""错误
select a, b, count(c) FROM t group by a
"""
"""正确
select a, b, count(c) FROM t group by a,b
"""

"""
GROUP BY 规则：
    select中的非聚合列必须出现在group by 子句中

数据库差异：
MySQL：在宽松模式下允许未聚合的列（但结果不确定）
PostgreSQL/SQL Server/Oracle：严格执行SQL标准，会拒绝查询
"""


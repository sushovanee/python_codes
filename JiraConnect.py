

from jira import JIRA

Jira =  JIRA('https://jira2.cerner.com')

issue_num = "SUPPLYCHN-607"

#auth_jira = JIRA(basic_auth=('SP046767', 'm1nv-SfwR'))

issue = Jira.issue(issue_num)

comments =  issue.fields.comment.comments

for comment in comments:
    print("Comment Author : ",comment.updateAuthor)
    print("Comment text : ",comment.body)
    print("\n")
    print("------------------------------------")
    print("\n") 
    

worklogs =  issue.fields.worklog.worklogs

for worklog in worklogs:
    print("Worklog Author : ",worklog.updateAuthor)
    print("Worklog text : ",worklog.timeSpent)
    print("\n")
    print("------------------------------------")
    print("\n") 
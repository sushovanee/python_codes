from jira import JIRA

jira = JIRA()

options = {"server": "https://https://jira2.cerner.com/"}
jira = JIRA(options)

auth_jira = JIRA(basic_auth=('SP046767', 'm1nv-SfwR'))

issue = jira.issue("SUPPLYCHN-8010")

# Find all comments made by Atlassians on this issue.
atl_comments = [
    comment
    for comment in issue.fields.comment.comments
    if re.search(r"@atlassian.com$", comment.author.emailAddress)
]
# https://leetcode.com/problems/accounts-merge/



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_acct = defaultdict(list)

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                email_to_acct[email].append(i)

        result = []
        visited = [False for _ in range(len(accounts))]

        def dfs(i):
            emails = set()
            if visited[i]:
                return emails
            visited[i] = True
            for email in accounts[i][1:]:
                emails.add(email)
                for acct in email_to_acct[email]:
                    emails |= dfs(acct)
            return emails
        
        for i, acct in enumerate(accounts):
            emails = dfs(i)
            if emails:
                result.append([acct[0]] + sorted(list(emails)))
        return result
